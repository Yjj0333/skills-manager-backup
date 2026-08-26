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
| 10 | SQL injection prevention | ☐ | | |
| 11 | Command injection prevention | ☐ | | |
| 12 | Template injection prevention | ☐ | | |
| 13 | No over-defense / dead code | ☐ | | |

## Status Legend

- ☐ Not checked
- ☑ Passed with evidence
- ⚠ Issue found, needs fix
- ✗ Failed, must fix before go-live

## Severity Guide

| Severity | Items | Impact if missing |
|----------|-------|-------------------|
| Critical | 4, 7, 8, 9, 10 | Data breach, unauthorized access, data manipulation |
| High | 2, 3, 5, 6, 11 | Account compromise, weak authentication |
| Medium | 1, 12, 13 | Maintenance burden, potential indirect risks |

## Decision Criteria

- All Critical items must be ☑ before go-live
- All High items should be ☑ or have documented mitigation plan
- Medium items should be addressed but do not block go-live
