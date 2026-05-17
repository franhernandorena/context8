---
name: project-init
description: Use when starting work on a new single-repo codebase for the first time — runs full exploration, builds mental model, creates md_docs/ with all agent-ready context files
---

# Project Init — New Project Bootstrap

## Overview
Full research, exploration, and documentation bootstrap for a new project. Runs systematic codebase exploration (directory structure, configs, git history, CI/CD, tests, entry points, infrastructure), builds a mental model, then creates a complete `md_docs/` structure. No code changes.

## When to use
- First time working on a codebase
- Project has no `md_docs/` directory
- Need to create agent-ready context before starting development

## When NOT to use
- Project already has `md_docs/` → use `project-continue`
- Multi-repo workspace → use `workflow-init`
- Need an honest assessment before committing to full bootstrap → use `project-audit` first

## Output
- `md_docs/AGENT_CONTEXT.md` — comprehensive project context
- `md_docs/AGENT_SYSTEM_PROMPT.md` — ready-to-paste system prompt
- `md_docs/PROJECT_OVERVIEW.md` — 1-page summary
- `md_docs/architecture/` — data_flow, key_patterns, module_map, infrastructure

## Full Prompt

@prompt.md
