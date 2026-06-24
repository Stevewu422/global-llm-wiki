---
title: LLM Wiki Implementations
created: 2026-06-25
updated: 2026-06-25
type: comparison
tags: [llm-wiki, comparison, skill, tooling, codex, openclaw]
sources: [raw/articles/2026-06-25-llm-wiki-landscape.md]
confidence: medium
---

# LLM Wiki Implementations

This page compares four implementation styles built on the [[llm-wiki-pattern]].

| Implementation | Best at | Shape | Practical lesson |
| --- | --- | --- | --- |
| [[kfchou-wiki-skills]] | Clear workflow decomposition | Skill set | Split wiki work into stable named actions |
| [[ndjordjevic-pin-llm-wiki]] | Deferred source intake | Queue pipeline | Use inbox-first collection when links arrive faster than they can be ingested |
| [[lewislulu-llm-wiki-skill]] | OpenClaw/Codex + review loop | Skill plus tooling | Build correction and audit into the workflow, not just generation |
| [[nashsu-llm-wiki]] | Full end-user product | Desktop app | Add UI, queueing, graph, and APIs when the wiki becomes a daily tool |

## Recommendation For This Repo

For this INPAY workspace, the most useful hybrid is:

- keep the Karpathy core layout from [[llm-wiki-pattern]]
- borrow queue and `inbox.md` ideas from [[ndjordjevic-pin-llm-wiki]]
- borrow explicit lint and audit discipline from [[kfchou-wiki-skills]]
- borrow review-centric thinking from [[lewislulu-llm-wiki-skill]]
- borrow `purpose.md` and product-shape thinking from [[nashsu-llm-wiki]]

That hybrid is what this local implementation is trying to realize.
