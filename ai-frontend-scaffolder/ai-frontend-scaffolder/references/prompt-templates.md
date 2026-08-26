# Prompt Templates for Frontend Tasks

## 1. Project Skeleton Generation

```
请按照以下规范搭建前端项目骨架：

技术栈：[from tech-stack-spec]
设计风格：[from frontend-skeleton-spec]
目录结构：[from spec]

要求：
1. 按照规范中的目录结构创建所有文件夹
2. 配置好 UI 组件库
3. 创建 design-tokens 文件
4. 创建基础布局组件（Header, Sidebar, Footer, PageContainer）
5. 创建一个示例首页
6. 配置好路由
7. 项目能正常启动
```

## 2. New Page Creation

```
请在现有前端项目中新增一个 [页面名称] 页面。

要求：
- 遵循项目既定的目录结构（放 pages/[module]/ 下）
- 使用设计 Token 中的颜色、字号、间距（不允许硬编码）
- 优先复用已有组件和 UI 组件库
- 如果有新的 UI 结构出现超过 2 次，封装为可复用组件
- 遵循已有的代码风格和项目规范
```

## 3. Component Extraction

```
项目中 [描述重复的 UI 结构] 在多处重复出现。
请将其封装为可复用组件：

- 放在 components/[ui|business]/ 目录下
- 使用设计 Token
- 提供 TypeScript 类型定义
- 支持必要的自定义 props
```

## 4. Design Token Update

```
请更新项目的设计 Token：

需要修改：[token name]: [old value] -> [new value]

要求：
- 只修改 tokens 文件
- 确保所有引用该 token 的地方自动生效
- 不要修改其他 Token
```

## 5. Theme Support

```
请为项目添加暗色模式支持：

要求：
- 基于现有设计 Token 创建暗色主题变量
- 添加主题切换功能
- 切换时有平滑过渡动画
- 记住用户偏好（localStorage）
```
