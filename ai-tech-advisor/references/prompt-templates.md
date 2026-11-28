# Prompt Templates for Tech Stack Tasks

## 1. Project Initialization (Pick by Stack)

### A. Java Backend (Spring Boot 3 / Spring Cloud — Default Primary Stack)

```text
请帮我初始化一个 Java 21 + Spring Boot 3.x（或 Spring Cloud）后端项目：
要求：
- 构建工具：Maven，父 pom.xml 锁定 Spring Boot / Spring Cloud / Alibaba 官方兼容 BOM
- 持久层与迁移：MyBatis-Plus（默认，或 Spring Data JPA）+ Flyway（禁生产开启 ddl-auto）
- 接口文档与鉴权：SpringDoc OpenAPI 3 / Knife4j + Spring Security 6（或 Sa-Token）
- 按架构范式（Modular Monolith 或 Spring Cloud 多模块）组织包结构，并配置 ArchUnit 边界测试与单命令 verify
- 初始化 Git 仓库与 .gitignore
```

### B. Frontend (React / Vue + TypeScript)

```text
请帮我初始化一个 [React / Vue / Next.js] 前端项目：
要求：
- 使用 [version]（初始化前确认当前最新稳定版本）+ TypeScript
- 使用 [UI library] 作为 UI 组件库
- 按 Feature-First / FSD（app/pages/widgets/features/entities/shared）组织目录
- 配置 ESLint（含 eslint-plugin-boundaries 边界检查）+ Prettier
```

### C. Python AI / Agent Service (`fastapi-langgraph-agent`)

```text
请帮我初始化一个 Python 3.11+ FastAPI（按需配 LangGraph）智能体服务：
要求：
- 使用 uv + pyproject.toml 管理依赖与虚拟环境（对标 Maven）
- 配置 FastAPI + Pydantic v2 + ruff + mypy + pytest + import-linter
- 严格遵守 async def 禁同步阻塞 IO、prompts/ 集中管理、evals/ 评测线与单命令 scripts/verify
```

## 2. Add AI Rules to Project

```text
请将以下规则写入项目根目录的 AGENTS.md（≤ 120 行总控路由）及对应子目录 AGENTS.md：

[paste the generated ai-rules content]

确保后续所有开发都遵守这些规则。
```

## 3. Technology Research

```text
请帮我评估 [technology name] 是否适合我的项目：
- 项目类型：[your project type]
- 目标用户：[your target users]
- 关键需求：[list key requirements]

请从社区活跃度、文档质量、维护状态、商业授权、AI 可维护性五个维度评估，并给出明确的"推荐/不推荐"结论。
```

## 4. Tech Stack Migration

```text
我的项目当前使用 [current tech]，想迁移到 [target tech]。
请分析：
- 迁移的必要性
- 预计工作量
- 风险点
- 迁移步骤

如果不适合迁移，请直接说明原因。
```
