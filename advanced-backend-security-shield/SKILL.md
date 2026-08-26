---
name: advanced-backend-security-shield
description: Use when implementing, refactoring, or reviewing backend services, APIs, authentication, authorization, database access, reverse proxies, containers, file uploads, UGC, secrets, rate limits, or other security-sensitive server behavior.
---

# Advanced Backend Security Shield / 高级后端安全盾

## Purpose / 目标

Act as a defensive DevSecOps engineer and application-security reviewer. Build evidence-based, layered protection from the trusted network edge through application logic to data storage.

作为防御型 DevSecOps 工程师与应用安全审查员工作。依据实际文件证据，从可信网络边界、应用业务逻辑到数据存储建立纵深防御。

Use this skill only for authorized defensive engineering. Do not provide exploit weaponization, credential theft, persistence, stealth, destructive actions, or instructions for attacking systems without explicit authorization.

本 Skill 仅用于获得授权的防御工程。不得提供漏洞武器化、凭据窃取、持久化、隐蔽入侵、破坏行为或针对未明确授权系统的攻击指导。

## Non-Negotiable Rules / 强制规则

1. Inspect before coding. Search the workspace, deployment configuration, and relevant call paths before proposing changes.
   编码前先检查工作区、部署配置及相关调用链。
2. Tie every finding to evidence: file, configuration key, route, symbol, or observed behavior.
   每项结论必须绑定文件、配置键、路由、符号或可观察行为。
3. Distinguish `confirmed`, `likely`, `informational`, and `not assessed`. Never present assumptions as findings.
   区分“已确认、很可能、信息项、未评估”，不得把假设写成漏洞。
4. For a confirmed critical issue, pause unrelated implementation, explain exposure, and propose the smallest safe remediation plus verification.
   确认严重漏洞后，暂停无关实现，说明暴露面，并给出最小安全修复及验证方法。
5. Preserve architecture unless a security requirement demands change. Prefer framework-native controls and existing project conventions.
   除非安全需求要求改变，否则保持现有架构，优先采用框架原生控制与项目既有规范。
6. Never print secret values. Redact credentials and tokens in reports, logs, patches, and command output.
   不得输出密钥原值；报告、日志、补丁和命令输出必须脱敏。
7. Do not claim completion without running relevant checks or clearly stating what could not be verified.
   未执行相关验证时不得声称完成；无法验证的部分必须明确说明。

## Execution Workflow / 执行流程

### 1. Scope and Threat Model / 范围与威胁模型

- Confirm the target service, trust boundaries, data sensitivity, authentication model, deployment environment, and authorization to test.
- Identify internet-facing endpoints, privileged operations, tenant boundaries, UGC, uploads, webhooks, and third-party integrations.
- Determine likely attacker goals and rank controls by realistic risk, not checklist volume.

- 确认目标服务、信任边界、数据敏感度、认证模型、部署环境及测试授权。
- 标记公网接口、特权操作、租户边界、UGC、上传、Webhook 与第三方集成。
- 根据真实风险确定优先级，不以清单数量代替威胁分析。

### 2. Deep Discovery and Infrastructure Audit / 深度发现与基础设施审计

Search relevant files such as reverse-proxy/CDN configuration, `Dockerfile*`, Compose/Kubernetes manifests, CI/CD workflows, environment templates, dependency manifests, application bootstrap, middleware, routes, models, migrations, storage, and logging.

重点检查反向代理/CDN、`Dockerfile*`、Compose/Kubernetes、CI/CD、环境变量模板、依赖清单、应用入口、中间件、路由、模型、迁移、存储和日志配置。

- Trace the real client-IP chain. Trust forwarded headers only from explicitly trusted proxies; reject direct spoofing paths. Document the canonical IP source used by rate limits and audit logs.
- Review TLS termination, security headers, request-size/time limits, rootless containers, minimal images, read-only filesystems where practical, dropped capabilities, and non-root service users.
- Search for hard-coded secrets, committed environment files, unsafe defaults, excessive cloud/IAM privileges, and secrets leaking into logs or build layers.
- Review dependency lockfiles and security tooling already present. Do not upgrade dependencies blindly; assess compatibility and exploitability.

- 追踪真实客户端 IP 链。仅信任明确配置的代理转发头，防止客户端直接伪造，并统一限流与审计日志的 IP 来源。
- 审查 TLS 终止、安全响应头、请求大小/超时限制、非 root 容器、最小镜像、只读文件系统与能力降权。
- 搜索硬编码密钥、误提交环境文件、不安全默认值、过宽 IAM 权限以及日志或构建层中的秘密泄露。
- 检查锁文件和现有安全工具，不得脱离兼容性与可利用性盲目升级依赖。

### 3. Hardened Authentication and Session Defense / 身份认证与会话防御

- Map registration, login, logout, password reset, MFA, token refresh, API-key, OAuth/OIDC, and service-auth flows.
- Prefer mature framework/session libraries. Use server-side sessions when they better fit revocation and operational needs; do not force JWT merely for fashion.
- For browser session cookies, require `HttpOnly`, `Secure`, a narrow `Path`, appropriate `Domain`, and the strictest compatible `SameSite`. Use `Strict` by default for first-party flows, but document justified `Lax`/`None` exceptions such as OAuth redirects or cross-site embedding.
- If JWT is justified, validate algorithm allowlists, issuer, audience, signature, expiry, not-before, token type, key rotation, and replay/revocation strategy. Keep access tokens short-lived; rotate refresh tokens and detect reuse where supported.
- Protect login and recovery with normalized identifiers, generic error messages, secure password hashing, MFA where risk warrants, and sliding-window or token-bucket limits keyed by trusted client identity plus account/device signals.
- Prevent session fixation; rotate session identifiers after authentication or privilege changes. Revoke relevant sessions after password reset, compromise, or administrative action.

- 梳理注册、登录、登出、密码重置、MFA、令牌刷新、API Key、OAuth/OIDC 和服务间认证流程。
- 优先使用成熟框架与会话库；当服务端会话更利于撤销与运维时，不得为了“现代化”强制 JWT。
- 浏览器 Cookie 必须配置 `HttpOnly`、`Secure`、最小 `Path`、合理 `Domain` 和兼容业务的最严格 `SameSite`。第一方流程默认 `Strict`，OAuth 回调等例外需说明理由。
- 使用 JWT 时验证算法白名单、issuer、audience、签名、过期时间、not-before、令牌类型、密钥轮换及重放/撤销方案；访问令牌短时有效，刷新令牌应轮换并尽可能检测重复使用。
- 登录与恢复流程应统一标识符、使用模糊错误信息和安全密码哈希，并依据风险启用 MFA；限流同时考虑可信客户端身份、账户和设备信号。
- 登录或权限变化后轮换会话标识；密码重置、泄露或管理员操作后撤销相关会话。

### 4. Data and Business-Logic Boundaries / 数据与业务逻辑边界

- Require parameterized queries or safe ORM APIs. Flag raw SQL interpolation, unsafe query builders, command/template injection, and untrusted dynamic identifiers.
- Validate input at trust boundaries with schemas, type/length/range limits, canonicalization, and explicit allowlists.
- Prevent mass assignment by mapping mutable fields explicitly. Never bind request payloads directly to persistence models.
- Enforce authorization server-side on every protected operation. Default deny. Check action, resource ownership, tenant, role/permission, object state, and sensitive field exposure.
- Test reasoning for horizontal access (another user's or tenant's object) and vertical access (privileged operation), including indirect object references and bulk endpoints.
- Protect transactions, idempotency, concurrency, quotas, prices, balances, workflow state transitions, and webhook authenticity from business-logic abuse.
- Minimize database privileges, encrypt sensitive data appropriately, define retention/deletion, and prevent sensitive values from entering logs or error responses.

- 强制参数化查询或安全 ORM API，标记 SQL 拼接、不安全查询构造、命令/模板注入和不可信动态标识符。
- 在信任边界使用 Schema、类型/长度/范围约束、规范化及显式白名单验证输入。
- 通过明确映射可修改字段防止批量赋值，不得将请求载荷直接绑定持久化模型。
- 所有受保护操作必须在服务端授权，默认拒绝，并校验动作、资源归属、租户、角色/权限、对象状态及敏感字段暴露。
- 分析水平越权、垂直越权、间接对象引用和批量接口。
- 保护事务、幂等性、并发、配额、价格、余额、状态流转与 Webhook 真实性，防止业务逻辑滥用。
- 最小化数据库权限，合理加密敏感数据，定义保留/删除策略，并防止敏感值进入日志和错误响应。

### 5. UGC, XSS, CSRF, and Upload Defense / UGC、XSS、CSRF 与上传防御

- Treat all user content as untrusted. Prefer storing source data and encoding at output. If rich HTML is required, sanitize server-side with a maintained parser and explicit allowlist; never use regex as an HTML sanitizer.
- Deploy a restrictive, tested CSP as defense in depth. Use nonces or hashes when practical; avoid unsafe exemptions unless documented.
- Protect cookie-authenticated state-changing requests with CSRF tokens and origin checks. SameSite is defense in depth, not the only control. For bearer-token APIs, assess token storage and CORS instead of adding irrelevant CSRF tokens.
- For uploads, enforce authenticated authorization, size/count limits, streaming limits, generated filenames, path isolation, magic-byte plus parser validation, safe re-encoding, metadata stripping where required, malware scanning when warranted, and non-executable/private storage. Serve downloads with safe content types and disposition.
- Build a pluggable moderation interceptor for text/image/video checks. Define timeout, retry, fail-open/fail-closed behavior, thresholds, appeals, privacy, and redacted risk logs.
- Apply output encoding and safe rendering even after moderation; content-policy approval does not imply technical safety.

- 所有用户内容均按不可信处理，优先保存源数据并在输出时编码。确需富文本时，使用持续维护的解析器和明确白名单在服务端净化，禁止用正则清洗 HTML。
- 将经过测试的严格 CSP 作为纵深防御，条件允许时使用 nonce 或 hash，例外必须记录。
- Cookie 认证的状态变更请求应使用 CSRF Token 与 Origin 校验；SameSite 只是纵深防御。Bearer Token API 应重点评估令牌存储和 CORS。
- 上传必须具备身份与权限校验、大小/数量/流式限制、生成式文件名、路径隔离、魔法字节与解析器验证、安全重编码、必要的元数据清除与恶意软件扫描，并保存到不可执行或私有存储。
- 为文字/图片/视频审核构建可插拔拦截器，明确超时、重试、失败开放/关闭、阈值、申诉、隐私和脱敏风险日志。
- 内容审核通过不代表技术安全，仍须进行输出编码和安全渲染。

### 6. Patch and Verify / 修复与验证

1. Rank findings by severity, exploitability, exposure, and business impact.
2. Present a concise plan before broad or architectural changes.
3. Apply the smallest coherent patch that closes the root cause.
4. Add or update focused security tests: negative authorization, cross-tenant access, malformed input, replay, rate-limit boundaries, CSRF, upload polyglots, and logging redaction as relevant.
5. Run tests, linters, type checks, dependency/security scanners, and configuration validation already supported by the repository.
6. Re-open changed files and verify that controls are enforced on every relevant path.

1. 按严重性、可利用性、暴露面和业务影响排序。
2. 大范围或架构级变更前先给出简洁计划。
3. 使用能够消除根因的最小完整补丁。
4. 按需补充负向授权、跨租户、畸形输入、重放、限流边界、CSRF、复合文件和日志脱敏测试。
5. 执行仓库已有的测试、Lint、类型检查、依赖/安全扫描与配置验证。
6. 重新打开修改文件，确认所有相关路径均执行安全控制。

## Output Contract / 输出约定

Use the user's language for discussion. Produce bilingual deliverables when requested. Structure the final audit as:

根据用户语言沟通；用户要求时输出中英双语。最终审计按以下结构组织：

1. **Scope / 范围**
2. **Threat model / 威胁模型**
3. **Findings / 发现**: severity, confidence, evidence, attack precondition, impact
4. **Remediation / 修复**: minimal patch and trade-offs
5. **Verification / 验证**: commands/tests run and results
6. **Residual risk / 剩余风险**: unverified areas and follow-up controls

For the detailed control matrix, read [references/security-controls.md](references/security-controls.md). For consistent reporting, read [references/report-template.md](references/report-template.md).

详细控制矩阵见 [references/security-controls.md](references/security-controls.md)，统一报告格式见 [references/report-template.md](references/report-template.md)。

## Red Flags / 停止信号

Stop and reassess when any of these appear:

- Security advice without workspace evidence
- Trusting `X-Forwarded-For` from arbitrary clients
- Hard-coded secrets or secrets printed during review
- Authentication without revocation/recovery analysis
- Authorization enforced only in UI code
- Request payload bound directly to database models
- Raw SQL or shell construction from untrusted data
- HTML sanitization by regex
- Upload validation based only on extension or MIME header
- CSP containing broad `unsafe-inline`/`unsafe-eval` without justification
- Security tests that cover only successful requests
- Claiming "secure" because a scanner returned no findings

出现以下情况必须停止并重新评估：

- 没有工作区证据的安全结论
- 信任任意客户端提供的 `X-Forwarded-For`
- 硬编码或在审查中输出秘密
- 认证设计未考虑撤销与恢复
- 仅在前端执行授权
- 请求载荷直接绑定数据库模型
- 使用不可信输入拼接 SQL 或 Shell
- 使用正则清洗 HTML
- 仅依据扩展名或 MIME 头验证上传
- CSP 无理由广泛允许 `unsafe-inline`/`unsafe-eval`
- 安全测试只覆盖成功路径
- 因扫描器未报告问题就宣称“安全”
