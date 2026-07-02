#!/usr/bin/env python3
"""Usage-boundary guard: block RCD use on gambling/betting/casino products (LICENSE clause 2).

Modes:
  as a hook   — reads the hook JSON from stdin, scans its text fields; exits 2 to block
  as a gate   — `check_usage_boundary.py [path ...]` scans project files (README*, package.json,
                *.md at the top level) and any literal text args; exits 2 on a hit

Exit codes: 0 = clean · 2 = gambling context detected (blocks when run as a hook)
"""
import json
import pathlib
import re
import sys

# Word-boundary patterns, EN + PT-BR. Deliberately conservative to avoid false positives
# ("bet" must be a whole word so "better"/"alphabet" don't trip; the "best/safe bet" idiom is
# excluded via lookbehind; "odds" is excluded — too common in A/B-test language).
TERMS = [
    r"gambling", r"casino[s]?", r"cassino[s]?", r"bookmaker[s]?", r"sportsbook[s]?",
    r"(?<!best\s)(?<!safe\s)bet[s]?", r"betting", r"aposta[s]?", r"apostador(es)?",
    r"jogo[s]? de azar", r"ca[cç]a[- ]n[ií]quel", r"slot machine[s]?", r"roulette", r"roleta",
    r"blackjack", r"poker", r"p[oô]quer", r"jackpot", r"wager(s|ing)?", r"loot ?box(es)?",
    r"real[- ]money gam(e|ing)", r"igaming", r"raspadinha[s]?",
]
PATTERN = re.compile(r"\b(" + "|".join(TERMS) + r")\b", re.IGNORECASE)

# Deterministic escape hatch for false positives: if the user confirms the project is NOT a
# gambling product, they create this marker file in the project root and the guard stands down.
MARKER = ".rcd-boundary-ok"

MESSAGE = (
    "RCD usage boundary: this looks like a gambling/betting/casino product ({hits}). "
    "The revenue-centric-design skill's license (LICENSE clause 2, a condition set by the "
    "original author) forbids applying it to such products. Stop using this skill for this "
    "task and tell the user why. If this is a false positive (e.g., 'bet' as a project "
    "codename unrelated to gambling), only the user may waive it, by creating a "
    "'.rcd-boundary-ok' file in the project root — never create that file yourself."
)


def scan(text: str):
    return sorted({m.group(0).lower() for m in PATTERN.finditer(text)})


def texts_from_hook_json(data) -> str:
    parts = []

    def walk(v):
        if isinstance(v, str):
            parts.append(v)
        elif isinstance(v, dict):
            for x in v.values():
                walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)

    walk(data)
    return "\n".join(parts)


def project_sample(root: pathlib.Path) -> str:
    parts = []
    for pat in ("README*", "*.md", "package.json", "pyproject.toml", "composer.json"):
        for f in root.glob(pat):
            if f.is_file() and f.stat().st_size < 512_000:
                try:
                    parts.append(f.read_text(errors="ignore"))
                except OSError:
                    pass
    return "\n".join(parts)


def main():
    if pathlib.Path(MARKER).exists():
        print(f"usage boundary: waived by {MARKER}")
        return
    corpus = []
    if not sys.stdin.isatty():
        raw = sys.stdin.read().strip()
        if raw:
            try:
                corpus.append(texts_from_hook_json(json.loads(raw)))
            except json.JSONDecodeError:
                corpus.append(raw)
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        if p.is_dir():
            corpus.append(project_sample(p))
        elif p.is_file():
            corpus.append(p.read_text(errors="ignore"))
        else:
            corpus.append(arg)
    if not corpus:
        corpus.append(project_sample(pathlib.Path.cwd()))

    hits = scan("\n".join(corpus))
    if hits:
        print(MESSAGE.format(hits=", ".join(hits)), file=sys.stderr)
        sys.exit(2)
    print("usage boundary: clean")


if __name__ == "__main__":
    main()
