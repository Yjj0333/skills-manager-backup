# Launch Checklist (Stage 9)

Print this before every production deployment. Every line needs actual output, not a claim.

## 0. Pre-launch Gate

- [ ] `backend-impl-source-of-truth.md` exists with fixed startup commands
- [ ] `backend-security-report.md` has no unresolved high-risk items
- [ ] Test suite passes — command and output captured

## 1. Secrets and Environment

- [ ] Production `.env` created on the server/platform only
- [ ] `.gitignore` covers `.env`; `.env.example` has placeholders only
- [ ] Production secrets generated fresh (DB password, JWT secret, API keys)
- [ ] No hardcoded `localhost` / accounts / passwords in source

## 2. Build and Start

- [ ] ONE build command documented and executed
- [ ] ONE start command documented and executed
- [ ] Process supervision in place (platform managed / `restart: always` / systemd / pm2)
- [ ] Log location identified and readable

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
