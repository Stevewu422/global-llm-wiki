---
type: memory-mode
status: active
updated: 2026-07-23
---

# Obsidian 统一记忆模式

## 权威模型

- 本 Vault 是本机 AI Agent 的唯一记忆读写界面。
- GitHub `Stevewu422/global-llm-wiki` 是可移植共享副本和同步源，不建立第二套内容结构。
- Codex、Claude Code、Cursor 等工具自身的 memory 只允许保存入口、索引和机器私有路由，不再保存与 Vault 重复的长期知识。
- `Home.md` 是人类入口；`AGENTS.md` 是 Agent 入口；`00-System/MEMORY.md` 是精炼路由；`98-AI-Context/CURRENT.md` 是当前状态。

## 读取流程

1. 读取 `00-System/USER.md`。
2. 读取 `98-AI-Context/CURRENT.md`。
3. 从 `00-System/MEMORY.md` 或 `97-AI-Memory/README.md` 路由到最少的相关页面。
4. 只在需要证据时搜索 Inbox、Daily 和 Archive。
5. 时间敏感事实必须现场复核，不把历史快照当实时状态。

## 写入流程

1. 仅在用户明确要求记住，或任务形成已验证、可复用、会影响后续工作的结果时写入。
2. 写入前搜索去重；冲突事实保留双方来源并请求裁决。
3. 临时或未验证内容进入 `10-Inbox/`，不直接进入长期记忆。
4. 写入后回读，并运行 `.\Scripts\memory.ps1 check`。
5. 提交前列出并执行验证命令；推送、发布或外发前获得用户确认。

## 内容路由

- 用户偏好与审批边界 → `00-System/USER.md`
- 精炼事实与导航 → `00-System/MEMORY.md`
- 跨项目决策与最佳实践 → `97-AI-Memory/`
- 当前任务状态 → `98-AI-Context/CURRENT.md`
- 活跃项目 → `06-Projects/`
- 项目详情与历史 → `30-Projects/`
- 已重复验证的流程 → `40-Playbooks/`
- 领域知识 → `50-Domains/`
- 未验证材料 → `10-Inbox/`

## 禁止事项

- 不保存聊天全文、一次性输出、可随时重查的数据或未经验证的猜测。
- 不保存密码、密钥、Token、Cookie、TOTP、二维码、完整支付信息、客户身份或私有后端地址。
- 不让多个 Agent 在各自私有记忆中维护互相冲突的长期事实。
