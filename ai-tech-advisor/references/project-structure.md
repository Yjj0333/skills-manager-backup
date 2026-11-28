# Project Directory Structure

Canonical project layouts by product form. The layout is decided at Stage 2 (tech stack selection), recorded in `tech-stack-spec.md`, and reused by every later stage. Never let later stages invent their own roots.

## Common Rules (all layouts)

| Path | Purpose | Created by |
|------|---------|-----------|
| `specs/` | ALL stage documents, one flat folder: `project-brief-spec.md`, `tech-stack-spec.md`, `db-design-spec.md`, `frontend-skeleton-spec.md`, `backend-api-spec.md`, `backend-architecture-spec.md`, `backend-impl-source-of-truth.md`, `backend-security-report.md`, `deploy-checklist.md`, `design-tokens.json` | Stage 1-9 as they run |
| `ai-rules/` | Generated agent rules staging (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `prompt-templates.md`); copy to project root / platform locations when wiring up | Stage 1-9 |
| project root | Only top-level folders + `README.md` + `.gitignore` — never loose code or spec files | Stage 2 |

- Naming: project folder and top-level code directories use kebab-case English (`my-shop`, `frontend/`, `backend/`).
- `.gitignore` baseline from day one: `node_modules/`, `.env`, `dist/`, `build/`, `__pycache__/`, `.venv/`, OS junk (`.DS_Store`, `Thumbs.db`).
- Frontend and backend never share a `src/` — each lives under its own root.

## Layout 1 — Full-stack Website (Next.js)

Single deployable; the project root IS the app root.

```
my-project/
├── specs/
├── ai-rules/
├── app/            ← Next.js App Router (framework convention)
├── src/            ← components, libs, styles (framework convention)
├── public/
└── package.json
```
Filled by: Stage 4 (frontend skeleton). Backend = Next.js API routes — no separate backend root.

## Layout 2 — Website with Separate Backend

```
my-project/
├── specs/
├── ai-rules/
├── frontend/       ← Stage 4 tree lives inside (its src/ is frontend/src/)
└── backend/        ← Stage 5-6 five-line skeleton lives inside
```

## Layout 3 — Mini Program + Backend

```
my-project/
├── specs/
├── ai-rules/
├── miniprogram/    ← Stage 4 (Taro / uni-app tree)
└── backend/        ← Stage 5-6
```

## Layout 4 — App (Mobile) + Backend

```
my-project/
├── specs/
├── ai-rules/
├── app/            ← Stage 4 (Expo / Flutter tree)
└── backend/        ← Stage 5-6
```

## Layout 5 — Admin Panel + Backend

```
my-project/
├── specs/
├── ai-rules/
├── admin/          ← Stage 4 (React + Ant Design / Vue + Element Plus tree)
└── backend/        ← Stage 5-6
```

## Layout 6 — API Service Only

```
my-project/
├── specs/
├── ai-rules/
└── backend/        ← Stage 5-6 (equals the working root for framework tools)
```

## Layout 7 — Modular Monolith (Default for Multi-Domain Systems)

Single deployable backend partitioned by bounded business modules with static dependency boundaries:

```
my-project/
├── specs/
├── ai-rules/               ← Root AGENTS.md (≤120 lines) + per-app AGENTS.md
├── frontend/               ← Feature-First / FSD (optional if API-only)
└── backend/
    ├── src/
    │   ├── modules/
    │   │   ├── orders/     ← index.ts / Facade (public) + internal domain/repo (private)
    │   │   └── inventory/  ← Owns its own tables; communicates via Facade/Events only
    │   └── shared/         ← Pure technical utilities ONLY (zero business logic)
    └── scripts/verify      ← Build + boundary lint/ArchUnit + Zero-Mock + tests
```

## Layout 8 — Spring Cloud Microservices Multi-Module

```
my-project/
├── specs/
├── ai-rules/               ← Root AGENTS.md + services/*/AGENTS.md
├── pom.xml                 ← Parent POM: ONLY place locking Spring Boot/Cloud/Alibaba BOMs
├── common/                 ← Pure Result, ErrorCode, TraceId, SecurityContext (ZERO domain code)
├── api-contracts/          ← Shared Feign interfaces, DTOs, Event schemas (e.g. order-api/)
├── gateway-service/        ← North-South ingress, JWT verify, strip spoofed X-User-* headers
├── services/
│   ├── auth-service/       ← Own Spring Boot app + own DB/Schema
│   ├── order-service/      ← Depends on api-contracts/*, NEVER directly on another *-service
│   └── agent-service/      ← Optional hybrid Python FastAPI + LangGraph AI service
├── frontend/               ← Optional web/admin UI talking ONLY to gateway-service
├── deploy/                 ← docker-compose.infra.yml (Nacos/DB/MQ) + docker-compose.yml
└── scripts/verify          ← Maven compile + ArchUnit + Zero-Mock + tests
```

## Layout 9 — Python FastAPI + LangGraph Agent Service

```
my-project/
├── specs/
├── ai-rules/
├── frontend/               ← Optional chat/workbench UI (consumes SSE stream + HITL cards)
└── agent-service/
    ├── app/
    │   ├── api/v1/         ← FastAPI async routers (SSE, runs, approval-resume, health)
    │   ├── graphs/         ← LangGraph StateGraph (only when looping/branching/HITL needed)
    │   ├── prompts/        ← Versioned prompt templates (NEVER inline in routes)
    │   ├── tools/          ← readonly/ | mutating/ | hitl_required/
    │   ├── rag/            ← ACL-before-retrieve retriever + ingestion
    │   ├── schemas/        ← Pydantic v2 I/O & structured-output models
    │   ├── core/           ← Config, auth, trace_id, recursion_limit & budget guards
    │   └── services/       ← Business & DB access
    ├── tests/              ← Endpoint + 401/403 + mocked-LLM graph tests
    ├── evals/              ← Golden dataset + evaluation runner (Line 6: Eval Line)
    ├── scripts/verify      ← ruff/mypy + import-linter + Zero-Mock + pytest + eval smoke
    └── pyproject.toml
```

## Notes for Later Stages

- Stage 4 (frontend): your directory tree goes INSIDE the frontend root above (`frontend/`, `miniprogram/`, `app/`, `admin/`, or project root for full-stack Next.js).
- Stage 5-6 (backend): your tree goes INSIDE `backend/` (or `services/*` / `agent-service/` for Layouts 8–9).
- Stage 3 (database): schema/migration files go under `backend/` (or per-service `services/<svc>/src/main/resources/db/migration/` for Spring Cloud, `agent-service/alembic/` for FastAPI).
- Stage 9 (deploy): launch scripts / Compose / Dockerfile live in `backend/`, `agent-service/`, or `deploy/`.
