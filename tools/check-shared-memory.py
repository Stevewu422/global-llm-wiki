#!/usr/bin/env python3
"""Read-only publication gates for the shared Obsidian memory snapshot."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "obsidian-vault"
INDEX = ROOT / "index.md"

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
SENSITIVE_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{16,}", re.IGNORECASE),
    re.compile(r"(?:api[_-]?key|password|passwd|token|secret)\s*[:=]\s*\S+", re.IGNORECASE),
    re.compile(r"authorization\s*:\s*bearer\s+\S+", re.IGNORECASE),
    re.compile(r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY", re.IGNORECASE),
)


def clean_markdown(text: str) -> str:
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def resolve_link(source: Path, target: str, files: list[Path]) -> bool:
    target = target.strip().replace("\\", "/")
    candidates = [
        source.parent / f"{target}.md",
        ROOT / f"{target}.md",
        VAULT / f"{target}.md",
    ]
    if any(candidate.is_file() for candidate in candidates):
        return True
    if "/" in target:
        return False
    matches = [path for path in files if path.stem == target]
    return len(matches) == 1


def check_links(files: list[Path]) -> list[str]:
    broken: list[str] = []
    for source in files:
        text = clean_markdown(source.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if not resolve_link(source, target, files):
                broken.append(f"{source.relative_to(ROOT).as_posix()} -> {target}")
    return sorted(set(broken))


def check_index_coverage() -> list[str]:
    index_text = clean_markdown(INDEX.read_text(encoding="utf-8"))
    missing: list[str] = []
    for path in sorted(VAULT.rglob("*.md")):
        target = path.relative_to(ROOT).with_suffix("").as_posix()
        if f"[[{target}" not in index_text:
            missing.append(target)
    return missing


def check_legacy_refs(files: list[Path]) -> list[str]:
    offenders: list[str] = []
    for path in files:
        text = clean_markdown(path.read_text(encoding="utf-8"))
        if "obsidian-vault/index" in text:
            offenders.append(path.relative_to(ROOT).as_posix())
    return offenders


def check_sensitive() -> list[str]:
    hits: list[str] = []
    allowed_suffixes = {".md", ".py", ".ps1", ".sh", ".toml", ".yaml", ".yml"}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in allowed_suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(pattern.search(text) for pattern in SENSITIVE_PATTERNS):
            hits.append(path.relative_to(ROOT).as_posix())
    return hits


def main() -> int:
    files = markdown_files()
    broken = check_links(files)
    unindexed = check_index_coverage()
    legacy = check_legacy_refs(files)
    sensitive = check_sensitive()

    for label, items in (
        ("broken wikilink", broken),
        ("unindexed snapshot page", unindexed),
        ("legacy index reference", legacy),
        ("possible sensitive content", sensitive),
    ):
        for item in items:
            print(f"{label}: {item}")

    print(
        "Shared-memory gates: "
        f"markdown={len(files)} broken={len(broken)} "
        f"unindexed={len(unindexed)} legacy={len(legacy)} sensitive={len(sensitive)}"
    )
    return 1 if broken or unindexed or legacy or sensitive else 0


if __name__ == "__main__":
    sys.exit(main())
