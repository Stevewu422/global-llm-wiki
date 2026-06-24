#!/usr/bin/env python
"""Minimal repo-local LLM Wiki helper."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple


DEFAULT_WIKI = Path.home() / "wiki"
REQUIRED_DIRS = [
    "raw/articles",
    "raw/papers",
    "raw/transcripts",
    "raw/assets",
    "entities",
    "concepts",
    "comparisons",
    "queries",
]
REQUIRED_FILES = ["SCHEMA.md", "purpose.md", "index.md", "log.md", "inbox.md", "AGENTS.md"]
PAGE_DIRS = ["entities", "concepts", "comparisons", "queries"]
RAW_PREFIX = "---\nsource_url:"
PAGE_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
INDEX_ENTRY_RE = re.compile(r"\[\[([^\]]+)\]\]")


def wiki_path(path_arg: str | None) -> Path:
    return Path(path_arg).resolve() if path_arg else DEFAULT_WIKI


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def ensure_tree(root: Path) -> None:
    for rel in REQUIRED_DIRS:
        (root / rel).mkdir(parents=True, exist_ok=True)


def queue_sources(root: Path, sources: List[str]) -> int:
    inbox = root / "inbox.md"
    content = read_text(inbox).splitlines()
    existing = {line[6:] for line in content if line.startswith("- [ ] ")}
    added = 0
    for source in sources:
        if source not in existing:
            content.append(f"- [ ] {source}")
            existing.add(source)
            added += 1
    write_text(inbox, "\n".join(content).rstrip() + "\n")
    return added


def parse_frontmatter(text: str) -> Dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}
    block = parts[0].splitlines()[1:]
    data: Dict[str, str] = {}
    for line in block:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def markdown_pages(root: Path) -> List[Path]:
    files: List[Path] = []
    for folder in PAGE_DIRS:
        files.extend(sorted((root / folder).glob("*.md")))
    return files


def slug_map(root: Path) -> Dict[str, Path]:
    return {path.stem: path for path in markdown_pages(root)}


def index_slugs(root: Path) -> Set[str]:
    text = read_text(root / "index.md")
    return set(INDEX_ENTRY_RE.findall(text))


def schema_tags(root: Path) -> Set[str]:
    tags: Set[str] = set()
    in_taxonomy = False
    for line in read_text(root / "SCHEMA.md").splitlines():
        if line.strip() == "## Tag Taxonomy":
            in_taxonomy = True
            continue
        if in_taxonomy and line.startswith("## "):
            break
        if in_taxonomy and line.startswith("- `") and line.endswith("`"):
            tags.add(line[3:-1])
    return tags


def orphan_and_broken_links(root: Path) -> Tuple[Dict[str, int], List[str]]:
    pages = slug_map(root)
    inbound = {slug: 0 for slug in pages}
    broken: List[str] = []
    for path in pages.values():
        for match in PAGE_LINK_RE.findall(read_text(path)):
            target = match.strip()
            if target in inbound:
                inbound[target] += 1
            else:
                broken.append(f"{path.relative_to(root)} -> [[{target}]]")
    return inbound, broken


def sha256_body(path: Path) -> str:
    text = read_text(path)
    if text.startswith("---\n") and "\n---\n" in text:
        body = text.split("\n---\n", 1)[1]
    else:
        body = text
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def lint(root: Path) -> int:
    issues: List[str] = []

    for rel in REQUIRED_DIRS:
        if not (root / rel).exists():
            issues.append(f"missing directory: {rel}")
    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            issues.append(f"missing file: {rel}")

    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1

    known_tags = schema_tags(root)
    pages = markdown_pages(root)
    page_slugs = set(slug_map(root))
    indexed = index_slugs(root)
    inbound, broken = orphan_and_broken_links(root)

    for path in pages:
        text = read_text(path)
        frontmatter = parse_frontmatter(text)
        for field in ["title", "created", "updated", "type", "tags", "sources"]:
            if field not in frontmatter:
                issues.append(f"{path.relative_to(root)} missing frontmatter field: {field}")
        if path.stem not in indexed:
            issues.append(f"{path.relative_to(root)} missing from index.md")
        if len(text.splitlines()) > 220:
            issues.append(f"{path.relative_to(root)} exceeds 220 lines")
        tag_value = frontmatter.get("tags", "")
        for tag in re.findall(r"[A-Za-z0-9_-]+", tag_value):
            if tag not in known_tags:
                issues.append(f"{path.relative_to(root)} uses unknown tag: {tag}")

    for slug, count in sorted(inbound.items()):
        if count == 0:
            issues.append(f"orphan page: {slug}")
    for item in broken:
        issues.append(f"broken wikilink: {item}")
    for slug in sorted(indexed - page_slugs):
        issues.append(f"index.md references missing page: {slug}")

    for path in sorted((root / "raw").rglob("*.md")):
        text = read_text(path)
        if not text.startswith(RAW_PREFIX):
            issues.append(f"{path.relative_to(root)} missing raw frontmatter")
            continue
        frontmatter = parse_frontmatter(text)
        expected = frontmatter.get("sha256")
        actual = sha256_body(path)
        if expected and expected != actual:
            issues.append(f"{path.relative_to(root)} sha256 mismatch")

    if issues:
        for issue in issues:
            print(f"ISSUE: {issue}")
        print(f"\nLint complete: {len(issues)} issue(s) found.")
        return 1

    print("Lint complete: no issues found.")
    return 0


def status(root: Path) -> int:
    pages = markdown_pages(root)
    raw_files = sorted((root / "raw").rglob("*.md"))
    inbox_lines = [line for line in read_text(root / "inbox.md").splitlines() if line.startswith("- [ ] ")]
    print(f"Wiki path: {root}")
    print(f"Pages: {len(pages)}")
    print(f"Raw sources: {len(raw_files)}")
    print(f"Inbox items: {len(inbox_lines)}")
    print(f"Last checked: {dt.datetime.now().isoformat(timespec='seconds')}")
    return 0


def cmd_init(root: Path) -> int:
    ensure_tree(root)
    print(f"Wiki tree ensured at: {root}")
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Repo-local LLM Wiki helper")
    parser.add_argument("--wiki", help="Override wiki path")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="Ensure the wiki directory tree exists")

    queue = sub.add_parser("queue", help="Append source URLs or notes to inbox.md")
    queue.add_argument("sources", nargs="+", help="Source URL(s) or notes to queue")

    sub.add_parser("lint", help="Validate structure, links, frontmatter, and raw hashes")
    sub.add_parser("status", help="Show simple wiki counts")

    args = parser.parse_args()
    root = wiki_path(args.wiki)

    if args.command == "init":
        return cmd_init(root)
    if args.command == "queue":
        added = queue_sources(root, args.sources)
        print(f"Queued {added} new source(s) in {root / 'inbox.md'}")
        return 0
    if args.command == "lint":
        return lint(root)
    if args.command == "status":
        return status(root)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
