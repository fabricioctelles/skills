#!/usr/bin/env python3
"""Deterministic scoring for a slop-eval report.

Usage:
    score.py axis CRIT MAJOR MINOR [--cap N]
        Axis score from confirmed tell counts:
        max(0, 100 - 30*CRIT - 15*MAJOR - 5*MINOR), then min(score, cap).
        Use --cap 40 for the Layout compounding rule (>=3 major layout tells).

    score.py overall [--cap N ...] [--fail-below N] 1:80:2 2:65:2 ... 7:NA:3
        One arg per axis, formatted axis:score:weight. Score NA (or N/A)
        excludes the axis from both sums. Caps apply to the weighted
        overall (signature gate: --cap 59; absolute-rule gate: --cap 69).
        Prints overall, Slop Index (100 - overall), and grade.
        --fail-below N exits non-zero when overall < N (CI gate).
"""
import sys

PENALTY = {"crit": 30, "major": 15, "minor": 5}


def grade(score: float) -> str:
    if score >= 80:
        return "A (Premium)"
    if score >= 60:
        return "B (Considered)"
    if score >= 40:
        return "C (Generic)"
    if score >= 20:
        return "D (Slop)"
    return "F (Pure slop)"


def pop_flag(args: list, flag: str, repeat: bool = False):
    vals = []
    while flag in args:
        i = args.index(flag)
        try:
            vals.append(float(args[i + 1]))
        except (IndexError, ValueError):
            sys.exit(f"{flag} requires a numeric value")
        del args[i : i + 2]
        if not repeat:
            break
    return vals


def cmd_axis(args: list) -> None:
    caps = pop_flag(args, "--cap", repeat=True)
    if len(args) != 3:
        sys.exit("axis mode needs exactly: CRIT MAJOR MINOR counts")
    try:
        crit, major, minor = (int(a) for a in args)
    except ValueError:
        sys.exit("tell counts must be integers")
    if min(crit, major, minor) < 0:
        sys.exit("tell counts must be >= 0")
    score = max(
        0,
        100 - PENALTY["crit"] * crit - PENALTY["major"] * major - PENALTY["minor"] * minor,
    )
    capped = min([score] + caps)
    detail = f" (capped from {score:g})" if capped < score else ""
    print(
        f"tells: {crit} crit / {major} major / {minor} minor"
        f"  ->  axis score = {capped:g}{detail}"
    )


def cmd_overall(args: list) -> None:
    caps = pop_flag(args, "--cap", repeat=True)
    fail_below = pop_flag(args, "--fail-below")
    if not args:
        sys.exit(__doc__)
    num = den = 0.0
    na = []
    for arg in args:
        try:
            axis, score, weight = arg.split(":")
        except ValueError:
            sys.exit(f"bad arg {arg!r}: expected axis:score:weight")
        if score.strip().upper() in ("NA", "N/A"):
            na.append(axis)
            continue
        s, w = float(score), float(weight)
        if not 0 <= s <= 100:
            sys.exit(f"axis {axis}: score {s} outside 0-100")
        num += s * w
        den += w
    if den == 0:
        sys.exit("no applicable axes")
    raw = num / den
    overall = min([raw] + caps)
    capped = f"  (capped from {raw:.2f})" if overall < raw else ""
    print(f"applicable axes: {len(args) - len(na)}  |  NA: {', '.join(na) or 'none'}")
    print(f"sum(score x weight) = {num:g}  |  sum(weight) = {den:g}")
    print(f"overall = {overall:.2f}{capped}")
    print(f"Slop Index = {100 - overall:.2f}")
    print(f"grade: {grade(overall)}")
    if fail_below and overall < fail_below[0]:
        sys.exit(f"FAIL: overall {overall:.2f} below threshold {fail_below[0]:g}")


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        sys.exit(__doc__)
    mode, args = sys.argv[1], sys.argv[2:]
    if mode == "axis":
        cmd_axis(args)
    elif mode == "overall":
        cmd_overall(args)
    else:
        sys.exit(f"unknown mode {mode!r}; use 'axis' or 'overall'\n\n{__doc__}")


if __name__ == "__main__":
    main()
