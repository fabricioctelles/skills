#!/usr/bin/env python3
"""Example runner wrapper that uses the root template."""

from __future__ import annotations

from pathlib import Path
import runpy
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

# runpy sets __file__ to the template's path, so the runner's default spec
# lookup would miss this example's loop.resolved.json; pass it explicitly.
if len(sys.argv) == 1:
    sys.argv = [sys.argv[0], str(HERE / "loop.resolved.json")]
runpy.run_path(str(ROOT / "templates" / "run-loop.py"), run_name="__main__")

