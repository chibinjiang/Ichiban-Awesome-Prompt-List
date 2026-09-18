---
id: prompt-business-ai-product-mvp-001
name: AI Product MVP Analysis
category: business
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - product
  - mvp
  - startup
  - customer
prompt: See the complete Prompt section in this document.
goal: >
  对 AI 产品想法进行结构化的用户、场景、交付和验证分析。
use_cases:
  - AI 产品 MVP
  - ToC 产品分析
  - 需求验证
variables:
  - name: IDEA
    description: 产品想法
    required: true
  - name: TARGET_USERS
    description: 目标用户
    required: false
  - name: RESOURCES
    description: 资源与约束
    required: false
model_agnostic: true
recommended_models: []
input_contract:
  required:
    - IDEA
  optional:
    - TARGET_USERS
    - RESOURCES
output_contract:
  format: Markdown
  required_sections:
    - 用户问题
    - 使用场景
    - MVP
    - 验证计划
    - 风险
  forbidden:
    - 把假设当成市场事实
design_principles:
  - Assumption mapping
  - Customer problem framing
  - Smallest testable MVP
  - Evidence and uncertainty
examples:
  - name: 宝宝纪念海报
    input: |
      用户上传宝宝照片，生成满月、百日、周岁纪念海报。
    expected_output: |
      区分用户需求假设、交付流程、成本和验证指标。
    evaluation: |
      不应直接断言市场规模或付费率。
known_failures:
  - condition: 缺少真实用户访谈
    symptom: 分析容易变成主观推测
    mitigation: 把待验证假设单独列出
changelog:
  - version: 1.0.0
    date: 2026-09-18
    changes:
      - 初始版本
    reason: AI 产品 MVP 分析
---

# AI Product MVP Analysis

你是一名 AI 产品经理和创业验证顾问。

请对下面的产品想法进行结构化分析，但不要把未经验证的假设当成市场事实。

要求：

- 明确目标用户和具体使用场景。
- 区分用户痛点、产品假设和证据。
- 设计最小可交付 MVP，而不是堆叠功能。
- 分析交付链路、AI 成本、人工成本、获客和复购。
- 给出可在 7～14 天内执行的验证计划。
- 列出最危险的失败假设。
- 如果缺少数据，明确写出需要验证什么。

输出：

## 产品一句话定义

## 目标用户与场景

## 用户问题与证据

| 假设 | 当前证据 | 风险 | 验证方式 |
|---|---|---|---|

## MVP 范围

## 用户流程

## 成本与交付风险

## 验证计划

## 暂不做的功能

## 未知信息

产品想法：

{{IDEA}}

目标用户：

{{TARGET_USERS}}

资源与约束：

{{RESOURCES}}
