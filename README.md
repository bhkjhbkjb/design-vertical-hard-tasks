# design-vertical-hard-tasks · 中文垂直领域高难度 Agent 评测任务设计

> 从专家真实工作问题设计/修订高难度 Agent 标注任务，含题库与专家语料引用。

用于从专家的真实专业工作问题中，设计或修订中文垂直领域高难度 Agent 评测（标注）任务。强制主动证据检索、九值主分类法、六字段输出（题目 / 一级目录 / 二级目录 / 相关附件 / 附件来源 / 后续交互思路）。内置通过题库（passed-prompt-library）与 Moment Research 专家实战语料索引。

## 📦 包含的 Skills

### `design-vertical-hard-tasks`
Design or revise Chinese vertical-domain high-difficulty Agent annotation tasks from experts' real professional work problems, with mandatory active evidence research, a controlled nine-value primary taxonomy, and a six-field output. 判断任务处于 DRAFT / READY / BLOCKED 状态。



## 🚀 安装与使用

这些 skills 面向 [WorkBuddy](https://www.codebuddy.cn) 的 skill 体系（亦兼容 Claude Code / Codex 等同类 skill 目录）。

```bash
git clone https://github.com/bhkjhbkjb/design-vertical-hard-tasks.git
# 把需要的 skill 文件夹复制到你的 skills 目录
cp -r design-vertical-hard-tasks/<skill-name> ~/.workbuddy/skills/
```

在 WorkBuddy 中直接以 skill 名称触发即可（如输入 `/<skill-name>` 或自然语言描述）。

## 📂 目录结构

```
design-vertical-hard-tasks/
├── SKILL.md
├── agents/openai.yaml
├── assets/            (task-design-card / task-record 模板)
├── references/        (题库 / 语料索引 / 审核规则 / 分类法等)
└── scripts/           (校验与清单构建脚本)
```

## 🔒 安全说明

本仓库已去除敏感信息（服务器 IP、API 密钥、内部地址等），相关位置以占位符（如 `<DEPLOY_SERVER_IP>`、`<MOMENT_RESEARCH_HOST>`）标注，请按你自己的运行环境替换。

---

*由 **Hreed** 维护 · 欢迎 Star / 提 Issue*
