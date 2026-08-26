# Pipeline Map — AI Project Toolkit

## Stage Dependencies

```
project-brief-spec.md
        │
        ▼
tech-stack-spec.md
        │
   ┌────┴────────────────┐
   │                     │
   ▼                     ▼
frontend-skeleton-spec   db-design-spec.md
   │    +                │
   │ frontend-skill-router (UI, parallel, optional)
   │                     │
   └────────┬────────────┘
            │
            ▼
      backend-api-spec.md
            │
            ▼
   backend-architecture-spec.md
            │
            ▼
   backend-impl-source-of-truth.md
            │
            ▼
      security-audit-report.md
```

## Skill → Spec File Mapping

| Skill | Reads | Writes |
|-------|-------|--------|
| ai-project-briefing | — | `project-brief-spec.md` |
| ai-tech-advisor | `project-brief-spec.md` | `tech-stack-spec.md` |
| ai-frontend-scaffolder | `tech-stack-spec.md`, `project-brief-spec.md` | `frontend-skeleton-spec.md` |
| ai-db-designer | `tech-stack-spec.md`, `project-brief-spec.md` | `db-design-spec.md` |
| frontend-skill-router | `project-brief-spec.md`, `frontend-skeleton-spec.md` | UI design artifacts |
| ai-backend-api-planner | `frontend-skeleton-spec.md`, `db-design-spec.md`, `tech-stack-spec.md` | `backend-api-spec.md` |
| backend-skeleton-builder | `backend-api-spec.md`, `tech-stack-spec.md` | `backend-architecture-spec.md` |
| backend-architecture-reviewer | `backend-architecture-spec.md` + code | `backend-impl-source-of-truth.md` |
| backend-security-checkpoint | `backend-impl-source-of-truth.md`, `backend-api-spec.md` | `security-audit-report.md` |

## Parallel Opportunities

| Condition | Can run in parallel |
|-----------|-------------------|
| `tech-stack-spec.md` exists | Stage 3 (frontend-scaffolder) + Stage 4 (db-designer) |
| `tech-stack-spec.md` exists | frontend-skill-router (UI only, no blockers) |
| Stage 3 + 4 complete | Stage 5 alone (no parallelism) |
| All stages complete | Business feature development begins |

## Minimum Required Files per Skill

### backend-skeleton-builder (Stage 6)
- **Required:** `backend-api-spec.md`
- **Required:** `tech-stack-spec.md`
- Recommended: `project-brief-spec.md`, `db-design-spec.md`

### backend-architecture-reviewer (Stage 7)
- **Required:** `backend-architecture-spec.md`
- **Required:** Actual backend code directory
- Recommended: `backend-api-spec.md`

### backend-security-checkpoint (Stage 8)
- **Required:** `backend-impl-source-of-truth.md`
- **Required:** `backend-api-spec.md`
- Recommended: Actual backend code directory
