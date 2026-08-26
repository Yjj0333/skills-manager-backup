# Field Type Reference Guide

## Common Field Types

### MySQL / MariaDB

| Purpose | Type | Example |
|---------|------|---------|
| Primary key | BIGINT UNSIGNED AUTO_INCREMENT | `id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT` |
| UUID primary key | CHAR(36) | `id CHAR(36) NOT NULL` |
| Short text | VARCHAR(n) | `username VARCHAR(50)` |
| Long text | TEXT | `content TEXT` |
| Email | VARCHAR(255) | `email VARCHAR(255)` |
| Phone | VARCHAR(20) | `phone VARCHAR(20)` |
| Boolean | TINYINT(1) | `is_active TINYINT(1) DEFAULT 1` |
| Money (cents) | BIGINT | `price_cents BIGINT NOT NULL` |
| Money (decimal) | DECIMAL(10,2) | `price DECIMAL(10,2) NOT NULL` |
| Date + time | TIMESTAMP | `created_at TIMESTAMP DEFAULT NOW()` |
| JSON data | JSON | `metadata JSON` |
| Status | TINYINT | `status TINYINT NOT NULL DEFAULT 1` |

### PostgreSQL

| Purpose | Type | Example |
|---------|------|---------|
| Primary key | BIGSERIAL / UUID | `id BIGSERIAL PRIMARY KEY` |
| Boolean | BOOLEAN | `is_active BOOLEAN DEFAULT true` |
| Money | NUMERIC(10,2) | `price NUMERIC(10,2)` |
| JSON data | JSONB | `metadata JSONB` |
| Timestamp | TIMESTAMPTZ | `created_at TIMESTAMPTZ DEFAULT NOW()` |

## Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| Table | snake_case, plural | `users`, `order_items` |
| Column | snake_case | `user_id`, `created_at` |
| Foreign key | `{table_singular}_id` | `user_id`, `order_id` |
| Index | `idx_{table}_{column}` | `idx_users_email` |
| Unique index | `uniq_{table}_{column}` | `uniq_users_email` |
| Join table | `{table1}_{table2}` (alphabetical) | `order_products` |

## Status Field Pattern

Always document values:
```
-- User status: 0=disabled, 1=active, 2=suspended, 3=pending
status TINYINT NOT NULL DEFAULT 1

-- Order status: 0=pending, 1=paid, 2=shipped, 3=completed, 4=cancelled, 5=refunded
status TINYINT NOT NULL DEFAULT 0
```
