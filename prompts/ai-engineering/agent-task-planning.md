---
id: prompt-ai-agent-task-planning-001
name: AI Agent Task Planning
category: ai-engineering
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - agent
  - planning
  - task-decomposition
  - tools
prompt: See the complete Prompt section in this document.
goal: >
  将复杂 AI Agent 任务拆解为可执行、可检查、可恢复的步骤。
use_cases:
  - Agent 工作流设计
  - 工具调用规划
  - 自动化任务设计
variables:
  - name: GOAL
    description: 用户目标
    required: true
  - name: TOOLS
    description: 可用工具
    required: false
  - name: CONSTRAINTS
    description: 约束
    required: false
model_agnostic: true
recommended_models: []
input_contract:
  required:
    - GOAL
  optional:
    - TOOLS
    - CONSTRAINTS
output_contract:
  format: Markdown
  required_sections:
    - 目标澄清
    - 执行计划
    - 工具调用
    - 失败恢复
    - 完成标准
  forbidden:
    - 未经授权的外部操作
design_principles:
  - Task Decomposition
  - Preconditions and postconditions
  - Failure Recovery
  - Human approval boundaries
examples:
  - name: 查询 ERP 库存
    input: |
      查询某 SKU 的库存，并说明数据时间。
    expected_output: |
      先确认 SKU、权限、时间范围，再调用只读工具。
    evaluation: |
      计划应明确权限、数据新鲜度和失败处理。
known_failures:
  - condition: 目标含糊
    symptom: 计划可能建立在错误假设上
    mitigation: 先列出澄清问题
changelog:
  - version: 1.0.0
    date: 2026-09-18
    changes:
      - 初始版本
    reason: Agent 任务规划
---

# AI Agent Task Planning

你是一名 AI Agent 架构师。

请把下面的目标设计成一个可执行、可检查、可恢复的任务计划。

要求：

- 先识别目标、输入、权限和完成标准。
- 将任务拆解为最小的可验证步骤。
- 每一步写明前置条件、动作、预期结果和失败处理。
- 涉及工具时，说明工具用途、输入和风险。
- 涉及写入、删除、发送或其他外部副作用时，明确人工确认边界。
- 不要假设不存在的工具、数据或权限。
- 对不确定信息单独列出。

输出：

## 目标澄清

## 执行计划

| 步骤 | 前置条件 | 动作 | 预期结果 | 失败处理 |
|---|---|---|---|---|

## 工具调用计划

## 权限与安全边界

## 完成标准

## 未知信息

目标：

{{GOAL}}

可用工具：

{{TOOLS}}

约束：

{{CONSTRAINTS}}
