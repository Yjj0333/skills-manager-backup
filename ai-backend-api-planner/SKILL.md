---
name: ai-backend-api-planner
description: Plan backend responsibilities, backend language/framework choice, API boundaries, business rules, auth, permission checks, validation, error responses, database interactions, and backend skeleton constraints. Use when the user mentions "后端", "后端架构", "后端骨架", "API", "接口设计", "业务逻辑", "权限校验", "后端乱", or needs to decide whether a project needs a backend.
---

# AI Backend API Planner

Guide the user through backend technical understanding and API boundary design before backend code is written. Discussion happens in Chinese; output documents and AI rules are generated in English.

**Core principle:** Backend is not "just writing APIs." Backend owns business rules, data flow, permission checks, validation, integrations, task execution, and API coordination.

## Pipeline Position

This is **Stage 5 of 9** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-db-designer** — design database from business objects and flows
4. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security
9. **backend-deploy-checkpoint** — pre-launch checklist: secrets, build & start, database backup + migration, smoke test, rollback

Read earlier stage specs before starting. If any earlier stage is missing, ask whether to continue with available context or go back to the missing stage.

## Auto-Detect Existing Context

Scan the project root and `specs/` (older projects may keep these at the project root):

| File | Action |
|------|--------|
| `specs/project-brief-spec.md` (+ `specs/modules/*.md`) | Read for Chinese SRS scope, role & ownership matrix, use-case `前置条件`/`可选事件流`/`后置条件`, and numbering/state rules |
| `specs/tech-stack-spec.md` | Read for backend language/framework/database choices |
| `specs/frontend-skeleton-spec.md` | Read for frontend pages and API needs |
| `specs/db-design-spec.md` | Read for tables, relationships, business objects |
| `specs/backend-api-spec.md` | Read and offer to update |
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

If `specs/tech-stack-spec.md` provides backend choice, confirm it.

If missing, recommend one unique option based on project type:

| Situation | Typical Recommendation |
|-----------|------------------------|
| Standard web/admin/enterprise system (Java primary stack) | **Java 21 + Spring Boot 3.x** (MyBatis-Plus + Flyway + Spring Security 6 / Sa-Token) |
| Small script / automation | Python script |
| AI/Agent workflow (`fastapi-langgraph-agent`) | Python + FastAPI (+ LangGraph when stateful/HITL) |
| Node/TS unified team backend | NestJS / Hono |
| Modern API service with concurrency | Go, if project warrants it |

**Rule:** Recommend one primary backend language/framework. Alternatives are only for explaining trade-offs.

## Step 4: Map Frontend Actions and SRS Use Cases to APIs

Derive the API list from **both** `specs/frontend-skeleton-spec.md` (if the project has a frontend) and the Chinese SRS Chapter 3 use cases in `specs/project-brief-spec.md` (+ `specs/modules/*.md`):
- Use-case `参与者` + `2.4 角色与权限矩阵概览` → `Auth` & `Ownership` columns
- Use-case `前置条件（约束）` + `可选事件流` → state-transition checks, validation rules, and business error codes
- Use-case `后置条件` + `数据描述` → `Tables` read/written, auto-numbering, and cascade updates

Create a table:

| Frontend action | API | Method | Auth | Ownership | Tables | Business rules |
|----------------|-----|--------|------|-----------|--------|----------------|
| Login | `/api/auth/login` | POST | No | — | users | password check, account status |
| List orders | `/api/orders` | GET | User | Only own orders unless admin | orders | scope query by current user |
| Create order | `/api/orders` | POST | User | Creates under current user | orders, order_items, products | stock, price, address, coupon |

The Ownership column states whose data each API touches. Every protected API must be able to answer "can this user act on THIS data?" — the Stage 8 horizontal-escalation audit checks this column against the permission design table.

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

Three API-level conventions to decide at design time, not during coding:

**Versioning:** all endpoints live under a version prefix (`/api/v1/...`). Changing a contract later means a new version — never silently break v1 clients.

**Pagination:** every list endpoint declares its convention. Default: `page` + `pageSize` request params, `total` in the response. Cursor-based pagination is the exception, only for very large or infinite-scroll feeds.

**Idempotency:** endpoints that create money/order records must define an idempotency strategy — a client-supplied idempotency key, or a unique business constraint (e.g. one order per user per slot) — so double-clicks and retries do not create duplicates.

**Machine-Readable Contract Source of Truth:** every backend MUST expose or export a machine-readable contract alongside `specs/backend-api-spec.md`:
- Monolith / FastAPI / Spring Boot: OpenAPI 3.1 spec (`/openapi.json` / `specs/openapi.yaml`) generated from Pydantic / Zod / SpringDoc DTOs so frontend TypeScript types never drift by hand.
- Spring Cloud Microservices: shared `api-contracts/*-api` module holding OpenFeign interfaces, Request/Response DTOs, and Domain Event schemas as the single contract source.

## Step 6: Define Backend Skeleton (By Architecture Archetype)

Adapt the backend structure to the **Architecture Archetype** declared in `specs/tech-stack-spec.md`:

### Option A: Layered / Modular Monolith (`layered-monolith` / `modular-monolith`)
For `modular-monolith`, enforce **strict bounded modules** under `backend/src/`:

**Java Spring Boot 3 Default Layout (`src/main/java/com/<org>/<app>/`):**
```text
modules/
  auth/
    api/          # Public Facade interface + exported DTOs ONLY (external modules depend ONLY on this)
    controller/   # @RestController: accepts RequestDTO + @Valid, returns Result<VO> (NEVER expose Entity)
    service/      # @Transactional(rollbackFor = Exception.class) at Service boundary (no remote HTTP/MQ inside)
    mapper/       # MyBatis-Plus Mapper (private to module — NEVER imported by other modules)
    entity/       # Persistence entities (private to module)
    dto/          # RequestDTO / ResponseVO
  orders/
    api/
    events/       # In-process Spring ApplicationEvent / domain events
    ...
common/           # Pure Result<T>, ErrorCode, TraceIdFilter, GlobalExceptionHandler (@RestControllerAdvice), SecurityConfig (ZERO business logic)
```

*(TypeScript/Node alternative: `src/modules/<domain>/{index.ts, routes.ts, controller.ts, service.ts, repository.ts, dto.ts}` + `middleware/` + `shared/`.)*

Layer & Modularity rules:
- Inside a module: Controller (`RequestDTO + @Valid`) → Service (`@Transactional`) → Mapper/Repository (`Entity`) — never bind or return `Entity` in Controller
- Across modules (`modular-monolith`): **zero circular dependencies (DAG)**; modules communicate ONLY through `modules/<domain>/api/` (Facade) or In-Process Domain Events, and each module touches ONLY its own tables

### Option B: Spring Cloud Microservices (`spring-cloud-microservices`)
- **North-South (`gateway-service`)**: external `/api/v1/**` routes, JWT verification, rate limiting, and **mandatory stripping of client-supplied `X-User-*` / `X-Internal-*` headers** before forwarding.
- **East-West (`api-contracts/*-api`)**: `/internal/v1/...` OpenFeign contracts with explicit connect/read timeouts and non-fake Sentinel/Resilience4j fallbacks (never fake `200` data).
- **Async Consistency**: cross-service writes declare Transactional Outbox events + MQ consumer idempotency (`processed_messages`).

### Option C: FastAPI + LangGraph Agent (`fastapi-langgraph-agent`)
*(For users new to FastAPI/LangGraph, explain contracts in plain language alongside technical details:)*
- **API & Streaming (`app/api/v1/`)**: REST endpoints + SSE streaming event contract (`token`, `tool_start`, `approval_required`, `done`, `error`).
- **Tool Risk & HITL Table**: classify every agent tool as `Read-Only` (auto with ACL), `Mutating` (idempotency key), or `Destructive/External` (MUST pause via LangGraph `interrupt()` and resume only via explicit user approval endpoint).
- **Complexity Check**: use LangGraph `StateGraph` only when multi-step tool loops, branching, or HITL pause/resume exist; single-pass AI calls stay pure FastAPI + Pydantic `with_structured_output`.

## Generate Outputs

After confirmation, generate:

### `specs/backend-api-spec.md` (English)

Include:

- Backend scenario decision
- Language and framework
- Backend responsibilities
- API list and contracts
- Ownership mapping per API
- API versioning, pagination, and idempotency rules
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
- Every protected API must declare its ownership rule (whose data it touches)
- List APIs declare pagination; money/order-creating APIs declare idempotency
- Every API must document database tables read/written
- Use unified response and error format
- Do not change backend language/framework without updating `specs/tech-stack-spec.md` and `specs/backend-api-spec.md`

### `ai-rules/prompt-templates.md`

Add prompts for:

- backend responsibility analysis
- API contract generation
- permission model review
- backend skeleton generation
- API/database consistency audit

## Offer Next Stage

After writing the spec:

> 后端/API 规划已完成。下一步建议使用 `backend-skeleton-builder` 搭建最小可运行后端骨架。
> 输入文件：`specs/backend-api-spec.md` + `specs/tech-stack-spec.md`
> 是否继续？

Do not generate skeleton code until the user confirms.

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
