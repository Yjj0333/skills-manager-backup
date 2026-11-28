---
name: ai-tech-advisor
description: Guide non-technical users through choosing the right tech stack for AI-assisted projects. Use when starting a new project, when the user mentions "技术选型", "选技术栈", "用什么框架", "开始新项目", or asks what technologies to use for their project. Also use when the user wants to evaluate or compare frameworks, libraries, or development tools.
---

# AI Tech Stack Advisor

Guide non-technical (or lightly technical) users through choosing the right tech stack. Discussion happens in Chinese; all output documents and AI rules are generated in English.

**Core principle:** One clear recommendation, not a menu of options. Converge to a single actionable path.

## Pipeline Position

This is **Stage 2 of 9** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-db-designer** — design database from business objects and flows
4. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security
9. **backend-deploy-checkpoint** — pre-launch checklist: secrets, build & start, database backup + migration, smoke test, rollback

Stages 3 & 4 can run in parallel after Stage 2.

Before starting, read `specs/project-brief-spec.md` if it exists. If no project brief exists, recommend using `ai-project-briefing` first unless the user already provides clear product scope.
After generating `specs/tech-stack-spec.md`, recommend `ai-db-designer` (Stage 3) and `ai-frontend-scaffolder` (Stage 4) as the next stages — they can run in parallel or in either order.

## When to Use

- Starting a new project and unsure what technologies to use
- User asks "what should I use to build X?"
- Beginning of a project lifecycle, before frontend or database design

**When NOT to use:**
- User already has a clear tech stack and just wants to code
- User is asking about a specific existing technology detail
- Mid-project technology migration

## Auto-Detect Existing Context

Before starting discussion, scan the project root and `specs/` for (older projects may keep these at the project root):

| File | Action if found |
|------|----------------|
| `specs/tech-stack-spec.md` | Read it, skip to convergence |
| `specs/frontend-skeleton-spec.md` | Read for context |
| `specs/db-design-spec.md` | Read for context |
| `README.md`, `package.json`, `src/` | Scan for existing project info |

If `specs/tech-stack-spec.md` exists, summarize it and ask: "I found an existing tech stack spec. Do you want to update it or start fresh?"

## Interaction Flow

1. **Load context** — auto-detect files or start fresh
2. **Ask project overview** — adaptive depth (see below)
3. **Confirm product form** — Website / Mini Program / App / Admin Panel / API Service / AI Agent App / Enterprise Multi-Domain System
4. **Select architecture archetype** — converge to ONE canonical archetype (`layered-monolith` / `modular-monolith` / `spring-cloud-microservices` / `fastapi-langgraph-agent` / hybrid)
5. **Recommend unique tech stack** — ONE recommendation with reasoning & BOM compatibility lock
6. **Technology evaluation** — checklist for each technology
7. **Converge and confirm** — summary table, user approval
8. **Generate outputs** — spec doc + progressive `ai-rules/` + prompt templates
9. **Offer code generation** — ask user before generating any code

## Adaptive Depth Strategy

Control discussion depth based on user responses:

- **Detailed answer (50+ chars with specifics)** → Summarize understanding, confirm, move on
- **Short/vague answer** → Ask one follow-up question to clarify
- **"I don't know" or very uncertain** → Offer 2-3 example directions for their project type

**Always one question per message.** Never overwhelm with multiple questions.

## Step 1: Ask Project Overview

First question (always ask):

> 你的项目是做什么的？一句话简单描述一下。

Follow-up questions (only if needed, one at a time):
1. 目标用户是谁？（个人用户/企业/内部团队/开发者）
2. 有没有参考产品？（竞品或类似产品链接）
3. 预期用户规模？（个人使用/小团队/公开上线/大规模）

## Step 2: Confirm Product Form

> 基于你描述的项目，确认一下产品形态：

| Option | Form | Typical Stack |
|--------|------|--------------|
| A | Website | Web frontend + backend + database |
| B | Mini Program | Taro 4 (React) / uni-app (Vue 3) + backend |
| C | App | React Native (Expo) / Flutter + backend |
| D | Admin Panel | React + Ant Design 5 / Vue 3 + Element Plus + backend |
| E | API Service | Backend framework + database |
| F | AI / Agent App | Python FastAPI + Pydantic v2 (+ LangGraph when multi-step/HITL) + PostgreSQL/pgvector |
| G | Enterprise Multi-Domain System (WMS/ERP/中台) | Modular Monolith or Spring Cloud Microservices (Java 21 + Spring Boot 3.x) |
| H | Not sure | AI analyzes and recommends |

If user picks H, analyze based on project description and recommend one with reasoning.

## Step 2.5: Select Architecture Archetype

Read `references/architecture-archetypes.md` and lock ONE Architecture Archetype before choosing concrete frameworks (never jump to microservices without a real operational reason):

| Archetype | When to Choose | Default Rule |
|-----------|----------------|--------------|
| `layered-monolith` | ≤ 5 core business objects, fast MVP | Single deployable, 3-layer separation |
| `modular-monolith` | > 5 core objects, WMS/ERP/SaaS (**default for medium/large**) | Single deployable + private module tables + public Facade + DAG + static boundary check |
| `spring-cloud-microservices` | Multi-team independent release, strict isolation, or genuine scaling heterogeneity | Java 21 + Spring Boot 3.x + Spring Cloud + Alibaba; Database-per-Service + `api-contracts/` + Gateway + Outbox |
| `fastapi-langgraph-agent` | AI workflows, RAG, tool-calling agents | Complexity-gated: simple AI = FastAPI + Pydantic only; stateful/HITL loop = FastAPI + LangGraph `StateGraph` |

*(Hybrid allowed only with clear reason: e.g., `spring-cloud-microservices` core + `fastapi-langgraph-agent` AI service behind Gateway.)*

If the project uses **FastAPI / LangGraph** and the user is a Java backend developer who has not learned them yet, briefly present the **Java-to-FastAPI/LangGraph mental-model table** from `references/architecture-archetypes.md` (`APIRouter ≈ @RestController`, `Pydantic ≈ DTO + @Valid`, `Depends ≈ Spring DI`, `async def ≈ WebFlux/Netty I/O 线程`, `Alembic ≈ Flyway`, `uv ≈ Maven`). For simple single-call AI inside an existing Java monolith, also note **Spring AI** as a zero-Python option.

## Step 3: Recommend Unique Tech Stack

Present ONE recommendation based on product form and Architecture Archetype. For backend services, **default to the user's primary Java 21 + Spring Boot 3.x ecosystem** unless the project is an AI/Agent runtime (`fastapi-langgraph-agent`) or a tiny static/SSR-only site.

**For Website / Admin Panel / Mini Program / App (Backend-backed):**
- **Backend (Default Java Primary Stack):** Java 21 + Spring Boot 3.x + Maven + **MyBatis-Plus** (default; Spring Data JPA optional) + **Flyway** + **SpringDoc OpenAPI 3 / Knife4j** + **Spring Security 6** (default; Sa-Token for lightweight admin panels)
- **Database:** MySQL 8 (default for Chinese Java/enterprise ecosystems) or PostgreSQL (when vector/`pgvector` or complex JSONB queries matter)
- **Frontend:**
  - Website: React 19 (Vite + TypeScript) + Tailwind CSS v4 + shadcn/ui (or Next.js 15 when SEO/SSR is mandatory)
  - Admin Panel: React + Ant Design 5 or Vue 3 + Element Plus
  - Mini Program: Taro 4 (React) or uni-app (Vue 3); deploy via WeChat Cloud Base or Docker VPS
  - App: Expo (React Native) or Flutter
- **Deployment:** Docker VPS / Railway (Spring Boot layered JAR `eclipse-temurin:21-jre` + Nginx/Vercel for frontend)

**For Enterprise Microservices (`spring-cloud-microservices`):**
- Runtime & Core: Java 21 + Spring Boot 3.x + Spring Cloud + Spring Cloud Alibaba (Gateway + Nacos + OpenFeign + Sentinel + RocketMQ/RabbitMQ) + MyBatis-Plus + Flyway
- Data: MySQL 8 / PostgreSQL (strict **Database-per-Service**, no cross-service DB sharing)
- Mandatory check: **verify and lock the official Spring Boot ↔ Spring Cloud ↔ Spring Cloud Alibaba BOM compatibility table** before generating `pom.xml`

**For AI / Agent App (`fastapi-langgraph-agent`):**
- Backend & Validation: Python 3.11+ (`uv` + `pyproject.toml`) + FastAPI + Pydantic v2 + `httpx` (async-first; no blocking IO inside `async def`)
- Orchestration: LangGraph `StateGraph` ONLY when looping tools, multi-step branching, or human-in-the-loop `interrupt` is required (single-pass AI in Java monoliths can stay on **Spring AI**; single-pass Python AI stays FastAPI + `with_structured_output`)
- Persistence & Retrieval: PostgreSQL (`pgvector` + Alembic + persistent LangGraph `PostgresSaver` checkpointer; `MemorySaver` forbidden in production)
- Streaming & Evals: Server-Sent Events (SSE) + `evals/` golden dataset regression suite

**For API Service:** Java 21 + Spring Boot 3.x + MyBatis-Plus + Flyway + SpringDoc OpenAPI 3.1 (or FastAPI for AI/ML-only services)

**Project directory structure** (details: `references/project-structure.md`):

| Archetype / Product form | Layout |
|--------------------------|--------|
| Full-stack website (Next.js) | Single app at project root |
| Frontend + separate backend | `frontend/` + `backend/` |
| Mini Program / App / Admin | `miniprogram/` or `app/` or `admin/` + `backend/` |
| API service | `backend/` only |
| Modular Monolith | `frontend/` (if any) + `backend/src/modules/<domain>/` (Layout 7) |
| Spring Cloud Microservices | `pom.xml` + `common/` + `api-contracts/` + `gateway-service/` + `services/*` + `deploy/` (Layout 8) |
| FastAPI + LangGraph Agent | `agent-service/` (or `frontend/` + `agent-service/` / `services/agent-service/`, Layout 9) |

Every layout also has `specs/` for stage documents and `ai-rules/` for progressive agent rules. Frontend and backend never share a `src/`. Include the chosen **Architecture Archetype** and layout in the recommendation.

**Critical rule:** Present ONE recommendation. If alternatives exist, explain why they are NOT recommended for this specific project.

## Step 4: Technology Evaluation

Evaluate each technology using the checklist (reference: `references/tech-checklist.md`):

| Check | What to verify |
|-------|---------------|
| Community | GitHub stars, recent commits, issue activity |
| Documentation | Official docs quality, Chinese resources |
| Maintenance | Last release date, active maintainers |
| License | Commercial use allowed? |
| AI-friendliness | Well-represented in AI coding agents' training data (Claude Code / Cursor / Codex)? Mainstream stacks are safer for unattended AI maintenance |
| Complexity | Can AI maintain it without human intervention? |

Present as a simple table. Flag any risks.

## Step 5: Converge and Confirm

> 以下是为你的项目推荐的技术栈：
>
> | Layer | Technology | Why |
> |-------|-----------|-----|
> | ... | ... | ... |
>
> 主要风险：...
>
> 这个方案可以吗？确认后我会生成技术选型文档和 AI 规则文件。

## Step 6: Generate Outputs

After user confirms, generate:

### 1. `specs/tech-stack-spec.md` (English)

Contains: project overview, **Architecture Archetype** (`layered-monolith` / `modular-monolith` / `spring-cloud-microservices` / `fastapi-langgraph-agent` / hybrid), recommended stack table + BOM compatibility locks, project directory structure, technology evaluation, risks and mitigations, alternatives considered, AI agent constraints.

### 2. `ai-rules/` directory (Progressive Context Harness)

Generate platform-specific rule files (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`):
- Keep the root rule file **concise (≤ 120 lines)** as the master router (Architecture Archetype, layout, single `verify` command, strict module & Zero-Mock red lines, `specs/` index).
- For multi-service or frontend/backend split projects, generate focused sub-directory rule files (`frontend/AGENTS.md`, `backend/AGENTS.md`, `services/<svc>/AGENTS.md`) instead of bloating the root file.

### 3. `ai-rules/prompt-templates.md`

Project-specific prompt templates from `references/prompt-templates.md`, customized for the chosen stack.

## Step 7: Offer Code Generation

> 技术选型文档和 AI 规则已生成。接下来我可以帮你：
>
> - **A) 初始化项目结构** — 按选定布局创建 specs/、backend/、frontend/ 等目录，生成框架初始化命令（Spring Initializr / mvn / npm create / uv init）和 .gitignore
> - **B) 将规则写入项目** — 把 AI 规则文件放到项目根目录
> - **C) 暂时不需要** — 我先看看文档

Only proceed when user confirms.

## Red Flags — STOP and Re-discuss

| Thought | Reality |
|---------|---------|
| User's tech choice is trendy but wrong | Explain why, offer better alternative |
| User wants to skip evaluation | At minimum check license and maintenance |
| User asks for multiple stacks to compare | Converge to one. Alternatives only for trade-off explanation |
| User says "just pick whatever" | Never skip. Analyze the project and pick with reasoning |

## Common Mistakes to Avoid

1. **Listing options instead of recommending one** — User needs direction, not a menu
2. **Choosing trendy over practical** — Best stack = one AI can maintain
3. **Skipping evaluation** — Quick check prevents painful surprises
4. **Forgetting deployment** — Must include how the project will be deployed
