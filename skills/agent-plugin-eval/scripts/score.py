#!/usr/bin/env python3
"""Compute an Agent Plugin evaluation score with a conformance gate.

Usage:
    score.py [--gate pass|partial|fail] 1:80:3 2:65:3 ... 8:NA:2

Each criterion is ID:SCORE:WEIGHT. NA or N/A excludes a criterion from both
sums. PARTIAL caps the final score at 59; FAIL caps it at 39.
"""

from __future__ import annotations

import argparse
import sys


CAPS = {"pass": None, "partial": 59.0, "fail": 39.0}


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


def parse_triple(value: str) -> tuple[str, float | None, float]:
    try:
        criterion, score_text, weight_text = value.split(":")
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"{value!r}: expected criterion:score:weight"
        ) from exc
    if not criterion:
        raise argparse.ArgumentTypeError("criterion ID cannot be empty")
    try:
        weight = float(weight_text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"{value!r}: weight must be numeric") from exc
    if weight <= 0:
        raise argparse.ArgumentTypeError(f"{value!r}: weight must be positive")
    if score_text.strip().upper() in {"NA", "N/A"}:
        return criterion, None, weight
    try:
        score = float(score_text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"{value!r}: score must be 0-100 or NA") from exc
    if not 0 <= score <= 100:
        raise argparse.ArgumentTypeError(f"{value!r}: score outside 0-100")
    return criterion, score, weight


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gate", choices=CAPS, default="pass")
    parser.add_argument("criteria", nargs="+", type=parse_triple)
    args = parser.parse_args()

    numerator = 0.0
    denominator = 0.0
    excluded: list[str] = []
    seen: set[str] = set()
    for criterion, score, weight in args.criteria:
        if criterion in seen:
            parser.error(f"duplicate criterion ID: {criterion}")
        seen.add(criterion)
        if score is None:
            excluded.append(criterion)
            continue
        numerator += score * weight
        denominator += weight

    if denominator == 0:
        parser.error("no applicable criteria")

    raw = numerator / denominator
    cap = CAPS[args.gate]
    final = min(raw, cap) if cap is not None else raw

    print(f"gate = {args.gate.upper()}")
    print(f"applicable criteria = {len(args.criteria) - len(excluded)}")
    print(f"N/A = {', '.join(excluded) or 'none'}")
    print(f"sum(score x weight) = {numerator:g}")
    print(f"sum(weight) = {denominator:g}")
    print(f"raw score = {raw:.2f}")
    if cap is None:
        print("cap = none")
    else:
        print(f"cap = {cap:g} ({args.gate.upper()} gate)")
    print(f"final score = {final:.2f}")
    print(f"grade = {grade(final)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
