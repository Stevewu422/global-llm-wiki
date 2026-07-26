---
type: active-project
status: active
updated: 2026-07-23
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
- GitHub remote 已连接，尚未推送。

## 下一步

- 人工抽查历史分类和领域图谱。
- 需要时配置 Git 提交和同步流程。
- 后续任务形成稳定经验时自动更新长期记忆。

## 验收

```powershell
.\Scripts\memory.ps1 check
git diff --check
```

## 关联

- README
- CURRENT
- HISTORY_CATALOG
