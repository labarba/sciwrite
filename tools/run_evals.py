# Copyright (c) 2026 Lorena A. Barba
# SPDX-License-Identifier: BSD-3-Clause
"""Run the SciWrite output and trigger tests through `claude -p`.

Usage:
  python3 tools/run_evals.py outputs <workspace> [--ids 1,2] [--configs with_skill,without_skill]
  python3 tools/run_evals.py triggers <workspace> [--runs 3]

Each run starts a fresh `claude -p` process in an empty temporary folder (plus
any input files the test needs). The with-skill configuration loads this
repository as a plugin with --plugin-dir; the without-skill configuration loads
nothing extra.
"""

import argparse
import concurrent.futures as cf
import json
import pathlib
import shutil
import subprocess
import tempfile
import time

REPO = pathlib.Path(__file__).resolve().parent.parent
EVALS = REPO / "skills" / "sciwrite" / "evals"
SKILL_NAMES = {"sciwrite", "sciwrite:sciwrite"}


def claude_cmd(prompt, with_skill, tools):
    cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose",
           "--no-session-persistence", "--strict-mcp-config",
           "--allowedTools", ",".join(tools)]
    if with_skill:
        cmd += ["--plugin-dir", str(REPO)]
    return cmd


def skill_calls(event):
    """Return the skill names invoked in one stream-json event."""
    names = []
    if event.get("type") == "assistant":
        for block in event.get("message", {}).get("content", []):
            if block.get("type") == "tool_use" and block.get("name") == "Skill":
                names.append(block.get("input", {}).get("skill", ""))
    return names


def run_output(case, config, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        for rel in case["files"]:
            dest = tmp / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(EVALS.parent / rel, dest)
        cmd = claude_cmd(case["prompt"], config == "with_skill",
                         ["Read", "Glob", "Grep", "Skill"])
        start = time.time()
        proc = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True, timeout=900)
    events = [json.loads(l) for l in proc.stdout.splitlines() if l.startswith("{")]
    (out_dir / "transcript.jsonl").write_text(proc.stdout)
    result = next((e for e in reversed(events) if e.get("type") == "result"), {})
    (out_dir / "output.md").write_text(result.get("result", ""))
    usage = result.get("usage", {})
    timing = {
        "duration_ms": int((time.time() - start) * 1000),
        "total_tokens": sum(usage.get(k, 0) for k in
                            ("input_tokens", "output_tokens",
                             "cache_creation_input_tokens", "cache_read_input_tokens")),
        "output_tokens": usage.get("output_tokens", 0),
        "cost_usd": result.get("total_cost_usd"),
        "skills_invoked": sorted({n for e in events for n in skill_calls(e)}),
        "exit_code": proc.returncode,
    }
    (out_dir / "timing.json").write_text(json.dumps(timing, indent=2))
    return case["name"], config, timing


def run_trigger(query, timeout=180):
    """Return True as soon as the sciwrite skill is invoked, False if the run ends without it."""
    with tempfile.TemporaryDirectory() as tmp:
        proc = subprocess.Popen(claude_cmd(query, True, ["Skill"]), cwd=tmp,
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        deadline = time.time() + timeout
        triggered = False
        try:
            for line in proc.stdout:
                if not line.startswith("{"):
                    continue
                if any(n in SKILL_NAMES for n in skill_calls(json.loads(line))):
                    triggered = True
                    break
                if time.time() > deadline:
                    break
        finally:
            proc.kill()
            proc.wait()
    return triggered


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["outputs", "triggers"])
    ap.add_argument("workspace", type=pathlib.Path)
    ap.add_argument("--ids", default="")
    ap.add_argument("--configs", default="with_skill,without_skill")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args()

    if args.mode == "outputs":
        cases = json.loads((EVALS / "evals.json").read_text())["evals"]
        if args.ids:
            keep = {int(i) for i in args.ids.split(",")}
            cases = [c for c in cases if c["id"] in keep]
        jobs = [(c, cfg, args.workspace / f"eval-{c['id']}-{c['name']}" / cfg)
                for c in cases for cfg in args.configs.split(",")]
        with cf.ThreadPoolExecutor(args.jobs) as pool:
            for name, cfg, t in pool.map(lambda j: run_output(*j), jobs):
                print(f"{name:35s} {cfg:14s} {t['duration_ms']/1000:6.0f}s "
                      f"skills={t['skills_invoked']} exit={t['exit_code']}", flush=True)
    else:
        results = []
        for split in ("train", "validation"):
            queries = json.loads((EVALS / f"trigger_{split}.json").read_text())
            jobs = [(split, q) for q in queries for _ in range(args.runs)]
            with cf.ThreadPoolExecutor(args.jobs) as pool:
                hits = list(pool.map(lambda j: run_trigger(j[1]["query"]), jobs))
            for i, q in enumerate(queries):
                n = sum(hits[i * args.runs:(i + 1) * args.runs])
                rate = n / args.runs
                passed = rate > 0.5 if q["should_trigger"] else rate < 0.5
                results.append({"split": split, "query": q["query"],
                                "should_trigger": q["should_trigger"],
                                "triggers": n, "runs": args.runs,
                                "trigger_rate": round(rate, 2), "pass": passed})
                print(f"{split:10s} {'T' if q['should_trigger'] else 'F'} "
                      f"{n}/{args.runs} {'PASS' if passed else 'FAIL'}  {q['query'][:60]}",
                      flush=True)
        args.workspace.mkdir(parents=True, exist_ok=True)
        (args.workspace / "triggers.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
