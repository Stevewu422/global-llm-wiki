---
title: AI Memory Maintenance Policy
created: 2026-07-23
updated: 2026-07-23
type: summary
tags: [obsidian, knowledge-base, agent-workflow]
sources: []
confidence: high
contested: false
contradictions: []
---

# 维护规则

## 记忆生命周期

1. 捕获：原始内容进入 Inbox 或 Daily。
2. 验证：核对来源、日期和适用范围。
3. 提炼：去掉流水账，只保留未来会影响决策的信息。
4. 归档：写入 USER、MEMORY、Projects 或 Playbooks。
5. 复查：过期内容标为 `stale` 或移入 Archive，不直接抹去证据。

## 值得长期保存

- 稳定偏好和明确审批边界
- 已验证的环境事实和项目约束
- 重要决策及其理由
- 重复出现的故障原因和有效修复
- 做过至少两次、可复用的工作流程

## 不应长期保存

- 一次性任务过程
- 未验证猜测
- 很快过期的状态
- 可从源系统随时重新查询的数据
- 任何凭据或敏感身份信息

## 每月整理

- 运行 `.\Scripts\memory.ps1 check`
- 清空已处理 Inbox
- 检查超过 90 天未验证的事实
- 合并重复条目
- 控制 USER 和 MEMORY 的容量
