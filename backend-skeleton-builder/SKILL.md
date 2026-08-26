---
name: backend-skeleton-builder
description: Guide non-technical users through building a minimal runnable backend skeleton with rules-first approach. Use when the user mentions "后端骨架", "后端搭建", "搭建后端", "后端底层架构", "最小可运行", "后端规则", "骨架搭建", or wants to set up backend structure before writing business features.
---

# Backend Skeleton Builder

Guide the user through building a minimal runnable backend skeleton based on established rules and architecture design documents. Discussion happens in Chinese; output documents and AI rules are generated in English.

**Core principle:** Do not write business features first. Define rules, write them into the architecture design document, then build the minimal runnable skeleton that enforces those rules.

## Pipeline Position

This is **Stage 6 of 8** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
4. **ai-db-designer** — design database from business objects and flows
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security

Read earlier stage specs before starting. If `backend-api-spec.md` is missing, recommend completing Stage 5 first. If `tech-stack-spec.md` is missing, recommend Stage 2 first.

## Auto-Detect Existing Context

Scan for:

| File | Action |
|------|--------|
| `project-brief-spec.md` | Read for business boundaries and user scenarios |
| `tech-stack-spec.md` | Read for confirmed backend language and framework |
| `frontend-skeleton-spec.md` | Read for frontend pages and API needs |
| `db-design-spec.md` | Read for database design and business objects |
| `backend-api-spec.md` | Read for API boundaries, auth, validation rules |
| `backend-architecture-spec.md` | Read and offer to update |
| Existing backend folders | Inspect current project structure |

## Interaction Flow

1. **Confirm business boundaries** — verify project scope and user scenarios are documented
2. **Confirm language and framework** — lock down tech route, no wavering
3. **Define engineering rules** — language conventions, framework best practices, project customs
4. **Write architecture design document** — merge business boundaries and engineering rules
5. **Build minimal skeleton** — four lines: startup, API, business, operations
6. **Verify skeleton runs** — confirm it actually starts and responds
7. **Generate outputs** — architecture spec, AI rules, prompt templates

## Step 1: Confirm Business Boundaries

Ask:

> 你的项目有哪些用户场景？主要业务逻辑是什么？主要功能有哪些？

If `project-brief-spec.md` exists, summarize it and confirm. The user must ensure AI clearly knows the business context. Without business boundaries, AI will guess what the user needs.

Check:
- Are user scenarios documented?
- Are main business flows clear?
- Are core business objects identified?

If missing, recommend completing `ai-project-briefing` first.

## Step 2: Confirm Language and Framework — Lock the Route

This step is NOT re-selection. It is confirmation and lockdown.

Ask:

> 当前后端语言和框架是什么？这个选择有没有写进项目架构设计文档？

Then require AI to answer:
- Why this language? Why not alternatives?
- Does this project truly need this complexity level?
- Is the choice driven by real project needs, or by "security feel" / "performance feel" / "advanced feel"?

**Key rule:** Vibe coding projects fear tech route wavering most. Today Python is simple, tomorrow Go is professional, next day Java is stable. Lock it down.

**Language selection guidance for vibe coding users:**

| Situation | Recommendation |
|-----------|---------------|
| Common business system, admin panel, API service | Simpler language, lower understanding cost, easier to maintain |
| Enterprise system, legacy requirement, performance-critical | Heavier language is justified, but must use mature framework |
| Company standard or historical system | Follow the standard, use framework to constrain AI |

**Constraint prompt for AI agent:**

> 请根据项目架构设计文档确认当前后端语言和框架是否适合本项目。不要重新发散选型，只判断是否存在为了"高级感""性能感"或"安全感"而过度选型的问题。如果当前语言或框架较重，请说明项目为什么真的需要它，以及后续必须遵守哪些成熟框架规范和最佳实践。

## Step 3: Define Engineering Rules from Three Sources

After locking the language and framework, require AI to explain rules from three sources:

### Source 1: Language engineering conventions
- Dependency management
- Configuration reading
- Logging patterns
- Exception handling
- Testing conventions

### Source 2: Framework best practices
- Different languages and frameworks have their own conventions
- Cannot mix conventions from different frameworks
- Must follow official documentation or mainstream best practices

### Source 3: Project architecture design document
- Language and framework only tell you "how to write in general"
- They don't know how YOUR users, orders, permissions, payments should be organized
- This is why Stage 1 (project briefing) exists

**These three sources must merge into the architecture design document.**

The document must explain:
- Which directories come from framework recommendations
- Which directories are project-customized, and why
- If deviating from framework conventions, what is the reason
- How new modules should organize files going forward

**Framework maximization principle:**

> 框架最大化利用——用框架就是为了少踩坑。HTTP 状态码、参数校验、错误处理、中间件、日志、路由分组，很多成熟框架本来就有推荐写法。能用框架自带能力就不要让 AI 在框架外面再手写一套。

Write this into agent constitution:

> 后端开发必须遵守当前语言工程规范和框架最佳实践，优先复用框架能力。新增依赖、目录调整、错误码自定义、框架更换，都要先说明原因，并更新项目架构设计文档。

## Step 4: Write Architecture Design Document

Require AI to generate the architecture design document with this prompt:

> 请根据立项文档和已确定的后端语言框架，整理项目架构设计文档。不要写业务代码。文档必须写清楚：
> - 后端语言和框架选择原因，不选其他方案的原因
> - 必须遵守的语言工程规范
> - 必须遵守的框架最佳实践
> - 框架最大化利用原则
> - 目录约束
> - 接口响应规则
> - 错误处理规则
> - 日志规则
> - 数据库连接方式
> - 权限校验入口
> - 以后新增模块应该怎么放文件

This document is NOT a manual. It is the constraint file for AI.

## Step 5: Build Minimal Runnable Skeleton — Four Lines

After the architecture design document is complete, build the skeleton. Emphasize: build FROM the document, not free improvisation.

**Skeleton prompt:**

> 请严格根据项目架构设计文档，基于当前后端语言和框架，按照该语言工程规范、该框架官方文档或主流最佳实践，搭建最小可运行后端骨架。先说明目录结构、目录作用、哪些是框架推荐、哪些是项目自定义。不要先写完整业务功能。

**Five constraints that cannot be dropped:**
1. Must be based on current language and framework
2. Must follow language conventions and framework best practices
3. Must execute according to architecture design document
4. Must explain directory structure BEFORE writing code
5. Only build minimal runnable skeleton, no complete business features

### Line 1: Startup Line

- Project must be able to start
- Configuration must be readable (port, database address, secrets NOT hardcoded)
- Must have configuration template (`.env.example`)
- Must have health check endpoint (`/health`)

This line answers: **Can this backend start and run?**

### Line 2: API Line

- Routes must follow current framework conventions
- Responses must be unified, but specify TWO categories:

**Success scenarios:**
| Type | Typical content |
|------|----------------|
| List | Array, pagination, total count |
| Object | Detail, created data, updated data |

**Failure scenarios:**
| Type | HTTP status code |
|------|-----------------|
| Parameter error | 400 |
| Not logged in | 401 |
| No permission | 403 |
| Not found | 404 |
| System error | 500 |

- HTTP status codes should reuse framework conventions and common standards
- If business error codes are needed, write rules first — AI cannot make them up on the fly

This line answers: **Can frontend, testing, and future vibe coding follow the same API rules?**

### Line 3: Business Line

- API layer only handles request and response
- Business rules go to business layer
- Database read/write go to data layer

Different frameworks use different names:
| Pattern | Layer names |
|---------|------------|
| MVC-style | Controller → Service → Repository |
| Handler-style | Handler → Use Case → Model |
| Lightweight | May not enforce these names |

Do NOT memorize directory names. Instead, ask AI to explain for the CURRENT framework:
- Where does the request enter?
- Where are business rules processed?
- Where is database accessed?
- Where are parameters validated?
- Where are permissions checked?

If the framework lacks a corresponding concept, ask AI what framework mechanism replaces it — do NOT invent a new pattern.

This line answers: **When adding features later, will request handling, business logic, and database access be separated?**

### Line 4: Operations Line

- Unified logging
- Unified error handling
- Database connection verification
- Permission check placeholder
- README with: how to start, how to configure, how to test

This line answers: **When something goes wrong, can we start it, check logs, and find database/permission entry points?**

## Step 6: Verify Skeleton Runs

After building, verify:
- Dependencies install successfully
- Server starts without errors
- Health check endpoint responds
- Configuration reads from environment/file
- At least one sample endpoint returns unified format
- Logs appear on request

## Generate Outputs

After confirmation, generate:

### `backend-architecture-spec.md` (English)

Include:
- Backend language and framework confirmation
- Language engineering conventions
- Framework best practices
- Framework maximization principle
- Directory structure with responsibilities
- API response format (success list, success object, all error types)
- Error handling rules
- Logging rules
- Database connection method
- Permission entry point
- New module file organization rules
- Startup instructions
- AI agent constraints

### `ai-rules/` updates

Add rules:
- Backend skeleton must be built from architecture design document, not improvised
- Framework maximization: use framework capabilities before writing custom solutions
- New dependencies, directory changes, error code customization, framework changes require justification and document update
- Business features must follow the four-line structure
- Do not write complete business features during skeleton phase

### `ai-rules/prompt-templates.md`

Add prompts for:
- Architecture design document generation
- Skeleton building
- Language/framework confirmation
- Directory structure explanation
- API response format verification
- Startup verification

## Offer Next Stage

After skeleton is built:

> 后端骨架已搭建完成。下一步建议使用 `backend-architecture-reviewer` 验收这套架构。是否继续？

## Red Flags

| Thought | Reality |
|---------|---------|
| "Let AI write login/order/payment first" | Define rules first, then build skeleton, then write features |
| "More directories = more professional" | Each directory needs one clear responsibility |
| "AI said it's done" | Verify it starts, responds, and follows the document |
| "Switch language midstream for security feel" | Security is determined by business code, not language |
| "Framework is too restrictive" | Framework constraints prevent AI from improvising |
| "Skip architecture doc, just code" | Without doc, AI guesses differently each time |

## Common Mistakes

1. Letting AI write business features before skeleton rules are set
2. Not locking down language and framework, allowing AI to waver
3. Not writing rules into architecture design document
4. Building skeleton without explaining directory structure first
5. Mixing request handling, business logic, and database access in one function
6. Hardcoding configuration values instead of using environment/config files
7. Not having a health check endpoint
8. Writing custom solutions when framework provides the capability
