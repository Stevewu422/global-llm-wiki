---
type: ai-memory-index
status: active
updated: 2026-07-23
agents: [Codex, Claude-Code, Cursor]
---

# AI Agent 长期记忆

本目录只保存未来会影响判断或执行方式的长期信息，不保存聊天记录。

## 当前模式

- 记忆主库：`/root/obsidian-vault`。
- Hermes 注入层：`/root/.hermes/memories/USER.md` 与 `MEMORY.md` 已软链接到 `00-System/USER.md` 与 `00-System/MEMORY.md`。
- 详细事实、项目知识、SOP 和历史归档全部下沉到本 Vault，不塞进每轮注入层。
- 状态核查：`python3 /root/.hermes/scripts/obsidian_memory_status.py`。

## 读取入口

- [[DECISIONS|长期决策]]
- [[BEST-PRACTICES|最佳实践]]
- 用户偏好
- 核心记忆路由
- 历史知识总目录
- 可复用工作流
- 研究领域

## 写入条件

满足以下任一条件才写入：

- 已验证并可复用的经验
- 会影响后续执行的明确决策
- 稳定工作流或最佳实践
- 项目跨阶段仍需保留的约束

## 禁止内容

- 聊天全文和逐轮对话
- 临时状态、一次性命令输出和未验证猜测
- 密钥、密码、Token、Cookie、TOTP、二维码、客户身份或私有地址

## 更新流程

1. 搜索现有记忆并去重。
2. 核对来源、有效期和适用范围。
3. 写入最小必要结论并链接详细页面。
4. 更新 `98-AI-Context/CURRENT.md` 或项目状态。
5. 在服务器上运行 `bash /root/obsidian-vault/Scripts/server-memory-check.sh`；Windows 本地副本才使用 `.\Scripts\memory.ps1 check`。


## Hermes 原记忆迁入通用页

- 通用遗留记忆

## 外部知识源

- [[Global-LLM-Wiki|Global LLM Wiki：跨项目 LLM/Obsidian 记忆知识源]]
