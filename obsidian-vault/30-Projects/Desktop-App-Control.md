---
type: project
status: historical
last_verified: 2026-07-15
domains: [Programming]
---

# 桌面应用控制

## 历史场景

- 微信残留登录态下的定向重启
- QQMusic 播放停止
- Windows 本机应用的启动、停止和结果核验

## 已验证经验

- 用户只要求启动应用时，应直接定位真实可执行文件并拉起，不扩大排障范围。
- 登录态残留可能存在于主进程和辅助进程；用户明确要求彻底重启时，应枚举目标应用的相关进程后定向结束。
- 媒体停止先尝试最小控制；只有用户明确同意后才升级为定向结束播放器进程。
- 不使用宽泛进程名匹配批量结束其他程序。
- 启动后通过目标进程和窗口标题做 post-check。

## 关联

- [[40-Playbooks/Desktop-Process-Targeted-Restart]]
- [[30-Projects/Windows-Local-Ops]]

## 来源

- Codex 历史：windows-desktop-process-management
- Codex 历史：desktop media control

