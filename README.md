# dev-workflows

Structured prompts for every stage of AI-assisted development. Install once, invoke from any AI coding agent via `/dev-workflows:skill-name`.

## Problem

An agent without structured context improvises: reads files at random, skips conventions, mixes planning with implementation, leaves inconsistent traces between sessions. These prompts enforce a reproducible sequence — orientation → documentation → work — across any AI tool you use.

## Quick Install

```bash
# Interactive — choose tools and scope
uv run install.py

# Or remotely (no clone needed)
uv run https://raw.githubusercontent.com/fnhernandorena/agents_prompts/main/install.py
```

Requires [uv](https://docs.astral.sh/uv/). Supports Claude Code, Codex, Cursor, Gemini CLI, and OpenCode. Installs globally (active in all projects) or locally (this project only).

---

## Skills

### Workflows — multi-repo workspaces

| Skill | Invoke | When to use |
|-------|--------|-------------|
| `workflow-init` | `/dev-workflows:workflow-init` | First session in a workspace with multiple repos |
| `workflow-continue` | `/dev-workflows:workflow-continue` | Resume an existing workspace session |
| `workflow-add-repo` | `/dev-workflows:workflow-add-repo` | Add a new repo to an existing workspace |

### Projects — single repos

| Skill | Invoke | When to use |
|-------|--------|-------------|
| `project-init` | `/dev-workflows:project-init` | First time an agent works in a repo — builds `md_docs/` |
| `project-continue` | `/dev-workflows:project-continue` | Start of every session in a documented repo |
| `project-handoff` | `/dev-workflows:project-handoff` | End a session cleanly for the next agent |
| `project-audit` | `/dev-workflows:project-audit` | Assess a repo with no or stale documentation |

### Tasks

| Skill | Invoke | When to use |
|-------|--------|-------------|
| `task-plan` | `/dev-workflows:task-plan` | Complex features, cross-module changes — plan before touching code |
| `task-do` | `/dev-workflows:task-do` | Execute a planned task step by step |
| `task-review` | `/dev-workflows:task-review` | Pre-PR review: correctness, security, tests, regressions |
| `task-hotfix` | `/dev-workflows:task-hotfix` | Urgent production fix with controlled speed |

---

## Typical Flow

```
New repo       → project-audit  → project-init → project-continue
                                                        ↓
Each session   ──────────────────────────────> project-continue
                                                        ↓
Each task      → task-plan → task-do → task-review → task-hotfix (if prod breaks)
                                                        ↓
End of session → project-handoff
```

For workspaces with multiple repos:
```
workspace-init → workspace-continue (each session) → workspace-add-repo (new repos)
```

---

## What Each Skill Produces

- `project-init` → `md_docs/` with `AGENT_CONTEXT.md`, architecture docs, module map
- `project-continue` → task file in `md_docs/tasks/YYYY-MM-DD_*.md`
- `project-handoff` → `md_docs/HANDOFF_YYYY-MM-DD.md` with state, decisions, next steps
- `project-audit` → `md_docs/AUDIT_YYYY-MM-DD.md` across 7 dimensions
- `task-plan` → task file with acceptance criteria, step-by-step plan, risk table
- `task-do` → implementation + updated task file with completion status
- `task-review` → review report: verdict READY FOR PR or BLOCKED with reasons
- `task-hotfix` → hotfix task file with root cause, fix, and blast radius

---

## Installation Details

The installer (`install.py`) is a single Python file with no external dependencies. It:

1. Detects which AI tools you have installed
2. Lets you pick which ones to install for
3. Lets you pick scope: global (agent's user config, all projects) or project-local
4. Copies `SKILL.md` + `prompt.md` for each skill into the right directory

**Global install paths:**
| Tool | Path |
|------|------|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.agents/skills/` |
| Cursor | `~/.cursor/skills/` |
| Gemini CLI | `~/.gemini/GEMINI.md` |
| OpenCode | `~/.config/opencode/AGENTS.md` |

**Project-local paths:** `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `./GEMINI.md`, `./AGENTS.md`

```bash
uv run install.py             # interactive
uv run install.py --dry-run   # preview, no writes
uv run install.py --uninstall # remove
```

---

## Repository Structure

```
agents_prompts/
├── install.py                    # Cross-platform installer
├── CLAUDE.md                     # Plugin context for Claude Code
├── GEMINI.md                     # Plugin context for Gemini CLI
├── gemini-extension.json         # Gemini extension manifest
│
├── workflows/                    # Source prompts — multi-repo
│   ├── init.md
│   ├── continue.md
│   └── add-repo.md
│
├── projects/                     # Source prompts — single repo
│   ├── init.md
│   ├── continue.md
│   ├── handoff.md
│   └── audit.md
│
├── tasks/                        # Source prompts — task execution
│   ├── plan.md
│   ├── do.md
│   ├── review.md
│   └── hotfix.md
│
└── skills/                       # Packaged skills (installed by install.py)
    ├── workflow-init/
    │   ├── SKILL.md              # Frontmatter + when to use + @prompt.md
    │   └── prompt.md             # Full prompt content
    ├── workflow-continue/
    ├── workflow-add-repo/
    ├── project-init/
    ├── project-continue/
    ├── project-handoff/
    ├── project-audit/
    ├── task-plan/
    ├── task-do/
    ├── task-review/
    └── task-hotfix/
```

---

## Rules

- Every skill enforces phases. Do not skip phases, even for "simple" tasks.
- Skills produce files (`md_docs/`, task files, handoff summaries). Output goes to disk, not inline.
- All documentation written in English unless explicitly overridden.
- `project-review` blocks PR if any security issue is unresolved.
- `task-hotfix` rule: if the fix requires more than 20 lines changed, pause and consider a targeted mitigation instead.
