---
name: project-handoff
description: Use when closing a project session — updates all stale md_docs, captures in-progress task state and git status, writes HANDOFF.md so the next agent can resume without re-reading source code
---

# Project Handoff — Close Session for Next Agent

## Overview
Closes a project session cleanly. Captures current git state, updates every stale section of `md_docs/`, documents in-progress tasks with precise progress logs, and writes `md_docs/HANDOFF.md` with immediate next steps, blockers, and warnings. No code changes.

## When to use
- Ending a session before work is fully complete
- Handing off to another agent or developer
- Before taking a long break from a project

## When NOT to use
- Work is fully complete → just commit and close
- Starting a session → use `project-continue`

## Output
- Updated `md_docs/AGENT_CONTEXT.md` (stale sections refreshed)
- Updated in-progress task files
- `md_docs/HANDOFF.md` with state, blockers, next steps

## Full Prompt

@prompt.md
