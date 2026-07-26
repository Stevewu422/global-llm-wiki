---
type: system-mode
status: active
updated: 2026-07-26
---

# Obsidian 统一长期记忆模式

## 结论

本机长期记忆以 `/root/obsidian-vault` 为唯一读写入口；GitHub `global-llm-wiki` 只保存经过验证、可移植、无敏感信息的公开安全副本。

## 统一入口

所有 Agent 从 `Home.md` 进入，不使用 the legacy snapshot index file。

## 读取顺序

1. `00-System/USER.md`
2. `98-AI-Context/CURRENT.md`
3. `00-System/MEMORY.md`
4. 最少的相关项目、领域、Playbook 或长期记忆页面

## 写入边界

- Vault 是本机唯一记忆读写入口。
- 公开 GitHub 副本只接收安全导出。
- 禁止导出 `USER.md`、`MEMORY.md`、`CURRENT.md`、`10-Inbox/`、`20-Daily/`、`Deploy/`、`Scripts/`、凭据、地址、服务器私有事实和完整聊天。
- 任何同步前必须保持工作树洁净，使用 `fetch` + `merge --ff-only`，禁止 `reset --hard`、force push、自动 stash、静默覆盖。
