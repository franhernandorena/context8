---
name: task-review
description: Use after task-do completes and before opening a PR — reviews diff for correctness, security vulnerabilities, test coverage gaps, convention violations, and regressions
---

# Task Review — Pre-PR Code Review

## Overview
Pre-PR review prompt. Loads the diff and task file, then systematically checks: correctness (logic vs. acceptance criteria), security (injection, secrets, auth), test coverage, convention compliance, and regressions. Produces a structured review report. Blocks PR if any security issue is unresolved.

## When to use
- `task-do` is complete
- Before opening a pull request
- Anytime you want a structured self-review of a diff

## When NOT to use
- Code not yet implemented → use `task-do` first
- Hotfix path (time-critical) → security check is still mandatory inside `task-hotfix`

## Output
- Review report (inline in session) with verdict: READY FOR PR or BLOCKED
- Missing tests added
- Task file updated with review outcome

## Full Prompt

@prompt.md
