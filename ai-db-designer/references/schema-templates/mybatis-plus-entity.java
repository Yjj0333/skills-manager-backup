// Java 21 + Spring Boot 3 + MyBatis-Plus Standard Entity Template
// Rules:
//   - NEVER bind or return persistence Entity classes directly in @RestController; map to RequestDTO / ResponseVO.
//   - Money fields MUST use BigDecimal; timestamps use LocalDateTime.
//   - Logical delete uses @TableLogic; concurrent balance/stock updates use @Version.

package com.example.app.modules.order.entity;

import com.baomidou.mybatisplus.annotation.FieldFill;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableLogic;
import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.Version;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@TableName("orders")
public class OrderEntity {

    @TableId(type = IdType.ASSIGN_ID)
    private Long id;

    private String orderNo;

    /** Ownership foreign key used by horizontal authorization checks. */
    private Long userId;

    private BigDecimal totalAmount;

    /** 0=draft, 1=pending_review, 2=approved, 3=completed, 9=void */
    private Integer status;

    @Version
    private Integer version;

    @TableLogic
    private Integer deleted;

    @TableField(fill = FieldFill.INSERT)
    private Long createdBy;

    @TableField(fill = FieldFill.INSERT_UPDATE)
    private Long updatedBy;

    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createdAt;

    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updatedAt;
}

// Optional JPA Alternative (when Spring Data JPA is chosen instead of MyBatis-Plus):
//   Use @Entity, @Table(name = "orders"), @Version, @SQLDelete / @SQLRestriction("deleted = 0"),
//   and @EntityListeners(AuditingEntityListener.class). Keep spring.jpa.hibernate.ddl-auto=validate in prod.
