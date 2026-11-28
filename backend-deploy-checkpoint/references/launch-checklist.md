# Launch Checklist (Stage 9)

Print this before every production deployment. Every line needs actual output, not a claim.

## 0. Pre-launch Gate

- [ ] `backend-impl-source-of-truth.md` exists with fixed startup commands
- [ ] `backend-security-report.md` has no unresolved high-risk items
- [ ] Test suite passes — command and output captured
- [ ] Production Purity (Zero-Mock) scan passes — zero business mocks, in-memory fake DBs, silent catch fallbacks, or unimplemented `200` stubs in production source

## 1. Secrets and Environment

- [ ] Production `.env` created on the server/platform only
- [ ] `.gitignore` covers `.env`; `.env.example` has placeholders only
- [ ] Production secrets generated fresh (DB password, JWT secret, API keys)
- [ ] No hardcoded `localhost` / accounts / passwords in source
- [ ] Any dev mock flag (e.g., `VITE_USE_MOCK` / `USE_MOCK`) is absent or forced `false` in production config

## 2. Build and Start

- [ ] Build & start command(s) documented and executed (1+1 for monolith; ordered startup `Infra → Nacos → Services → Gateway` for Spring Cloud)
- [ ] Process supervision in place (platform managed / `restart: always` / systemd / pm2)
- [ ] Log location identified and readable (with `trace_id` propagation)
- [ ] (Java Spring Boot) `SPRING_PROFILES_ACTIVE=prod`, `-XX:MaxRAMPercentage=75.0`, `server.shutdown=graceful`, `spring.flyway.clean-disabled=true` (no `ddl-auto=update/create-drop`)
- [ ] (Spring Cloud) Every service passes `/actuator/health/readiness`; internal ports unexposed
- [ ] (FastAPI+LangGraph) Production checkpointer is `PostgresSaver`/`RedisSaver` (NOT `MemorySaver`), `recursion_limit`/budgets set, `evals/` baseline passes

## 3. Database Go-Live (fixed order)

- [ ] Backup executed — file exists and is non-empty
- [ ] Migrations executed — full output captured (dry-run first if supported)
- [ ] Connection verified — one real read and one real write succeeded
- [ ] Key table row counts recorded before/after

## 4. Smoke Test (against production URL)

- [ ] `GET /health` → 200, unified format
- [ ] One core business endpoint (read) → 200 with real data
- [ ] One protected endpoint without token → 401/403, no stack trace in body

## 5. Error Tracking and Rollback

- [ ] Error tracking connected (Sentry or log location) — test error created and found
- [ ] Release tagged (e.g. `v1.0.0-launch`)
- [ ] Rollback steps documented — exact commands or platform action
- [ ] Daily database backup scheduled

## Sign-off

| Item | Status | Evidence |
|------|--------|----------|
| Sections 0-4 all checked | | |
| Unresolved items (with reasons) | | |
| Go-live decision | | |
