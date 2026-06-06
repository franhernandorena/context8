# Module Map

```
┌──────────────────────────────────────────────────┐
│                  dev-workflows                    │
├──────────────────────────────────────────────────┤
│                                                  │
│  install.py ──── reads ───── skills/<name>/     │
│       │                       ├── SKILL.md       │
│       │                       └── prompt.md      │
│       │                                          │
│       ├──→ Claude Code:  ~/.claude/skills/       │
│       ├──→ Codex:        ~/.agents/skills/       │
│       ├──→ Cursor:       ~/.cursor/skills/       │
│       ├──→ Gemini CLI:   ~/.gemini/skills/       │
│       └──→ OpenCode:     ~/.config/opencode/     │
│                                                  │
├── Plugin manifests                               │
│   .claude-plugin/plugin.json                     │
│   .codex-plugin/plugin.json                      │
│   .cursor-plugin/plugin.json                     │
│   gemini-extension.json                          │
│                                                  │
├── Source prompts                                 │
│   workflows/  →  skills/workflow-*/              │
│   projects/   →  skills/project-*/               │
│   tasks/      →  skills/task-*/                  │
│                                                  │
└──────────────────────────────────────────────────┘
```

## Skill categories

```
Workflows (multi-repo)
├── workflow-init
├── workflow-continue
└── workflow-add-repo

Projects (single repo)
├── project-init
├── project-continue
├── project-handoff
└── project-audit

Tasks
├── task-plan
├── task-do
├── task-review
└── task-hotfix

[Future] Agent Generators
├── create-qa-agent
├── create-architect-agent
├── create-backend-agent
├── create-frontend-agent
├── create-database-agent
├── create-cloud-agent
├── create-devops-agent
└── create-security-agent
```
