# Infrastructure

## Deployment model

No cloud infrastructure. Este plugin se distribuye via git y se instala localmente.

## How to run locally

```bash
uv run install.py              # interactive install
uv run install.py --dry-run    # preview only
uv run install.py --uninstall  # remove installed skills
```

## Local install paths

| Tool | Global | Project-local |
|------|--------|---------------|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.agents/skills/` |
| OpenCode | `~/.config/opencode/AGENTS.md` | `./AGENTS.md` |

## Dependencies

- Python 3.11+
- `uv` (Astral) para ejecutar el instalador
- `questionary` para el TUI (dependency of install.py script)
