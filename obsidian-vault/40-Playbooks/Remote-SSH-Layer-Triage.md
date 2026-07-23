---
type: playbook
status: verified
last_verified: 2026-06-26
---

# SSH 分层诊断

## 三层

1. TCP：目标端口是否可达。
2. Protocol：SSH banner 是否正常返回。
3. Authentication：用户名、密钥或密码是否通过。

## 决策

- TCP 失败：检查网络、安全组和实例状态。
- TCP 成功但 banner 失败：不要反复更换认证方式，转向远端 sshd、系统负载或云控制台。
- banner 成功但认证失败：再检查账号、密钥和权限。
- 需要整机重启时，先确认云 CLI/API 或控制台 fallback 是否可用。

## 安全

- 不把主机地址、密码、密钥和云凭据写入知识库。
