#!/usr/bin/env python3
"""Self-Checkout Is Judging You — writes one funny line to entry.txt.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200 chars,
not only whitespace.
"""
import os
import sys

ENTRY = "No spoon, twelve yoghurts. This isn't a shop, it's a hostage situation with live cultures."

def main() -> int:
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        print(f"gate fail: entry is {len(ENTRY)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
