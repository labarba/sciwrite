"""Summarize how long and how dense each review output is.

Usage:
  python3 tools/noise_stats.py <workspace/iteration-N> [<workspace/iteration-M> ...]

For each eval-*/<config>/output.md, prints the word count and the number of
severity labels (CRITICAL, MAJOR, MINOR), plus items in a "Minor edits" list.
"""

import pathlib
import re
import sys

for it in map(pathlib.Path, sys.argv[1:]):
    print(f"== {it}")
    for out in sorted(it.glob("eval-*/*/output.md")):
        text = out.read_text()
        counts = {s: len(re.findall(rf"\b{s}\b", text)) for s in ("CRITICAL", "MAJOR", "MINOR")}
        minor_list = 0
        m = re.search(r"#+\s*Minor edits\s*\n(.*?)(\n#+\s|\Z)", text, re.S)
        if m:
            minor_list = len(re.findall(r"^\s*[-*\d]", m.group(1), re.M))
        print(f"{out.parent.parent.name:40s} {out.parent.name:14s} "
              f"words={len(text.split()):5d} C={counts['CRITICAL']:2d} "
              f"MAJ={counts['MAJOR']:2d} MIN={counts['MINOR']:2d} minor_list={minor_list:2d}")
