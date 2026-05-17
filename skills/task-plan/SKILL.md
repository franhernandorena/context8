---
name: task-plan
description: Use before implementing any complex feature, cross-module change, or risky refactor — produces a detailed step-by-step task file with acceptance criteria, risks, and ordered implementation steps
---

# Task Plan — Detailed Task Breakdown

## Overview
Planning-only prompt. Loads project context, understands the task, runs targeted codebase reconnaissance, and produces a detailed `md_docs/tasks/` file with ordered steps, acceptance criteria, unknowns, risks, and a test plan. No application code is written.

## When to use
- Complex features spanning multiple files or modules
- Risky refactors where implementation order matters
- Any task where you want a written plan before starting
- Use when the task is ambiguous and you need to force clarification first

## When NOT to use
- Task is trivial and well-understood → go straight to `task-do`
- Hotfix needed urgently → use `task-hotfix`

## Output
- `md_docs/tasks/YYYY-MM-DD_[description].md` — complete task file with status "Planned"

## Full Prompt

@prompt.md
