# Security Control Matrix / 安全控制矩阵

Load this reference when performing a full review or when the target includes the listed surface.

执行完整审计或目标包含对应攻击面时读取本文件。

| Surface / 攻击面 | Evidence / 证据 | Required review / 必查项 | Verification / 验证 |
|---|---|---|---|
| Reverse proxy/CDN | Proxy config, app trust-proxy settings | Trusted proxy hops, canonical client IP, TLS, header overwrite | Spoof forwarded headers from an untrusted path |
| Container/runtime | Dockerfile, manifests, runtime policy | Non-root user, minimal image, capabilities, secrets, filesystem/network policy | Inspect built image and runtime identity |
| Secrets | Source, env templates, CI/CD, logs | No hard-coded values, least privilege, rotation, redaction | Secret scan; inspect logs and build args |
| Authentication | Routes, middleware, session/token config | Enumeration, hashing, MFA, rotation, expiry, logout, reset, fixation | Negative and replay tests |
| Authorization | Controllers/services/repositories | Default deny, role/action/resource/tenant checks, field filtering | Cross-user, cross-tenant, and privilege tests |
| Input/injection | Schemas, queries, templates, commands | Parameterization, canonicalization, limits, allowlists | Malformed and injection payload tests |
| Business logic | Transactions, workflows, webhooks | Idempotency, concurrency, state transitions, quotas, signature verification | Replay and race-condition tests |
| UGC/XSS | Renderers, sanitizers, headers | Contextual encoding, maintained sanitizer, CSP | Stored/reflected payload tests in test environment |
| CSRF/CORS | Cookie/token auth, middleware, proxy | CSRF token/origin checks, credentialed CORS allowlist | Cross-origin negative tests |
| Uploads | Multipart handlers, storage, processors | Size/count, magic bytes, parser, re-encode, metadata, private storage | Polyglot, oversized, malformed file tests |
| Moderation | Interceptor, provider client, queues | Thresholds, timeout, fail mode, privacy, appeals, audit logs | Provider failure and threshold boundary tests |
| Data protection | Schema, backups, logs, exports | Classification, encryption, retention, deletion, minimization | Restore/delete/export access tests |
| Observability | Logs, metrics, alerts | Redaction, correlation IDs, security events, abuse alerts | Trigger controlled events and inspect output |

## Severity / 严重性

- **Critical / 严重**: Practical compromise of authentication, privileged execution, broad sensitive-data exposure, or cross-tenant isolation.
- **High / 高**: Exploitable authorization, injection, stored XSS, secret exposure, or meaningful account compromise with realistic preconditions.
- **Medium / 中**: Limited-impact weakness, defense-in-depth failure, or exploit requiring substantial prerequisites.
- **Low / 低**: Hardening issue with low direct exploitability.
- **Informational / 信息**: Observation or recommended practice without a demonstrated vulnerability.

## Confidence / 置信度

- **Confirmed / 已确认**: Directly demonstrated by code, configuration, or a controlled test.
- **Likely / 很可能**: Strong evidence exists, but runtime behavior was not verified.
- **Possible / 可能**: Suspicious pattern requiring more evidence.
- **Not assessed / 未评估**: Outside available scope, access, or tooling.
