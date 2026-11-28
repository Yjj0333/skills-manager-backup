# Backend Security Checklist for Non-Technical Users

Use this checklist to track which security items have been verified.

## Checkpoint Status Table

| # | Checkpoint | Status | Evidence Location | Notes |
|---|-----------|--------|-------------------|-------|
| 1 | Security boundary table | ☐ | | |
| 2 | Critical input validation | ☐ | | |
| 3 | Password strength rules | ☐ | | |
| 4 | Password hashed storage | ☐ | | |
| 5 | Admin account extra rules | ☐ | | |
| 6 | Login failure rate limit | ☐ | | |
| 7 | Authentication on protected endpoints | ☐ | | |
| 8 | Role-based authorization | ☐ | | |
| 9 | Data ownership checks | ☐ | | |
| 10 | SQL injection prevention (incl. MyBatis `${}` banned / enum allowlist for `ORDER BY`) | ☐ | | |
| 11 | Command injection & unsafe deserialization prevention (no Fastjson `autoType`) | ☐ | | |
| 12 | Template injection prevention | ☐ | | |
| 13 | No over-defense / dead code | ☐ | | |
| 14 | Dependency vulnerabilities scanned (Maven OWASP/`trivy`, `npm audit`, `pip-audit`) | ☐ | | |
| 15 | Secrets excluded (`.gitignore` covers `.env`, clean git history) | ☐ | | |
| 16 | Production error non-leakage, Actuator `health,info`-only, & file upload allowlists | ☐ | | |
| 17 | (Spring Cloud) Gateway strips client `X-User-*` / `X-Internal-*` & internal ports isolated | ☐ | | |
| 18 | (FastAPI+LangGraph) RAG filters ACL before retrieval (no cross-tenant leakage) | ☐ | | |
| 19 | (FastAPI+LangGraph) Destructive tools gated by `interrupt()` HITL & untrusted context isolated | ☐ | | |
| 20 | (FastAPI+LangGraph) `recursion_limit`, tool timeouts, and per-user token/rate budgets enforced | ☐ | | |

## Status Legend

- ☐ Not checked
- ☑ Passed with evidence
- ⚠ Issue found, needs fix
- ✗ Failed, must fix before go-live

## Severity Guide

| Severity | Items | Impact if missing |
|----------|-------|-------------------|
| Critical | 4, 7, 8, 9, 10, 15, 17, 18, 19 | Data breach, identity spoofing, cross-tenant RAG leak, unauthorized destructive tool execution |
| High | 2, 3, 5, 6, 11, 14, 16, 20 | Account compromise, vulnerable dependencies, runaway loop/token abuse, error/upload exposure |
| Medium | 1, 12, 13 | Maintenance burden, potential indirect risks |

## Decision Criteria

- All Critical items must be ☑ before go-live
- All High items should be ☑ or have documented mitigation plan
- Medium items should be addressed but do not block go-live
