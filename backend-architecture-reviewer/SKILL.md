---
name: backend-architecture-reviewer
description: Guide non-technical users through verifying and accepting AI-built backend architecture using rules, examples, and evidence. Use when the user mentions "后端验收", "架构验收", "骨架验收", "骨架检查", "后端骨架乱", "验收后端", "检查架构", or wants to verify whether the backend skeleton is stable enough to start writing business features.
---

# Backend Architecture Reviewer

Guide the user through verifying and accepting AI-built backend architecture. Verification is based on rules, examples, and evidence — not on reading every line of code. Discussion happens in Chinese; output documents and AI rules are generated in English.

**Core principle:** Do not trust "it's done." Require AI to produce evidence for every verification item. Items without evidence are marked "unverified," never "basically complete."

## Pipeline Position

This is **Stage 7 of 8** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
4. **ai-db-designer** — design database from business objects and flows
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security

Read earlier stage specs before starting. If `backend-architecture-spec.md` is missing, recommend completing Stage 6 first.

## Auto-Detect Existing Context

Scan for:

| File | Action |
|------|--------|
| `project-brief-spec.md` | Read for business scope and MVP boundary |
| `tech-stack-spec.md` | Read for backend language/framework choices |
| `backend-api-spec.md` | Read for API boundaries and rules |
| `backend-architecture-spec.md` | Read as primary verification baseline |
| `backend-impl-source-of-truth.md` | Read if exists, offer to update |
| Existing backend folders | Inspect current code structure |

## Interaction Flow

1. **Rule-based audit** — verify against architecture design document with evidence
2. **Directory responsibility table** — verify each directory has one clear job
3. **Minimal module demonstration** — verify rules actually work in code
4. **API response examples** — verify unified response format with concrete samples
5. **Framework reuse audit** — verify framework capabilities are properly used
6. **Startup evidence pack** — verify the project can actually run
7. **Consolidation** — produce verification report and implementation source-of-truth document
8. **Git commit** — save verified architecture as first stable version

## Step 1: Rule-Based Audit — Evidence, Not Claims

The first verification question is NOT "is the architecture done?" It is: "can these rules hold up when we keep adding features?"

**Audit prompt:**

> 请根据项目实际业务文档以及项目架构设计文档，对后端架构层代码做详细的审计和验收。每一项必须说明：规则来源、对应文件、验证方式、实际结果、是否通过。没有证据的项目标记为"未验收"，不允许写"通过"。

What to check in AI's response:
- Does every item cite evidence (file, command, response, log)?
- Are unverified items honestly marked?
- Do any items conflict with future business logic?

If AI only says "completed," "optimized," or "follows best practices" without files, commands, response examples, and log results — **it does not count as verification.**

If the explanation is too technical, tell AI:

> 用最直白的语言告诉我，不要说一堆技术名词。

This rule applies to every step. If you cannot understand the answer, the answer is not qualified.

## Step 2: Directory Responsibility Table

Do not judge quality by directory count. More directories ≠ more professional.

**Directory audit prompt:**

> 请根据当前后端架构输出目录责任表。每一行包含：目录、主要职责、以后应该放什么、禁止放什么、对应的框架机制、示例文件。请标注哪些目录来自框架推荐或框架本身，哪些是项目业务自定义的。同时请按当前框架说明：请求入口在哪里、业务规则在哪里、数据库访问在哪里、参数校验在哪里、错误处理在哪里、权限校验入口在哪里。

Check three things in the response:

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | Single responsibility | Each directory has ONE clear main job |
| 2 | Future guidance | Clearly states what goes in and what is forbidden |
| 3 | Origin labeled | Distinguishes framework-recommended vs project-customized |

**Fail signals:**
- Every directory says "handles business logic" — responsibilities not separated
- Cannot explain why API entry point should not contain complex business logic
- Cannot explain why database access should not scatter across request handlers
- Cannot explain why configuration should not be hardcoded in business code

## Step 3: Minimal Module Demonstration — Prove Rules Work

The directory responsibility table only proves AI can explain. It does not prove AI will follow rules when writing code.

Do NOT ask for complete business code. Ask for a minimal module demonstration.

**Demonstration prompt:**

> 请做一次最小模块演练。不写完整业务代码，只输出：文件清单和调用路径。请说明：需要新增或修改哪些文件、每个文件放在哪个目录、每个文件负责什么、请求从哪里进入、参数在哪里校验、业务规则在哪里处理、数据访问在哪里处理、统一响应和统一错误在哪里处理。这些安排是否符合项目架构设计文档。

Check two things:

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | File placement | Follows the directory responsibility table from Step 2 |
| 2 | Layer separation | Request entry, parameter validation, business rules, data access, response, and error handling are in separate locations |

**Fail signals:**
- Files placed differently from the directory table each time
- AI says "it can all be written in one endpoint"
- Request handling, business judgment, and database operations are in one function

If this step fails, the architecture is not ready for business development.

## Step 4: API Response Examples — Concrete Samples Required

"Unified response" is the easiest item for AI to fake. AI often says "I've unified success and failure responses" but lacks specific scenarios.

**Response audit prompt:**

> 请输出当前后端架构的接口响应样例，至少包含：列表成功、详情对象成功、创建成功、更新成功、删除成功、空列表、参数错误、未登录、无权限、资源不存在、系统异常。每个场景都要给出：HTTP 状态码、响应 JSON 示例、由哪个文件或框架机制统一处理。

Two areas that must not be missed:

### Success responses — list vs object must be separate

| Type | Must include |
|------|-------------|
| List | Array, pagination info, total count |
| Object | Single detail, created data, updated data |

"data contains the result" is not sufficient. List and object have different structures.

### Error responses — HTTP status codes must follow standards

| Error type | Expected HTTP status |
|------------|---------------------|
| Parameter error | 400 |
| Not logged in | 401 |
| No permission | 403 |
| Resource not found | 404 |
| System error | 500 |

- HTTP status codes should reuse framework conventions and common standards
- If project needs business error codes, rules must be documented: error code format, naming convention, who maintains them
- Do not let AI invent error codes on the fly

## Step 5: Framework Reuse Audit

Using a framework means leveraging mature capabilities. If AI writes custom solutions outside the framework for things the framework already handles, that is a problem.

**Framework audit prompt:**

> 请审查当前后端架构的框架复用和封装边界：哪些能力直接复用了框架、哪些是项目自定义封装、每个自定义封装解决什么问题、如果去掉会有什么影响、是否存在为了显得专业而提前封装的内容。

Check:
- Framework capabilities (parameter validation, exception handling, HTTP status codes, middleware, logging, route grouping) are used where available
- Custom wrappers have clear justification
- No "might need it later" wrappers that are not currently used

**Rule to write into agent constitution:**

> 后端开发必须遵守后端架构实施真源文档中的框架最大化利用原则。HTTP 状态码、参数校验、错误处理、路由分组、中间件、日志、依赖注入等能力，优先复用当前框架推荐机制。确需自定义时，必须说明原因并更新后端架构实施真源文档。

## Step 6: Startup Evidence Pack

Previous steps verify code organization and API rules. This step verifies the project actually runs.

This is NOT about understanding every command. It is about fixing: how to start, what configuration, is the database connected, where to check logs.

**Evidence pack prompt:**

> 请输出后端架构运行证据包：依赖安装命令、启动命令、服务监听端口、健康检查命令和结果、配置读取位置、.env.example 内容检查、数据库连接验证方式和结果、请求日志示例、错误日志示例。每一项都要写明实际执行结果。没有执行的项目标记为"未验证"。

Check:
- Are startup steps fixed? (not different each time)
- Is configuration source clear?
- Is database connection verified?
- Are log locations identified?

**Fail signals:**
- "Theoretically it can start" — not verified
- Different startup command this time vs last time — startup rules not locked down
- No actual execution results — just documentation, not evidence

**Best outcome:** Future business development can reference this evidence pack directly, without AI re-guessing how to run the project.

## Step 7: Consolidation — Verification Report

Do not let AI scatter answers. Do not let AI repeat previous explanations. This step only does consolidation.

**Consolidation prompt:**

> 请汇总本次后端架构验收结果。不要重新发散，也不要重复解释前面的内容。列出：验收项、是否通过、证据位置、未通过原因、下一步处理、是否影响进入业务开发。最后给出明确结论：当前后端架构是否可以开始写业务功能？没有证据的项目必须标记为"未验证"，不能写"基本完成"。

This report decides one thing: **Can this architecture serve as a stable starting point for business development?**

### If critical items fail:

- Directory responsibilities unclear
- API responses have no examples
- Error handling not unified
- Startup evidence not fixed

→ Do NOT start business development. Fix these first.

### If critical items pass:

→ Proceed to generate the implementation source-of-truth document.

## Step 8: Generate Implementation Source-of-Truth Document

The agent constitution (CLAUDE.md / AGENTS.md) should only contain top-level constraints, not all backend details. The correct approach:

1. AI generates a detailed `backend-impl-source-of-truth.md` from verified results
2. Agent constitution references it with one rule

**Source-of-truth document must include:**
- Current backend language and framework, with rule sources
- Directory responsibilities: what goes where, what is forbidden
- New module file organization rules
- API response format rules
- Error handling rules
- Startup and configuration evidence
- Database and logging entry points
- Framework reuse boundaries (what uses framework, what is custom)

**Agent constitution reference rule:**

> 后端开发必须先读取并遵守后端架构实施真源文档。新增或修改后端功能前，必须确认目录责任、接口规则、错误处理规则、启动证据和框架复用边界。任何目录调整、规则变更、框架更换或新增关键依赖，都必须先说明原因，并同步更新后端架构实施真源文档。

This keeps the agent constitution clean while ensuring AI follows detailed rules.

## Step 9: Git Commit

After verification passes, remind user:

> 验收通过后，建议让 AI 先提交一次 git commit，把这套后端架构作为第一个稳定版本。后面写业务功能时，基于这个版本往下加。

## Generate Outputs

### `backend-impl-source-of-truth.md` (English)

The implementation source-of-truth document generated in Step 8.

### `ai-rules/` updates

Add rules:
- Backend development must read and follow `backend-impl-source-of-truth.md`
- Before adding or modifying backend features, confirm directory responsibilities, API rules, error handling rules, startup evidence, and framework reuse boundaries
- Any directory adjustment, rule change, framework change, or new critical dependency must explain rationale and update the source-of-truth document
- Detailed rules live in the source-of-truth document; agent constitution only references it

### `ai-rules/prompt-templates.md`

Add prompts for:
- Architecture audit with evidence
- Directory responsibility table
- Minimal module demonstration
- API response example generation
- Framework reuse audit
- Startup evidence pack
- Verification report consolidation

## Offer Next Stage

After verification passes:

> 后端架构验收已通过，实施真源文档已生成。下一步建议使用 `backend-security-checkpoint` 检查接口与权限安全。是否继续？

## Red Flags

| Thought | Reality |
|---------|---------|
| "AI said it's done, so it's done" | Require evidence for every item |
| "I can't read code, so I can't verify" | Verify with rules, examples, and evidence — not code reading |
| "More directories = better architecture" | Each directory needs one clear responsibility |
| "Basically complete is good enough" | Unverified = unverified, never "basically complete" |
| "Skip verification, start business code" | Architecture problems compound — fix now or pay much more later |
| "AI explains differently each time" | Rules are not locked down — do not proceed |

## Common Mistakes

1. Accepting "completed" without evidence
2. Judging architecture quality by directory count
3. Not checking if API response format covers all scenarios (list, object, errors)
4. Not verifying the project actually starts and responds
5. Putting all backend rules in agent constitution instead of a separate source-of-truth document
6. Not committing the verified architecture as a stable version
7. Starting business development when directory responsibilities are unclear
8. Letting AI change startup commands or configuration sources between sessions
