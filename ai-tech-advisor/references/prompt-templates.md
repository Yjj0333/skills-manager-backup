# Prompt Templates for Tech Stack Tasks

## 1. Project Initialization

After choosing your tech stack, use this prompt to initialize the project:

```
请帮我初始化一个 [framework] 项目。
要求：
- 使用 [version] 版本
- 使用 [UI library] 作为 UI 组件库
- 按照框架官方推荐的目录结构组织
- 配置 ESLint + Prettier
- 初始化 Git 仓库
```

## 2. Add AI Rules to Project

```
请将以下规则写入项目的 AGENTS.md（或 CLAUDE.md / .cursorrules）：

[paste the generated ai-rules content]

确保后续所有开发都遵守这些规则。
```

## 3. Technology Research

```
请帮我评估 [technology name] 是否适合我的项目：
- 项目类型：[your project type]
- 目标用户：[your target users]
- 关键需求：[list key requirements]

请从社区活跃度、文档质量、维护状态、商业授权、AI可维护性 五个维度评估，并给出明确的"推荐/不推荐"结论。
```

## 4. Tech Stack Migration

```
我的项目当前使用 [current tech]，想迁移到 [target tech]。
请分析：
- 迁移的必要性
- 预计工作量
- 风险点
- 迁移步骤

如果不需要迁移，请直接说明原因。
```
