---
id: prompt-category-name-001
name: Prompt Name
category: coding
version: 0.1.0
status: draft
language: zh-CN
tags:
  - tag
goal: >
  用一句话描述该 Prompt 解决的问题。
use_cases:
  - 场景一
  - 场景二
non_use_cases:
  - 不适用场景
variables:
  - name: INPUT
    description: 输入内容
    required: true
model_agnostic: true
recommended_models: []
input_contract:
  required:
    - INPUT
  optional: []
output_contract:
  format: Markdown
  required_sections:
    - 总结
  forbidden:
    - 无依据的断言
design_principles:
  - Role-Task-Context-Constraints
examples:
  - name: 基础示例
    input: |
      示例输入
    expected_output: |
      示例输出
    evaluation: |
      评价
known_failures:
  - condition: 尚未发现
    symptom: 尚未发现
    mitigation: 持续测试
changelog:
  - version: 0.1.0
    date: 2026-09-18
    changes:
      - 初始版本
    reason: 初始创建
---

# Prompt Name

## Prompt

```text
你是一名……

任务：
{{INPUT}}
```

## 使用说明

说明如何填充变量、如何判断输出是否合格。
