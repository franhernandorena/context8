---
name: project-continue
description: Use at the start of any session on an existing project — checks git state, loads md_docs context, sets up or resumes task file, and enforces working rules before any code changes
---

# Project Continue — Session Bootstrap

## Overview
Session bootstrap for an existing project. Orients in the codebase (git state, branch, local changes), loads project context from `md_docs/`, sets up or resumes a task file, and establishes working rules for code, git, testing, and documentation. Do not start work until Phase 3 is complete.

## When to use
- Starting any new session on a project that already has `md_docs/`
- Resuming after a handoff

## When NOT to use
- Project has no `md_docs/` → use `project-init` first
- Multi-repo workspace → use `workflow-continue`

## Output
- Oriented agent with loaded context, task file ready, working rules active

## Full Prompt

@prompt.md
