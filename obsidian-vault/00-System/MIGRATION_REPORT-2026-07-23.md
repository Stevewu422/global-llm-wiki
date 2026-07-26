---
type: migration-report
status: completed
date: 2026-07-23
source: codex-memory-and-global-llm-wiki
---

# 历史知识迁移报告

## 结论

已将过去 ChatGPT/Codex 记忆中的高复用知识提炼到当前 Obsidian Vault。采用主题提炼而非整包复制，历史任务流水和敏感内容没有进入长期知识层。

## 数据源

- Codex 记忆注册表：`C:\Users\wuyun\.codex\memories\MEMORY.md`
- Codex rollout summaries：仅用于核对来源，不整包复制
- GitHub Wiki：[Stevewu422/global-llm-wiki](https://github.com/Stevewu422/global-llm-wiki)
- 当前 Vault 已确认的 `USER.md` 和领域设置

## 注入结果

- 用户偏好：保留在 `00-System/USER.md`
- 核心长期记忆：压缩保留在 `00-System/MEMORY.md`
- 历史项目：5 个结构化项目页
- 研究领域：6 个领域页补充已验证知识
- 可复用方法：4 个 playbook
- GitHub Wiki：保留为外部权威源，避免产生双份 canonical 数据

## 安全过滤

以下内容未迁移：

- 密钥、Token、Cookie、TOTP、二维码和登录材料
- 私有服务器地址及客户身份信息
- 单次 CPU、内存、清理量等快速过期状态
- 未取得用户验收的故障结论
- 重复的自动化运行流水

## 状态规则

- 历史事实只代表当时已验证结果，不代表当前状态。
- 使用项目知识前，应重新检查路径、仓库状态、设备状态或线上数据。
- 新知识继续遵循 `[[MEMORY_POLICY]]`。
