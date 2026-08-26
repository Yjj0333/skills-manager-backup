---
name: ai-backend-api-planner
description: Plan backend responsibilities, backend language/framework choice, API boundaries, business rules, auth, permission checks, validation, error responses, database interactions, and backend skeleton constraints. Use when the user mentions "后端", "后端架构", "后端骨架", "API", "接口设计", "业务逻辑", "权限校验", "后端乱", or needs to decide whether a project needs a backend.
---

# AI Backend API Planner

Guide the user through backend technical understanding and API boundary design before backend code is written. Discussion happens in Chinese; output documents and AI rules are generated in English.

**Core principle:** Backend is not "just writing APIs." Backend owns business rules, data flow, permission checks, validation, integrations, task execution, and API coordination.

## Pipeline Position

This is **Stage 5 of 5** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
4. **ai-db-designer** — design database from business objects and flows
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation

Read earlier stage specs before starting. If any earlier stage is missing, ask whether to continue with available context or go back to the missing stage.

## Auto-Detect Existing Context

Scan for:

| File | Action |
|------|--------|
| `project-brief-spec.md` | Read for product scope and MVP boundary |
| `tech-stack-spec.md` | Read for backend language/framework/database choices |
| `frontend-skeleton-spec.md` | Read for frontend pages and API needs |
| `db-design-spec.md` | Read for tables, relationships, business objects |
| `backend-api-spec.md` | Read and offer to update |
| Existing backend folders | Inspect current routes/controllers/services/models |

## Interaction Flow

1. **Decide backend scenario** — script/task vs product-grade backend
2. **Clarify backend responsibilities** — business rules, data flow, auth, validation
3. **Confirm language and framework** — from tech stack or recommend one
4. **Map frontend needs to APIs** — pages/actions -> API endpoints
5. **Map APIs to database tables** — read/write relationships
6. **Define auth and permissions** — login, roles, protected actions
7. **Define validation and error format** — parameters, business exceptions, response shape
8. **Define backend skeleton constraints** — modules, layers, middleware, logging
9. **Generate outputs** — backend API spec, AI rules, prompt templates
10. **Offer code generation** — backend skeleton only after confirmation

## Step 1: Decide Backend Scenario

Ask:

> 这个需求是一个小脚本，还是项目级后端？

Explain:

- **Small script** — file processing, batch cleanup, report generation, scheduled one-off task; avoid overbuilding a backend.
- **Product-grade backend** — users, orders, content, roles, payments, review workflows, statistics, API collaboration.

If it is a small script, recommend the simplest script route and do not force a full backend.

## Step 2: Clarify Backend Responsibilities

Ask the agent to analyze before coding:

> 先不要写代码。请基于当前项目的前端流程、数据库设计和业务需求，分析后端要负责哪些业务逻辑，前端需要哪些 API，每个 API 涉及哪些数据库表、权限、参数校验和异常情况。

Backend responsibilities usually include:

- Business rules: who can login, submit, pay, refund, review, publish, delete
- Data flow: validate input, process business action, update database
- API coordination: frontend actions mapped to stable endpoints
- Auth: login state, tokens/sessions, identity lookup
- Permissions: user/admin/role checks on protected operations
- Validation: parameters, state transitions, ownership checks
- Integrations: payment callbacks, third-party APIs, notifications
- Tasks: async jobs, scheduled tasks, queues if needed

## Step 3: Confirm Language and Framework

If `tech-stack-spec.md` provides backend choice, confirm it.

If missing, recommend one unique option based on project type:

| Situation | Typical Recommendation |
|-----------|------------------------|
| Small script / automation | Python script |
| Frontend TypeScript project | Node.js / TypeScript backend |
| AI/data-heavy lightweight service | Python + FastAPI |
| Enterprise admin/business system | Java/Spring Boot or NestJS, depending context |
| Modern API service with concurrency | Go, if project warrants it |

**Rule:** Recommend one primary backend language/framework. Alternatives are only for explaining trade-offs.

## Step 4: Map Frontend Actions to APIs

Create a table:

| Frontend action | API | Method | Auth | Tables | Business rules |
|----------------|-----|--------|------|--------|----------------|
| Login | `/api/auth/login` | POST | No | users | password check, account status |
| List orders | `/api/orders` | GET | User | orders | only own orders unless admin |
| Create order | `/api/orders` | POST | User | orders, order_items, products | stock, price, address, coupon |

Ask the user to confirm missing actions.

## Step 5: Define API Contract

For each API, specify:

- Endpoint and method
- Auth requirement
- Request parameters
- Response shape
- Validation rules
- Business rules
- Database tables read/written
- Error cases

Use consistent response format:

```json
{
  "success": true,
  "data": {},
  "error": null
}
```

Error shape:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ORDER_STOCK_NOT_ENOUGH",
    "message": "Stock is not enough"
  }
}
```

## Step 6: Define Backend Skeleton

Recommend a clean backend structure, adapted to framework:

```
src/
  modules/
    auth/
      routes.ts
      controller.ts
      service.ts
      dto.ts
    users/
    orders/
  middleware/
    auth.ts
    error-handler.ts
  database/
    client.ts
    migrations/
  shared/
    errors.ts
    response.ts
    validation.ts
  config/
  tests/
```

Layer rule:

- Routes define HTTP entry points
- Controllers parse request/response
- Services implement business logic
- Repositories/ORM access database
- Middleware handles cross-cutting concerns
- Shared error/response formats stay centralized

## Generate Outputs

After confirmation, generate:

### `backend-api-spec.md` (English)

Include:

- Backend scenario decision
- Language and framework
- Backend responsibilities
- API list and contracts
- Auth and permission model
- Validation rules
- Error response format
- Database read/write mapping
- Backend skeleton structure
- External SDKs/integrations
- AI agent constraints

### `ai-rules/` updates

Add rules:

- Do not write backend endpoints before API contract is confirmed
- Business-critical validation must be backend-side, never frontend-only
- Every protected API must declare auth and permission rules
- Every API must document database tables read/written
- Use unified response and error format
- Do not change backend language/framework without updating `tech-stack-spec.md` and `backend-api-spec.md`

### `ai-rules/prompt-templates.md`

Add prompts for:

- backend responsibility analysis
- API contract generation
- permission model review
- backend skeleton generation
- API/database consistency audit

## Offer Code Generation

After writing the spec:

> 后端/API 规划已完成。接下来我可以帮你：
> - A) 生成后端骨架代码
> - B) 生成 API 路由 + 空 service/controller
> - C) 暂时不生成代码

Only generate code after explicit confirmation.

## Red Flags

| Thought | Reality |
|---------|---------|
| "Just write login/order APIs" | First map API boundaries, auth, validation, tables |
| "Frontend already checks this" | Business-critical checks must be backend-side |
| "Let's add Redis/queue early" | Add only when a concrete need exists |
| "API is just CRUD" | Product APIs encode business rules and state transitions |
| "Switch backend framework midstream" | Update tech stack and backend spec first |

## Common Mistakes

1. Treating backend as a pile of endpoints
2. Not mapping APIs to database tables
3. Putting permissions only in frontend
4. No unified error format
5. Mixing route/controller/service/database logic in one file
6. Adding heavy infrastructure before business need is clear
