---
name: backend-security-checkpoint
description: Guide non-technical users through auditing backend API and permission security using structured prompts and evidence. Use when the user mentions "接口安全", "权限安全", "后端安全", "安全检查", "安全验收", "越权", "注入", "密码安全", or wants to verify backend security before going live. Different from advanced-backend-security-shield which is for technical security engineering — this skill is for non-technical vibe coding users.
---

# Backend Security Checkpoint

Guide non-technical users through auditing backend API and permission security. This skill provides six structured verification prompts that users can send directly to AI to check the most critical security issues. Discussion happens in Chinese; output documents and AI rules are generated in English.

**Core principle:** Do not accept "security is handled." Require AI to show where risks are, what rules exist, where they are enforced in code, and how to verify they actually block unauthorized requests.

**Difference from `advanced-backend-security-shield`:** That skill is a full DevSecOps engineering tool for technical users. This skill is for non-technical vibe coding users who need structured prompts to verify security without reading code.

## Pipeline Position

This is **Stage 8 of 8** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
4. **ai-db-designer** — design database from business objects and flows
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security

Read earlier stage specs before starting. If backend architecture has not been verified (Stage 7), recommend completing verification first.

## Auto-Detect Existing Context

Scan for:

| File | Action |
|------|--------|
| `project-brief-spec.md` | Read for business scope |
| `backend-api-spec.md` | Read for API boundaries and permission rules |
| `backend-architecture-spec.md` | Read for architecture rules |
| `backend-impl-source-of-truth.md` | Read for implementation details |
| `backend-security-report.md` | Read if exists, offer to update |
| Existing backend code | Inspect routes, middleware, auth, validation |

## Core Concept: Security as Checkpoints

Backend security is distributed across every step of request processing. Think of it as checkpoints that a request must pass through:

| Checkpoint | What it checks |
|------------|---------------|
| Authentication | Who sent this request? Are they logged in? |
| Authorization | Can this person do this action? |
| Input validation | Is the data from frontend trustworthy? |
| Data ownership | Does this data belong to them? |
| Injection prevention | Will user input be executed as commands? |

Each checkpoint blocks different risks. Missing one = one gap. "Security is handled" cannot cover all of them at once.

## Interaction Flow

1. **Security boundary table** — map all checkpoints to concrete locations
2. **Input validation audit** — verify critical parameters are server-side validated
3. **Password and admin security** — verify password rules and storage
4. **Permission design table** — verify auth and authorization for every endpoint
5. **Injection prevention check** — verify user input never enters critical statements directly
6. **Over-defense check** — verify no useless complexity masquerading as security
7. **Generate outputs** — security report, AI rules

## Checkpoint 1: Security Boundary Table

Before checking individual areas, get the full picture.

**Prompt to send to AI:**

> 请根据项目架构设计文档和当前业务功能，输出后端安全边界表。不要只说"已做安全处理"，请按以下维度分别说明：接口输入、登录状态、权限设计、密码规则、数据归属、注入风险。每个维度说明：风险是什么、当前在哪里处理、处理规则是什么、如何验证、哪些还没有验证。

If AI's response is too technical:

> 用大白话重讲一遍，别用技术名词。

**This rule applies to ALL checkpoints.** If you cannot understand the explanation, the explanation is not qualified. Ask AI to rephrase in plain language.

If the boundary table is unclear, do not proceed to ask "can we go live?"

## Checkpoint 2: Input Validation — Frontend Input Is Untrusted by Default

**Why untrusted?** Backend APIs are essentially public. Someone who wants to exploit them will NOT use the frontend page. They use tools to bypass the entire frontend and send requests directly to the backend. Frontend validation only improves user experience and reduces unnecessary API calls. It does NOT protect business results.

Critical parameters that MUST be validated server-side:
- Price, quantity, amount
- User role, user ID
- Order ownership
- Data status changes
- Any value that affects money, identity, or data belonging

**Prompt to send to AI:**

> 请审查当前后端接口的输入安全。不要只说"已做参数校验"，请按接口说明：哪些参数来自前端、哪些参数会影响身份/权限/金额/库存/数据归属或数据库写入、每个关键参数在哪里校验、校验失败返回什么、是否有示例请求证明。

You do not need to understand all the code. Just check:
- Are critical parameters separated from ordinary parameters?
- Ordinary parameter errors = display issues at most
- Critical parameter errors = unauthorized access, wrong amounts, wrong data ownership

## Checkpoint 3: Password and Admin Account Security

Two layers to check:

### Layer 1: Password strength

Attackers do not guess passwords manually. They use dictionaries of millions of common passwords and brute-force automatically. Passwords like `abc123`, `123456` are cracked in seconds.

Registration, login, password change, password reset, and admin account creation endpoints must NOT allow weak passwords.

### Layer 2: Password storage

Passwords must NEVER be stored in plaintext in the database. If the database leaks, all passwords are exposed.

Admin accounts require extra attention — a weak admin password compromises the entire system.

**Prompt to send to AI:**

> 请审查当前后端的账号和密码安全规则。请说明：注册、登录、修改密码、重置密码、创建管理员账号分别在哪里校验密码强度。请检查是否包含：密码长度、字符组合、常见弱密码拦截、密码是否哈希存储（禁止明文保存）、登录失败次数限制、管理员账号额外要求。没有实现的项目标记为"未验证"，不要默认安全。

Minimum requirements (do not need complex policies at first):
1. Password rules exist and are enforced
2. Admin accounts have stricter requirements
3. Backend actually rejects obviously weak passwords

## Checkpoint 4: Permission Design Table

Permission design is where AI makes the most mess. Two things to distinguish:

| Concept | Question | Term |
|---------|----------|------|
| Authentication | Who are you? | Login verification |
| Authorization | What can you do? | Permission control |

Being logged in does NOT mean you can do everything.

**Two types of unauthorized access:**

| Type | Description | Example |
|------|-------------|---------|
| Vertical escalation | Normal user calls admin-only endpoint | Changing someone's role, deleting backend data |
| Horizontal escalation | Valid user accesses another user's data | Changing order ID in URL to see someone else's order |

Many vibe coding projects only check "is user logged in?" but miss "can this user access THIS data?" — horizontal escalation mostly comes from this gap.

**For multi-role projects (user, merchant, operator, admin):** Permission rules must be defined during project briefing or feature design. Otherwise AI guesses differently each time — sometimes an endpoint is admin-only, sometimes any logged-in user can access it.

**Prompt to send to AI:**

> 请根据项目功能设计文档输出权限设计表。每个接口都要说明：是否需要登录、允许哪些角色访问、是否只能操作自己的数据、管理员是否可以访问、权限判断在哪个文件或中间件处理、无权限时返回什么、有没有测试证明。

This table is NOT formality. It is the rule for all future business development. With this table, AI knows which permission pattern to follow when adding new endpoints.

## Checkpoint 5: Injection Prevention

**One sentence:** User input content, which should only be data, gets executed as commands by the backend.

Most common types:
| Type | What happens |
|------|-------------|
| SQL injection | User input becomes part of database query, executing unintended operations |
| Command injection | User input becomes part of system command |
| Template injection | User input becomes part of HTML/template rendering |

**Correct prevention** is NOT custom filtering by AI. It is using the framework and database tools' built-in mechanisms:
- Parameterized queries (prepared statements) — separate commands from data
- ORM query builders
- Allowlist field validation
- Content escaping / content sanitization

**Prompt to send to AI:**

> 请检查当前接口是否存在注入风险。重点检查：SQL 注入、数据库查询注入、命令注入、HTML 或模板内容注入。请说明哪些位置使用了框架 ORM、参数化查询、白名单校验、内容转义或内容清洗。如果存在字符串拼接用户输入的情况，请标记为风险并给出修复方案。

You do not need to understand how these mechanisms work. Just check one thing:
- Is it using the framework/database's built-in protection mechanism?
- Or is it AI's custom filtering code?

If AI wrote custom filtering and claims it's secure — be extra suspicious. Custom protection is usually where the most gaps are.

## Checkpoint 6: Over-Defense Check — Strict Where Needed, Simple Where Not

When you mention security, some AI goes to the opposite extreme — piling on defenses everywhere.

**Common over-defense patterns:**
- Login already enforced upstream, but downstream still checks "what if not logged in?"
- Parameter type already validated, but adds impossible condition branches
- Branches that never execute in real operation (dead code)
- Adds complexity that does not make the system safer, only harder to maintain

**What actually needs strict checking:**
- Is the user logged in?
- Does the user have permission for this action?
- Does this data belong to the user?
- Does the record allow modification?
- Do amounts and inventory follow business rules?

**What does NOT need complex backend security logic:**
- Input format hints (frontend experience)
- Display optimization (frontend concern)
- Conditions that are logically impossible given prior checks

**Prompt to send to AI:**

> 请审查当前接口安全逻辑是否存在过度防御。区分：必须校验的业务规则、框架已经处理的基础校验、可以由前端体验层处理的提示校验、以及永远不会触发的防御分支（死代码）。不要为了安全感新增重复判断或不可能成立的条件。任何新增安全封装都必须说明解决什么真实风险。

This prevents AI from building a pile of unmaintainable, never-triggered defenses that create a false sense of security.

## Generate Outputs

After all checkpoints, generate:

### `backend-security-report.md` (English)

Include:

| Section | Content |
|---------|---------|
| Security boundary table | All checkpoints mapped to code locations |
| Input validation | Critical parameters, validation locations, evidence |
| Password security | Rules, storage method, admin requirements |
| Permission design table | Every endpoint's auth and authorization rules |
| Injection prevention | Mechanisms used, risk locations if any |
| Over-defense findings | Unnecessary complexity identified |
| Unverified items | Explicitly listed with reasons |
| Conclusion | Can the backend go live? What must be fixed first? |

### `ai-rules/` updates

Add rules:
- Frontend input is untrusted by default for all critical parameters
- Password rules must be enforced at registration, login, password change, reset, and admin creation
- Every endpoint must declare authentication requirement and allowed roles
- User input must never be concatenated directly into SQL, system commands, or templates
- New security wrappers must explain what real risk they solve
- Permission design table must be updated when new endpoints are added

### `ai-rules/prompt-templates.md`

Add prompts for:
- Security boundary table generation
- Input validation audit
- Password security audit
- Permission design table generation
- Injection prevention check
- Over-defense review

## Offer Integration

After security checkpoint:

> 接口与权限安全检查已完成。建议将安全规则同步更新到后端架构实施真源文档中。如果有未通过项，请先修复再考虑上线。

## Red Flags

| Thought | Reality |
|---------|---------|
| "AI said security is handled" | "Handled" is a comfort word, not evidence |
| "Features work, so it's safe" | Features working = normal flow passes. Security = abnormal requests get blocked |
| "Frontend already validates this" | Anyone can bypass frontend and send requests directly |
| "I heard language X is more secure" | Security is determined by business code, not language choice |
| "More security checks = more secure" | Over-defense creates unmaintainable dead code |
| "Custom filtering is good enough" | Framework/database built-in mechanisms are almost always more reliable |

## Common Mistakes

1. Accepting "security is handled" without evidence
2. Only checking if features work, not if unauthorized requests are blocked
3. Trusting frontend validation for critical business parameters
4. Not separating authentication (who are you) from authorization (what can you do)
5. Missing horizontal escalation checks (user A accessing user B's data)
6. Allowing weak passwords, especially for admin accounts
7. Storing passwords in plaintext
8. AI writing custom SQL/command filtering instead of using framework mechanisms
9. Adding useless security branches that never trigger
10. Not defining permission rules before writing business code
