# Copyright (c) 2026 Lorena A. Barba
# SPDX-License-Identifier: BSD-3-Clause
"""Grade SciWrite test outputs against their assertions with a blind LLM judge.

Usage:
  python3 tools/grade_evals.py <workspace/iteration-N>

For every eval-*/<config>/output.md, asks a fresh `claude -p` judge to grade each
assertion PASS or FAIL with quoted evidence. The judge is not told which
configuration produced the output. Writes grading.json beside each output and
benchmark.json in the iteration folder.
"""

import concurrent.futures as cf
import json
import pathlib
import statistics
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
EVALS = REPO / "skills" / "sciwrite" / "evals"

JUDGE = """You are grading the output of an AI writing reviewer against a list of assertions.

Rules:
- Grade each assertion PASS or FAIL. Require concrete evidence for a PASS: quote or
  point to the part of the output that satisfies it. If the evidence is missing,
  partial or ambiguous, grade FAIL.
- Grade only what the output says. Do not reward effort or good intentions.
- Reply with JSON only, no prose and no code fence, in this shape:
  {{"assertion_results": [{{"text": "...", "passed": true, "evidence": "..."}}]}}

The user's request was:
<request>
{prompt}
</request>

The reviewer's output was:
<output>
{output}
</output>

Assertions to grade, in order:
{assertions}
"""


def grade(case, run_dir):
    output = (run_dir / "output.md").read_text()
    prompt = JUDGE.format(prompt=case["prompt"], output=output,
                          assertions="\n".join(f"{i+1}. {a}" for i, a in enumerate(case["assertions"])))
    with tempfile.TemporaryDirectory() as tmp:
        proc = subprocess.run(["claude", "-p", prompt, "--output-format", "json",
                               "--no-session-persistence", "--strict-mcp-config",
                               "--allowedTools", ""],
                              cwd=tmp, capture_output=True, text=True, timeout=600)
    text = json.loads(proc.stdout)["result"].strip()
    text = text[text.index("{"):text.rindex("}") + 1]
    results = json.loads(text)["assertion_results"]
    passed = sum(r["passed"] for r in results)
    grading = {"assertion_results": results,
               "summary": {"passed": passed, "failed": len(results) - passed,
                           "total": len(results),
                           "pass_rate": round(passed / len(results), 3)}}
    (run_dir / "grading.json").write_text(json.dumps(grading, indent=2))
    return run_dir, grading


def main():
    it = pathlib.Path(sys.argv[1])
    cases = {c["id"]: c for c in json.loads((EVALS / "evals.json").read_text())["evals"]}
    jobs = []
    for run_dir in sorted(it.glob("eval-*/*")):
        if (run_dir / "output.md").exists():
            cid = int(run_dir.parent.name.split("-")[1])
            jobs.append((cases[cid], run_dir))
    with cf.ThreadPoolExecutor(4) as pool:
        graded = list(pool.map(lambda j: grade(*j), jobs))

    by_config = {}
    for run_dir, g in graded:
        t = json.loads((run_dir / "timing.json").read_text())
        by_config.setdefault(run_dir.name, []).append(
            (g["summary"]["pass_rate"], t["duration_ms"] / 1000, t["total_tokens"], t.get("cost_usd") or 0))
        print(f"{run_dir.parent.name:40s} {run_dir.name:14s} "
              f"{g['summary']['passed']}/{g['summary']['total']}")

    def stats(xs):
        return {"mean": round(statistics.mean(xs), 3),
                "stddev": round(statistics.stdev(xs), 3) if len(xs) > 1 else 0.0}
    summary = {cfg: {"pass_rate": stats([r[0] for r in rows]),
                     "time_seconds": stats([r[1] for r in rows]),
                     "tokens": stats([r[2] for r in rows]),
                     "cost_usd": stats([r[3] for r in rows])}
               for cfg, rows in by_config.items()}
    if {"with_skill", "without_skill"} <= summary.keys():
        summary["delta"] = {k: round(summary["with_skill"][k]["mean"] - summary["without_skill"][k]["mean"], 3)
                            for k in ("pass_rate", "time_seconds", "tokens", "cost_usd")}
    (it / "benchmark.json").write_text(json.dumps({"run_summary": summary}, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
