---
name: backend-deploy-checkpoint
description: Guide non-technical users through a minimal pre-launch checklist for their AI-built backend: production secrets and environment config, build and start commands, database backup before migration, smoke tests, error tracking, and a rollback plan. Use when the user mentions "上线", "部署", "发布", "go live", "准备上线", "上线检查", or wants to make their finished project publicly accessible.
---

# Backend Deploy Checkpoint

Guide the user through the last gate before real users touch the project. Discussion in Chinese; outputs in English.

**Core principle:** Launch failures are boring and predictable — secrets committed to git, migrations run without backup, no way back to the last working version. A short fixed-order checklist prevents all three.

## Pipeline Position

This is **Stage 9 of 9** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-db-designer** — design database from business objects and flows
4. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security
9. **backend-deploy-checkpoint** — pre-launch checklist: secrets, build & start, database backup + migration, smoke test, rollback

Final stage. If `backend-impl-source-of-truth.md` is missing, recommend `backend-architecture-reviewer` (Stage 7) first. If the security report has unresolved high-risk items, recommend fixing them first — do not launch on a red foundation.

## When to Use

- Backend passed architecture review (Stage 7) and security checkpoint (Stage 8), user wants to go live
- User says "上线", "部署", "发布", "go live"
- Re-deploying after major changes (run Steps 2-6 again)

**When NOT to use:**
- Local-only tool with no public users
- User just wants to run the project locally (that is Stage 6 startup evidence)
- Still mid-development and only testing startup

## Auto-Detect Existing Context

| File | Action |
|------|--------|
| `backend-impl-source-of-truth.md` | Read for startup commands, config, database entry points |
| `backend-security-report.md` | Check unresolved items; block launch on high-risk ones |
| `deploy-checklist.md` | Read and offer to update |
| `tech-stack-spec.md` | Read for deployment route (Vercel / Railway / Docker VPS / WeChat Cloud) |
| `.env.example`, `.gitignore`, `Dockerfile`, `docker-compose.yml` | Scan current deployment readiness |

## Interaction Flow

1. **Pre-launch gate** — verify review, security, and tests are done
2. **Secrets and environment** — production config, nothing committed to git
3. **Build and start** — one build command, one start command, process supervision
4. **Database go-live** — backup first, then migrate, then verify
5. **Smoke test** — health, one business endpoint, one rejected unauthorized request
6. **Error tracking and rollback** — optional Sentry, git tag rollback, backup schedule
7. **Generate outputs** — deploy checklist, AI rules

## Step 1: Pre-launch Gate

Ask AI to confirm three things, with evidence:

> 确认三件事：1）backend-impl-source-of-truth.md 存在且启动命令已在其中固化；2）backend-security-report.md 中没有未修复的高危项；3）测试套件运行通过并贴出输出。任何一项不满足，先回对应阶段补齐，不要带病上线。

If any item fails, route back to Stage 7 / Stage 8 / Stage 6. Do not continue this checklist.

## Step 2: Secrets and Environment

- Production `.env` is created on the server or platform, never in git
- `.gitignore` covers `.env`; `.env.example` holds placeholder names only
- Database password, JWT secret, third-party API keys: generated fresh for production, not reused from development
- No hardcoded `localhost`, `127.0.0.1`, accounts, or passwords left in source

**Prompt:**

> 请生成生产环境所需的环境变量清单：每个变量名、用途、示例占位值（不要真实密钥）。并检查代码中是否残留硬编码的地址、账号、密码，如有请列出位置并给出修复方式。

## Step 3: Build and Start

Pick ONE deployment route (from `tech-stack-spec.md` if present):

| Route | Typical form | Supervision |
|-------|-------------|-------------|
| Platform hosting (Vercel / Railway / WeChat Cloud) | Push to deploy | Managed by platform |
| Docker on VPS | Dockerfile + compose | `restart: always` |
| Bare VPS | Build + start script | systemd or pm2 |

Requirements regardless of route:

- ONE documented build command and ONE start command, recorded in the checklist
- The server survives a reboot (process supervision), not just the current SSH session
- Logs go to a location the user can actually find and read

## Step 4: Database Go-Live — Backup, Migrate, Verify

The order is fixed. **Never run a migration without a fresh backup.**

1. **Backup** — dump the current database; confirm the backup file exists and is non-empty
2. **Migrate** — run migrations; if the tool supports dry-run, do that first and show the plan
3. **Verify** — application connects; one real read and one real write succeed; record row counts of key tables before and after

**Prompt:**

> 请按"备份 → 迁移 → 验证"的顺序执行数据库上线：先给出备份命令并确认备份文件存在且非空，再执行迁移并贴出完整输出，最后验证应用连接并做一次真实读写。没有备份不允许执行迁移。

## Step 5: Smoke Test

Three requests against the production URL, actual outputs recorded:

| Request | Expected |
|---------|----------|
| `GET /health` | 200, unified response format |
| One core business endpoint (read) | 200 with real data |
| One protected endpoint without a token | 401/403 — not 500, no stack trace in the body |

If any smoke test fails — stop, fix, redeploy. The first wave of real users will hit exactly these paths without mercy.

## Step 6: Error Tracking and Rollback

- **Error tracking (recommended):** connect Sentry or equivalent; at minimum confirm where errors land and how to read them. Create one test error and find it in the dashboard — that is the evidence.
- **Rollback:** tag the current release (`git tag v1.0.0-launch`); document the one-command way back (previous image / previous tag / platform rollback). The worst launch outcome is not downtime — it is not knowing how to return to the last working version.
- **Backup schedule:** daily database backup from day one (platform automatic backup, or cron + dump).

## Generate Outputs

After all steps pass, generate:

### `deploy-checklist.md` (English)

| Section | Content |
|---------|---------|
| Deployment route | Platform/Docker/VPS decision and reason |
| Commands | The one build command, the one start command |
| Environment variables | Names, purposes, placeholder examples (never real secrets) |
| Database go-live | Backup command and file confirmation, migration output, verification results |
| Smoke test results | Health, business endpoint, unauthorized rejection — with outputs |
| Error tracking | Where errors go, how to read them, test-error evidence |
| Rollback | Tag name and exact rollback steps |
| Backup schedule | Frequency and command |

### `ai-rules/` updates

Add rules:

- Production secrets live only on the server or platform, never in git
- Production database migration requires a fresh backup first — no exceptions
- Every release is tagged before deploy; rollback steps stay current in `deploy-checklist.md`
- Config or deployment changes must update `deploy-checklist.md`

### `ai-rules/prompt-templates.md`

Add prompts for:

- Environment variable list generation
- Backup-migrate-verify execution
- Production smoke test
- Rollback step documentation

## Offer Next: Iteration Mode

> 上线检查已完成，项目正式上线。之后进入日常迭代：新需求先更新对应的规格文档，实现后跑测试回归，再按需更新真源文档。随时可以用 `ai-architect-orchestrator` 查看项目当前状态。

## Red Flags

| Thought | Reality |
|---------|---------|
| "It runs on my machine" | Production has a different environment, domain, database, and real users |
| "Backup is overkill for v1" | The first migration without backup is how data gets lost |
| "Rollback = fix forward" | Without a tagged last-good release, "fix forward" can take hours at peak traffic |
| "Secrets in .env.example is fine" | Example files get committed; real values must never be there |
| "Smoke test = open the homepage" | The homepage can work while login and orders are broken |
| "We'll add monitoring later" | Error tracking takes ten minutes now and is the only way to know it broke |

## Common Mistakes

1. Skipping the pre-launch gate with unresolved security findings
2. Running migrations without a backup
3. Real secrets in `.env.example` or already in commit history
4. No process supervision — the server dies with the SSH session
5. No rollback tag or documented rollback steps
6. Smoke testing only the homepage instead of core endpoints
7. Forgetting a recurring database backup schedule
