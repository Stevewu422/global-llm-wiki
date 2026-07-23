---
type: project
status: active
last_verified: 2026-07-23
domains: [Programming, INPAY]
---

# Windows 本机运维

## 默认安全边界

- 先诊断和排序，不因“看看原因”就擅自结束进程。
- 未明确授权时，不结束前台应用、浏览器、IDE、数据库、Docker 或同步客户端。
- 资源优化先做真实快照，再做低风险、有限范围清理。

## 性能排查

- 当前 CPU 热点使用 `Win32_PerfFormattedData_PerfProc_Process`，避免用累计 CPU 时间判断瞬时压力。
- 推荐顺序：CPU 热点 → 内存大户 → 磁盘健康 → 是否由临时文件驱动。
- 历史上本机压力多由同步、WMI、浏览器/WebView、Codex 和虚拟化进程共同造成；具体热点必须实时复查。
- 临时目录清理收益低或以 busy/denied 为主时，应停止扩大范围，转向进程驱动的压力分析。

## 音频排查

- 顺序：目标设备链 → 服务 → 静音 → 默认输出 → 驱动/枚举状态。
- `AudioDeviceCmdlets` 可用于读取和切换默认设备。
- `Present=False`、`CM_PROB_PHANTOM` 表明问题可能在设备枚举或驱动层。
- 最终验收以用户明确“可以听见了”为准；重启前后的复检都是完成条件。

## 关联

- [[40-Playbooks/Windows-Safe-Diagnostics]]
- [[50-Domains/编程]]

## 来源

- Codex 历史：Windows performance and device troubleshooting
- Codex 历史：automation/local-windows-maintenance
- Codex 历史：Windows audio troubleshooting

