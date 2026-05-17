---
name: workflow-add-repo
description: Use when adding a new repository to an existing bootstrapped workspace — explores the new repo, creates its md_docs/, and updates root workspace overview
---

# Workflow Add Repo — Add Repo to Existing Workspace

## Overview
Adds a new child repo to a workspace that already has a root `md_docs/`. Explores the new repo fully, creates its complete `md_docs/`, and updates the workspace-level index and overview. No code changes.

## When to use
- A new repo was added to the workspace folder
- Workspace is already bootstrapped (`md_docs/WORKSPACE_OVERVIEW.md` exists)
- The new repo does not yet appear in `md_docs/README.md`

## When NOT to use
- Workspace not yet bootstrapped → run `workflow-init` first
- First time setting up the entire workspace → use `workflow-init`

## Output
- `[new-repo]/md_docs/` — full context for the new repo
- Updated `md_docs/README.md` — repo table
- Updated `md_docs/WORKSPACE_OVERVIEW.md` — cross-repo relationships

## Full Prompt

@prompt.md
