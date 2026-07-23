---
type: project
status: active
last_verified: 2026-07-23
domains: [AI, Programming, INPAY]
---

# AI Agent 生态

## 项目范围

- ChatGPT、Codex、Hermes、OpenClaw 和 Telegram 自动化
- 代理记忆、技能库、知识迁移和跨项目协作
- GitHub Wiki 作为可追溯的长期知识层

## 已验证架构

1. 原始材料进入 Inbox/raw，不直接成为长期事实。
2. 经来源核对、去重和有效期判断后，整理到领域、项目或 playbook。
3. 每个结构化页面进入索引，并通过 Wiki 链接连接相关概念。
4. 自动化写入后必须回读；工具成功不等于交付成功。
5. 凭据、私有端点和身份材料永不进入知识库。

## 权威知识源

- 当前 Obsidian Vault：用户偏好、项目记忆和工作上下文
- [global-llm-wiki](https://github.com/Stevewu422/global-llm-wiki)：跨项目 LLM Wiki 模式研究
- Codex memory：历史任务索引和来源证据

## 关键经验

- 判断本机应用身份不能只看进程名，应结合安装包、配置和日志。
- 在错误仓库或错误作用域发现问题后，应先停止、回滚并重新确认目标。
- 网页认证、本地 API 和代理配置属于不同链路，不能在没有证据时混为一谈。

## 关联

- [[50-Domains/AI]]
- [[50-Domains/编程]]
- [[40-Playbooks/Knowledge-Migration]]

## 来源

- Codex 历史：ChatGPT web voice companion
- Codex 历史：local Codex auth diagnostics
- GitHub `Stevewu422/global-llm-wiki`

