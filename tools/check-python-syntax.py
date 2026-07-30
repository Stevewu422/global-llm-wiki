#!/usr/bin/env python3
"""Parse repository Python tools without generating bytecode caches."""

from __future__ import annotations

import ast
from pathlib import Path


TOOLS_ROOT = Path(__file__).resolve().parent


def main() -> int:
    failures: list[str] = []
    paths = sorted(TOOLS_ROOT.glob("*.py"))

    for path in paths:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError, UnicodeError) as exc:
            failures.append(f"{path.name}: {exc}")

    print(f"Python syntax gates: files={len(paths)} errors={len(failures)}")
    for failure in failures:
        print(f"  {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
