---
name: codegraph-skill-router
description: "Fast router for deciding whether to use CodeGraph or ordinary repository search. Use when the user asks about CodeGraph/code graph/codebase semantic search, cross-file tracing, callers/callees, symbol references, import graphs, architecture relationships, impact analysis, or Chinese phrases like 什么时候调用 CodeGraph, 要不要用 CodeGraph, 追调用链, 查引用, 跨文件理解, 影响范围, 架构关系."
---

# CodeGraph Skill Router

Use this skill to decide whether a code task should start from the existing CodeGraph index or fall back to ordinary repository exploration with `rg` and file reads.

This skill is a fast routing layer. Prefer existing indexes over fresh text search when CodeGraph MCP tools are visible. It must not perform indexing or re-indexing unless the user explicitly asks.

Chinese requests are first-class.

## Quick Rule

Use CodeGraph first for **indexed repository understanding**, especially symbols, files, callers/callees, imports, architecture, and impact. Use `rg`/file reads for **fallback after CodeGraph is unavailable, uninitialized, slow, or insufficient**, and for exact non-symbol text searches.

Route note format:

```text
Route: <ordinary-search | codegraph-aware>. Reason: <why>.
```

Then proceed with the selected workflow. Do not stop after routing unless the user only asked when to use CodeGraph.

## Index-First Rules

- Before using `rg` for repository exploration, check whether a matching CodeGraph MCP tool is visible in the current tool list or discoverable via `tool_search`.
- If CodeGraph tools are visible, prefer the existing index first: `codegraph_context` for task/architecture questions, `codegraph_search` for symbols, `codegraph_files` for file layout, `codegraph_callers`/`codegraph_callees`/`codegraph_trace` for flows, and `codegraph_impact` before shared refactors.
- Use `codegraph_status` when you need to confirm whether a target project is indexed, stale, or healthy.
- If no CodeGraph tool is visible, route to `ordinary-search` and continue with `rg`, file reads, and targeted tests.
- If CodeGraph says the project is not initialized, route to `ordinary-search` unless the user explicitly asked to initialize/build an index.
- If a CodeGraph call is slow, missing, errors, or times out once, stop using CodeGraph for that turn, mention the fallback briefly, and continue with ordinary search.
- Do not index or re-index automatically. If the user explicitly asks to initialize, build, refresh, or re-index, use a visible indexing MCP tool when available; otherwise use the local `codegraph` CLI and verify with `codegraph_status`.
- Avoid broad source dumps as the first call. Start with the narrowest indexed query that can answer the task.

## Tool Selection

Use only MCP tools that are actually available in the active Codex session. Do not invent or assume a tool name from this document.

If available, prefer indexed tools in this order:

| User Need | Prefer A Narrow Visible Tool For |
|-----------|----------------------------------|
| Understand a task, feature, subsystem, or bug | indexed context/task lookup |
| Find a symbol/function/class/type | symbol search or definition lookup |
| Inspect project layout | indexed file tree |
| Understand one function/class | AI/source context for that exact symbol |
| Prepare to edit shared code | edit context, callers, related tests, history |
| Trace callers/callees or request flow | callers, callees, or call graph |
| Estimate impact before modify/delete/rename | impact analysis |
| Inspect file/module imports | dependency/import graph |
| Find tests related to a symbol | related test lookup |
| Find similar/duplicate implementations | similarity or duplicate lookup |

If the only available CodeGraph option is broad repository exploration, use it only for architecture/subsystem questions; otherwise use `rg`/file reads.

## Use CodeGraph When

Prefer CodeGraph when the answer can benefit from the existing index:

- project layout and indexed file inventory
- task/feature/subsystem context
- callers, callees, call graph, request flow, event flow
- symbol definitions, references, implementations, overrides
- module dependency, imports, exports, coupling
- impact analysis before rename/delete/signature changes
- architecture/subsystem explanation across multiple files
- finding related tests for a shared symbol
- large repo exploration where exact `rg` searches are noisy
- checking index health/status when debugging CodeGraph behavior

## Avoid CodeGraph When

Use ordinary `rg`, file reads, and targeted tests when:

- CodeGraph tools are not visible in the current session
- CodeGraph reports that the project is not initialized and the user did not ask to build an index
- a previous CodeGraph call in the turn timed out or errored
- the user gives an exact file path and asks to read or edit that file directly
- exact non-symbol text search is enough
- the change is clearly local to one already-open file
- the task is lint/format/config lookup only
- generated artifacts are involved
- dependency install/runtime errors are local and visible
- the user asks for a simple shell result or a named file's contents
- the user asks to modify this skill itself

Fallback rule: start with CodeGraph when tools and an index are available. Fall back to ordinary search when the indexed result is missing, stale, too broad, or cannot answer the exact text/file question.

## Workflow

1. Classify the request:
   - Indexed repo understanding/symbol/layout/relationship/impact -> possible `codegraph-aware`
   - Exact non-symbol text, named file read/edit, local runtime output -> possible `ordinary-search`
2. Run the availability gate:
   - CodeGraph tool visible and project indexed -> `codegraph-aware` by default
   - CodeGraph tool not visible -> `ordinary-search`
3. Announce route in one line.
4. If routing to CodeGraph, use the narrowest visible indexed tool.
5. Open/read source files for any claims that matter.
6. For edits, verify callers/tests with CodeGraph first when the indexed call succeeds; otherwise use `rg`.
7. Verify with targeted tests/searches after the edit.

## Validation Rule

CodeGraph is context, not the final source of truth. For important claims or edits:

- inspect the actual files returned by CodeGraph
- confirm line numbers and signatures from source
- verify tests or callers when changing behavior
- do not claim completion from graph results alone

## Toolkit Integration

Use this router as a cross-cutting helper, not a stage replacement:

1. `ai-project-briefing`: usually ordinary docs/file work; use CodeGraph only for an existing repo's real relationships.
2. `ai-tech-advisor`: ordinary research/spec reading; use CodeGraph only if evaluating an existing codebase's actual stack.
3. `ai-frontend-scaffolder`: use CodeGraph only when existing routes/components/dependencies must be traced across files.
4. `ai-db-designer`: use CodeGraph only to trace ORM models, migrations, repositories, and DB consumers in existing projects.
5. `ai-backend-api-planner`: use CodeGraph for existing controllers/routes/services, API call chains, auth middleware, and impact analysis when tools are available.

## Output Rule

When the user asks "when should I use CodeGraph?", answer:

Use CodeGraph first when an existing index is available: project layout, symbol search, cross-file relationships, call/import graphs, impact analysis, and architecture understanding should start from the index. Use `rg` and direct file reads as fallback for unavailable/uninitialized/slow CodeGraph, exact non-symbol text, named-file edits, and final verification.
