---
name: task-hotfix
description: Use for urgent production bugs where normal planning overhead is too slow — triage, locate root cause, minimal fix, security check, verify, and ship with a fast-track PR
---

# Task Hotfix — Urgent Production Fix

## Overview
Compressed but complete fix workflow. Phases are triage (5 min max), root cause confirmation, minimal fix, security check, full verification, and fast-track PR. Speed with control — phases are compressed, not skipped. A rushed fix that introduces a regression is worse than the original bug.

## When to use
- Production is broken and time matters
- Normal `task-plan` → `task-do` cycle is too slow
- Root cause is suspected but needs confirmation

## When NOT to use
- Not urgent → use `task-plan` + `task-do` for full discipline
- Root cause completely unknown with no hypothesis → investigate first, then use this

## Hard rule
If the fix requires more than 20 lines changed: pause. Use a targeted mitigation (feature flag, rollback) while a proper fix is planned.

## Output
- Minimal fix committed on `hotfix/[description]` branch
- Task file with confirmed root cause
- Fast-track PR with root cause, fix, and blast radius documented

## Full Prompt

@prompt.md
