---
type: active-project
status: active
updated: 2026-07-30
domains: [AI, Programming]
---

# Obsidian AI Agent 记忆系统

## 目标

搭建可扩展、可审阅、支持多 Agent、支持 GitHub 同步和知识图谱的 Obsidian 知识库。

## 当前状态

- Vault 已建立并可在 Obsidian 中打开。
- Codex、Claude Code、Cursor 已有统一入口规则。
- 历史知识迁移覆盖 21/21 个主题。
- 健康检查支持目录、容量、敏感信息和 Wiki 链接。
- GitHub 共享仓库已发布并与 Hermes 通过 ff-only 同步。
- 六小时 cron 已修正 Vault/共享仓库的不同安全模型：Vault 可为非版本化
  权威库，只有共享仓库和 Hermes clone 必须满足 Git 工作树洁净。
- Python 语法检查改为 AST 解析，字节码缓存不会再污染同步工作树。

## 下一步

- 观察六小时 cron 的下一次自然触发及 no-op 行为。
- 人工抽查历史分类和领域图谱。
- 后续任务形成稳定经验时自动更新长期记忆。

## 验收

```powershell
.\Scripts\memory.ps1 check
.\Scripts\memory.ps1 preflight
git diff --check
```

## 关联

- README
- CURRENT
- HISTORY_CATALOG
