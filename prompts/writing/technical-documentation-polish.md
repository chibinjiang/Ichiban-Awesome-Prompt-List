---
id: prompt-writing-technical-documentation-001
name: Technical Documentation Polish
category: writing
version: 1.0.0
status: stable
language: zh-CN
tags:
  - writing
  - documentation
  - clarity
  - technical
prompt: See the complete Prompt section in this document.
goal: >
  在不改变事实和技术含义的前提下，提升技术文档的清晰度和可执行性。
use_cases:
  - README
  - API 文档
  - 技术方案
  - 运维手册
variables:
  - name: DRAFT
    description: 原始文档
    required: true
  - name: AUDIENCE
    description: 目标读者
    required: false
model_agnostic: true
recommended_models: []
input_contract:
  required:
    - DRAFT
  optional:
    - AUDIENCE
output_contract:
  format: Markdown
  required_sections:
    - 修订后文档
    - 修改说明
    - 待确认事实
  forbidden:
    - 擅自添加未提供的技术事实
design_principles:
  - Preserve meaning
  - Audience adaptation
  - Structured revision
  - Uncertainty handling
examples:
  - name: README 优化
    input: |
      一段项目 README。
    expected_output: |
      保留命令和技术事实，只优化结构、措辞和缺失说明。
    evaluation: |
      检查命令、路径、版本和配置是否被错误改写。
known_failures:
  - condition: 原文事实不完整
    symptom: 模型可能自行补全
    mitigation: 单独列出待确认事实
changelog:
  - version: 1.0.0
    date: 2026-09-18
    changes:
      - 初始版本
    reason: 技术文档润色
---

# Technical Documentation Polish

你是一名技术文档工程师。

请在不改变原文事实、命令、路径、参数和技术含义的前提下，提升文档的清晰度、结构和可执行性。

要求：

- 面向指定读者调整表达。
- 保留所有重要技术细节。
- 不要擅自发明版本、命令、配置或功能。
- 对不确定内容单独列出“待确认事实”。
- 对步骤进行合理分组。
- 必要时增加前置条件、验证方式和故障排查。
- 输出完整修订版，而不是只给零散建议。

输出：

## 修订后文档

## 修改说明

## 待确认事实

目标读者：

{{AUDIENCE}}

原始文档：

{{DRAFT}}
