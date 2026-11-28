---
name: ai-db-designer
description: Design database structure from business processes. Use when the user mentions "设计数据库", "建表", "数据库规范", "数据模型", "ER图", or asks how to structure their database. Also use when the user has a messy existing database that needs redesign.
---

# AI Database Designer

Guide users through designing a clean database structure from their business processes. Discussion in Chinese; outputs in English.

**Core principle:** Databases come from business processes, not from guessing. Understand the business objects first, then design the tables.

## Pipeline Position

This is **Stage 3 of 9** in the AI Project Toolkit pipeline:

1. **ai-project-briefing** — clarify product idea, MVP, scope, flows, business objects
2. **ai-tech-advisor** — choose the technical route and stack
3. **ai-db-designer** — design database from business objects and flows
4. **ai-frontend-scaffolder** — design frontend skeleton and UI rules
5. **ai-backend-api-planner** — design backend responsibilities, API boundaries, auth, validation
6. **backend-skeleton-builder** — build minimal runnable backend skeleton with rules-first approach
7. **backend-architecture-reviewer** — verify and accept the backend architecture
8. **backend-security-checkpoint** — audit API and permission security
9. **backend-deploy-checkpoint** — pre-launch checklist: secrets, build & start, database backup + migration, smoke test, rollback

Stage 3 and 4 (ai-db-designer and ai-frontend-scaffolder) can run in parallel after Stage 2.

Before starting, read `specs/project-brief-spec.md`, `specs/tech-stack-spec.md`, and `specs/frontend-skeleton-spec.md` if they exist. If product scope or frontend flows are missing, recommend returning to the missing earlier stage.
After generating `specs/db-design-spec.md`, recommend `ai-backend-api-planner` as the next stage.

## When to Use

- Starting to design the database for a project
- User says "设计数据库", "建表", "数据库规范"
- After frontend skeleton is defined (UI reveals what data is needed)
- Existing database is messy and needs redesign

**When NOT to use:**
- Project uses no database (static site, client-only app)
- User just wants to run a query
- Database is well-designed and just needs new features

## Auto-Detect Existing Context

Scan the project root and `specs/` (older projects may keep these at the project root):

| File | Action if found |
|------|----------------|
| `specs/project-brief-spec.md` (+ `specs/modules/*.md`) | Read for core business objects, state machines, and Chapter 3 use-case `数据描述` / `后置条件` (fields, status enums, uniqueness, ownership) |
| `specs/tech-stack-spec.md` | Read for database choice (MySQL/PostgreSQL/etc.) |
| `specs/frontend-skeleton-spec.md` | Read for page structure (what data does each page need?) |
| `specs/db-design-spec.md` | Read and offer to update |
| `src/main/resources/db/migration/V*.sql`, `*Entity.java`, `*Mapper.xml`, `schema.*`, `migrations/`, `prisma/schema.prisma` | Read current state |

If `specs/tech-stack-spec.md` is NOT found, ask user about database preference before proceeding.

## Interaction Flow

1. **Extract business objects** — from frontend pages or user discussion
2. **Confirm object relationships** — 1:1, 1:N, N:M
3. **Choose database service** — primary DB + optional cache
4. **Design table structure** — columns, types, indexes
5. **Define field conventions** — naming, critical rules
6. **Confirm and generate** — spec doc + AI rules + schema file
7. **Offer code generation** — ask before generating

## Adaptive Depth Strategy

- **Detailed answer** → Summarize, confirm, move on
- **Short answer** → Ask one follow-up about specific user flows
- **Unsure** → Walk through common patterns for their project type

Always one question per message.

## Step 1: Extract Business Objects

**If `specs/project-brief-spec.md` (or `specs/modules/*.md`) and/or `specs/frontend-skeleton-spec.md` exist**, synthesize business objects, logical fields, status enums, and ownership relationships from the Chinese SRS (`2.6 核心业务对象与状态机概览` + Chapter 3 `数据描述`) and cross-check against frontend pages (if available):

> 根据需求规格说明书（及前端页面结构，如有），我初步整理了以下业务对象与关键状态：
> - [Object 1] — 对应 [模块/用例/页面]，包含状态 [状态枚举]
> - [Object 2] — 对应 [模块/用例/页面]，归属 [归属字段如 user_id]

**If neither spec exists**, ask the user:

> 你的项目里有哪些核心"东西"需要记录？
>
> 比如电商项目：用户、商品、订单、支付记录...
> 比如内容平台：用户、文章、评论、标签...
> 比如预约系统：用户、服务项目、预约记录、时间段...

Each business object approximately maps to one database table. Do not rush to create tables yet — just identify the objects.

## Step 2: Confirm Object Relationships

For each pair of related objects, confirm relationship type:

> | Object A | Relationship | Object B | Example |
> |----------|-------------|----------|---------|
> | User | 1:N | Order | 一个用户有多个订单 |
> | Order | N:M | Product | 一个订单包含多个商品 |

**Relationship types explained simply:**
- **1:1** — 一对一：一个用户对应一份简历
- **1:N** — 一对多：一个用户有多个订单
- **N:M** — 多对多：需要中间表（如 order_products）

## Step 3: Choose Database Service

If `specs/tech-stack-spec.md` has a database choice:

> 技术选型中选了 [MySQL/PostgreSQL]，继续用这个吗？

If no prior spec:

> 主数据库用哪个？
> - A) MySQL — 最流行，适合大部分业务
> - B) PostgreSQL — 功能更强，适合复杂查询
> - C) SQLite — 轻量，适合本地工具
> - D) 不确定，帮我选

Then ask about cache:

> 需要 Redis 做缓存吗？
> - A) 需要 — 有高并发/缓存/队列需求
> - B) 暂时不需要
> - C) 不确定

If C: explain most projects don't need Redis at start. Add later when there's a specific performance need.

## Step 4: Design Table Structure

For each business object, design the table.

**Naming conventions:**
- Table names: `snake_case`, plural (`users`, `order_items`)
- Column names: `snake_case` (`user_id`, `created_at`)
- Foreign keys: `{referenced_table_singular}_id` (`user_id`, `order_id`)

**Standard fields for every table:**

| Field | Type | Description |
|-------|------|-------------|
| id | BIGINT / UUID | Primary key |
| created_at | TIMESTAMP | Auto-set on creation |
| updated_at | TIMESTAMP | Auto-set on update |
| deleted_at | TIMESTAMP NULL | Soft delete (nullable) |

**Ownership field rule:** any table holding user-owned records (orders, articles, addresses, files...) MUST include an ownership foreign key such as `user_id`. Backend "this data belongs to this user" checks and the Stage 8 horizontal-escalation audit depend on it — without the column, ownership cannot be enforced at the data level.

**Architecture-Specific Data Isolation Rules (based on `specs/tech-stack-spec.md` Archetype):**
- **`modular-monolith`**: Every table MUST declare one `Owning Module` (e.g., `orders`, `inventory`). Other modules MUST NOT write to or `JOIN` another module's private tables directly — cross-module queries go through the owning module's public Facade.
- **`spring-cloud-microservices`**: **Database-per-Service** — each microservice owns an isolated database or dedicated schema + DB user. **Never create cross-service foreign keys or shared tables.** For cross-service state changes, add an `outbox_events` table in the producer service and a `processed_messages` idempotency table in each consumer service; stock/balance tables MUST include a `version` column (or conditional `WHERE stock >= qty` check) for concurrency safety.
- **`fastapi-langgraph-agent`**: Include persistent LangGraph checkpointer tables (`checkpoints` / `checkpoint_writes` via `PostgresSaver`) for conversation/HITL resume — never rely on in-memory state. If using RAG, document/chunk tables MUST carry ACL metadata columns (`tenant_id`, `owner_id`, `visibility`) so vector/BM25 retrieval filters permissions before LLM context assembly.

**Present each table as:**

```
### Table: `users`
| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| id | BIGINT | NO | AUTO_INCREMENT | Primary key |
| username | VARCHAR(50) | NO | - | Unique username |
| email | VARCHAR(255) | NO | - | Unique email |
| password_hash | VARCHAR(255) | NO | - | Bcrypt hash |
| ... | ... | ... | ... | ... |

Indexes:
- UNIQUE: email, username
- INDEX: phone, status
```

**Three Normal Forms check (explain simply):**
1. 字段原子化 — 一个字段只存一种信息
2. 围绕主对象 — 用户表放用户信息，订单表放订单信息
3. 不互相依赖 — 已有 city_id 就不存 city_name

## Step 5: Define Field Conventions

| Rule | Example |
|------|---------|
| Passwords MUST be hashed | `password_hash` with bcrypt, NEVER plaintext |
| Money MUST use integer or DECIMAL | `price_cents BIGINT` not `price FLOAT` |
| Status fields MUST have defined values | `status: 0=disabled, 1=active, 2=suspended` |
| Phone supports international format | `VARCHAR(20)` not `VARCHAR(11)` |
| Enums as TINYINT with docs | Document what each value means |

**Anti-patterns:**
- Plaintext passwords
- FLOAT for money
- Chinese column names
- Magic numbers without documentation
- Missing ownership field on user-owned data ("my orders" cannot be enforced later)

## Step 6: Confirm and Generate

> 以上是完整的数据库设计。确认后我会生成：
> 1. `specs/db-design-spec.md` — 数据库设计文档（英文）
> 2. `ai-rules/` — AI 规则文件（多平台）
> 3. `schema` 文件 — 根据你选的 ORM 生成
>
> 确认生成吗？

## Step 7: Generate Outputs

### 1. `specs/db-design-spec.md` (English)

Contains: database service, business objects, entity relationships, all table definitions, field conventions, three normal forms compliance, index strategy, AI agent constraints.

### 2. `ai-rules/` directory

Platform-specific rules: AGENTS.md / CLAUDE.md / .cursorrules covering naming conventions, field type rules, schema-first workflow, prohibited patterns.

### 3. Schema & Migration files

Based on ORM/stack choice, using templates from `references/schema-templates/`, placed under the `backend/` root (or `services/<svc>/` for Spring Cloud) per framework conventions:
- **Java + Flyway + MyBatis-Plus (Default Java Stack)** → `backend/src/main/resources/db/migration/V1__init_schema.sql` (`flyway-mysql.sql`) + `Entity.java` (`mybatis-plus-entity.java`)
- **Java + Spring Data JPA** → Flyway SQL (`V1__init_schema.sql`) + `@Entity` classes (NEVER enable `hibernate.ddl-auto=update/create-drop` in production)
- Prisma → `backend/prisma/schema.prisma`
- Sequelize → migration template under `backend/`
- Django / SQLAlchemy → `backend/models.py` or `alembic/`
- Raw SQL → `backend/schema.sql`

## Step 8: Offer Code Generation

> 数据库设计已生成。接下来我可以帮你：
>
> - **A) 生成 Migration 文件** — 可执行的数据库迁移脚本
> - **B) 生成 Migration + Seed Data** — 迁移脚本 + 测试数据
> - **C) 暂时不需要** — 我先看看文档

## Red Flags

| Thought | Reality |
|---------|---------|
| Just let AI create tables directly | Always design first, generate schema, then create tables |
| FLOAT is fine for prices | FLOAT causes rounding errors. Use INT or DECIMAL |
| Add indexes later when slow | Add indexes on FKs and common query fields from start |
| Soft delete is unnecessary | For financial/order/user data, soft delete is essential |
| User insists on MongoDB | This pipeline designs relationally (migrations, normal forms, ownership fields, schema templates). Explain the mismatch; only proceed if the user accepts a simplified non-relational flow |
| No schema file needed, just create tables | Schema files are the source of truth |

## Common Mistakes

1. **Skipping business object discovery** — Tables without business context lead to wrong structure
2. **Not confirming relationships** — Wrong cardinality cascades into bad foreign keys
3. **Ignoring naming conventions** — Mixed naming makes code painful
4. **No schema/migration file** — Lose track of structure, can't version control
5. **Creating all tables at once** — Build incrementally, test each module
