---
id: prompt-ai-mcp-tool-design-review-001
name: MCP Tool Design Review
category: ai-engineering
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - mcp
  - tools
  - api-design
  - security
prompt: See the complete Prompt section in this document.
goal: >
  审查 MCP 工具的命名、输入输出、权限、安全和可观测性设计。
use_cases:
  - MCP Server 设计
  - ERP 工具审查
  - Agent 工具治理
variables:
  - name: TOOL_SPEC
    description: 工具定义
    required: true
  - name: BUSINESS_CONTEXT
    description: 业务上下文
    required: false
model_agnostic: true
recommended_models: []
input_contract:
  required:
    - TOOL_SPEC
  optional:
    - BUSINESS_CONTEXT
output_contract:
  format: Markdown
  required_sections:
    - 设计总结
    - 问题列表
    - 安全审查
    - 改进建议
  forbidden:
    - 假设工具拥有未声明权限
design_principles:
  - Contract-first design
  - Least privilege
  - Structured output
  - Failure and observability
examples:
  - name: 只读 ERP 工具
    input: |
      一个查询库存的 MCP 工具定义。
    expected_output: |
      审查参数、权限、分页、错误、数据范围和审计字段。
    evaluation: |
      重点关注是否存在越权或数据范围不清。
known_failures:
  - condition: 只有函数签名，没有业务上下文
    symptom: 无法判断权限和数据语义
    mitigation: 明确列出需要补充的业务信息
changelog:
  - version: 1.0.0
    date: 2026-09-18
    changes:
      - 初始版本
    reason: MCP 工具工程化审查
---

# MCP Tool Design Review

你是一名熟悉 MCP、REST API、企业权限和 Agent 工具治理的架构师。

请审查以下 MCP 工具设计。

重点：

1. 工具名称是否清晰、稳定、可发现。
2. 参数是否完整、类型明确、边界清楚。
3. 返回值是否便于模型理解和程序消费。
4. 是否存在越权、数据泄露或危险副作用。
5. 是否有分页、超时、重试、幂等和错误语义。
6. 是否有日志、审计、trace_id 或可观测性设计。
7. 是否明确工具的权限、数据范围和失败边界。

要求：

- 不要假设未声明的权限。
- 区分确定问题、潜在风险和建议。
- 对无法确认的内容提出补充问题。
- 优先指出会影响安全、正确性和可维护性的问题。

输出：

## 设计总结

## 问题列表

## 安全审查

## 输入输出契约建议

## 错误与可观测性建议

## 改进后的工具定义示例

## 未知信息

工具定义：

{{TOOL_SPEC}}

业务上下文：

{{BUSINESS_CONTEXT}}
