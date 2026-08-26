---
name: ai-tech-advisor
description: Guide non-technical users through choosing the right tech stack for AI-assisted projects. Use when starting a new project, when the user mentions "技术选型", "选技术栈", "用什么框架", "开始新项目", or asks what technologies to use for their project. Also use when the user wants to evaluate or compare frameworks, libraries, or development tools.
---

# AI Tech Stack Advisor

Guide non-technical (or lightly technical) users through choosing the right tech stack. Discussion happens in Chinese; all output documents and AI rules are generated in English.

**Core principle:** One clear recommendation, not a menu of options. Converge to a single actionable path.

## Pipeline Position

This is **Stage 2 of 8** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-db-designer** — design database from business objects and flows
4. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security

Before starting, read `project-brief-spec.md` if it exists. If no project brief exists, recommend using `ai-project-briefing` first unless the user already provides clear product scope.
After generating `tech-stack-spec.md`, recommend `ai-frontend-scaffolder` as the next stage.

## When to Use

- Starting a new project and unsure what technologies to use
- User asks "what should I use to build X?"
- Beginning of a project lifecycle, before frontend or database design

**When NOT to use:**
- User already has a clear tech stack and just wants to code
- User is asking about a specific existing technology detail
- Mid-project technology migration

## Auto-Detect Existing Context

Before starting discussion, check the project directory for:

| File | Action if found |
|------|----------------|
| `tech-stack-spec.md` | Read it, skip to convergence |
| `frontend-skeleton-spec.md` | Read for context |
| `db-design-spec.md` | Read for context |
| `README.md`, `package.json`, `src/` | Scan for existing project info |

If `tech-stack-spec.md` exists, summarize it and ask: "I found an existing tech stack spec. Do you want to update it or start fresh?"

## Interaction Flow

1. **Load context** — auto-detect files or start fresh
2. **Ask project overview** — adaptive depth (see below)
3. **Confirm product form** — Website / Mini Program / App / Admin Panel / API Service
4. **Recommend unique tech stack** — ONE recommendation with reasoning
5. **Technology evaluation** — checklist for each technology
6. **Converge and confirm** — summary table, user approval
7. **Generate outputs** — spec doc + AI rules + prompt templates
8. **Offer code generation** — ask user before generating any code

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
| B | Mini Program | WeChat/Taro/uni-app + backend |
| C | App | React Native/Flutter + backend |
| D | Admin Panel | React+Ant Design / Vue+Element Plus + backend |
| E | API Service | Backend framework + database |
| F | Not sure | AI analyzes and recommends |

If user picks F, analyze based on project description and recommend one with reasoning.

## Step 3: Recommend Unique Tech Stack

Present ONE recommendation based on product form:

**For Website:**
- Frontend: [React/Vue/Next.js] + reason
- UI Library: [Ant Design/Element Plus/etc.] + reason
- Backend: [Node.js/Python/Go] + reason
- Database: [MySQL/PostgreSQL] + reason
- Deployment: [Vercel/Docker/VPS] + reason

**For Mini Program:** Platform + Backend + Database
**For App:** Approach + Backend + Database
**For Admin Panel:** Frontend + Backend + Database
**For API Service:** Framework + Database + Docs

**Critical rule:** Present ONE recommendation. If alternatives exist, explain why they are NOT recommended for this specific project.

## Step 4: Technology Evaluation

Evaluate each technology using the checklist (reference: `references/tech-checklist.md`):

| Check | What to verify |
|-------|---------------|
| Community | GitHub stars, recent commits, issue activity |
| Documentation | Official docs quality, Chinese resources |
| Maintenance | Last release date, active maintainers |
| License | Commercial use allowed? |
| AI-friendliness | Well-known to AI coding agents? |
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

### 1. `tech-stack-spec.md` (English)

Contains: project overview, recommended stack table, technology evaluation, risks and mitigations, alternatives considered, AI agent constraints.

### 2. `ai-rules/` directory

Generate platform-specific rule files with the same content, different format:
- `AGENTS.md` (Codex)
- `CLAUDE.md` (Claude Code)
- `.cursorrules` (Cursor)

Rules include: tech stack constraints, framework convention requirements, prohibited actions.

### 3. `ai-rules/prompt-templates.md`

Project-specific prompt templates from `references/prompt-templates.md`, customized for the chosen stack.

## Step 7: Offer Code Generation

> 技术选型文档和 AI 规则已生成。接下来我可以帮你：
>
> - **A) 生成项目初始化命令** — create-react-app / vue create / npx 等
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
