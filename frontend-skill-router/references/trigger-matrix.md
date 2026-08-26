# Trigger Matrix

Use this reference when more than one frontend skill could apply. Prefer one primary skill, one or two supporting skills, and one validation gate.

## Installed Skill Roles

| Skill | What It Does | Trigger When User Says Or Needs | Do Not Use As |
|---|---|---|---|
| `impeccable` | Production-grade frontend interface design, UX review, polish, hardening, audit, live iteration | app UI, dashboard/仪表盘, admin/后台, product flow/产品流程, forms/表单, settings/设置, onboarding/引导, empty states/空状态, UX copy/文案, responsive/响应式, a11y/无障碍, performance/性能, polish/打磨, critique/评审, harden/生产化, colorize/配色, typeset/排版, layout/布局 | Backend-only work |
| `baseline-ui` | Tailwind/component quality gate: accessibility, animation limits, typography utilities, layout anti-patterns | Tailwind, React views, UI components/组件, icon-only buttons/纯图标按钮, cn utility, Radix/Base UI/React Aria primitives, h-dvh, z-index scale, skeletons/骨架屏, empty/error states/空状态/错误状态 | Icon design, brand identity, broad visual concepting |
| `gsap-frameworks` | GSAP patterns for Vue/Nuxt/Svelte/SvelteKit: mounted DOM, scoped selectors, cleanup, ScrollTrigger refresh | GSAP with Vue/Nuxt/Svelte/SvelteKit, onMounted, onMount, onUnmounted, ScrollTrigger cleanup/清理, plugin registration/插件注册, 动效生命周期 | Generic CSS animation, React-only GSAP unless no React-specific skill exists |
| `design-taste-frontend` | Anti-generic landing, portfolio, marketing, editorial, visual redesign implementation | landing page/落地页, portfolio/作品集, marketing site/营销页, official website/官网, brand page/品牌页, non-templated website/不模板化, visual redesign/视觉重设计, premium consumer/高端消费, agency/创意代理, editorial/编辑感, Awwwards-lite | Dense dashboards, product workflows, data tables |
| `redesign-existing-projects` | Audit and upgrade existing UI without changing stack or behavior | make this existing site/app premium/把现有项目变高级, modernize/现代化, redesign/重设计, improve what is there/在现有基础上优化, keep functionality/不破坏功能 | Greenfield blank-slate design |
| `image-to-code` | Image-first website design and high-fidelity implementation | screenshot to code/截图转代码, image to website/图片转网页, match this mockup/还原设计稿, generated comp to frontend/设计图转前端, high visual fidelity/高保真还原 | Pure UX audit, mobile-only concept images |
| `imagegen-frontend-web` | Premium website section reference images, one image per section | generate website concepts/出网页概念图, landing page design references/落地页参考图, visual comps for every section/每个 section 出图, image direction before coding/先出图再写代码 | Code generation, mobile app screens |
| `imagegen-frontend-mobile` | Premium mobile app screen and flow images | iOS/Android app mockups/移动端 mockup, onboarding flow images/引导流程图, mobile screen concepts/手机界面概念图, phone mockups/手机壳展示 | Websites, desktop dashboards, code |
| `brandkit` | Brand identity boards, logo systems, visual worlds, guideline imagery | brand kit/品牌板, logo direction/logo 方向, identity deck/品牌提案, icon language/图标语言, visual world/视觉世界, brand guidelines/品牌规范 | Component accessibility checks |
| `gpt-taste` | High-motion Awwwards/GSAP page engineering | kinetic landing page/高动效落地页, scroll pinning/滚动固定, animated bento/动效 bento, cinematic campaign/电影感 campaign, advanced GSAP/高级 GSAP, huge editorial spacing/大留白编辑感 | Quiet product UI, accessibility-first dashboards |
| `high-end-visual-design` | Premium agency visual overlay: typography, haptic cards, cinematic spacing, polished motion | make it feel expensive/更高级, high-end agency/高端代理商质感, $150k build, premium visual polish/高级视觉打磨 | Safety-critical utilitarian UI as a primary router |
| `minimalist-ui` | Clean editorial/utilitarian minimalism | minimalist/极简, calm/克制, document-style/文档感, warm monochrome/暖单色, flat bento, no gradients/不要渐变, no heavy shadows/不要重阴影 | Rich brand/campaign motion |
| `industrial-brutalist-ui` | Swiss mechanical, terminal, tactical telemetry aesthetic | brutalist/粗粝主义, declassified/解密档案感, command center/指挥中心, telemetry/遥测, raw industrial dashboard/工业仪表盘, devtool with edge/开发者工具硬核风 | Soft consumer onboarding |
| `stitch-design-taste` | Google Stitch-ready semantic `DESIGN.md` | Stitch, DESIGN.md, semantic design system prompt/语义化设计系统提示词, agent-friendly design rules/给代理用的设计规则 | Direct frontend implementation |
| `full-output-enforcement` | Completeness guard for long output | full code/完整代码, no placeholders/不要占位, don't truncate/不要截断, exhaustive file/完整文件, complete implementation/完整实现 | Design taste or routing decisions |
| `design-taste-frontend-v1` | Legacy v1 taste rules | user explicitly asks for v1/明确要 v1, older project depends on previous taste-skill behavior/旧项目依赖旧规则 | Default new frontend routing |

## Primary Skill Decision Tree

1. If the deliverable is a brand board, logo, identity, visual world, or icon-language concept, choose `brandkit`.
2. If the deliverable is mobile screen images or app-flow images, choose `imagegen-frontend-mobile`.
3. If the deliverable is website reference images only, choose `imagegen-frontend-web`.
4. If the deliverable is code that must match a screenshot/mockup/generated image, choose `image-to-code`.
5. If the work is an existing UI upgrade, choose `redesign-existing-projects`, then pick the surface companion:
   - product/app/dashboard companion: `impeccable`
   - landing/portfolio/marketing companion: `design-taste-frontend`
6. If the surface is product UI, dashboard, admin, app shell, form, workflow, state design, or UX quality, choose `impeccable`.
7. If the surface is landing, portfolio, marketing, editorial, event, product page, or brand website, choose `design-taste-frontend`.
8. If the explicit focus is high-motion creative GSAP page engineering, choose `gpt-taste`.
9. If the explicit focus is only Tailwind/component quality, choose `baseline-ui`.
10. If the explicit focus is only Vue/Svelte/Nuxt GSAP implementation details, choose `gsap-frameworks`.

## Support Skill Pairings

| Primary | Common Support | Why |
|---|---|---|
| `impeccable` | `baseline-ui` | Adds Tailwind/component/a11y guardrails after UX and product decisions |
| `impeccable` | `industrial-brutalist-ui` | Gives a dashboard/devtool a deliberate tactical aesthetic |
| `impeccable` | `minimalist-ui` | Keeps product UI calm, sparse, and editorial |
| `design-taste-frontend` | `baseline-ui` | Verifies implementation quality after visual direction |
| `design-taste-frontend` | `imagegen-frontend-web` | Creates section references before coding |
| `redesign-existing-projects` | `impeccable` | Existing product UI redesign |
| `redesign-existing-projects` | `design-taste-frontend` | Existing marketing/portfolio redesign |
| `image-to-code` | `baseline-ui` | Checks accessibility/layout quality after matching the image |
| `image-to-code` | `imagegen-frontend-web` | Generates missing section references before implementation |
| `brandkit` | `high-end-visual-design` | Adds premium agency-level art direction |
| `gpt-taste` | `gsap-frameworks` | Applies lifecycle-safe GSAP in Vue/Nuxt/Svelte/SvelteKit |
| `gpt-taste` | `baseline-ui` | Catches text overflow, accessible buttons, motion and Tailwind issues |
| `stitch-design-taste` | `brandkit` | Brand identity informs the Stitch design system |

## Conflict Rules

- `impeccable` and `design-taste-frontend`: choose by surface. Product tools and dashboards go to `impeccable`; marketing, landing, portfolio, and editorial pages go to `design-taste-frontend`.
- `baseline-ui` and visual design skills: `baseline-ui` validates implementation. It should not choose the art direction.
- `brandkit` and `baseline-ui`: `brandkit` designs identity and icon language; `baseline-ui` checks icon buttons and UI accessibility.
- `imagegen-frontend-web` and `image-to-code`: use `imagegen-frontend-web` when the user wants images only; use `image-to-code` when images must become frontend code.
- `imagegen-frontend-mobile` and `impeccable`: use mobile image generation for concept screens; use `impeccable` only if coding a frontend/product UI afterward.
- `gpt-taste` and `gsap-frameworks`: `gpt-taste` decides the kinetic creative page; `gsap-frameworks` makes Vue/Svelte/Nuxt GSAP lifecycle safe.
- `high-end-visual-design`, `minimalist-ui`, and `industrial-brutalist-ui`: treat these as style overlays unless the user explicitly asks for that style as the main artifact.
- `full-output-enforcement`: add only when completeness is a risk; it does not decide design.

## Trigger Examples

| User Prompt | Route |
|---|---|
| "Make this SaaS dashboard feel production-ready" | primary `impeccable`, validation `baseline-ui` |
| "Redesign this old marketing site without breaking behavior" | primary `redesign-existing-projects`, support `design-taste-frontend`, validation `baseline-ui` |
| "Recreate this screenshot as a React page" | primary `image-to-code`, validation `baseline-ui` |
| "Generate design references for every section of this landing page" | primary `imagegen-frontend-web` |
| "Create premium iOS onboarding flow mockups" | primary `imagegen-frontend-mobile` |
| "Design a logo, brand board, and icon language for this AI tool" | primary `brandkit`, support `high-end-visual-design` |
| "Use GSAP scroll pinning in this Svelte page and clean it up on unmount" | primary `gsap-frameworks`, support `gpt-taste` if creative direction is also needed |
| "Build an Awwwards-style high-motion campaign page" | primary `gpt-taste`, support `gsap-frameworks` for Vue/Svelte/Nuxt or validation `baseline-ui` for Tailwind |
| "Review this Tailwind component for UI issues" | primary `baseline-ui` |
| "Write a Google Stitch DESIGN.md" | primary `stitch-design-taste` |
| "Output every file completely, no omissions" | add `full-output-enforcement` to the selected primary skill |
| "把这个 SaaS dashboard 做得更像生产级产品" | primary `impeccable`, validation `baseline-ui` |
| "帮我 redesign 这个旧官网，不要破坏功能" | primary `redesign-existing-projects`, support `design-taste-frontend`, validation `baseline-ui` |
| "根据这张截图还原成 React 页面" | primary `image-to-code`, validation `baseline-ui` |
| "给这个 landing page 每个 section 出设计参考图" | primary `imagegen-frontend-web` |
| "做一组 iOS onboarding flow 高级视觉图" | primary `imagegen-frontend-mobile` |
| "给这个 AI 工具做 logo、品牌板和 icon language" | primary `brandkit`, support `high-end-visual-design` |
| "Svelte 页面用 GSAP 做 scroll pinning，注意清理" | primary `gsap-frameworks`, support `gpt-taste` if creative direction is also needed |
| "做一个 Awwwards 风格高动效 campaign page" | primary `gpt-taste`, support `gsap-frameworks` for Vue/Svelte/Nuxt or validation `baseline-ui` for Tailwind |
| "检查这个 Tailwind component 有没有 UI 问题" | primary `baseline-ui` |
| "给 Google Stitch 写 DESIGN.md" | primary `stitch-design-taste` |
| "完整输出所有文件，不要省略" | add `full-output-enforcement` to the selected primary skill |

## Recommended Routing Note

Use this compact note before acting:

```text
Skill stack: primary=<skill>; support=<skill(s)>; validation=<skill/checks>.
Reason: <why this stack matches the artifact and constraints>.
```

Then continue the task. Do not only recommend skills unless the user asked for advice.
