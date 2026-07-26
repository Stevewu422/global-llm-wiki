#!/usr/bin/env python3
"""Read-only publication gates for the shared Obsidian memory snapshot.

The shared repo is public-safe and Home-rooted. This checker intentionally fails
on legacy obsidian-vault/index.md, broken wiki links, unindexed exported pages,
and obvious credential/private patterns.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "obsidian-vault"
ROOT_INDEX = ROOT / "index.md"

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
SENSITIVE_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{16,}", re.IGNORECASE),
    re.compile(r"(?:api[_-]?key|password|passwd|token|secret)\s*[:=]\s*\S+", re.IGNORECASE),
    re.compile(r"authorization\s*:\s*bearer\s+\S+", re.IGNORECASE),
    re.compile(r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY", re.IGNORECASE),
    re.compile(r"(?<![A-Za-z0-9])(?:\d{1,3}\.){3}\d{1,3}(?![A-Za-z0-9])"),
)
FORBIDDEN_EXPORTS = {
    "obsidian-vault/index.md",
    "obsidian-vault/00-System/USER.md",
    "obsidian-vault/00-System/MEMORY.md",
    "obsidian-vault/98-AI-Context/CURRENT.md",
}
FORBIDDEN_EXPORT_PREFIXES = (
    "obsidian-vault/10-Inbox/",
    "obsidian-vault/20-Daily/",
    "obsidian-vault/Deploy/",
    "obsidian-vault/Scripts/",
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
        text = clean_markdown(source.read_text(encoding="utf-8", errors="ignore"))
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if not resolve_link(source, target, files):
                broken.append(f"{source.relative_to(ROOT).as_posix()} -> {target}")
    return sorted(set(broken))


def check_index_coverage() -> list[str]:
    index_text = clean_markdown(ROOT_INDEX.read_text(encoding="utf-8", errors="ignore"))
    missing: list[str] = []
    for path in sorted(VAULT.rglob("*.md")):
        rel = path.relative_to(ROOT).with_suffix("").as_posix()
        rel_md = path.relative_to(ROOT).as_posix()
        if rel_md == "obsidian-vault/EXPORT_MANIFEST.md":
            continue
        if f"[[{rel}" not in index_text:
            missing.append(rel)
    return missing


def check_legacy_refs(files: list[Path]) -> list[str]:
    offenders: list[str] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        text = clean_markdown(path.read_text(encoding="utf-8", errors="ignore"))
        if rel == "obsidian-vault/index.md" or "obsidian-vault/index" in text:
            offenders.append(rel)
    return sorted(set(offenders))


def check_forbidden_exports() -> list[str]:
    hits: list[str] = []
    for path in sorted(VAULT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in FORBIDDEN_EXPORTS or any(rel.startswith(prefix) for prefix in FORBIDDEN_EXPORT_PREFIXES):
            hits.append(rel)
    return hits


def check_sensitive() -> list[str]:
    hits: list[str] = []
    allowed_suffixes = {".md", ".py", ".ps1", ".sh", ".toml", ".yaml", ".yml"}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in allowed_suffixes:
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = clean_markdown(path.read_text(encoding="utf-8", errors="ignore"))
        if any(pattern.search(text) for pattern in SENSITIVE_PATTERNS):
            hits.append(rel)
    return hits


def main() -> int:
    files = markdown_files()
    required = [
        "agents/shared.md",
        "agents/claude.md",
        "agents/codex.md",
        "agents/hermes.md",
        "agents/MEMORY_PROTOCOL.md",
        "obsidian-vault/Home.md",
        "tools/check-shared-memory.py",
        "tools/sync-agent-memory.sh",
    ]
    missing_required = [rel for rel in required if not (ROOT / rel).is_file()]
    broken = check_links(files)
    unindexed = check_index_coverage()
    legacy = check_legacy_refs(files)
    forbidden = check_forbidden_exports()
    sensitive = check_sensitive()

    for label, items in (
        ("missing required file", missing_required),
        ("broken wikilink", broken),
        ("unindexed snapshot page", unindexed),
        ("legacy index reference", legacy),
        ("forbidden exported private path", forbidden),
        ("possible sensitive content", sensitive),
    ):
        for item in items:
            print(f"{label}: {item}")

    print(
        "Shared-memory gates: "
        f"markdown={len(files)} broken={len(broken)} unindexed={len(unindexed)} "
        f"legacy={len(legacy)} forbidden={len(forbidden)} sensitive={len(sensitive)}"
    )
    return 1 if missing_required or broken or unindexed or legacy or forbidden or sensitive else 0


if __name__ == "__main__":
    sys.exit(main())
