# Key Patterns & Conventions

## File/folder naming

- `lowercase-with-hyphens` for skill directory names
- `SKILL.md` for skill definitions (UPPERCASE)
- `prompt.md` for prompt content (lowercase)

## Skill definition format

Every SKILL.md must have:
1. YAML frontmatter: `name`, `description`
2. `## Overview` — what the skill does
3. `## When to use` / `## When NOT to use`
4. `## Output` — what files/artifacts it produces
5. `## Full Prompt` — the complete instruction block

## Module boundary rules

- Each skill is self-contained in `skills/<name>/`
- Skills do not depend on each other
- Source prompts in `workflows/`, `projects/`, `tasks/` mirror the skills/ structure
- Installer reads from `skills/` only

## Error handling pattern

- Installer: try/except per skill fetch, collect errors, report at end
- Skills: hard stops when unexpected state found, document blockers

## How new skills are added

1. Create `skills/<name>/SKILL.md` with full prompt
2. Create `skills/<name>/prompt.md` with prompt content
3. Add the skill to `install.py` SKILLS list
4. Update README.md with the new skill
5. Update .context8/ if architecture changed

## Anti-patterns

- Do NOT skip phases in a skill prompt
- Do NOT mix planning and implementation in a single output
- Do NOT write secrets to .context8/ or any documentation file
- Do NOT assume a specific AI tool — skills must be tool-agnostic
