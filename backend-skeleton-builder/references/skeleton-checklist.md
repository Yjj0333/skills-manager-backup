# Backend Skeleton Checklist

Use this checklist to verify the minimal runnable backend skeleton is complete.

## Five Lines Verification

### Line 1: Startup Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 1 | Project starts without errors | ☐ | |
| 2 | Configuration reads from env/file (not hardcoded) | ☐ | |
| 3 | `.env.example` template exists | ☐ | |
| 4 | Health check endpoint responds (`/health`) | ☐ | |

### Line 2: API Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 5 | Routes follow framework conventions | ☐ | |
| 6 | List success response format defined | ☐ | |
| 7 | Object success response format defined | ☐ | |
| 8 | Error responses unified (400/401/403/404/500) | ☐ | |
| 9 | Business error code rules documented (if needed) | ☐ | |

### Line 3: Business Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 10 | Request entry point identified | ☐ | |
| 11 | Business logic layer separated | ☐ | |
| 12 | Data access layer separated | ☐ | |
| 13 | Parameter validation location identified | ☐ | |
| 14 | Permission check location identified | ☐ | |

### Line 4: Operations Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 15 | Unified logging works | ☐ | |
| 16 | Unified error handling works | ☐ | |
| 17 | Database connection verified | ☐ | |
| 18 | Permission middleware placeholder exists | ☐ | |
| 19 | README has startup/config/test instructions | ☐ | |

### Line 5: Testing Line

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 20 | Test framework initialized (Vitest/Jest/pytest etc.) | ☐ | |
| 21 | At least one sample endpoint test passes (unified success format) | ☐ | |
| 22 | At least one unauthorized-rejection test passes (expects 401/403) | ☐ | |
| 23 | Test command (`npm test` / `pytest`) runs green | ☐ | |

## Architecture Document Checks

| # | Item | Status |
|---|------|--------|
| 24 | Language and framework confirmed and locked | ☐ |
| 25 | Language engineering conventions documented | ☐ |
| 26 | Framework best practices documented | ☐ |
| 27 | Directory structure explained with origins | ☐ |
| 28 | New module file organization rules documented | ☐ |
| 29 | Framework maximization principle stated | ☐ |

## Decision Criteria

- All Line 1 items (1–4) must pass before proceeding
- All Line 2 items (5–9) must pass for consistent API development
- All Line 3 items (10–14) must pass for maintainable business code
- Line 4 items (15–19) must pass for operational readiness
- Line 5 items (20–23) must pass before skeleton acceptance
- Architecture document items (24–29) must pass for sustainable development
