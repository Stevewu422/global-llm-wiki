---
type: knowledge-map
status: active
updated: 2026-07-23
---

# 当前知识地图

```mermaid
flowchart TD
    A["00-System<br/>规则与索引"]
    C["98-AI-Context<br/>当前上下文"]
    M["97-AI-Memory<br/>长期经验与决策"]
    P["06-Projects<br/>活跃项目"]
    H["30-Projects<br/>历史与详细项目"]
    W["40-Playbooks<br/>可复用流程"]
    D["50-Domains<br/>六大研究领域"]
    I["10-Inbox / 20-Daily<br/>原始输入"]
    R["90-Archive<br/>历史证据"]
    G["GitHub global-llm-wiki<br/>外部权威知识源"]

    A --> C
    A --> M
    C --> P
    P --> H
    M --> W
    M --> D
    I --> M
    H --> R
    D --> G
```

## 领域关系

```mermaid
flowchart LR
    AI["AI"] --> Programming["编程"]
    AI --> Design["设计"]
    AI --> INPAY["INPAY"]
    Programming --> INPAY
    Design --> INPAY
    Crypto["Crypto"] --> INPAY
    Crypto --> Stocks["美股"]
    AI --> Stocks
```

## 导航

- [[97-AI-Memory/README|长期记忆]]
- 当前上下文：仅保留在本机 Vault
- [[06-Projects/README|活跃项目]]
- [[00-System/HISTORY_CATALOG|历史目录]]
- [[50-Domains/README|研究领域]]
- [[40-Playbooks/README|可复用流程]]
