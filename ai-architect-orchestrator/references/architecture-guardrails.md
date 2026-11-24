# Chief Architect Governance & Guardrails — AI Project Toolkit

Reference rules enforced by `ai-architect-orchestrator` across all stages to prevent architectural drift, cross-spec mismatches, and mock/fake-code pollution in production source paths.

---

## 1. Production Code Purity (Zero-Mock / Zero-Stub / Zero-Silent-Fallback)

### Five Zero-Tolerance Prohibitions (正式业务代码目录严禁出现)

Inside production source directories (`src/`, `app/`, `pages/`, `components/`, `services/`, `modules/`, `routes/`, `controllers/`, etc. — excluding `tests/`, `__tests__/`, `seeds/`, and explicitly isolated `mocks/`):

1. **No hardcoded business mock data in production paths**: never embed `MOCK_*`, `mockOrders`, `dummyList`, `sampleUsers`, `fakeResponse`, or hardcoded business arrays directly into components, services, controllers, or API handlers.
2. **No silent catch-to-mock fallbacks**: never swallow API, DB, or integration errors and silently return mock/sample data (e.g., `try { await fetchOrders() } catch { return MOCK_ORDERS }` or falling back to fake data when an endpoint returns empty/error). Failures MUST propagate through the unified error handler (`ErrorState` + retry on frontend; unified 4xx/5xx JSON + server log on backend).
3. **No in-memory fake databases**: never store or mutate business entities in module-level arrays, `Map`, or `Set` (e.g., `const fakeDb = []`, `let mockUsers = [...]`) in place of real database persistence.
4. **No fake authentication, authorization, or payment/webhook bypasses**: never hardcode fake user sessions, fixed tokens, `if (req.headers['x-mock-user'])` backdoors, skipped signature/JWT checks, or `// TODO: add permission check later` in production routes.
5. **No fake `200` success responses for unimplemented endpoints**: if an endpoint is not yet implemented, either do not mount the route or explicitly return `501 Not Implemented` — never return `{ success: true, data: ... }` stub payloads.

### Only Three Permitted Locations for Mock / Sample Data

| Permitted Location | Condition | Production Build / Runtime Rule |
|--------------------|-----------|---------------------------------|
| **1. Automated test suites** (`tests/`, `__tests__/`, `*.test.*`, `*.spec.*`) | Unit, integration, and contract tests | Excluded from production runtime bundle and API handlers |
| **2. Isolated frontend preview mocks** (`mocks/` / MSW / independent adapter) | **Only** when the user explicitly requests previewing UI before backend endpoints exist | Must live outside `pages/`/`components/`/`services/`, gated strictly by `DEV && USE_MOCK === 'true'`, **default `false`**, and MUST block or strip in production builds (`vite`/`next` build check) |
| **3. Database seed scripts** (`seeds/`, `prisma/seed.*`, `fixtures/`) | Explicit CLI-invoked dev/test seeding | Never auto-executed inside HTTP request handlers or app boot in production |

### Static Purity Audit Checklist (Mock 污染静态扫描清单)

Run this scan at **Gate 5** (before Stage 7, Stage 8, Stage 9, and any milestone sign-off):

- **Scope**: project production source directories (`frontend/src/`, `admin/src/`, `miniprogram/src/`, `app/`, `backend/src/`), **excluding** `node_modules/`, `.venv/`, `dist/`, `build/`, `tests/`, `__tests__/`, `*.test.*`, `*.spec.*`, `seeds/`, and explicitly isolated `mocks/`.
- **High-risk keywords & patterns to scan**:
  - Identifiers: `\b(mock|fake|dummy|stub|sampleData|testData)\b` (case-insensitive)
  - Placeholders: `\b(TODO|FIXME|XXX|HACK|placeholder)\b` in auth, permission, payment, or DB logic
  - Silent fallback anti-pattern: `catch\s*\(.*\)\s*\{[^}]*(return|set\w+)\s*(\[|MOCK|mock|fake|sample|dummy)`
  - Fake persistence / hardcoded auth: `const\s+\w*(db|store|users|orders)\s*=\s*\[`, `x-mock-`, `skipAuth`, `return true\s*//\s*(temp|todo|mock)`
  - Unimplemented `200` stubs: route handlers returning static literals without calling service/DB
- **Verdict Rule**:
  - Any unexempted hit in production source paths = **`🚫 阻塞（正式代码混入 Mock/占位逻辑）`**.
  - Must be deleted and replaced with real DB/API wiring (or moved into gated `mocks/` only for pre-backend UI preview with explicit user acknowledgment) before proceeding.

---

## 2. Cross-Spec Consistency & Constitution Wiring Matrix

Before unlocking downstream design or implementation stages, verify alignment across specs and agent rules:

### A. Agent Rules Wiring (`ai-rules/` → Project Root)

| Check | Expected State | If Missing |
|-------|----------------|------------|
| Stage 2+ projects | `ai-rules/AGENTS.md`, `CLAUDE.md`, `.cursorrules` synced to project root (or active platform location) | Flag `⚠️ 规则未落盘根目录`, instruct syncing before coding |
| Zero-Mock rule present | Root agent rules explicitly forbid mock data, in-memory fake DBs, and silent catch-to-mock fallbacks in production code | Remind user/agent to add the rule from Stage 4/6 outputs |

### B. Cross-Spec Contract Matrix

| Upstream Spec | Downstream Spec | Must Match (Zero Drift) |
|---------------|-----------------|-------------------------|
| `specs/project-brief-spec.md` (`2.6 对象与状态机`, `3.X 数据描述`) | `specs/db-design-spec.md` | Every core P0 business object has a table; status enums & ownership FKs (`user_id` / `owner_id`) match SRS rules |
| `specs/project-brief-spec.md` (`2.4 角色权限`, `3.X 前置/可选流/后置`) + `specs/db-design-spec.md` | `specs/backend-api-spec.md` | Every P0 use case maps to explicit API endpoint(s) with matching Auth, Roles, Ownership rule, Error codes, Pagination, Idempotency |
| `specs/backend-api-spec.md` (response envelope `{success, data, error}`, endpoints) | `specs/frontend-skeleton-spec.md` & `services/` | Frontend `services/` consumes exact backend envelope, version prefix (`/api/v1/...`), pagination shape, and maps failure codes to `ErrorState` |
| `specs/backend-architecture-spec.md` | `specs/backend-impl-source-of-truth.md` & code | Actual directory responsibilities, startup commands, and 5-line rules match verified evidence |

---

## 3. Vertical Slice MVP Delivery Protocol (Stage 7 → Stage 8)

Do **not** build all frontend pages with fake data first and all backend endpoints separately at the end ("big-bang mock integration"). Deliver the MVP in vertical end-to-end slices:

1. **Slice 0 — Auth, Session & Role Guardrails**
   - DB migration + real register/login/me endpoints + password hashing + auth/role middleware + frontend login/guard + happy-path & 401/403 tests.
2. **Slice 1 — Core Primary Business Flow (P0 Main Entity)**
   - DB migration + real backend CRUD/state-transition APIs + ownership checks + unit/integration tests + real frontend list/detail/form wired directly to API + `loading`/`empty`/`error` states (zero mock data).
3. **Slice 2..N — Remaining P0 Modules (One Module at a Time)**
   - Repeat end-to-end per SRS module (`specs/modules/*.md` or Chapter 3).
   - **Gate between slices**: Previous slice passes API tests, frontend real-API smoke check, and Zero-Mock scan before starting the next slice.

---

## 4. Architecture Decision Record (ADR) & Change Impact Protocol

Whenever an agent or user proposes a structural change during Stage 6–9 or Iteration Mode, require an impact check and a lightweight ADR entry (recorded in `specs/adr-log.md` or appended to `specs/backend-impl-source-of-truth.md`).

### Trigger Conditions
- Adding a new critical runtime dependency (cache, queue, auth SDK, third-party payment/storage)
- Changing directory layout, layer boundaries, or project profile
- Changing unified API response envelope, error code convention, or auth/session mechanism
- Changing database engine, ORM, or core entity ownership/state-machine model

### Lightweight 5-Part ADR Format

```markdown
### ADR-00X: [决策标题]
- **日期与状态**：YYYY-MM-DD | Proposed / Accepted / Superseded
- **背景问题**：[为什么现有架构/方案无法满足需求]
- **最终决策与原因**：[选定的方案及核心依据]
- **放弃的备选方案**：[考虑过但未选的方案及原因]
- **受影响文档与验证**：[同步更新 specs/*.md 列表 + 回归/静态扫描验证结果]
```
