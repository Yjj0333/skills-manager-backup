# Prompt Templates for Database Tasks

## 1. Business Object Discovery

```
请根据以下业务流程，整理出所有需要存储的业务对象：

业务描述：[your business description]
主要用户操作：
1. [user action 1]
2. [user action 2]
3. [user action 3]

对于每个业务对象，请说明：
- 对象名称
- 对应什么业务场景
- 包含哪些关键信息
```

## 2. Table Design

```
请为以下业务对象设计数据库表：

业务对象：[object name]
业务场景：[description]
关键信息：[list of fields]

要求：
- 遵循三大范式
- 使用 snake_case 命名
- 包含 id, created_at, updated_at, deleted_at 标准字段
- 关键字段要有索引
- 状态字段用 TINYINT 并注明每个值的含义
- 金额用 BIGINT（分）或 DECIMAL
- 密码只存 hash
```

## 3. Schema Migration

```
请根据以下数据库设计，生成 [Prisma/Sequelize/Django] 的 migration 文件：

[table definitions from db-design-spec.md]

要求：
- 按照框架的 migration 规范生成
- 包含所有索引和约束
- 可以直接执行
```

## 4. Schema Review

```
请审查以下数据库设计，检查：

1. 是否符合三大范式
2. 命名是否一致（snake_case）
3. 字段类型是否合理（特别是金额、状态、密码）
4. 索引是否充分（外键、常用查询字段）
5. 是否有数据一致性风险

设计内容：
[paste your table definitions]
```

## 5. Seed Data Generation

```
请为以下数据库表生成测试数据：

[table definitions]

要求：
- 每张表 5-10 条测试数据
- 数据要符合业务逻辑
- 关联数据要正确（如订单属于某个用户）
- 密码字段用 hash 占位符
```
