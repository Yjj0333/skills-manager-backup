# Prompt Templates for Database Tasks

## 1. Business Object Discovery

```text
请根据以下业务流程，整理出所有需要存储的业务对象：

业务描述：[your business description]
主要用户操作：
1. [user action 1]
2. [user action 2]
3. [user action 3]

对于每个业务对象，请说明：
- 对象名称与归属模块（Owning Module / Service）
- 对应什么业务场景
- 包含哪些关键信息（含归属字段如 user_id）
```

## 2. Table Design

```text
请为以下业务对象设计数据库表：

业务对象：[object name]
归属模块：[owning module or service]
业务场景：[description]
关键信息：[list of fields]

要求：
- 遵循三大范式，禁止跨模块外键或跨服务共享表
- 使用 snake_case 命名
- 包含 id, created_at, updated_at, deleted（或 deleted_at）, version（如涉及并发）标准字段
- 含归属字段（如 user_id / tenant_id）及关键查询复合索引
- 状态字段用 TINYINT 并注明每个枚举值含义
- 金额用 DECIMAL(18,2)（或 BIGINT 分），严禁 FLOAT/DOUBLE
- 密码只存 BCrypt hash
```

## 3. Schema & Flyway Migration

```text
请根据以下数据库设计，生成 [Flyway SQL + MyBatis-Plus Entity / Spring Data JPA / Alembic / Prisma] 迁移与模型文件：

[table definitions from db-design-spec.md]

要求（Java 默认方案）：
- Flyway 迁移放 `backend/src/main/resources/db/migration/V1__init_schema.sql`（如微服务放各服务目录下）
- 包含所有主键、唯一约束与索引，注释清晰
- MyBatis-Plus Entity 严格配置 BigDecimal、LocalDateTime、@TableLogic、@Version 与审计字段
- 严禁生产开启 JPA ddl-auto: update/create-drop，确保 Flyway 可重复执行
```

## 4. Schema Review

```text
请审查以下数据库设计，检查：

1. 是否符合三大范式与模块/微服务数据隔离规则（表归属清晰，无跨服务共享表）
2. 命名是否一致（snake_case）
3. 字段类型是否合理（特别是 DECIMAL 金额、TINYINT 状态、BCrypt 密码、version 乐观锁）
4. 索引是否充分（外键、归属字段 + 状态组合索引、常用查询字段）
5. 若涉及微服务跨库写操作，是否包含 outbox_events 与 processed_messages 幂等表

设计内容：
[paste your table definitions]
```

## 5. Seed Data Generation

```text
请为以下数据库表生成开发测试数据（放 seeds/ 或非生产 profile 迁移中，禁止混入正式接口）：

[table definitions]

要求：
- 每张表 5-10 条测试数据
- 数据符合业务逻辑与外键关联（如订单属于具体 user_id）
- 密码字段使用 BCrypt hash 占位符
```
