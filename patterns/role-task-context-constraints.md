# Role–Task–Context–Constraints

## 概念

通过角色、任务、上下文和约束明确告诉模型：

- 它要扮演什么工作角色
- 要完成什么任务
- 可以使用哪些背景信息
- 必须遵守哪些边界

## 适用场景

几乎所有需要稳定输出的任务。

## 基础结构

```text
角色：
任务：
上下文：
约束：
输出格式：
```

## 常见失败

- 角色描述过度，挤占真正任务空间
- 约束互相冲突
- 上下文缺少关键事实
- 输出要求过于模糊

## 相关 Prompt

- `prompt-coding-python-review-001`
- `prompt-ai-agent-task-planning-001`
