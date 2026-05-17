# Dev Workflows Plugin

Structured prompts for every stage of development work with an AI agent.

## Available Skills

### Workflows (multi-repo workspaces)
- `dev-workflows:workflow-init` — bootstrap a new multi-repo workspace
- `dev-workflows:workflow-continue` — resume an existing workspace session
- `dev-workflows:workflow-add-repo` — add a new repo to an existing workspace

### Projects (single repos)
- `dev-workflows:project-init` — bootstrap a new project (creates md_docs/)
- `dev-workflows:project-continue` — start a session on an existing project
- `dev-workflows:project-handoff` — close a session cleanly for the next agent
- `dev-workflows:project-audit` — assess a project with no or stale documentation

### Tasks
- `dev-workflows:task-plan` — produce a detailed implementation plan
- `dev-workflows:task-do` — execute a planned task step by step
- `dev-workflows:task-review` — pre-PR code review (correctness, security, tests)
- `dev-workflows:task-hotfix` — urgent production fix with controlled speed

## Typical Flow

```
project-audit → project-init → project-continue → task-plan → task-do → task-review
                                                                        ↓
                                                               task-hotfix (if prod breaks)
```

## Rules
- Every skill enforces phases. Do not skip phases, even for "simple" tasks.
- Skills produce files (`md_docs/`, task files, handoff summaries). Output goes to disk, not inline.
- All documentation written in English unless explicitly overridden.
