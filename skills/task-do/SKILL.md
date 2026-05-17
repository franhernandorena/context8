---
name: task-do
description: Use to implement a task that already has a Planned task file in md_docs/tasks/ — executes each step with verification, hard stops on unexpected state, and closes the task with full documentation
---

# Task Do — Execute a Planned Task

## Overview
Implementation prompt. Requires a task file with status "Planned". Loads context, sets up the branch, runs baseline tests, then executes each step from the implementation plan with verification, commits, and hard stops. Closes the task with updated documentation and an optional PR.

## When to use
- A task file with status "Planned" exists in `md_docs/tasks/`
- Ready to implement (context loaded, branch set up)

## When NOT to use
- No task file exists → run `task-plan` first
- Urgent production bug → use `task-hotfix`

## Output
- Implemented changes committed atomically
- Task file updated to "Complete"
- `md_docs/` updated if architecture changed
- PR opened (if required)

## Full Prompt

@prompt.md
