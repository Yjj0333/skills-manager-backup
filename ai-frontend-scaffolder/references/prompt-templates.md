# Prompt Templates for Frontend Tasks (Feature-First / FSD)

## 1. Project Skeleton Generation

```text
请按照以下规范搭建前端项目骨架：

技术栈：[from tech-stack-spec]
设计风格：[from frontend-skeleton-spec]
目录结构：Strict Feature-First / FSD（app/pages/widgets/features/entities/shared）

要求：
1. 按照规范创建目录结构，并配置 eslint-plugin-boundaries 单向导入限制
2. 配置好 UI 组件库与 design-tokens 文件
3. 创建基础布局（widgets/app-shell/）与三态复用组件（shared/ui/ Loading/Empty/ErrorState）
4. 对接 OpenAPI 契约客户端（shared/api/），严禁在正式源码目录写入业务 Mock 或 catch 回退假数据
5. 配置好路由与单命令 verify，确认可正常启动
```

## 2. New Page & Feature Creation

```text
请在现有前端项目中新增一个 [页面/功能域名称] 模块：

要求：
- 业务组件、状态与接口调用内聚在 `features/<domain>/{ui,model,api}/`，仅通过 `features/<domain>/index.ts` 对外暴露；页面入口 `pages/<domain>/` 只做薄组装
- 严禁跨 feature 深层导入内部文件，严禁 `shared/` 反向引用业务层
- 使用设计 Token 中的颜色、字号、间距（不允许硬编码），三态复用 `shared/ui/`
- 接口直接对接真实后端 API（严禁硬编码 Mock 列表或 catch 静默返回假数据）
```

## 3. Component Extraction

```text
项目中 [描述重复的 UI 结构] 在多处重复出现。
请将其封装为可复用组件：

- 纯通用基础 UI 组件放 `shared/ui/`，域内复用组件放 `features/<domain>/ui/`，跨领域组合块放 `widgets/`
- 使用设计 Token，提供完整 TypeScript 类型定义与自定义 props
```

## 4. Design Token Update

```text
请更新项目的设计 Token：

需要修改：[token name]: [old value] -> [new value]

要求：
- 只修改 tokens 文件
- 确保所有引用该 token 的地方自动生效
- 不要修改其他 Token
```

## 5. Theme Support

```text
请为项目添加暗色模式支持：

要求：
- 基于现有设计 Token 创建暗色主题变量
- 添加主题切换功能
- 切换时有平滑过渡动画
- 记住用户偏好（localStorage）
```
