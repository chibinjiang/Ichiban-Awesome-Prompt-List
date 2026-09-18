# Ichiban-Awesome-Prompt-List

> A curated, versioned, and experimentally validated prompt engineering knowledge base.

**Ichiban-Awesome-Prompt-List** 是一个面向真实工程任务的 Prompt Engineering Knowledge Base。

它不只是收藏 Prompt 文本，而是沉淀：

- 可直接复用的 Prompt Cards
- 可迁移的 Prompt Patterns
- 真实任务实验记录
- 测试集、Rubrics 与评估结果
- 失败案例与边界条件
- Prompt 版本历史与模型适配经验

## 核心理念

> 不收藏“看起来很厉害”的 Prompt，只沉淀经过真实任务验证、能够解释、能够迭代的 AI 工作方法。

## 项目结构

```text
Ichiban-Awesome-Prompt-List/
├── prompts/          # 可直接复用的 Prompt Cards
├── patterns/         # Prompt 设计模式与方法论
├── experiments/      # 真实任务实验记录
├── evaluations/      # 测试集、Rubrics、评估结果
├── datasets/         # 可脱敏、可公开的测试数据
├── docs/             # 规范、指南、模型适配说明
├── scripts/          # 索引、搜索、校验工具
├── tests/            # Python 工具测试
├── .github/workflows/ # CI
└── pyproject.toml
```

## 快速开始

### 1. 安装

需要 Python 3.11+ 与 uv。

```bash
uv sync --extra dev
```

### 2. 校验 Prompt Cards

```bash
uv run ichiban-prompt validate
```

### 3. 生成索引

```bash
uv run ichiban-prompt index
```

### 4. 搜索 Prompt

```bash
uv run ichiban-prompt search "SQLAlchemy"
uv run ichiban-prompt search "MCP"
uv run ichiban-prompt search "代码审查"
```

### 5. 运行测试

```bash
uv run pytest
```

## Prompt Card 最低要求

每条 Prompt 至少应该记录：

1. 目标与适用场景
2. 完整 Prompt 正文
3. 输入契约
4. 输出契约
5. 设计原理
6. 至少一个执行示例
7. 已知失败案例或明确说明尚未发现
8. 版本历史

## 生命周期

```text
draft → experimental → stable → deprecated
```

- `draft`: 想法或初版，尚未验证
- `experimental`: 已有真实使用记录，但仍在迭代
- `stable`: 有测试用例、成功案例和已知边界
- `deprecated`: 被新版本替代或不再推荐

## 质量成熟度

| 等级 | 含义 |
|---|---|
| 0 | 草稿 |
| 1 | 至少真实使用过一次 |
| 2 | 有输入输出与测试记录 |
| 3 | 多个任务验证，已记录失败边界 |
| 4 | 有回归测试，可稳定复用 |

成熟度不是绝对质量分数，而是沉淀程度。

## 安全与隐私

不要提交：

- API Key、Token、Cookie、密码
- 真实客户数据、ERP 敏感数据
- 未获授权的源代码或业务资料
- 个人身份信息
- 真实生产日志中的敏感字段

真实案例应先脱敏，必要时使用合成数据。

## 贡献方式

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

MIT，详见 [LICENSE](LICENSE)。
