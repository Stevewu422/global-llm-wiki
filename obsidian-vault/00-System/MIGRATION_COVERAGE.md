---
type: migration-coverage
status: completed
updated: 2026-07-23
source_groups: 21
---

# 迁移覆盖矩阵

| # | 历史主题 | 主要目标 | 状态 |
|---:|---|---|---|
| 1 | 用户画像与协作偏好 | `00-System/USER.md` | 已迁移 |
| 2 | 日本保险索赔邮件与中文翻译 | `Insurance-Correspondence` | 已迁移 |
| 3 | INPAY 法中客诉与退款 | `INPAY-Operations` | 已迁移 |
| 4 | RayBan 工作区 SoundWire 排障 | `SoundWire-Audio-Recovery` | 已迁移 |
| 5 | ChatGPT 网页语音伴侣 | `ChatGPT-Voice-RayBan` | 已迁移 |
| 6 | Codex 本机认证诊断 | `Auth-State-Diagnostics` | 已迁移 |
| 7 | Windows 性能与设备排障 | `Windows-Local-Ops` | 已迁移 |
| 8 | 微信进程重启 | `Desktop-App-Control` | 已迁移 |
| 9 | Hermes 远程重启诊断 | `Hermes-Remote-Ops` | 已迁移 |
| 10 | INPAY Logo 设计交付 | `AI-Content-Production` | 已迁移 |
| 11 | Cipay 现有仓库接入 | `Git-Existing-Repository-Connection` | 已迁移 |
| 12 | automation-2 本机维护 | `Windows-Local-Ops` | 已迁移并去重 |
| 13 | Orange Max It 脚本与 APK | `Orange-Max-It` | 已迁移 |
| 14 | Fujifilm 打印排障 | `Printing-Device-Ops` | 已迁移 |
| 15 | inpay2 SoundWire 完整修复 | `SoundWire-Audio-Recovery` | 已迁移并合并 |
| 16 | inpay2 工作区与高风险条款 | `INPAY-Operations` | 已迁移 |
| 17 | Codex 对话查找与导航 | `Codex-Conversation-Management` | 已迁移 |
| 18 | Windows automation 近期运行 | `Windows-Local-Ops` | 已去重，仅保留稳定方法 |
| 19 | QQMusic 本机控制 | `Desktop-App-Control` | 已迁移 |
| 20 | Windows automation 历史运行 | `Windows-Local-Ops` | 已去重，仅保留稳定方法 |
| 21 | World Cup / Polymarket 技能 | `World-Cup-Polymarket` | 已迁移 |

## 排除项

- 重复的每日快照和自动化流水
- 快速过期的 PID、CPU、内存和单次清理量
- 密钥、密码、Token、Cookie、TOTP、设备序列号和私有地址
- 客户联系方式与非必要身份资料
- 未经过重启后复检或用户验收的“已修复”声明

