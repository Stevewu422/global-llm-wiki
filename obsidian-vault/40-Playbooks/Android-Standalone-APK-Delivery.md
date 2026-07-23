---
type: playbook
status: verified
last_verified: 2026-07-14
---

# Android 独立 APK 交付

## 流程

1. 区分脚本、执行器、已有业务 App 和目标独立 APK。
2. 确认目标包名、入口、权限和与现有 App 的隔离要求。
3. 建立完整 Android 工程与可复现构建链。
4. 编译并回读 APK 文件、签名和包信息。
5. 连接真机执行安装。
6. 启动目标 Activity，验证核心流程和失败回滚。

## 完成标准

- Gradle wrapper 或工程目录存在不等于 APK 完成。
- 静态补丁成功不等于真机业务流程成功。
- 只有实际生成、安装、启动和验证后才能宣布交付完成。

