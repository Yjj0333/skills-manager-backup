# Backend Skeleton Checklist

Use this checklist to verify the minimal runnable backend skeleton is complete.

## Five Lines (+ Conditional Eval Line) Verification

### Line 1: Startup Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 1 | Project starts without errors | ☐ | |
| 2 | Configuration reads from env/file (not hardcoded) | ☐ | |
| 3 | `.env.example` template exists | ☐ | |
| 4 | Health check endpoint responds (`/health` or Actuator `liveness`/`readiness`) | ☐ | |

### Line 2: API Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 5 | Routes follow framework conventions | ☐ | |
| 6 | List success response format defined | ☐ | |
| 7 | Object success response format defined | ☐ | |
| 8 | Error responses unified (400/401/403/404/500) | ☐ | |
| 9 | Business error code rules documented (if needed) | ☐ | |

### Line 3: Business Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 10 | Request entry point identified | ☐ | |
| 11 | Business logic layer separated | ☐ | |
| 12 | Data access layer separated | ☐ | |
| 13 | Parameter validation location identified | ☐ | |
| 14 | Permission check location identified | ☐ | |

### Line 4: Operations Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 15 | Unified logging with `request_id` / `trace_id` propagation works | ☐ | |
| 16 | Unified error handling works | ☐ | |
| 17 | Database connection verified | ☐ | |
| 18 | Permission middleware placeholder exists | ☐ | |
| 19 | README has startup/config/test/`verify` instructions | ☐ | |

### Line 5: Testing, Static Boundary & `verify` Harness Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 20 | Test framework initialized (Vitest/Jest/pytest/JUnit 5) | ☐ | |
| 21 | Sample endpoint happy-path test passes (unified success format) | ☐ | |
| 22 | Unauthorized-rejection test passes (expects 401/403) | ☐ | |
| 23 | Static module boundary check configured (ArchUnit / import-linter / eslint-plugin-boundaries) | ☐ | |
| 24 | Single-command `verify` harness runs green | ☐ | |

### Conditional Archetype Checks (Modular / Spring Cloud / FastAPI+LangGraph)

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 25 | (`modular-monolith`) Module public Facade + DAG zero-cycle check passes | ☐ | |
| 26 | (`spring-cloud-microservices`) Parent BOM locked, `common/` pure, Gateway + `api-contracts` + `docker-compose.infra.yml` ready | ☐ | |
| 27 | (`fastapi-langgraph-agent`) `app/prompts/`, async non-blocking check, `recursion_limit`, persistent checkpointer, Line 6 `evals/` smoke test | ☐ | |

## Architecture Document Checks

| # | Item | Status |
|---|------|--------|
| 28 | Language, framework, and Architecture Archetype confirmed and locked | ☐ |
| 29 | Language engineering conventions documented | ☐ |
| 30 | Framework best practices documented | ☐ |
| 31 | Directory structure & module boundary rules explained with origins | ☐ |
| 32 | New module file organization rules documented | ☐ |
| 33 | Framework maximization principle stated | ☐ |

## Decision Criteria

- All Line 1–5 items (1–24) must pass before skeleton acceptance
- Applicable conditional items (25–27) must pass for the chosen Architecture Archetype
- Architecture document items (28–33) must pass for sustainable development
