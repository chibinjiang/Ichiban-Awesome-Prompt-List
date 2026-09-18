# Contributing Guide

感谢你为 Ichiban-Awesome-Prompt-List 贡献内容。

## 贡献类型

欢迎提交：

- 新 Prompt Card
- Prompt Pattern
- 实验记录
- 测试用例
- 失败案例
- 模型适配经验
- 文档改进
- 校验器和索引工具改进

## 提交前检查

```bash
uv run ichiban-prompt validate
uv run pytest
uv run ichiban-prompt index
```

## 新增 Prompt 的要求

### 必填字段

- 唯一 `id`
- `name`
- `category`
- `version`
- `status`
- `language`
- `tags`
- `goal`
- `use_cases`
- `prompt`
- `input_contract`
- `output_contract`
- `design_principles`
- `examples`
- `known_failures`
- `changelog`

### 内容要求

1. Prompt 必须能够独立理解和执行。
2. 使用 `{{VARIABLE}}` 表示待填充变量。
3. 不要把某个模型的偶然行为描述成普遍规律。
4. 区分事实、推断、建议和未知信息。
5. 不要承诺“100%准确”“绝不出错”等无法验证的结果。
6. 尽可能记录失败案例。
7. 不要提交敏感信息。
8. 复杂 Prompt 应提供最小可用示例。

## 命名规范

文件名使用小写 kebab-case：

```text
python-systematic-code-review.md
mcp-tool-design-review.md
agent-task-planning.md
```

ID 使用稳定、可读的格式：

```text
prompt-coding-python-review-001
pattern-structured-output-001
experiment-code-review-001
```

## 版本规范

采用 Semantic Versioning：

- `MAJOR`: 破坏输入或输出契约
- `MINOR`: 增加能力或约束
- `PATCH`: 修复错别字、格式或非行为性问题

## Commit 建议

```text
feat(prompt): add python code review prompt
fix(prompt): reduce false positives
test(eval): add sqlalchemy n-plus-one case
docs(pattern): explain structured output
chore(repo): regenerate index
```

## Pull Request 描述建议

```markdown
## What changed?

## Why?

## Validation

## Known limitations

## Privacy check

- [ ] No secrets
- [ ] No personal data
- [ ] No confidential business data
```
