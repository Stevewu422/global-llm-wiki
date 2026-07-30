---
type: ai-memory-decisions
status: active
updated: 2026-07-30
---

# 长期决策

## 知识架构

- Obsidian Vault 是本机 AI Agent 的可审阅记忆入口。
- `97-AI-Memory` 保存长期经验和决策；`98-AI-Context` 保存当前上下文；`06-Projects` 保存活跃项目状态。
- 详细历史和证据保留在 `30-Projects`、`40-Playbooks`、`50-Domains` 和 `90-Archive`，不复制到核心记忆。
- GitHub `Stevewu422/global-llm-wiki` 是跨项目 LLM Wiki 的外部权威知识源。
- 本机 Vault 可以是非版本化权威库；若 `.git` 没有 HEAD 且 tracked 文件
  为 0，不把全部 Vault 页面误判为未知 Git 修改，也不自动初始化或提交。
- 只有可移植共享仓库和 Hermes clone 必须满足 Git 工作树洁净。

## 执行边界

- 配置和后台变更采用：备份 → 修改 → 回读 → 验证。
- 工具返回成功不代表任务完成，以用户可见结果或验收命令为准。
- 发布、外发和不可逆动作需要用户确认。
- 未明确授权时，不擅自结束前台应用、重启设备或扩大操作范围。
- Hermes 严格 SSH 成功后仍需远端仓库、备份和入口预检明确完成，不能只凭
  连接成功放行写入。

## 信息安全

- 记忆库不保存凭据、客户身份、完整支付信息或私有后端地址。
- 历史快照不冒充当前状态；易变化事实使用前必须重新验证。
