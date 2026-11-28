-- Flyway Migration Template (Java 21 + Spring Boot 3 + MyBatis-Plus Default)
-- Path: backend/src/main/resources/db/migration/V1__init_schema.sql
-- Rules:
--   1. Never enable hibernate.ddl-auto=update/create-drop in production; keep spring.flyway.clean-disabled=true.
--   2. Every user-owned table MUST carry an ownership foreign key (e.g. user_id).
--   3. Money MUST use DECIMAL(18,2) (or BIGINT cents); never FLOAT/DOUBLE.
--   4. Concurrent inventory/balance tables MUST include version INT for optimistic locking.

CREATE TABLE users (
    id            BIGINT       NOT NULL COMMENT 'Primary key (Snowflake ID or AUTO_INCREMENT)',
    username      VARCHAR(50)  NOT NULL COMMENT 'Unique login username',
    email         VARCHAR(255) NOT NULL COMMENT 'Unique email',
    password_hash VARCHAR(255) NOT NULL COMMENT 'BCrypt password hash (never plaintext)',
    role          VARCHAR(32)  NOT NULL DEFAULT 'USER' COMMENT 'Role code: USER, ADMIN',
    status        TINYINT      NOT NULL DEFAULT 1 COMMENT '0=disabled, 1=active, 2=suspended',
    version       INT          NOT NULL DEFAULT 0 COMMENT 'Optimistic lock version',
    deleted       TINYINT      NOT NULL DEFAULT 0 COMMENT 'Logical delete: 0=active, 1=deleted',
    created_by    BIGINT       NULL COMMENT 'Creator user ID',
    updated_by    BIGINT       NULL COMMENT 'Last updater user ID',
    created_at    DATETIME(3)  NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    updated_at    DATETIME(3)  NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
    PRIMARY KEY (id),
    UNIQUE KEY uk_users_username (username),
    UNIQUE KEY uk_users_email (email),
    KEY idx_users_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Users table';

CREATE TABLE orders (
    id            BIGINT         NOT NULL COMMENT 'Primary key (Snowflake ID)',
    order_no      VARCHAR(64)    NOT NULL COMMENT 'Unique business order number',
    user_id       BIGINT         NOT NULL COMMENT 'Ownership FK -> users.id (required for horizontal auth)',
    total_amount  DECIMAL(18, 2) NOT NULL COMMENT 'Order total amount (never FLOAT)',
    status        TINYINT        NOT NULL DEFAULT 0 COMMENT '0=draft, 1=pending_review, 2=approved, 3=completed, 9=void',
    version       INT            NOT NULL DEFAULT 0 COMMENT 'Optimistic lock version',
    deleted       TINYINT        NOT NULL DEFAULT 0 COMMENT 'Logical delete: 0=active, 1=deleted',
    created_by    BIGINT         NULL,
    updated_by    BIGINT         NULL,
    created_at    DATETIME(3)    NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    updated_at    DATETIME(3)    NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
    PRIMARY KEY (id),
    UNIQUE KEY uk_orders_order_no (order_no),
    KEY idx_orders_user_status (user_id, status),
    KEY idx_orders_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Orders table (Owning Module: orders)';

-- Spring Cloud Microservices Add-on (Database-per-Service):
--   Producer service: add outbox_events (id, aggregate_type, aggregate_id, event_type, payload_json, status, created_at)
--   Consumer service: add processed_messages (message_id PRIMARY KEY, consumer_group, processed_at) for idempotency
