---
type: active-project
status: active
updated: 2026-08-03
domains: [AI, Programming]
---

# Obsidian AI Agent 记忆系统

## 目标

搭建可扩展、可审阅、支持多 Agent、支持 GitHub 同步和知识图谱的 Obsidian 知识库。

## 当前状态

- 已统一为 Obsidian 单一读写界面，GitHub 仅承担可移植共享与同步。
- 本机和 Hermes 健康检查已覆盖模式契约、入口漂移、YAML、敏感信息和 Wiki 链接。
- Vault 已建立并可在 Obsidian 中打开。
- Codex、Claude Code、Cursor 已有统一入口规则。
- 历史知识迁移覆盖 21/21 个主题。
- 健康检查支持目录、容量、敏感信息和 Wiki 链接。
- GitHub 共享仓库已发布并与 Hermes 通过 ff-only 同步。
- 六小时 cron 已修正 Vault/共享仓库的不同安全模型：Vault 可为非版本化
  权威库，只有共享仓库和 Hermes clone 必须满足 Git 工作树洁净。
- Python 语法检查改为 AST 解析，字节码缓存不会再污染同步工作树。
- Codex 六小时任务已改用本地固定运行手册和 Hermes 固定只读预检脚本，
  不再拼接复杂的 PowerShell→SSH→Unix shell 命令。
- Codex 整轮任务已增加两小时陈旧门限的原子锁，并使用每轮唯一 Owner ID；
  重叠实例不能释放当前实例的锁。
- Hermes 预检已现场验证输出真实仓库双哈希及 `REMOTE_PREFLIGHT_OK`；
  本机、GitHub 与 Hermes 当前均为 `b3d8973`。

## 下一步

- 观察 2026-08-03 下一次六小时 cron 的自然触发，确认固定预检、Owner锁、
  no-op 和锁释放行为。
- 人工抽查历史分类和领域图谱。
- 后续任务形成稳定经验时自动更新长期记忆。

## 验收

```powershell
.\Scripts\memory.ps1 check
.\Scripts\memory.ps1 preflight
git diff --check
```

## 关联

- [[97-AI-Memory/README]]
- CURRENT（本机私有入口，不进入公开共享副本）
- [[00-System/HISTORY_CATALOG]]
- [[00-System/OBSIDIAN_MEMORY_MODE]]
