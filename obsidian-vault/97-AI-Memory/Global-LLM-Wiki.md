---
type: external-knowledge-source
status: active
updated: 20260724-001155
source_url: https://github.com/Stevewu422/global-llm-wiki
local_repo: /root/source-repos/global-llm-wiki
archived_copy: 90-Archive/External/global-llm-wiki
commit: c227d1dbb4ca15d85e6cc81071b99ffdb0080840
---

# Global LLM Wiki

## 结论

`Stevewu422/global-llm-wiki` 已下载到本机并作为 Obsidian 长期记忆的外部知识源接入。

- 本地 Git 仓库：`/root/source-repos/global-llm-wiki`
- Obsidian 归档副本：`90-Archive/External/global-llm-wiki`
- 当前 commit：`c227d1d` / `c227d1dbb4ca15d85e6cc81071b99ffdb0080840`
- Markdown 文件数：61
- 总文件数：64

## 用途

这个仓库是跨项目 LLM Wiki / Obsidian AI memory 的公开安全版本，适合沉淀：

- Hermes / Codex / OpenClaw 协作模式
- LLM Wiki 与 Markdown 长期知识库方法
- 可复用 workflow、tool comparison、operating notes
- 从聊天和项目中提炼出来、未来可复用的高信号知识

## 使用入口

- 仓库说明：[[90-Archive/External/global-llm-wiki/README|README]]
- Schema：[[90-Archive/External/global-llm-wiki/SCHEMA|SCHEMA]]
- Agent Guide：[[90-Archive/External/global-llm-wiki/AGENTS|AGENTS]]
- Wiki Index：[[90-Archive/External/global-llm-wiki/index|Wiki Index]]
- Public Obsidian Snapshot：[[90-Archive/External/global-llm-wiki/obsidian-vault/index|Obsidian Vault Index]]
- LLM Wiki Pattern：[[90-Archive/External/global-llm-wiki/concepts/llm-wiki-pattern|llm-wiki-pattern]]
- Implementations Comparison：[[90-Archive/External/global-llm-wiki/comparisons/llm-wiki-implementations|llm-wiki-implementations]]

## 并入当前 Obsidian 记忆后的规则

1. 不把该仓库全文塞进 `00-System/USER.md` 或 `00-System/MEMORY.md`，避免每轮注入过重。
2. 高频只保留这个索引页和路径；需要细节时按链接读取归档副本或本地 Git 仓库。
3. 如果后续要吸收其中某个 workflow，先验证，再精炼到 `40-Playbooks/` 或 `97-AI-Memory/`。
4. 该仓库是公开安全版本；仍要继续执行密钥检查，禁止把私密地址、凭据、二维码并入公开 Wiki。

## 同步命令

```bash
cd /root/source-repos/global-llm-wiki
git pull --rebase origin main
```

同步后如需刷新 Obsidian 归档副本，重新复制到：

```text
/root/obsidian-vault/90-Archive/External/global-llm-wiki
```
