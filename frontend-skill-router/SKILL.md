---
name: frontend-skill-router
description: "Frontend meta-skill that decides which installed UI/design skills to load and in what order. Use this whenever the user asks in English or Chinese to build, redesign, polish, audit, animate, generate, convert, or improve frontend surfaces: websites (网站/官网), landing pages (落地页), portfolios (作品集), dashboards (仪表盘), product UI (产品界面), mobile app screens (移动端界面), Tailwind components (组件), GSAP motion (动效), brand kits (品牌板), icon systems (图标体系), screenshots-to-code (截图转代码), image-first design (先出图再实现), or routing phrases like 调用哪个前端skill and 前端skill规则."
---

# Frontend Skill Router

Use this skill as the front door for **frontend implementation, visual design, redesign, motion, screenshot-to-code, and UI quality routing**.

This router selects installed frontend/design skills. It does not replace `ai-frontend-scaffolder`, which owns frontend skeleton planning, directory rules, design tokens, module boundaries, and component reuse policy.

Chinese requests are first-class. Route based on the artifact the user wants, not only the words they use.

## Boundary With the Five-Stage Toolkit

Use the five-stage AI Project Toolkit for project planning:

1. `ai-project-briefing` — product idea, MVP, user flows, business objects
2. `ai-tech-advisor` — technical route and stack
3. `ai-frontend-scaffolder` — frontend skeleton, framework, UI library, tokens, directories
4. `ai-db-designer` — database design
5. `ai-backend-api-planner` — backend/API/auth/validation

Use **this router after or alongside Stage 3** when the user wants concrete UI work:

| User Intent | Route |
|-------------|-------|
| Frontend architecture, directory structure, tokens, UI library choice | `ai-frontend-scaffolder` |
| Build/redesign a real page/component/dashboard | `frontend-skill-router` |
| Visual polish, interaction quality, accessibility audit | `frontend-skill-router` |
| Screenshot/image to code | `frontend-skill-router` -> `image-to-code` |
| Landing page visual direction | `frontend-skill-router` -> `design-taste-frontend` |
| Existing project visual upgrade | `frontend-skill-router` -> `redesign-existing-projects` |

If the project has no `frontend-skeleton-spec.md` and the user asks for broad frontend structure, recommend `ai-frontend-scaffolder` first. If the user asks for a concrete surface now, route here and inspect existing code before applying style rules.

## Coverage

This router covers installed frontend skills such as:

- `impeccable`
- `baseline-ui`
- `gsap-frameworks`
- `brandkit`
- `industrial-brutalist-ui`
- `gpt-taste`
- `image-to-code`
- `imagegen-frontend-mobile`
- `imagegen-frontend-web`
- `minimalist-ui`
- `full-output-enforcement`
- `redesign-existing-projects`
- `high-end-visual-design`
- `stitch-design-taste`
- `design-taste-frontend`
- `design-taste-frontend-v1`

Before relying on a skill, confirm it is installed or available in the current session. If a named support skill is missing, use the closest available fallback and say so briefly.

## First Move

1. Classify the artifact: production app UI, landing/portfolio, existing redesign, mobile concept image, brand system, image-to-code, high-motion page, Tailwind component, GSAP implementation, final audit, or skeleton planning.
2. If it is skeleton planning, route to `ai-frontend-scaffolder` instead of this router.
3. Pick one primary skill. Add supporting skills only when they materially change the result.
4. Announce the stack:

```text
Skill stack: primary=<skill>; support=<skill(s)>; validation=<skill or checks>.
Reason: <one sentence tied to the user's artifact>.
```

5. Load selected skills and follow their workflows.
6. For ambiguous routing, prefer the smallest stack that covers the user request.

## Default Skill Stacks

| Task Type | Primary | Support | Validation |
|-----------|---------|---------|------------|
| Production app UI, dashboard, admin, forms, settings | `impeccable` | existing design system | `baseline-ui` |
| Landing page, marketing site, portfolio | `design-taste-frontend` | `high-end-visual-design` if premium polish needed | `baseline-ui` |
| Existing website/app redesign | `redesign-existing-projects` | `impeccable` for product UI, `design-taste-frontend` for marketing | `baseline-ui` |
| Screenshot/image to code | `image-to-code` | design style skill if needed | `baseline-ui` |
| Mobile app concept images | `imagegen-frontend-mobile` | brand/style skill if needed | visual inspection |
| Website reference images only | `imagegen-frontend-web` | brandkit if identity matters | visual inspection |
| Brand identity, logo, visual world, icon strategy | `brandkit` | UI skill only after identity direction | `baseline-ui` for implementation |
| GSAP-heavy campaign page | `gpt-taste` | `gsap-frameworks` for non-React lifecycle/framework use | browser/screenshot checks |
| Vue/Nuxt/Svelte GSAP implementation | surface skill first | `gsap-frameworks` | browser/screenshot checks |
| Tailwind/component quality audit | existing implementation skill | none | `baseline-ui` |
| Long complete code with no placeholders | task's normal primary skill | `full-output-enforcement` only when needed | targeted tests/build |

## Routing Defaults

Use `impeccable` as the primary skill for production product UI: dashboards, app shells, admin tools, forms, settings, onboarding, empty states, UX copy, accessibility, polish, audits, hardening, performance, responsive behavior, and live browser iteration.

Use `design-taste-frontend` as the primary skill for landing pages, portfolios, marketing sites, brand/editorial pages, and non-templated visual redesigns. Do not use it as the default for dense dashboards or multi-step product flows.

Use `redesign-existing-projects` when the user wants an existing website or app upgraded while preserving the current stack and behavior.

Use `baseline-ui` as an implementation quality gate for Tailwind, React views, component styling, icon-only buttons, accessible primitives, animation duration, viewport units, typography utilities, z-index discipline, loading/empty/error states, and anti-pattern checks. Use it late, not as the creative direction.

Use `gsap-frameworks` for Vue, Nuxt, Svelte, SvelteKit, or lifecycle-based framework work involving GSAP, ScrollTrigger, scoped selectors, plugin registration, or cleanup on unmount.

Use `imagegen-frontend-web` when the deliverable is website/landing-page reference images only. It does not write code.

Use `imagegen-frontend-mobile` when the deliverable is mobile app screen concept images or screen-flow images only.

Use `image-to-code` when visual fidelity is the core task: screenshot-to-site, generated comp-to-code, high-fidelity visual rebuild, or image-first web implementation.

Use `brandkit` when brand identity, logo direction, brand boards, visual worlds, guideline imagery, or icon-system strategy should drive the UI.

Use `gpt-taste` for Awwwards-style, kinetic, GSAP-heavy campaign pages with scroll pinning, bento choreography, motion physics, and wide editorial hero work.

Use `high-end-visual-design`, `minimalist-ui`, or `industrial-brutalist-ui` as style overlays only when the prompt explicitly calls for that aesthetic or the design strongly points there.

Use `stitch-design-taste` when the output is a Google Stitch-ready `DESIGN.md` or semantic design-system prompt.

Use `full-output-enforcement` only when the task requires long, complete, unabridged code, the user explicitly forbids placeholders/truncation, or the expected output is likely to be truncated.

## Sequencing Rules

- For code work, inspect the existing project before applying style rules.
- Respect current framework, component library, dependencies, and design system.
- For visual-first work, create or inspect the visual source before implementation.
- For motion work, choose the surface skill first; motion supports the surface.
- For Tailwind/component work, run `baseline-ui` last as a guardrail.
- For brand/icon work, route concepting to `brandkit`; route implementation behavior/accessibility to `baseline-ui`.
- For five-stage projects, do not let visual implementation override `project-brief-spec.md`, `tech-stack-spec.md`, or `frontend-skeleton-spec.md`.

## Output Shape

When routing, include a compact routing note before doing the work:

```text
Skill stack: primary=<skill>; support=<skill(s)>; validation=<skill or checks>.
Reason: <one sentence tied to the user's artifact>.
```

Then proceed with the selected skill workflow. Do not stop after routing unless the user explicitly asked only for a recommendation.

## Practical Examples

- "搭前端骨架/目录/组件规范" -> use `ai-frontend-scaffolder`, not this router.
- "把这个后台页面做得更专业" -> `impeccable + baseline-ui`.
- "重做这个官网首页" -> `redesign-existing-projects + design-taste-frontend + baseline-ui`.
- "按这张截图还原页面" -> `image-to-code + baseline-ui`.
- "做一套 App 概念图" -> `imagegen-frontend-mobile`.
- "给这个页面加 GSAP 动效" -> choose surface skill, then `gsap-frameworks` if framework lifecycle matters.
