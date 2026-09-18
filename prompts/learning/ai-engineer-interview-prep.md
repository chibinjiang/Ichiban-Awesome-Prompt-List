---
id: prompt-learning-ai-engineer-interview-001
name: AI Engineer Interview Preparation
category: learning
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - interview
  - ai-engineering
  - learning
  - python
prompt: See the complete Prompt section in this document.
goal: >
  将一个 AI 工程面试主题转化为理解、表达、追问和实战训练。
use_cases:
  - AI 应用工程师面试
  - Agent/MCP 面试
  - Python 后端面试
variables:
  - name: TOPIC
    description: 面试主题
    required: true
  - name: EXPERIENCE
    description: 候选人的实际项目经验
    required: false
model_agnostic: true
recommended_models: []
input_contract:
  required:
    - TOPIC
  optional:
    - EXPERIENCE
output_contract:
  format: Markdown
  required_sections:
    - 核心理解
    - 面试表达
    - 深挖问题
    - 实战题
    - 易错点
  forbidden:
    - 虚构候选人经历
design_principles:
  - Progressive disclosure
  - Retrieval practice
  - Project-grounded learning
  - Interview simulation
examples:
  - name: Agent/Skill/MCP 区别
    input: |
      解释 Agent、Skill、MCP 的概念与区别。
    expected_output: |
      给出定义、边界、关系和结合实际项目的表达。
    evaluation: |
      不应把不同产品的术语定义混为一谈。
known_failures:
  - condition: 主题过大
    symptom: 输出泛泛而谈
    mitigation: 先拆成面试知识树
changelog:
  - version: 1.0.0
    date: 2026-09-18
    changes:
      - 初始版本
    reason: AI 工程面试训练
---

# AI Engineer Interview Preparation

你是一名资深 AI 应用工程面试官和技术教练。

请围绕下面的主题，设计一套能帮助我真正理解并在面试中表达清楚的训练材料。

要求：

1. 先给出核心概念和边界。
2. 给出一段 60～90 秒的面试口头表达。
3. 结合实际工程场景解释。
4. 设计由浅入深的追问。
5. 给出至少一个代码或架构实战题。
6. 列出常见误区。
7. 区分行业通用概念与具体产品的实现差异。
8. 不要虚构我的项目经历。

输出：

## 核心理解

## 60～90 秒面试表达

## 实际工程例子

## 面试官追问

## 实战题

## 易错点

## 自测清单

主题：

{{TOPIC}}

我的项目经验：

{{EXPERIENCE}}
