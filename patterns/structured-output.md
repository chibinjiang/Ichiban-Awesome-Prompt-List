# Structured Output

## 概念

通过固定字段、Markdown 标题、表格或 JSON Schema 约束输出，使结果更容易阅读、验证和被程序消费。

## 适用场景

- API 返回
- 代码审查
- 需求分析
- 多步骤工作流
- Agent 工具调用前的计划

## 注意事项

结构化输出不能自动保证内容正确。格式校验与事实校验是两件事。

## 最小示例

```text
请严格输出以下字段：

summary:
risks:
recommendations:
unknowns:
```
