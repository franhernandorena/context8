---
name: workflow-continue
description: Use when resuming work on a multi-repo workspace that was previously bootstrapped — reorients across all repos, finds in-progress tasks, syncs remotes before any work
---

# Workflow Continue — Resume Multi-Repo Workspace

## Overview
Session bootstrap for returning to an existing workspace. Checks git state across all repos, loads cross-repo context, finds the active task, and enforces working rules for the session. Do not start work until all phases are complete.

## When to use
- Starting a new session on a workspace that already has `md_docs/`
- Resuming after a handoff from another agent

## When NOT to use
- Workspace not yet bootstrapped → use `workflow-init` first
- Single repo (no workspace) → use `project-continue`

## Output
- Oriented agent with loaded context, active task identified, remotes synced

## Full Prompt

@prompt.md
