# Claude Code × Obsidian Memory

本仓库是共享 AI Agent 记忆库。

## 开始任务

1. 读取 `00-System/USER.md`。
2. 读取 `98-AI-Context/CURRENT.md`。
3. 按需读取 `97-AI-Memory/README.md` 和 `06-Projects/` 中的相关项目。
4. 不要一次性载入整个 Vault。

## 更新记忆

只有当任务形成已验证经验、明确决策、稳定工作流、项目推进或最佳实践时才更新。

- 长期经验与决策：`97-AI-Memory/`
- 当前上下文：`98-AI-Context/CURRENT.md`
- 活跃项目：`06-Projects/`
- 详细历史：`30-Projects/`
- 可复用流程：`40-Playbooks/`

禁止保存聊天记录、未验证猜测、凭据、客户身份或私有地址。新内容先去重，写后运行 `.\Scripts\memory.ps1 check`。提交前列出并执行验证命令，发布或推送前取得用户确认。



## 统一入口与读取顺序

- 统一入口：`Home.md`。不得使用或重新生成 the legacy snapshot index file。
- 标准读取顺序：
  1. `00-System/USER.md`
  2. `98-AI-Context/CURRENT.md`
  3. `00-System/MEMORY.md`
  4. 最少的相关项目或长期记忆页面
- GitHub 共享仓库只保存公开安全副本；Vault 是本机唯一记忆读写入口。
