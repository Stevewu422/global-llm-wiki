---
type: project
status: historical
last_verified: 2026-07-13
domains: [Programming, INPAY]
---

# 打印与设备运维

## 历史场景

- Windows 上 Fujifilm 网络打印机连接和真实作业核验。

## 已验证经验

- 端到端排查顺序：打印对象 → 作业队列 → Spooler → 端口/驱动 → 网络连通 → 设备面板。
- `Get-PrintJob` 能区分“根本没发送”和“Windows 已完成发送”。
- Windows 作业显示完成但没有出纸时，应优先查看缺纸、卡纸、保留作业或认证限制。
- WSD 端口枚举不稳定时，可从 PnP 设备属性恢复真实 IPP 路径。
- 重建打印对象或重启 Spooler 可能需要管理员权限，权限不足时保持只读诊断。

## 关联

- [[obsidian-vault/40-Playbooks/Printer-End-to-End-Verification]]
- [[obsidian-vault/30-Projects/Windows-Local-Ops]]

## 来源

- Codex 历史：Windows printer troubleshooting in inpay2
