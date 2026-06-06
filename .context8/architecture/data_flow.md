# Data Flow

## User invokes a skill

```
User writes /dev-workflows:task-plan
        │
        ▼
AI agent loads skills/<skill>/SKILL.md
        │
        ▼
Agent follows SKILL.md phases:
  Phase 1 → Read context files
  Phase 2 → Understand the task
  Phase 3 → Codebase reconnaissance
  Phase 4 → Build plan / create files
  Phase 5 → Write output files
        │
        ▼
Output goes to disk:
  .context8/tasks/YYYY-MM-DD_*.md
  .context8/HANDOFF_*.md
  .context8/AUDIT_*.md
```

## Installation flow

```
User runs: uv run install.py
        │
        ▼
install.py detects tools (Claude, Codex, etc.)
        │
        ▼
User selects tools, scope, skills
        │
        ▼
install.py copies from skills/<name>/ to
  tool-specific paths (global or project-local)
```

## Plugin registration flow

```
Claude Code starts
        │
        ▼
Reads .claude-plugin/plugin.json → finds "skills": "./skills/"
        │
        ▼
Registers /dev-workflows:<skill> for each skill dir
        │
        ▼
User can invoke any skill via slash command
```
