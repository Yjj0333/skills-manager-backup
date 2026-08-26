# Directory Structure Templates by Framework

## React (Vite + TypeScript)

```
src/
  pages/
    Home/index.tsx
    Auth/Login.tsx, Register.tsx
  components/
    ui/           # Generic reusable (Button, Card, Modal)
    layout/       # Header, Sidebar, Footer, PageContainer
    business/     # Domain-specific
  hooks/
  services/       # API layer (api.ts, auth.ts, user.ts)
  utils/
  stores/         # State management (Zustand/Redux)
  styles/         # tokens.ts, global.css, themes/
  types/
  constants/
```

## Vue 3 (Vite + TypeScript)

```
src/
  views/          # Page-level components
  components/
    ui/
    layout/
    business/
  composables/    # Vue composables
  services/
  utils/
  stores/         # Pinia stores
  styles/
  types/
  constants/
  router/
```

## Next.js (App Router)

```
src/
  app/
    page.tsx              # Home
    layout.tsx            # Root layout
    auth/login/page.tsx
    dashboard/page.tsx, layout.tsx
  components/
    ui/
    layout/
    business/
  hooks/
  lib/            # api.ts, utils.ts
  styles/         # tokens.ts, globals.css
  types/
```

## Vue + Element Plus (Admin Panel)

```
src/
  views/
    dashboard/index.vue
    system/user/index.vue, role/index.vue
  components/
    ui/           # Element Plus wrappers
    layout/       # AppLayout, AppHeader, AppSidebar
    business/
  composables/
  api/
  utils/
  stores/
  styles/
  types/
  router/
```
