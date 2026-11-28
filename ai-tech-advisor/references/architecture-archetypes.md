# Standard Engineering Architecture Archetypes & Agent Harness

Canonical architecture templates selected at Stage 2 (`ai-tech-advisor`), recorded in `specs/tech-stack-spec.md`, and enforced across Stages 3–9 by `ai-architect-orchestrator`.

---

## 1. Architecture Archetype Decision Tree (选型决策树)

Always start with the simplest architecture that satisfies real operational constraints. **Never split into microservices just to "look enterprise."**

```
Project Scope & Runtime Needs
  │
  ├─ AI / LLM Agent / RAG / Multi-step Tool Workflow?
  │    └─ YES ──▶ Archetype 4: fastapi-langgraph-agent
  │               (Hybrid: pair with Spring Cloud or Next.js when enterprise core exists)
  │
  ├─ Truly independent scaling / polyglot runtime / multi-team isolation / strict compliance?
  │    └─ YES ──▶ Archetype 3: spring-cloud-microservices
  │               (Java 21 + Spring Boot 3.x + Spring Cloud + Alibaba)
  │
  ├─ Multi-domain business system (> 5 core business objects, e.g., WMS / ERP / SaaS)?
  │    └─ YES ──▶ Archetype 2: modular-monolith  [DEFAULT FOR MEDIUM/LARGE]
  │
  └─ Small MVP / simple utility (≤ 5 core business objects)?
       └─ YES ──▶ Archetype 1: layered-monolith
```

---

## 2. Archetype 1: `layered-monolith` (轻量分层单体)

- **When to use:** ≤ 5 core business objects, single team/solo vibe coding, fast MVP validation.
- **Structure:** Standard 3-layer separation (`routes/controller → service → repository`) under a single backend root + single database.
- **Guardrails:** Request handling, business rules, and DB access stay separated; unified response/error envelope; Zero-Mock purity; single `verify` script.

---

## 3. Archetype 2: `modular-monolith` (严格模块化单体 — 中大型业务默认主力)

Single deployable process, **strictly partitioned by bounded domain modules** so it never rots into a Big Ball of Mud and can split cleanly into microservices later.

### Mandatory Hard Constraints
1. **Table Ownership (数据表私有权):** Every table in `specs/db-design-spec.md` declares ONE `Owning Module`. Other modules **MUST NOT** write to or `JOIN` another module's private tables directly.
2. **Unique Public Facade / Port:** Cross-module reads or commands MUST call the owning module's public facade/API interface (`modules/<domain>/index.ts` or `Facade` / `Port`), never deep-import `modules/<other>/repository` or internal entities.
3. **Module DAG (Zero Circular Dependencies):** `specs/backend-architecture-spec.md` declares a directed acyclic module dependency matrix. `Module A ↔ Module B` circular imports are forbidden; break cycles via **In-Process Domain Events** or an extracted orchestration layer.
4. **`shared/` Zero-Business Rule:** `shared/` or `common/` holds ONLY pure technical utilities (logger, error envelope, clock, pagination helper) — zero business models or domain logic.
5. **Machine-Enforced Boundaries:** Configure static architecture checks that fail `verify` on violations:
   - TypeScript/Node: `eslint-plugin-boundaries` or `dependency-cruiser`
   - Java/Spring Boot: `Spring Modulith` (`ApplicationModules.verify()`) or `ArchUnit`
   - Python: `import-linter`

---

## 4. Archetype 3: `spring-cloud-microservices` (Spring Cloud 企业级微服务)

- **Default Stack:** Java 21 + Spring Boot 3.x + Spring Cloud + Spring Cloud Alibaba (`Spring Cloud Gateway` + `Nacos` + `OpenFeign` + `Sentinel` / `Resilience4j` + `RocketMQ` or `RabbitMQ`) + MySQL / PostgreSQL.
- **BOM Compatibility Lock:** Before generating `pom.xml`, MUST verify and lock the official Spring Boot ↔ Spring Cloud ↔ Spring Cloud Alibaba BOM version compatibility matrix in `specs/tech-stack-spec.md`. Never mix mismatched major/minor releases.

### Canonical Multi-Module Layout
```text
my-project/
├── pom.xml                       ← Parent POM: ONLY place locking BOM & dependency versions
├── common/                       ← Pure technical primitives ONLY (Result, ErrorCode, TraceId, SecurityContext)
├── api-contracts/                ← Shared Feign clients + Request/Response DTOs + Domain Event schemas
│   ├── order-api/
│   └── inventory-api/
├── gateway-service/              ← North-South ingress: JWT verification, rate limit, header stripping
├── services/
│   ├── auth-service/             ← Independent Spring Boot app + own DB/Schema
│   ├── order-service/
│   └── inventory-service/
└── deploy/
    ├── docker-compose.infra.yml  ← Nacos, MySQL/Postgres, Redis, MQ
    └── docker-compose.yml        ← Multi-service orchestration with health/readiness order
```

### Seven Non-Negotiable Microservice Constraints
1. **Parent BOM Single Source of Truth:** Child modules never invent conflicting Spring/Netty/Jackson dependency versions.
2. **`common/` Zero Business Pollution:** `common/` must never contain domain entities, business enums, or service-specific DTOs.
3. **No Direct Service-to-Service Maven Dependency:** `order-service` MUST NOT depend on `inventory-service` in `pom.xml`; it depends ONLY on `api-contracts/inventory-api`.
4. **Database-per-Service:** Every `*-service` owns an isolated database (or isolated DB schema + dedicated DB user). Cross-service SQL `JOIN` or shared-table writes are strictly prohibited.
5. **Gateway Trust Boundary:** `gateway-service` verifies external JWT/sessions, injects canonical identity headers (`X-User-Id`, `X-User-Roles`), and **strips any client-supplied `X-User-*` / `X-Internal-*` headers** on ingress. Internal services only expose `/internal/v1/...` on private networks and are not directly internet-exposed.
6. **Timeout, Real Degradation & Concurrency Safety:**
   - Every OpenFeign client sets explicit `connectTimeout` and `readTimeout`;
   - Sentinel / Resilience4j fallbacks MUST return explicit degraded errors or read-only safe state — **NEVER return fake `200` business data**;
   - Cross-service state changes use **Transactional Outbox (`outbox_events`) + MQ + Idempotent Consumer (`processed_messages`) + Saga compensation** — never bare DB write followed by bare MQ publish;
   - Stock/balance updates use conditional optimistic locking (`WHERE stock >= qty` or `version = ?`).
7. **Distributed Observability & Probes:** Propagate W3C `traceparent` / Micrometer `traceId` across Gateway → Feign → MQ; expose Actuator `/actuator/health/liveness` and `/actuator/health/readiness`.

*(Hybrid Note: When enterprise business runs on Spring Cloud and needs AI/Agent workflows, mount an isolated `services/agent-service/` built with Archetype 4 behind Gateway / OpenAPI rather than writing complex LLM orchestration in Java.)*

---

## 5. Archetype 4: `fastapi-langgraph-agent` (Python FastAPI + LangGraph 智能体架构)

Designed specifically so **Java backend engineers who have not yet learned FastAPI or LangGraph** can govern Python AI agents safely using familiar Spring/Java mental models, avoiding silent runtime bugs or runaway token bills.

### Java 工程师秒懂对标映射表（Java ↔ FastAPI + LangGraph）

| Python / AI 概念 | 对标你熟悉的 Java/Spring 概念 | 大白话作用与核心红线 |
| :--- | :--- | :--- |
| **`uv` + `pyproject.toml`** | **Maven + `pom.xml`** | 依赖与虚拟环境管理；锁死包版本（`uv.lock` ≈ Maven BOM） |
| **FastAPI `APIRouter`** | **Spring MVC `@RestController`** | 收请求、推 SSE 流式响应；默认异步非阻塞 |
| **Pydantic `BaseModel`** | **`RequestDTO` + Jakarta `@Valid`** | 自动反序列化 + 参数校验，不合法直接抛 422/400 |
| **`Depends(...)`** | **Spring DI 构造注入 / `HandlerInterceptor`** | 注入当前用户鉴权、DB 会话、权限检查依赖 |
| **`async def` 事件循环** | **WebFlux / Netty I/O 线程** | **严禁在 `async def` 里调同步阻塞代码**（如 `requests.get`/`time.sleep`/同步 JDBC 式驱动），否则全服务卡死 |
| **SQLAlchemy Async + Alembic** | **MyBatis-Plus / JPA + Flyway** | ORM 与版本化数据库迁移脚本 |
| **LangGraph `StateGraph`** | **持久化多步编排状态机** | 把 AI 干活拆成节点（查库 → 调工具 → 总结）和条件边；比手写 `while` 循环更可控 |
| **Checkpointer (`PostgresSaver`)** | **数据库状态快照（Spring StateMachine 持久化）** | 每走一步自动存档进库；断网或等人工审批后按 `thread_id` 续跑（**生产禁 `MemorySaver`**） |
| **Interrupt (HITL)** | **高危操作前的异步挂起人工审批** | AI 想删数据/发请求/动资金时暂停，前端确认后调用恢复接口继续执行 |
| **`evals/` 评测线** | **Prompt 回归 JUnit 测试套** | 每次改 Prompt 或换模型跑标准考卷（JSONL），防止效果退化 |

### 复杂度分流门禁（Complexity Gate — Do NOT Over-Engineer）
- **Simple Deterministic AI inside Java Monolith:** single LLM call / fixed summarize or classify inside a Spring Boot service → consider **Spring AI** directly in Java (no need to spin up Python).
- **Simple Deterministic Python AI Flow** (single LLM call, no looping tool calls, no human pause): use **FastAPI + Pydantic `with_structured_output` ONLY**. Do **NOT** force LangGraph.
- **Stateful / Multi-Step Agent Flow** (autonomous tool selection, retry/reflection loops, multi-agent routing, or human-in-the-loop pause/resume): use **FastAPI + LangGraph `StateGraph`**.

### Canonical Directory Layout
```text
agent-service/
├── app/
│   ├── api/v1/          ← FastAPI routers (chat, runs, resume-approval, health)
│   ├── graphs/          ← LangGraph StateGraph definitions, state schemas, nodes, edges
│   ├── prompts/         ← Versioned prompt templates (Markdown/YAML) — NEVER inline in routes
│   ├── tools/           ← Tool registry grouped by risk: readonly/ | mutating/ | hitl_required/
│   ├── rag/             ← Ingestion, chunking, ACL-filtered retriever
│   ├── schemas/         ← Pydantic v2 request/response/SSE & structured-output contracts
│   ├── core/            ← Config, auth, logging/trace_id, LLM client, budgets/limits
│   └── services/        ← Business orchestration & DB repositories
├── tests/               ← FastAPI endpoint tests, 401/403 tests, mocked-LLM graph unit tests
├── evals/               ← Golden dataset (JSONL) + scoring script (Line 6: Eval Line)
├── scripts/verify       ← Single-command verification harness
└── pyproject.toml
```

### Six Beginner-Proof Hard Constraints (防炸六铁律)
1. **No Sync Blocking Inside `async def`:** FastAPI routes and async graph nodes MUST use async SDKs (`httpx.AsyncClient`, `asyncpg`, `ainvoke`/`astream`). Never call blocking `requests.get`, `time.sleep`, or sync DB drivers directly inside `async def` (use `asyncio.to_thread` only if an unavoidable sync library exists).
2. **Mandatory Loop & Budget Circuit Breakers:** Every `StateGraph` invocation MUST pass `recursion_limit` (e.g. `{"recursion_limit": 15}`), per-tool timeout, and per-user/session token or rate budget. Unbounded loops are strictly forbidden.
3. **Centralized Prompts & Strict Structured Output:** All system prompts live under `app/prompts/` with version headers; model JSON outputs MUST be parsed through Pydantic v2 schemas (`with_structured_output`), never fragile string slicing or `eval()`.
4. **Tool Risk Tiers & Mandatory HITL (`interrupt`):** Classify every tool in `app/tools/`:
   - `Read-Only` (search, query): auto-executable within user ACL;
   - `Mutating` (draft, safe update): idempotency key required;
   - `Destructive / External` (delete, payment, external email/API write): MUST trigger LangGraph `interrupt()` and wait for explicit user approval endpoint before executing.
5. **ACL-Before-Retrieve RAG & Injection Guard:** Vector/BM25 retrieval MUST apply metadata permission filters (`tenant_id` / `user_id` / `role`) **inside the DB query before context assembly** (never filter after retrieval). Wrap retrieved external text in explicit untrusted data delimiters (`<untrusted_context>...</untrusted_context>`).
6. **Persistent Checkpointer in Production (Zero `MemorySaver`):** `MemorySaver` / `InMemorySaver` is allowed ONLY in `tests/`. Staging and production MUST configure `PostgresSaver` or `RedisSaver` so thread states survive restarts and HITL approvals work reliably.

---

## 6. Coding Agent Engineering Harness (面向 AI 编程的仓库级约束模版)

Every project generated by this toolkit MUST enforce two repository-level Agent Harness mechanisms:

1. **Progressive Context Rules (`AGENTS.md` / `CLAUDE.md` / `.cursorrules`)**:
   - **Root `AGENTS.md` ≤ 120 lines**: keeps ONLY (a) selected Architecture Archetype & directory map, (b) single `verify` command, (c) strict module dependency & Zero-Mock red lines, (d) `specs/` index.
   - **Sub-directory `AGENTS.md`** (e.g. `frontend/AGENTS.md`, `backend/AGENTS.md`, `services/<svc>/AGENTS.md`): holds stack-specific conventions loaded only when working inside that folder.
2. **Single-Command Deterministic `verify` Harness (`scripts/verify.ps1` / `scripts/verify.sh` or `package.json` `verify`)**:
   - Must execute sequentially and exit non-zero on any failure:
     1. Build / Typecheck / Compile (`tsc --noEmit` / `mvn test-compile` / `ruff check` + `mypy`)
     2. Static Module Boundary Check (`eslint-plugin-boundaries` / `ArchUnit` / `import-linter`)
     3. Zero-Mock Purity Scan on production source paths
     4. Test Suite (`vitest` / `mvn test` / `pytest`, including happy path + 401/403 authorization tests)
     5. *(Archetype 4 only)* Lightweight deterministic `evals/` smoke check
