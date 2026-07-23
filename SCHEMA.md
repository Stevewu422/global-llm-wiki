# Wiki Schema

## Domain
This wiki covers INPAY's AI operating system, knowledge workflows, reusable skills,
Hermes/Codex/OpenClaw collaboration patterns, and external LLM Wiki approaches that
help the team build a durable internal knowledge base.

## Conventions
- File names: lowercase, hyphens, no spaces.
- Every wiki page starts with YAML frontmatter.
- Use `[[wikilinks]]` for internal links; target at least 2 outbound links per page.
- When updating a page, bump `updated`.
- Every new page must be listed in `index.md`.
- Every change must be appended to `log.md`.
- Use provenance markers like `^[raw/articles/file.md]` on synthesis-heavy pages.

### Portable Obsidian Vault Snapshot

The `obsidian-vault/` directory is a public-safe portable snapshot of an existing
Obsidian vault. It may preserve native vault directory names, Unicode file names,
and established frontmatter types so internal wikilinks remain stable.

- Its complete page catalog lives in `obsidian-vault/index.md`.
- Every exported page is also listed from the root `index.md`.
- Private user context, credentials, endpoints, workspace state, caches, backups,
  and machine-specific deployment files must be excluded before export.
- New root wiki pages outside this snapshot continue to follow lowercase,
  hyphenated filenames and the standard frontmatter schema.

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [tag-a, tag-b]
sources: [raw/articles/source-file.md]
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

## Raw Frontmatter
```yaml
---
source_url: https://example.com
ingested: YYYY-MM-DD
sha256: <body sha256>
---
```

## Tag Taxonomy
- `llm-wiki`
- `knowledge-base`
- `rag-alternative`
- `agent-workflow`
- `codex`
- `openclaw`
- `hermes`
- `inpay`
- `research`
- `ingest`
- `query`
- `lint`
- `audit`
- `comparison`
- `tooling`
- `desktop-app`
- `obsidian`
- `mcp`
- `skill`
- `operations`

Rule: only use tags from this list. Add new tags here before using them elsewhere.

## Page Thresholds
- Create a page when a concept/entity is central to one source or repeated across 2+ sources.
- Update existing pages instead of duplicating.
- Do not create pages for passing mentions.
- Split pages over ~200 lines.

## Entity Pages
Entity pages should explain what the thing is, where it fits, and how it relates to
other tools, skills, or workflows.

## Concept Pages
Concept pages should define the concept, explain the current implementation state,
and link to related entities and comparisons.

## Comparison Pages
Comparison pages should use tables when possible and end with a practical recommendation.

## Update Policy
When sources conflict:
1. Prefer newer, better-supported sources.
2. Note both positions with dates and source references.
3. Set `contested: true` and add `contradictions:` if needed.
4. Surface the issue in lint output.
