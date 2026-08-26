# CodeGraph Routing Rules

This reference explains when to start from the existing CodeGraph index and when to fall back to ordinary repository exploration.

The router must be cheap. Prefer existing indexes over fresh text search when CodeGraph MCP tools are visible. Do not perform indexing or re-indexing unless the user explicitly asks.

## Capability Map

| Route | Use When | Tooling |
|---|---|---|
| `codegraph-aware` | Indexed repository understanding: files, symbols, references, imports, callers, callees, architecture, impact | Visible CodeGraph MCP tools reading an existing index |
| `ordinary-search` | Exact non-symbol text, named-file read/edit, config lookup, visible runtime errors, or CodeGraph unavailable/uninitialized/slow | `rg`, file reads, tests |
| `add-lang` | Add tree-sitter language support to CodeGraph | Only via explicit `/add-lang` or direct user request |
| `agent-eval` | Benchmark CodeGraph retrieval quality | Only via explicit `/agent-eval` or direct user request |

## Availability Gate

Before using `rg` for repository exploration:

1. Confirm whether a matching CodeGraph tool is visible in the current tool list or discoverable via `tool_search`.
2. If CodeGraph tools are visible, start from the existing index for layout, symbols, architecture, flows, and impact.
3. Use `codegraph_status` when you need to confirm whether a target project is indexed, stale, or healthy.
4. If no CodeGraph tool is visible, route to `ordinary-search`.
5. If CodeGraph says the project is not initialized, route to `ordinary-search` unless the user explicitly asked to build an index.
6. If the first CodeGraph call is missing, slow, errors, or times out, stop using CodeGraph for that turn and continue with ordinary search.
7. Do not index or re-index automatically. If the user explicitly asks, use a visible indexing MCP tool when available; otherwise use the local `codegraph` CLI and verify with `codegraph_status`.

## Trigger Phrases

Use CodeGraph-aware exploration for:

- "what files are in this project?"
- "show the indexed structure"
- "search the index for this symbol"
- "where is this function/class/type used?"
- "who calls this?"
- "trace this request/event flow"
- "what imports this module?"
- "what implements this interface?"
- "show the impact of changing this symbol"
- "explain how this subsystem works across files"
- "find entrypoints for this feature"
- "先从索引看"
- "查一下索引"
- "项目结构"
- "查这个函数在哪里被调用"
- "追调用链"
- "跨文件理解这个功能"
- "影响范围分析"
- "找入口"
- "架构关系"

Use ordinary search for:

- "find this exact string" when it is not a symbol/code relationship query
- "open this file" when an exact path is provided
- "change this one component" when the target file is already known and no impact check is needed
- "rename this label"
- "fix this obvious import"
- "format/lint this file"
- "搜一下这个字符串"
- "打开这个文件"
- "只改这个文件"

Use `add-lang` only when the user explicitly invokes `/add-lang` or says:

- "add language support to CodeGraph"
- "给 CodeGraph 加 Lua/Zig/Elixir 支持"

Use `agent-eval` only when the user explicitly invokes `/agent-eval` or says:

- "benchmark CodeGraph"
- "测试 CodeGraph 效果"
- "对比用不用 CodeGraph"

## Practical Heuristic

Ask: "Can the existing CodeGraph index answer this faster or with better relationships?"

- If yes, start with CodeGraph.
- If the task is exact non-symbol text or a named file edit/read, use ordinary search or direct file reads.
- If CodeGraph is unavailable, uninitialized, stale, or times out, simulate the graph manually: search definitions, references, imports, tests, and call sites with `rg`, then read the connecting files.

## Installation Notes

CodeGraph may be installed as an MCP server or CLI, but this router should not install or start it automatically during normal coding tasks.

When the user explicitly asks to initialize, build, refresh, or re-index a project and no indexing MCP tool is visible, use the local CLI:

```powershell
codegraph index "<project-path>"
```

Then verify through MCP:

```text
codegraph_status(projectPath: "<project-path>")
```

If the user explicitly asks to diagnose CodeGraph itself, useful local checks include:

```bash
npm list -g @colbymchenry/codegraph
npx @colbymchenry/codegraph --help
```

On PowerShell:

```powershell
Get-Command codegraph -ErrorAction SilentlyContinue
```

## CodeGraph Repo Workflows

When in the CodeGraph repo:

- New language support means `add-lang` only when explicitly requested.
- Retrieval quality experiments mean `agent-eval` only when explicitly requested.
- Internal code changes still need normal engineering judgment: inspect files, run tests, and avoid committing unless asked.

## Reporting Format

When routing, use:

```text
Route: <route>. Reason: <short reason>.
```

Examples:

```text
Route: codegraph-aware. Reason: The task asks for call relationships across files and a narrow CodeGraph caller tool is available.
```

```text
Route: codegraph-aware. Reason: CodeGraph tools are visible and the user asked to inspect the existing project index.
```

```text
Route: ordinary-search. Reason: The user gave an exact non-symbol string and no indexed relationship lookup is needed.
```
