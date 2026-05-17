---
name: project-audit
description: Use when joining a project with no md_docs, stale documentation, unknown technical debt, or before starting new work on an unfamiliar codebase — produces scored assessment before any changes
---

# Project Audit — Assess Existing Project

## Overview
Read-only assessment of an existing project. Explores the codebase fully, evaluates 7 dimensions (documentation, tests, architecture, conventions, dependencies/security, operational readiness, technical debt), and writes a structured audit report with dimension scores, critical findings, and prioritized next steps. No code changes.

## When to use
- Joining an unfamiliar codebase
- `md_docs/` doesn't exist or is clearly stale
- Suspecting significant technical debt before planning new work
- Need an honest baseline before committing to `project-init`

## When NOT to use
- Starting work when context is already known → use `project-continue`
- First session but project is well-documented → use `project-init` directly

## Output
- `md_docs/AUDIT.md` — dimension scores, critical findings, recommended next steps

## Full Prompt

@prompt.md
