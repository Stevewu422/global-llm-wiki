---
type: project
status: historical
last_verified: 2026-06-26
domains: [AI, Programming, INPAY]
---

# Hermes 远程运维

## 历史场景

- 从 Windows 工作区诊断远程 Hermes/Linux 主机重启失败。
- TCP 端口可达，但 SSH 在认证前无法返回协议 banner。

## 已验证经验

- 必须区分三层：TCP 可达、SSH banner 正常、认证成功。
- TCP 端口打开不代表能够执行远程命令。
- 不同 SSH 客户端都卡在 banner 时，问题更可能在远端 SSH transport，而非密码或密钥。
- 如果本机未配置云 CLI/API fallback，应尽早发现；SSH banner 连续失败后应转向云控制台。
- 服务器地址、凭据和私有连接材料不写入知识库。

## 关联

- [[obsidian-vault/40-Playbooks/Remote-SSH-Layer-Triage]]
- [[obsidian-vault/30-Projects/AI-Agent-Ecosystem]]

## 来源

- Codex 历史：remote Hermes reboot triage
