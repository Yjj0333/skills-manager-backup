---
name: ai-project-briefing
description: Guide non-technical users through AI-assisted project initiation, product clarification, MVP boundaries, user flows, business objects, milestones, and structured Chinese Software Requirement Specification (SRS) documents. Use when starting a project, when the user mentions "立项", "项目规划", "需求梳理", "需求文档", "需求规格说明书", "MVP", "产品讨论", "先别写代码", or has only a rough idea and needs to clarify what to build before coding.
---

# AI Project Briefing（项目立项与中文需求规格说明书）

Guide the user through product discovery and structured requirement analysis before any architecture or code is written. **Both the discussion and the generated Software Requirement Specification (`specs/project-brief-spec.md` and optional `specs/modules/*.md`) MUST be written in Chinese** (following the professional Chinese SRS standard in [references/srs-template.md](references/srs-template.md), with optional English identifiers in parentheses for downstream database/API mapping).

**Core principle:** Do not start coding or picking frameworks from a one-sentence idea. First turn the idea into a clear, testable, Chinese SRS covering 引言, 系统介绍（业务架构 / 领域 Q&A / 角色权限 / MVP 边界 / 状态机）, 模块化功能用例规格表（11 项标准维度）, and 非功能需求与验收标准.

## Pipeline Position

This is **Stage 1 of 9** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, flows, roles, business objects, and Chinese SRS
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-db-designer** — design database from business objects, state enums, and use-case data descriptions
4. **ai-frontend-scaffolder** — design frontend skeleton, UI rules, and state handling
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, permissions, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security
9. **backend-deploy-checkpoint** — pre-launch checklist: secrets, build & start, database backup + migration, smoke test, rollback

If later-stage specs exist, read them as context and offer to sync the SRS. If `specs/project-brief-spec.md` does not exist (or is only a rough draft), complete and confirm it before recommending Stage 2 or any code work.

## Language & Boundary Rules

- **SRS outputs (`specs/project-brief-spec.md`, `specs/modules/*.md`, `ai-rules/prompt-templates.md`)**: **MUST be in Chinese** (规范中文). Technical/field hints such as suggested snake_case identifiers (`order_number`, `user_id`) or standard acronyms (`WMS`, `SKU`, `ERP`) may appear alongside Chinese labels for Stage 3/5 alignment.
- **`ai-rules/` platform files (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`)**: may be written in Chinese or bilingual CN/EN so any coding agent enforces the constraints cleanly.
- **Stage boundary (do NOT overstep)**: Stage 1 defines **business requirements, roles, workflows, state machines, and logical data descriptions**. Do **NOT** lock in specific programming languages, frameworks, ORMs, or physical SQL indexes here — those belong to Stage 2 (`ai-tech-advisor`) and Stage 3 (`ai-db-designer`). *(Exception: if the user already provides existing legacy SQL/schemas or mandatory integration constraints, record them as reference inputs/constraints in `补充说明` or `数据描述`.)*

## Auto-Detect Existing Context

Before starting discussion, scan the project root and `specs/` (older projects may keep files at the project root):

| File | Action |
|------|--------|
| `specs/project-brief-spec.md` | Read and ask whether to update, expand to full SRS, or continue |
| `specs/modules/*.md` | Read existing split module use-case documents if present |
| `specs/tech-stack-spec.md` | Read as downstream technical/constraint context |
| `specs/frontend-skeleton-spec.md` | Read for existing page/UI assumptions |
| `specs/db-design-spec.md` | Read for existing data model assumptions |
| `specs/backend-api-spec.md` | Read for existing backend scope assumptions |
| `README.md`, prototypes, old requirement docs, existing code | Scan to extract existing domain knowledge and avoid contradicting reality |

## Adaptive Project Sizing Strategy

Match document depth and file layout to project complexity — never truncate large systems and never over-engineer tiny tools:

| Project Scale | Criteria | Output Strategy |
|---------------|----------|-----------------|
| **Lightweight / Small MVP** | ≤ 8 core use cases (e.g., landing tool, single-workflow utility, simple CRUD app) | Single-pass clarification → generate complete Chinese SRS directly in `specs/project-brief-spec.md` (with concise Chapters 1–4 and all 11-row use-case tables inline). |
| **Medium Business System** | 9–15 core use cases (e.g., standard SaaS, admin portal, booking/e-commerce MVP) | Two-step generation: **First** confirm Chapters 1–2 + full Chapter 3 use-case directory; **Second** write complete `specs/project-brief-spec.md` module by module (using symmetric reuse notes for repetitive enable/disable/CRUD flows). |
| **Large / Multi-Module System** | > 15 core use cases (e.g., WMS, ERP, multi-role marketplace) | **Index + Module Files**: Put Chapters 1, 2, 4 and Chapter 3 **Module & Use-Case Index** in `specs/project-brief-spec.md`, and write detailed 11-row use-case specs per module under `specs/modules/<module-name>.md` (e.g., `specs/modules/01-storage-location.md`, `02-inbound.md`). This guarantees zero truncation and clean downstream context loading. |

## Interaction Flow

Follow this 8-step sequence (still **one focused question per message** during discovery):

1. **Scan & open project context** — ensure a project folder/context exists and inspect existing docs
2. **Clarify Chapter 1 (引言)** — one-sentence positioning, target users, core pain points, v1 scope, terminology
3. **Explore Chapter 2 (系统介绍)** — business module architecture, end-to-end main flow, domain Q&A, roles & data ownership matrix, MVP boundary (P0 / P1 / Non-Goals), core business objects & state transitions
4. **Converge Chapter 3 Directory (功能用例清单)** — break down modules (`3.X → 3.X.Y → 3.X.Y.Z`) and prioritize (P0/P1); identify symmetric use cases that can share rules
5. **Detail Chapter 3 Use Cases (11 项标准规格表)** — capture preconditions/state constraints, numbered main flow, optional/error branches, postconditions (initial state, auto-numbering rules, cascade updates), logical data descriptions, and domain examples
6. **Confirm Chapter 4 (非功能需求与验收)** — user/data scale, performance/security baseline, milestones, testable acceptance criteria, open questions
7. **Outline Confirmation → Generate Chinese SRS** — present the module/use-case outline for confirmation, then write `specs/project-brief-spec.md` (+ `specs/modules/*.md` if large), `ai-rules/`, and `ai-rules/prompt-templates.md`
8. **Offer Next Stage** — recommend `ai-tech-advisor` (Stage 2)

## Adaptive Depth & Questioning Rules

- **If the user gives a detailed brief or existing document:** Summarize it into the SRS outline immediately, highlight only missing gaps (e.g., unclear permissions, missing state transitions, unbounded scope), and ask to confirm.
- **If the idea is vague:** Ask **one targeted question at a time**. Never dump a 10-question form on a non-technical user.
- **If the user asks to start coding immediately:** Pause politely and explain that without confirmed use-case boundaries, roles, and state rules, AI-generated code will drift and cause rework.
- **If the scope is huge:** Converge on v1 MVP modules first (P0), move P1/P2 into backlog, and split large use-case catalogs into `specs/modules/*.md`.

### Required First Question (when starting fresh)

> 你的项目一句话是什么？它面向谁，要解决什么核心问题？

Follow up one question at a time as needed to fill Chapters 1–4:
- 第一版最核心的用户是谁，他们从头到尾怎么完成一次关键操作？
- 用户为什么愿意换用它，而不是继续用 Excel / 微信群 / 现有系统？
- 第一版（P0）必须做哪些模块和功能？哪些明确放到后续版本或第一版坚决不做？
- 系统里有哪几类角色？普通用户能不能只看自己的数据，还是需要多部门/多租户/审核流隔离？
- 核心单据或业务对象有哪些关键状态流转和硬性限制（比如：什么状态下不能修改或删除、单号/编号有没有固定规则、有没有批次/库存/金额扣减联动）？
- 预期用户量级、核心数据规模以及主要使用终端（网页/后台/小程序/App/PDA）是什么？

## Discussion Guardrail

Explicitly hold this posture throughout Stage 1:

> 当前阶段只做产品讨论与《需求规格说明书（SRS）》设计，暂时不选具体开发框架、不写业务代码。你要以产品架构顾问的角色追问业务盲区、补全前置约束与异常流、收敛 MVP 边界，确保产出物可直接指导下游建表、画页面与设计 API。

## Generate Outputs

After user confirmation, generate strictly in **Chinese** (following [references/srs-template.md](references/srs-template.md)):

### 1. `specs/project-brief-spec.md` (中文《需求规格说明书》)

Must contain all 4 chapters modeled on the standard SRS template:
- **1 引言**：`1.1 目的`、`1.2 范围`（含 v1 Non-Goals）、`1.3 目标与读者对象`、`1.4 术语与缩写`（表格）
- **2 系统介绍**：`2.1 概述`（含产品定位与初始形态倾向）、`2.2 业务架构与核心流程`（Mermaid 业务架构图与端到端流程图）、`2.3 业务领域 Q&A`、`2.4 角色与权限矩阵概览`（含水平归属范围）、`2.5 MVP 边界规划`（P0 / 后续 / 明确不做）、`2.6 核心业务对象与状态机概览`（含 Mermaid 状态图）
- **3 功能用例**：按 `3.X 模块 → 3.X.Y 子模块 → 3.X.Y.Z 用例` 组织，每个核心用例使用 **11 项标准规格表**：
  `名称` / `优先级` / `功能描述` / `参与者` / `前置条件（约束）` / `事件流（操作序列）` / `可选事件流` / `后置条件` / `数据描述` / `补充说明` / `修改历史`
  *(For large systems > 15 use cases, keep the module index in `specs/project-brief-spec.md` and write detailed tables into `specs/modules/<module>.md`.)*
- **4 非功能需求、里程碑与验收标准**：`4.1 非功能需求与规模预期`、`4.2 里程碑规划`、`4.3 验收标准`、`4.4 待确认问题`、`4.5 AI 协作约束`

### 2. `ai-rules/` updates

Generate or update platform rules (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`) to enforce:
- Do not write implementation code before `specs/project-brief-spec.md` is confirmed
- Always read `specs/project-brief-spec.md` (and `specs/modules/*.md`) before designing database, UI, or APIs
- Never silently pull P1/P2 or Non-Goals features into v1 without explicit user approval
- Keep `specs/project-brief-spec.md` (and module use-case tables + `修改历史`) in Chinese and update specs first whenever requirements change

### 3. `ai-rules/prompt-templates.md`

Populate Chinese prompt templates from [references/prompt-templates.md](references/prompt-templates.md) customized for this project:
- 产品立项与业务盲区追问
- 模块拆解与功能用例目录收敛
- 标准 11 项功能用例规格表生成
- MVP 边界与 Non-Goals 审校
- 中文 SRS 质量自检与验收口径核对

## Offer Next Stage

After writing and confirming the Chinese SRS:

> 中文《需求规格说明书》（`specs/project-brief-spec.md`）已完成。下一步建议使用 `ai-tech-advisor`（Stage 2）根据这份需求与预期规模确定技术栈和项目目录布局。是否继续？

Do not start Stage 2 or generate code unless the user confirms.

## Red Flags

| Thought | Reality |
|---------|---------|
| "The idea is simple, code now" | Simple ideas still break without preconditions, state transitions, and acceptance criteria |
| "Write specs in English because it's code-adjacent" | Requirement specs (`project-brief-spec.md`) MUST be in Chinese so business owners and non-technical users can audit every rule |
| "Skip optional/error flows in use cases" | Happy-path-only specs force AI to guess validation, state locks, and error handling during coding |
| "Pick Next.js + MySQL + Redis in Stage 1" | Tech stack choices belong to Stage 2; Stage 1 captures business constraints and scale only |
| "Dump 40 use cases in one giant truncated message" | For >15 use cases, confirm the index first and split cleanly into `specs/modules/*.md` |

## Common Mistakes

1. Writing `specs/project-brief-spec.md` in English instead of Chinese
2. Writing vague narrative prose instead of structured 11-item use-case tables (missing preconditions, state locks, data descriptions, or exception branches)
3. Leaving out role & data-ownership overview (`谁能看谁的数据`), causing Stage 5/8 permission gaps
4. Letting AI smuggle P1/Non-Goals features into v1
5. Picking concrete frameworks/ORMs or physical SQL indexes in Stage 1 instead of leaving them to Stage 2/3
