---
type: project
status: historical
last_verified: 2026-07-12
domains: [AI, Programming]
---

# ChatGPT 语音与 RayBan

## 项目范围

- Windows 独立 ChatGPT 网页语音窗口
- RayBan/手机连接工作区的音频链排障
- 浏览器登录态、麦克风权限和桌面快捷方式

## 已验证经验

- 修改“ChatGPT App 行为”前必须先确认目标是安装的应用、网页还是某个代码仓库。
- 进程名不能单独证明应用身份，应结合系统安装包信息和配置。
- 用户接受网页认证时，可采用浏览器 app mode；首次登录和麦克风授权仍需用户完成。
- Windows PowerShell 5 在中文 OneDrive 路径下存在编码兼容问题，启动脚本和快捷方式可采用 ASCII 文件名及显式 UTF-8 读取。
- 用户说“你直接运行吧”时，默认由代理直接执行并验证，而不是继续往返教学命令。

## 音频验收

- 音频命令成功不代表用户听得见。
- 用户点名 SoundWire 后，应转到对应设备枚举和驱动链，而不是持续切换无关默认输出。

## 关联

- [[obsidian-vault/40-Playbooks/SoundWire-Audio-Recovery]]
- [[obsidian-vault/40-Playbooks/Auth-State-Diagnostics]]
- [[obsidian-vault/30-Projects/AI-Agent-Ecosystem]]

## 来源

- Codex 历史：ChatGPT web voice companion
- Codex 历史：Windows audio troubleshooting in rayban手机连接
