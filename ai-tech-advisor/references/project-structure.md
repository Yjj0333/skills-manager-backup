# Project Directory Structure

Canonical project layouts by product form. The layout is decided at Stage 2 (tech stack selection), recorded in `tech-stack-spec.md`, and reused by every later stage. Never let later stages invent their own roots.

## Common Rules (all layouts)

| Path | Purpose | Created by |
|------|---------|-----------|
| `specs/` | ALL stage documents, one flat folder: `project-brief-spec.md`, `tech-stack-spec.md`, `db-design-spec.md`, `frontend-skeleton-spec.md`, `backend-api-spec.md`, `backend-architecture-spec.md`, `backend-impl-source-of-truth.md`, `backend-security-report.md`, `deploy-checklist.md`, `design-tokens.json` | Stage 1-9 as they run |
| `ai-rules/` | Generated agent rules staging (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `prompt-templates.md`); copy to project root / platform locations when wiring up | Stage 1-9 |
| project root | Only top-level folders + `README.md` + `.gitignore` — never loose code or spec files | Stage 2 |

- Naming: project folder and top-level code directories use kebab-case English (`my-shop`, `frontend/`, `backend/`).
- `.gitignore` baseline from day one: `node_modules/`, `.env`, `dist/`, `build/`, `__pycache__/`, `.venv/`, OS junk (`.DS_Store`, `Thumbs.db`).
- Frontend and backend never share a `src/` — each lives under its own root.

## Layout 1 — Full-stack Website (Next.js)

Single deployable; the project root IS the app root.

```
my-project/
├── specs/
├── ai-rules/
├── app/            ← Next.js App Router (framework convention)
├── src/            ← components, libs, styles (framework convention)
├── public/
└── package.json
```
Filled by: Stage 4 (frontend skeleton). Backend = Next.js API routes — no separate backend root.

## Layout 2 — Website with Separate Backend

```
my-project/
├── specs/
├── ai-rules/
├── frontend/       ← Stage 4 tree lives inside (its src/ is frontend/src/)
└── backend/        ← Stage 5-6 five-line skeleton lives inside
```

## Layout 3 — Mini Program + Backend

```
my-project/
├── specs/
├── ai-rules/
├── miniprogram/    ← Stage 4 (Taro / uni-app tree)
└── backend/        ← Stage 5-6
```

## Layout 4 — App (Mobile) + Backend

```
my-project/
├── specs/
├── ai-rules/
├── app/            ← Stage 4 (Expo / Flutter tree)
└── backend/        ← Stage 5-6
```

## Layout 5 — Admin Panel + Backend

```
my-project/
├── specs/
├── ai-rules/
├── admin/          ← Stage 4 (React + Ant Design / Vue + Element Plus tree)
└── backend/        ← Stage 5-6
```

## Layout 6 — API Service Only

```
my-project/
├── specs/
├── ai-rules/
└── backend/        ← Stage 5-6 (equals the working root for framework tools)
```

## Notes for Later Stages

- Stage 4 (frontend): your directory tree goes INSIDE the frontend root above — full-stack: project root; split: `frontend/`; mini program: `miniprogram/`; app: `app/`; admin: `admin/`.
- Stage 5-6 (backend): your tree goes INSIDE `backend/` (API-service layout: project root).
- Stage 3 (database): schema/migration files go under `backend/` per framework convention (`backend/prisma/schema.prisma`, `backend/models.py`, `backend/schema.sql`).
- Stage 9 (deploy): launch scripts / Dockerfile live in `backend/`, or an optional top-level `deploy/`.
