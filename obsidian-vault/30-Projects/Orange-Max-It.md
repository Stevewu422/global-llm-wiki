---
type: project
status: historical
last_verified: 2026-07-14
domains: [Programming, INPAY]
---

# Orange Max It

## 项目范围

- Auto.js 支付脚本稳定性优化
- 从相邻成熟脚本迁移容错模式
- 独立 Android APK 工程与真机安装目标

## 已验证脚本模式

- 将前台恢复、页面确认、有限按钮重试、订单状态更新、失败回滚和防重入集中到主支付流程。
- 迁移相邻脚本逻辑时保留目标应用边界，不修改原业务包。
- 重试失败时优先恢复目标 App 到前台，不默认强制返回首页，以免破坏多页中间状态。
- 静态补丁和代码回读只能证明修改落地，不能证明真机流程可用。

## APK 交付边界

- Auto.js 脚本不是可直接安装的独立 APK。
- 需要完整 Android 壳工程、构建链、包名隔离和设备测试。
- 只有生成 APK 并完成真机安装/启动验证，才能宣布“独立 APK 已完成”。

## 关联

- [[40-Playbooks/Android-Standalone-APK-Delivery]]
- [[50-Domains/编程]]
- [[50-Domains/INPAY]]

## 来源

- Codex 历史：orange max it script maintenance and standalone APK packaging

