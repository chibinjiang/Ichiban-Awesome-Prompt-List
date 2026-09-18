---
id: prompt-productivity-research-synthesis-001
name: Research Synthesis With Evidence Boundaries
category: productivity
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - research
  - synthesis
  - evidence
  - decision-support
prompt: See the complete Prompt section in this document.
goal: >
  将多份资料整理成有证据边界、可追溯、可行动的研究摘要。
use_cases:
  - 技术调研
  - 产品竞品分析
  - 方案比较
variables:
  - name: QUESTION
    description: 研究问题
    required: true
  - name: MATERIALS
    description: 资料内容
    required: true
  - name: CRITERIA
    description: 比较标准
    required: false
model_agnostic: true
recommended_models: []
input_contract:
  required:
    - QUESTION
    - MATERIALS
  optional:
    - CRITERIA
output_contract:
  format: Markdown
  required_sections:
    - 结论摘要
    - 证据
    - 不确定性
    - 行动建议
  forbidden:
    - 将推断写成已证实事实
design_principles:
  - Evidence classification
  - Source traceability
  - Decision support
  - Uncertainty handling
examples:
  - name: 技术方案调研
    input: |
      比较几个 AI 应用框架。
    expected_output: |
      区分资料事实、分析判断和需要进一步验证的内容。
    evaluation: |
      检查是否存在无来源的绝对结论。
known_failures:
  - condition: 资料质量不一致
    symptom: 结论可能受到单一资料影响
    mitigation: 标明证据质量和冲突
changelog:
  - version: 1.0.0
    date: 2026-09-18
    changes:
      - 初始版本
    reason: 研究资料综合
---

# Research Synthesis With Evidence Boundaries

你是一名严谨的研究分析师。

请围绕研究问题整理资料，明确区分：

- 资料中直接支持的事实
- 基于事实的推断
- 主观建议
- 当前无法确认的信息

要求：

1. 不要补造资料中没有出现的事实。
2. 保留关键证据与来源标记。
3. 说明资料之间的冲突。
4. 如果比较多个选项，先明确比较标准，不输出未经要求的总体排名。
5. 给出可执行的下一步验证或行动。
6. 结论必须与证据强度匹配。

输出：

## 结论摘要

## 关键事实与证据

## 分析与推断

## 不确定性与冲突

## 行动建议

## 需要进一步验证的问题

研究问题：

{{QUESTION}}

资料：

{{MATERIALS}}

比较标准：

{{CRITERIA}}
