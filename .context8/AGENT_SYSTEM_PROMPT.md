You are working on **dev-workflows**, a plugin of structured prompts (skills) for AI coding agents. The plugin provides skills for project bootstrapping, session management, and task lifecycle across 5 AI tools (Claude Code, Codex, Cursor, Gemini CLI, OpenCode).

**Tech stack**: Python 3.11+, uv, questionary, Markdown skills

**Primary workflow**:
1. Use `project-continue` skill at session start
2. Read `AGENT_CONTEXT.md` for project context
3. Check `tasks/` for in-progress tasks
4. Work through task files step by step

**Key conventions**:
- Skills go in `skills/<name>/SKILL.md` with YAML frontmatter
- Each skill has strict phases — never skip them
- All documentation in English
- `install.py` is the single entry point for deployment

**What NOT to do**:
- Do NOT modify `.claude-plugin/`, `.codex-plugin/`, or `.cursor-plugin/` without understanding the plugin manifest format
- Do NOT write code without first checking existing tasks
- Do NOT skip exploration phases — they exist for a reason
