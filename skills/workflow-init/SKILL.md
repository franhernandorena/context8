---
name: workflow-init
description: Use when setting up a new multi-repo workspace for the first time — discovers child repos, creates root md_docs/ and per-repo md_docs/ with agent-ready context
---

# Workflow Init — Multi-Repo Workspace Bootstrap

## Overview
Bootstraps a workspace: a parent folder containing multiple independent repos. Creates a root `md_docs/` (navigation + cross-repo overview) and a full `md_docs/` inside each child repo. No code changes — documentation only.

## When to use
- First time working in a folder that contains multiple git repos
- Workspace has no `md_docs/` at the root level
- Need agent-ready context before starting cross-repo work

## When NOT to use
- Single repo → use `project-init` instead
- Workspace already bootstrapped → use `workflow-continue`
- Adding one new repo to existing workspace → use `workflow-add-repo`

## Output
- `md_docs/README.md` — workspace index
- `md_docs/WORKSPACE_OVERVIEW.md` — cross-repo context
- `[repo]/md_docs/` — full context for each child repo

## Full Prompt

@prompt.md
