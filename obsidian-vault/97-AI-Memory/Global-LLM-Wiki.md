---
type: external-knowledge-source
status: active
updated: 20260726
source_url: https://github.com/Stevewu422/global-llm-wiki
---

# Global LLM Wiki

## 结论

`Stevewu422/global-llm-wiki` 已下载到本机并作为 Obsidian 长期记忆的外部知识源接入。

- 共享 Git 仓库：`Stevewu422/global-llm-wiki`
- 公共快照入口：`obsidian-vault/Home.md`

## 用途

这个仓库是跨项目 LLM Wiki / Obsidian AI memory 的公开安全版本，适合沉淀：

- Hermes / Codex / OpenClaw 协作模式
- LLM Wiki 与 Markdown 长期知识库方法
- 可复用 workflow、tool comparison、operating notes
- 从聊天和项目中提炼出来、未来可复用的高信号知识

## 使用入口

- 仓库说明：[[README|README]]
- Schema：[[SCHEMA|SCHEMA]]
- Agent Guide：[[AGENTS|AGENTS]]
- Wiki Index：[[index|Wiki Index]]
- Public Obsidian Snapshot：[[obsidian-vault/Home|Obsidian Vault Home]]
- LLM Wiki Pattern：[[concepts/llm-wiki-pattern|llm-wiki-pattern]]
- Implementations Comparison：[[comparisons/llm-wiki-implementations|llm-wiki-implementations]]

## 并入当前 Obsidian 记忆后的规则

1. 不把该仓库全文塞进 `00-System/USER.md` 或 `00-System/MEMORY.md`，避免每轮注入过重。
2. 高频只保留这个索引页；需要细节时按链接读取共享 Git 仓库。
3. 如果后续要吸收其中某个 workflow，先验证，再精炼到 `40-Playbooks/` 或 `97-AI-Memory/`。
4. 该仓库是公开安全版本；仍要继续执行密钥检查，禁止把私密地址、凭据、二维码并入公开 Wiki。

## 同步命令

同步必须使用仓库内的 `tools/sync-agent-memory.ps1` 或
`tools/sync-agent-memory.sh`，并坚持 fast-forward only、完整门禁和发布回读。
