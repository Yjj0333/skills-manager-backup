---
name: ai-frontend-scaffolder
description: Design unified frontend architecture and skeleton before writing any pages. Use when the user mentions "搭前端", "前端骨架", "前端架构", "前端规范", "设计风格", or asks how to structure their frontend project. Also use when the user complains their AI-written frontend looks inconsistent across pages.
---

# AI Frontend Scaffolder

Guide users through designing a unified frontend skeleton before writing any pages. Discussion in Chinese; outputs in English.

**Core principle:** The problem with AI-written frontends is not ugly pages — it is no unified rules. Design the skeleton first, then build page by page.

## Pipeline Position

This is **Stage 3 of 5** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
4. **ai-db-designer** — design database from business objects and flows
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation

Before starting, read `project-brief-spec.md` and `tech-stack-spec.md` if they exist. If no tech stack spec exists, recommend `ai-tech-advisor` first unless the user already provides frontend framework and UI library choices.
After generating `frontend-skeleton-spec.md`, recommend `ai-db-designer` as the next stage.

## When to Use

- Starting to build the frontend of a project
- User complains AI-written frontend looks inconsistent
- After tech stack is chosen, before writing frontend code

**When NOT to use:**
- Project has no frontend (pure API service)
- User just wants to modify a single page
- Backend-only work

## Auto-Detect Existing Context

| File | Action if found |
|------|----------------|
| `tech-stack-spec.md` | Read for frontend framework + UI library choice |
| `frontend-skeleton-spec.md` | Read and offer to update rather than start fresh |
| `db-design-spec.md` | Read for business object context |
| `src/`, `pages/`, `components/` | Scan current project state |

If `tech-stack-spec.md` is NOT found, ask user about frontend framework and UI library before proceeding.

## Interaction Flow

1. **Confirm frontend framework & UI library** — from spec or user input
2. **Determine design style** — references or AI recommendation
3. **Define design tokens** — colors, typography, spacing, borders, shadows
4. **Set directory & module rules** — structure based on framework
5. **Define style system** — component reuse, i18n, theme
6. **Confirm and generate** — spec doc + AI rules + token file
7. **Offer code generation** — ask before generating

## Adaptive Depth Strategy

- **Detailed answer** → Summarize, confirm, move on quickly
- **Short answer** → Ask one follow-up
- **Unsure** → Recommend based on project type with reasoning

Always one question per message.

## Step 1: Confirm Frontend Framework and UI Library

If `tech-stack-spec.md` exists:

> 我看到你之前选的技术栈用了 [framework] + [UI library]，继续用这套吗？

If no spec exists, ask framework first:

> 你准备用什么前端框架？
> - A) React — 生态最大，AI 最熟悉
> - B) Vue — 中文生态好，上手快
> - C) Next.js — React 全栈，适合 SEO
> - D) Nuxt.js — Vue 全栈
> - E) 小程序原生 / Taro / uni-app
> - F) 不确定，帮我选

Then ask UI library:

> UI 组件库用哪个？
> - A) Ant Design（React，企业级）
> - B) Element Plus（Vue，中文生态好）
> - C) MUI（React，Material Design）
> - D) shadcn/ui（React，可定制性强）
> - E) 已包含在框架中
> - F) 不确定，帮我选

## Step 2: Determine Design Style

> 接下来确定整体设计风格。你可以：
> - A) 给我几个你喜欢的网站链接，我来分析
> - B) 给我几张参考截图
> - C) 用文字描述你想要的感觉
> - D) 不确定，你推荐一个

**If user provides references:** Analyze and extract color palette, typography, spacing rhythm, component style, layout pattern. Present structured summary.

**If user is unsure,** recommend based on project type:
- SaaS tool → Modern minimal, clean cards
- Content platform → Reading-optimized, clear hierarchy
- Admin panel → Enterprise style, high info density
- AI product → Tech-forward, dark mode, subtle animations
- Marketing site → Bold typography, visual impact

## Step 3: Define Design Tokens

Based on design style, propose tokens as a structured table:

| Category | Token | Value | Usage |
|----------|-------|-------|-------|
| Color | primary | #1677FF | Buttons, links, active states |
| Color | bg | #FFFFFF | Page background |
| Color | text | #1F1F1F | Body text |
| Typography | font-family | Inter, system-ui | All text |
| Typography | font-size-base | 14px | Body text |
| Spacing | space-unit | 8px | Base spacing unit |
| Spacing | page-padding | 24px | Page container |
| Border | radius-base | 8px | Cards, buttons |
| Shadow | shadow-md | 0 4px 12px rgba(0,0,0,0.08) | Cards, dropdowns |

> 这些 Token 是项目所有样式的统一来源，AI 写页面时不允许硬编码颜色和字号。

Confirm with user, adjust as needed.

## Step 4: Set Directory and Module Rules

Propose framework-specific directory structure. General pattern:

```
src/
  pages/          # Page components, one folder per route
  components/
    ui/           # Generic reusable (Button, Card, Modal)
    layout/       # Layout (Header, Sidebar, Footer)
    business/     # Domain-specific components
  hooks/          # Custom hooks / composables
  services/       # API calls and data fetching
  utils/          # Utility functions
  stores/         # State management
  styles/         # Global styles, tokens, themes
  types/          # TypeScript types/interfaces
  constants/      # App-wide constants
```

**Module boundary rules:**
> 功能模块之间的边界：登录/注册 → pages/auth/，用户中心 → pages/user/，订单 → pages/orders/ 等。
> 每个模块自包含，不跨模块引用内部组件。

Ask user to confirm or adjust module names.

## Step 5: Define Style System

### 5a. Component Reuse Rule

> 组件复用规则：UI 结构出现超过 2 次，必须封装为可复用组件。
> 优先级：UI 组件库组件 > 基于组件库封装 > 从零写

### 5b. Multi-language

> 是否需要支持多语言？
> - A) 目前只需要中文
> - B) 需要中英双语
> - C) 未来可能需要，先预留

If B/C: all user-facing text must go through translation files.

### 5c. Theme

> 是否需要主题切换（暗色模式）？
> - A) 只需要默认主题
> - B) 需要亮色/暗色切换
> - C) 未来可能需要，先预留

If B/C: define theme token structure with CSS variables.

## Step 6: Confirm and Generate

> 以上是前端骨架的完整设计。确认后我会生成：
> 1. `frontend-skeleton-spec.md` — 前端骨架规范（英文）
> 2. `ai-rules/` — AI 规则文件（多平台）
> 3. `design-tokens.json` — 设计 Token
>
> 确认生成吗？

## Step 7: Generate Outputs

### 1. `frontend-skeleton-spec.md` (English)

Contains: tech stack, design style, design tokens table, directory structure, module boundaries, component reuse rules, style system (i18n/theme), Phase 1 deliverables, AI agent constraints.

### 2. `ai-rules/` directory

Platform-specific rules: AGENTS.md / CLAUDE.md / .cursorrules covering directory conventions, component reuse, token constraints, no hardcoding.

### 3. `design-tokens.json`

From `references/design-token-template.ts`, customized for this project.

## Step 8: Offer Code Generation

> 前端骨架规范已生成。接下来我可以帮你：
>
> - **A) 生成项目骨架代码** — 目录结构、配置、Token、基础布局组件
> - **B) 生成骨架 + 首页** — 骨架基础上加首页模板
> - **C) 暂时不需要** — 我先看看文档

## Red Flags

| Thought | Reality |
|---------|---------|
| Skip design style, just use defaults | Style inconsistency is the #1 AI frontend problem |
| Tokens are overkill for small projects | Even 3-page sites benefit from consistent tokens |
| User said "just make it look good" | Still must confirm a specific style direction |
| Directory structure doesn't matter yet | It matters MORE before coding starts |

## Common Mistakes

1. Starting to write pages without skeleton — guarantees inconsistency
2. Not defining component reuse rules — leads to duplicate code everywhere
3. Hardcoding styles instead of using tokens — makes redesign painful
4. Skipping module boundaries — AI will mix unrelated features in one folder
