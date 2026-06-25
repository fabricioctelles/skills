#!/usr/bin/env python3
"""Example runner wrapper that uses the root template."""

from __future__ import annotations

from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
runpy.run_path(str(ROOT / "templates" / "run-loop.py"), run_name="__main__")

