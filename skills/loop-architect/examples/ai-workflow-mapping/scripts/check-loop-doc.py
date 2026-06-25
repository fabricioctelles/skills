#!/usr/bin/env python3
"""Check that a generated workflow map has the expected sections."""

from __future__ import annotations

from pathlib import Path
import sys


REQUIRED = ["Owner", "Input", "Output", "Checkpoint"]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check-loop-doc.py <delivery-path>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8")
    missing = [item for item in REQUIRED if item not in text]
    if missing:
        print(f"missing required text: {', '.join(missing)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

