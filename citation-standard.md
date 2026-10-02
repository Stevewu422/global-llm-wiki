---
title: Structured Citation Standard
created: 2026-10-02
updated: 2026-10-02
type: concept
tags: [knowledge-base, agent-workflow]
sources: []
confidence: medium
---

# Structured citation fields

This authoring convention extends [[SCHEMA]] and follows [[agents/MEMORY_PROTOCOL]]. Formatting a source does not verify its claims.

Use a frontmatter `citation` list. Every entry requires `id`, `type`, `locator`, and `status`. Map important claims to citation IDs rather than treating a page-level source as proof of every statement.

```yaml
citation: [{"id":"c1","type":"official","locator":"actual-source-url","status":"unverified"}]
```

- Types: official, paper, user, local, legacy.
- Status: unverified, verified, unavailable, disputed.
- Optional fields: title, published_at, accessed_at, verified_at, claim, scope.
- Use ISO dates; omit unknown dates. Record accessed_at only after reading the source, and verified_at only when the evidence supports the mapped claim.
- Legacy migration preserves the original source text and verification dates. Use type=legacy, status=unverified and provenance_status=legacy-transcribed. A migration timestamp is not a verification timestamp.
- Missing sources remain explicit gaps; never invent citations or approvals. Retain conflicting evidence for review.
- Public exports exclude private user records, operational identifiers, private source locations and approval evidence.

## Validation and maintenance

Check required fields, unique IDs, nonempty locators, valid dates and verified_at for verified entries. Report missing citations separately from unverified citations. Strict publication checks fail on missing or malformed citations within the declared scope; they do not claim factual verification merely because syntax passes.

Before batch migration, declare the directories and exclusions, back up each target, preserve its body, and independently read back the result. Skip existing citation metadata rather than silently replacing it. Review source gaps and high-risk unverified claims during periodic memory maintenance. Empty citation lists are allowed only in blank templates.

This page publishes the reusable convention only, not private migration reports or historical source records.
