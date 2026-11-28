# Directory Structure Templates by Framework (Feature-First / Strict Modularity)

All templates enforce one-way dependencies: `app → pages/views → widgets → features/<domain> → entities/<domain> → shared`.
External imports into any feature MUST pass through its public `index.ts` barrel ONLY; configure `eslint-plugin-boundaries` (or `dependency-cruiser`) to enforce this automatically.

## React (Vite + TypeScript)

```text
src/
  app/
    providers/
    router.tsx
  pages/
    home/index.tsx
    auth/LoginPage.tsx, RegisterPage.tsx
    orders/OrdersPage.tsx
  widgets/
    app-shell/            # Header, Sidebar, Footer, PageContainer
  features/
    auth/
      index.ts            # Public API ONLY
      ui/                 # LoginForm, RegisterForm (private)
      model/              # useAuth, authStore (private)
      api/                # authApi.ts (private)
    orders/
      index.ts
      ui/
      model/
      api/
  entities/
    user/
    order/
  shared/
    ui/                   # Generic reusable (Button, Card, Modal, LoadingState, EmptyState, ErrorState)
    api/                  # HTTP client + OpenAPI generated types
    styles/               # tokens.ts, global.css, themes/
    lib/                  # Pure technical utilities ONLY (zero business rules)
```

## Vue 3 / Admin Panel (Vite + TypeScript + Element Plus)

```text
src/
  app/
    router/
  views/
    dashboard/index.vue
    system/user/index.vue, role/index.vue
  widgets/
    app-layout/           # AppLayout, AppHeader, AppSidebar
  features/
    auth/
      index.ts            # Public barrel ONLY
      ui/
      model/              # Pinia store / composables
      api/
    user-management/
      index.ts
      ui/
      model/
      api/
  entities/
    user/
  shared/
    ui/                   # Element Plus wrappers & unified 3-state components
    api/                  # Request client + OpenAPI contract types
    styles/
    lib/
```

## Next.js (App Router)

```text
src/
  app/
    page.tsx              # Home route shell
    layout.tsx            # Root layout
    auth/login/page.tsx
    dashboard/page.tsx, layout.tsx
  widgets/
  features/
    auth/
      index.ts
      ui/
      model/
      api/
  entities/
  shared/
    ui/
    api/
    styles/               # tokens.ts, globals.css
    lib/
```
