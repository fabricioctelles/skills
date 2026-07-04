#!/usr/bin/env python3
"""Weighted overall score for a skill-evaluation scorecard.

Usage:
    score.py [--fail-below N] 1:80:2 2:65:2 3:85:1 ... 15:NA:1 16:NA:1

One arg per criterion, formatted criterion:score:weight.
Score NA (or N/A) excludes the criterion from both sums.
Prints sum(score x weight), sum(weight), overall, and grade.
--fail-below N exits non-zero when overall < N (CI gate).
"""
import sys


def grade(score: float) -> str:
    if score >= 80:
        return "A"
    if score >= 60:
        return "B"
    if score >= 40:
        return "C"
    if score >= 20:
        return "D"
    return "F"


def main() -> None:
    args = sys.argv[1:]
    fail_below = None
    if "--fail-below" in args:
        i = args.index("--fail-below")
        try:
            fail_below = float(args[i + 1])
        except (IndexError, ValueError):
            sys.exit("--fail-below requires a numeric threshold")
        del args[i : i + 2]
    if not args:
        sys.exit(__doc__)
    num = den = 0.0
    na = []
    for arg in args:
        try:
            crit, score, weight = arg.split(":")
        except ValueError:
            sys.exit(f"bad arg {arg!r}: expected criterion:score:weight")
        if score.strip().upper() in ("NA", "N/A"):
            na.append(crit)
            continue
        s, w = float(score), float(weight)
        if not 0 <= s <= 100:
            sys.exit(f"criterion {crit}: score {s} outside 0-100")
        num += s * w
        den += w
    if den == 0:
        sys.exit("no applicable criteria")
    overall = num / den
    print(f"applicable criteria: {len(args) - len(na)}  |  N/A: {', '.join(na) or 'none'}")
    print(f"sum(score x weight) = {num:g}")
    print(f"sum(weight) = {den:g}")
    print(f"overall = {overall:.2f}  ->  grade {grade(overall)}")
    if fail_below is not None and overall < fail_below:
        sys.exit(f"FAIL: overall {overall:.2f} below threshold {fail_below:g}")


if __name__ == "__main__":
    main()
