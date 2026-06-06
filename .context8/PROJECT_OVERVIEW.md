# Dev Workflows — Project Overview

## What it does

Plug-n-play structured prompts for AI coding agents. Install once via `uv run install.py`, then invoke any skill from your AI agent via `/dev-workflows:<skill-name>`. Each skill enforces a reproducible, phased workflow — no more improvisation.

## Who uses it

Developers using Claude Code, Codex, Cursor, Gemini CLI, or OpenCode who want consistent, structured agent interactions.

## Key architectural decisions

- **Skills as Markdown files**: Simple, version-controllable, platform-agnostic
- **Single installer for all tools**: `install.py` detects the environment and adapts
- **Phased prompts**: Every skill has mandatory phases — no skipping, no improvisation
- **File-based state**: Tasks, handoffs, audits all go to `.context8/` on disk

## Current state

Stable with 11 skills covering workspace management, project lifecycle, and task execution. Well-documented with README and installation guide.

## Next priorities

- Add agent-generator skills (create specialized agent prompts: QA, Architect, Backend, Frontend, DB, Cloud, DevOps/SRE, Security)
- Add tests for `install.py`
- Add CI/CD pipeline
