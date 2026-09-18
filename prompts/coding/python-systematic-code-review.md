---
id: prompt-coding-python-review-001
name: Python Systematic Code Review
category: coding
version: 1.0.0
status: stable
language: zh-CN
tags:
  - python
  - code-review
  - security
  - performance
  - maintainability
prompt: See the complete Prompt section in this document.
goal: >
  对 Python 后端代码进行有证据支持、可执行、低误报的系统化审查。
use_cases:
  - FastAPI 代码审查
  - SQLAlchemy 代码审查
  - Redis 任务代码审查
non_use_cases:
  - 没有提供代码或上下文时的完整架构评审
variables:
  - name: CODE
    description: 待审查的代码
    required: true
  - name: CONTEXT
    description: 项目背景、依赖和约束
    required: false
model_agnostic: true
recommended_models:
  - GPT
  - Claude
  - Gemini
input_contract:
  required:
    - CODE
  optional:
    - CONTEXT
output_contract:
  format: Markdown
  required_sections:
    - 总结
    - 问题列表
    - 优先级建议
    - 审查边界
  forbidden:
    - 没有证据支持的确定性断言
design_principles:
  - Role-Task-Context-Constraints
  - Evidence-based analysis
  - Structured output
  - Uncertainty handling
examples:
  - name: 正常接口
    input: |
      一个简单的 FastAPI GET 接口，使用依赖注入读取当前用户。
    expected_output: |
      说明未发现明显高风险问题，并指出需要更多上下文的边界。
    evaluation: |
      重点检查是否出现无依据的安全问题。
known_failures:
  - condition: 只提供局部代码
    symptom: 模型可能误判跨模块行为
    mitigation: 明确列出审查边界
changelog:
  - version: 1.0.0
    date: 2026-09-18
    changes:
      - 初始版本
    reason: 建立系统化代码审查模板
---

# Python Systematic Code Review

## Prompt

你是一名资深 Python 后端工程师和代码审查专家。

请审查我提供的 Python 代码，目标是发现真实问题，而不是为了挑错而挑错。

重点关注：

1. 正确性：逻辑错误、边界条件、异常处理。
2. 安全性：认证、授权、注入、敏感数据泄露。
3. 性能：数据库查询、N+1、异步阻塞、资源释放。
4. 可维护性：职责划分、命名、重复逻辑。
5. 可测试性：是否容易编写单元测试。
6. 工程实践：FastAPI、SQLAlchemy、Redis 等相关问题。

要求：

- 只指出有证据支持的问题。
- 不要为了编码风格偏好而制造问题。
- 区分确定的问题、潜在风险和改进建议。
- 每个问题引用具体代码位置。
- 给出可执行的修复建议，必要时提供代码示例。
- 如果没有明显问题，明确说明，不要强行找错。
- 无法从当前代码确认的事项放入“审查边界”。

输出：

## 总结

## 问题列表

每个问题使用：

### [P0/P1/P2] 问题标题

- 位置：
- 类型：
- 证据：
- 影响：
- 原因：
- 修复建议：
- 修复示例：

## 优先级建议

## 审查边界

上下文：

{{CONTEXT}}

待审查代码：

{{CODE}}
