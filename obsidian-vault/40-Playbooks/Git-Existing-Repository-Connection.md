---
type: playbook
status: verified
last_verified: 2026-07-23
---

# 连接已有 Git 仓库

## 流程

1. 检查当前目录是否已有 `.git`。
2. 回读 `git status --short --branch` 和 `git remote -v`。
3. 无 remote 时添加用户指定的真实地址。
4. `git fetch` 后检查远程默认分支。
5. 只有确认不会覆盖本地改动后，才 checkout、merge 或 rebase。
6. 推送前运行验证并获得发布确认。

## 验收

```powershell
git status --short --branch
git remote -v
git log -1 --oneline --decorate
```
