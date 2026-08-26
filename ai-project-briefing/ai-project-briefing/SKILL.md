---
name: ai-project-briefing
description: Guide non-technical users through AI-assisted project initiation, product clarification, MVP boundaries, user flows, business objects, milestones, and project brief documents. Use when starting a project, when the user mentions "立项", "项目规划", "需求梳理", "MVP", "产品讨论", "先别写代码", or has only a rough idea and needs to clarify what to build before coding.
---

# AI Project Briefing

Guide the user through project initiation before any code is written. Discussion happens in Chinese; output documents and AI rules are generated in English.

**Core principle:** Do not start coding from a one-sentence idea. First turn the idea into a clear project brief, MVP boundary, user flow, data object list, and acceptance criteria.

## Pipeline Position

This is **Stage 1 of 5** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
4. **ai-db-designer** — design database from business objects and flows
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation

If later stage specs exist, read them as context and offer to update the brief. If this stage has no `project-brief-spec.md`, create it before recommending code work.

## Auto-Detect Existing Context

Before discussion, scan the project folder for:

| File | Action |
|------|--------|
| `project-brief-spec.md` | Read and ask whether to update or continue |
| `tech-stack-spec.md` | Read as downstream technical context |
| `frontend-skeleton-spec.md` | Read for existing UI assumptions |
| `db-design-spec.md` | Read for business object assumptions |
| `backend-api-spec.md` | Read for backend scope assumptions |
| `README.md`, docs, existing code | Scan to avoid overwriting reality |

## Interaction Flow

1. **Create/open project space** — ensure the user has a named project folder
2. **Clarify product idea** — what it is, who uses it, what problem it solves
3. **Explore user scenarios** — key users, jobs-to-be-done, main workflows
4. **Define MVP boundary** — first version must-have, later, explicitly not now
5. **Identify business objects** — users, orders, tasks, articles, files, permissions, etc.
6. **Sketch user flow and data flow** — core path from entry to completion
7. **Explore differentiation** — similar products, opportunities, value proposition
8. **Set milestones and acceptance criteria** — what counts as first version done
9. **Generate outputs** — project brief, AI rules, prompt templates
10. **Offer next stage** — recommend `ai-tech-advisor`

## Adaptive Depth Strategy

- If the user gives a clear product description, summarize and move quickly.
- If the idea is vague, ask one question at a time.
- If the user wants to code immediately, pause and explain that this stage is for discussion only.
- If the project is too large, decompose it into sub-projects and brief the first one.

## Required First Question

Ask:

> 你的项目一句话是什么？它面向谁，解决什么问题？

Then follow with one question at a time:

- 第一版最核心的用户操作是什么？
- 用户为什么会用它，而不是继续用现有方案？
- 第一版必须做哪些功能？哪些功能明确后面再做？
- 项目里有哪些核心业务对象需要记录？
- 这个项目更适合先做网页、小程序、App、后台系统，还是纯后端服务？

## Discussion Guardrail

Explicitly tell the agent:

> 当前阶段只做产品讨论和立项设计，暂时不要写代码。你要以产品合伙人和架构顾问的角色追问、补全盲区、收敛 MVP，不要进入代码生成模式。

## Generate Outputs

After confirmation, generate:

### `project-brief-spec.md` (English)

Include:

- Project overview
- Target users
- Core problem
- Product value and differentiation
- MVP scope
- Explicit non-goals for v1
- User journey
- Core business objects
- Initial product form recommendation
- Milestones
- Acceptance criteria
- Open questions
- AI agent constraints

### `ai-rules/` updates

Generate or update platform rules:

- `AGENTS.md` for Codex
- `CLAUDE.md` for Claude Code
- `.cursorrules` for Cursor

Rules must include:

- Do not write implementation code before project brief is confirmed
- Always check `project-brief-spec.md` before planning features
- Do not add v2/later features into v1 without explicit approval
- Update the brief when product scope changes

### `ai-rules/prompt-templates.md`

Add prompts for:

- product clarification
- MVP boundary review
- competitor/reference analysis
- user flow review
- acceptance criteria audit

## Offer Next Stage

After writing the brief:

> 立项文档已完成。下一步建议使用 `ai-tech-advisor` 选择技术栈。是否继续？

Do not start technical implementation unless the user asks to continue.

## Red Flags

| Thought | Reality |
|---------|---------|
| "The idea is simple, code now" | Simple ideas still need MVP boundary and acceptance criteria |
| "AI can decide the product" | AI can advise, but user intent controls the product |
| "We'll define scope while coding" | That causes drift and dead code |
| "The brief is just paperwork" | It is the source of truth for later stages |

## Common Mistakes

1. Starting with code before product scope is clear
2. Letting AI add attractive but non-MVP features
3. Not documenting what v1 explicitly will not do
4. Skipping business objects until database design
5. Treating the brief as final instead of versioned and updatable
