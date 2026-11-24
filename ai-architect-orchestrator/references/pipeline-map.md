# Pipeline Map — AI Project Toolkit

## Stage Dependencies & Gates

```
Stage 1: specs/project-brief-spec.md (+ optional specs/modules/*.md, 中文 SRS)
        │
        ▼
Stage 2: specs/tech-stack-spec.md
        │
   ┌────┴───────────────────────────────────┐
   │ (parallel after Stage 2)               │
   ▼                                        ▼
Stage 3: specs/db-design-spec.md      Stage 4: specs/frontend-skeleton-spec.md
   │  (+ backend schema files)           │  (+ specs/design-tokens.json)
   │                                     │
   │                                     └─▶ Parallel UI Track: frontend-skill-router
   │                                         (optional, any time after Stage 2; UI only)
   └────────────────┬───────────────────────┘
                    │
                    ▼
Stage 5: specs/backend-api-spec.md
                    │
                    ▼
Stage 6: specs/backend-architecture-spec.md (+ minimal runnable 5-line skeleton)
                    │
                    ▼
Stage 7: specs/backend-impl-source-of-truth.md (architecture verified)
                    │
                    ▼
   ┌──────────────────────────────────────────────────────────────┐
   │ Milestone Gate: Vertical-Slice MVP Implementation            │
   │ Implement core P0 slices end-to-end (Zero-Mock; see          │
   │ `references/architecture-guardrails.md`):                    │
   │ - specs/project-brief-spec.md (功能用例 & 验收标准)           │
   │ - specs/backend-api-spec.md & backend-impl-source-of-truth.md│
   │ - specs/frontend-skeleton-spec.md (+ frontend-skill-router)  │
   └──────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
Stage 8: specs/backend-security-report.md
         (+ optional advanced-backend-security-shield for technical deep hardening)
                                  │
                                  ▼
Stage 9: specs/deploy-checklist.md
                                  │
                                  ▼
         Iteration Mode (spec-first updates -> code -> regression -> doc sync)
```

## Skill → Spec File Mapping

| Stage | Skill | Reads | Writes |
|-------|-------|-------|--------|
| 1 | `ai-project-briefing` | Existing docs/code (if any) | `specs/project-brief-spec.md` (+ optional `specs/modules/*.md`), `ai-rules/` |
| 2 | `ai-tech-advisor` | `specs/project-brief-spec.md` | `specs/tech-stack-spec.md`, `ai-rules/` |
| 3 | `ai-db-designer` | `specs/tech-stack-spec.md`, `specs/project-brief-spec.md` (+ `specs/modules/*.md`), `specs/frontend-skeleton-spec.md` (if exists) | `specs/db-design-spec.md`, ORM schema under `backend/`, `ai-rules/` |
| 4 | `ai-frontend-scaffolder` | `specs/tech-stack-spec.md`, `specs/project-brief-spec.md` (+ `specs/modules/*.md`), `specs/db-design-spec.md` (if exists) | `specs/frontend-skeleton-spec.md`, `specs/design-tokens.json`, `ai-rules/` |
| UI (Parallel) | `frontend-skill-router` | `specs/project-brief-spec.md`, `specs/frontend-skeleton-spec.md` (if exists) | Concrete UI pages / components / design artifacts |
| 5 | `ai-backend-api-planner` | `specs/project-brief-spec.md` (+ `specs/modules/*.md`), `specs/tech-stack-spec.md`, `specs/db-design-spec.md`, `specs/frontend-skeleton-spec.md` (if applicable) | `specs/backend-api-spec.md`, `ai-rules/` |
| 6 | `backend-skeleton-builder` | `specs/backend-api-spec.md`, `specs/tech-stack-spec.md`, `specs/project-brief-spec.md`, `specs/db-design-spec.md` | `specs/backend-architecture-spec.md`, 5-line minimal runnable backend skeleton, `ai-rules/` |
| 7 | `backend-architecture-reviewer` | `specs/backend-architecture-spec.md`, `specs/backend-api-spec.md`, `specs/tech-stack-spec.md`, actual backend code | `specs/backend-impl-source-of-truth.md`, `ai-rules/` |
| 8 | `backend-security-checkpoint` | `specs/backend-impl-source-of-truth.md`, `specs/backend-api-spec.md`, `specs/project-brief-spec.md`, actual backend code | `specs/backend-security-report.md`, `ai-rules/` |
| 8+ (Optional) | `advanced-backend-security-shield` | Infra/reverse-proxy/Dockerfiles, `specs/backend-impl-source-of-truth.md`, backend code | Hardened controls & evidence-based DevSecOps review |
| 9 | `backend-deploy-checkpoint` | `specs/backend-impl-source-of-truth.md`, `specs/backend-security-report.md`, `specs/tech-stack-spec.md` | `specs/deploy-checklist.md`, `ai-rules/` |

## Parallel Opportunities

| Condition | Can run in parallel |
|-----------|-------------------|
| `specs/tech-stack-spec.md` exists | Stage 3 (`ai-db-designer`) + Stage 4 (`ai-frontend-scaffolder`) |
| `specs/tech-stack-spec.md` exists (has frontend) | `frontend-skill-router` (concrete UI design/build, does not block backend) |
| Stage 3 + Stage 4 complete (or exempted) | Stage 5 alone (integrates DB, frontend, and SRS contracts) |
| Stage 7 complete + MVP implementation | Backend MVP modules + Frontend pages can proceed concurrently per `specs/backend-api-spec.md` |

## Project Profile & Stage Exemptions

Detect product form from `specs/tech-stack-spec.md` or `specs/project-brief-spec.md` before flagging missing stages:

| Project Profile | Exempted Stages (`➖ 不适用`) | Notes |
|-----------------|-------------------------------|-------|
| API Service Only | Stage 4 (`ai-frontend-scaffolder`), `frontend-skill-router` | Stage 5 only requires `specs/db-design-spec.md` + `specs/tech-stack-spec.md` + `specs/project-brief-spec.md` |
| Static Site / Pure Client App (no DB & no backend) | Stage 3 (if no DB), Stage 5–9 | Complete Stage 1 → Stage 2 → Stage 4 + `frontend-skill-router` |
| Small Script / One-off Automation | Stage 3–4 (if no UI/DB), Stage 6–9 | Decided in Stage 5 Step 1; follow simplest script route |
| Local-Only Tool (no public users) | Stage 9 (`backend-deploy-checkpoint`) | Stop after Stage 8 (or Stage 7 for local non-networked tools) |

## Minimum Required Files per Skill (Stages 1–9)

### Stage 1: `ai-project-briefing`
- **Required:** None (entry stage; scans existing docs/code if present)
- **Output:** `specs/project-brief-spec.md` (中文 SRS；大型项目可附 `specs/modules/*.md`)

### Stage 2: `ai-tech-advisor`
- **Required:** `specs/project-brief-spec.md` (confirmed MVP scope, user scale, product form)

### Stage 3: `ai-db-designer`
- **Required:** `specs/tech-stack-spec.md`, `specs/project-brief-spec.md`
- **Recommended:** `specs/frontend-skeleton-spec.md` (if Stage 4 already ran, used to cross-check page data needs), `specs/modules/*.md`

### Stage 4: `ai-frontend-scaffolder`
- **Required:** `specs/tech-stack-spec.md`, `specs/project-brief-spec.md`
- **Recommended:** `specs/db-design-spec.md`, `specs/modules/*.md`
- **Exempt when:** Project is API-service-only or CLI/script

### Stage 5: `ai-backend-api-planner`
- **Required:** `specs/project-brief-spec.md`, `specs/tech-stack-spec.md`, `specs/db-design-spec.md` (unless project uses no DB)
- **Required (unless API-only):** `specs/frontend-skeleton-spec.md`
- **Recommended:** `specs/modules/*.md`

### Stage 6: `backend-skeleton-builder`
- **Required:** `specs/backend-api-spec.md`, `specs/tech-stack-spec.md`
- **Recommended:** `specs/project-brief-spec.md`, `specs/db-design-spec.md`

### Stage 7: `backend-architecture-reviewer`
- **Required:** `specs/backend-architecture-spec.md`, actual backend code directory (skeleton must exist, not docs-only), Gate 5 Zero-Mock Purity pass (see `references/architecture-guardrails.md`)
- **Recommended:** `specs/backend-api-spec.md`, `specs/tech-stack-spec.md`

### Milestone Gate (Between Stage 7 & Stage 8): Vertical-Slice MVP Implementation
- **Required before Stage 8:** `specs/backend-impl-source-of-truth.md` passes architecture review AND MVP slices are delivered end-to-end (real DB + real backend P0 endpoints + real frontend wiring + tests, passing Gate 5 Zero-Mock Production Purity scan)

### Stage 8: `backend-security-checkpoint`
- **Required:** `specs/backend-impl-source-of-truth.md`, `specs/backend-api-spec.md`, actual backend code with real MVP business endpoints implemented, Gate 5 Zero-Mock Purity pass
- **Recommended:** `specs/project-brief-spec.md` (role & permission matrix), `specs/db-design-spec.md` (ownership fields)

### Stage 9: `backend-deploy-checkpoint`
- **Required:** `specs/backend-impl-source-of-truth.md` (locked startup commands), `specs/backend-security-report.md` (no unresolved Critical/High issues or blocking verdict), `specs/tech-stack-spec.md`, Gate 5 Zero-Mock Purity pass (zero business mocks or active `USE_MOCK` toggles in production code/build)
- **Exempt when:** Local-only tool with no public users
