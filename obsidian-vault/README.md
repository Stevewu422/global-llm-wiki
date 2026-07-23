# ChatGPT × Obsidian 记忆库

这是一个本地优先、人工可审阅的 AI 记忆系统。Obsidian 负责浏览和编辑，ChatGPT/Codex 通过根目录的 `AGENTS.md` 获得读写规则。

## 快速开始

1. 在 Obsidian 中选择“打开本地仓库”，指向本目录。
2. 打开 `Home.md`，从仪表盘进入各区域。
3. 对 ChatGPT 说“记住：……”，它会按类型写入合适位置。
4. 对 ChatGPT 说“从记忆里查……”，它会先读精炼记忆，再按需搜索历史。
5. 定期运行：

```powershell
.\Scripts\memory.ps1 check
```

## 常用命令

```powershell
# 快速捕获一条待整理记忆
.\Scripts\memory.ps1 capture -Text "需要记录的内容" -Topic "主题"

# 全库搜索
.\Scripts\memory.ps1 search -Query "关键词"

# 检查结构、敏感信息风险、长期记忆容量和失效链接
.\Scripts\memory.ps1 check
```

`capture` 只写入 Inbox，不会自动提升为长期记忆。长期记忆应由 ChatGPT 与你共同确认后整理。

## 目录

- `00-System`：用户画像、精炼长期记忆、维护说明
- `06-Projects`：AI Agent 当前活跃项目入口
- `10-Inbox`：未整理、未验证的输入
- `20-Daily`：每日工作记录
- `30-Projects`：项目背景、决策和状态
- `40-Playbooks`：可复用流程
- `80-Templates`：Obsidian 模板
- `90-Archive`：不再活跃但需保留的材料
- `97-AI-Memory`：跨 Agent 的长期经验、决策和最佳实践
- `98-AI-Context`：跨 Agent 的当前任务上下文
- `Scripts`：捕获、搜索和健康检查
