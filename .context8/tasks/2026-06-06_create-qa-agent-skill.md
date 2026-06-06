# Task: Create QA/Test Agent Generator Skill

**Date**: 2026-06-06
**Status**: Complete
**Branch**: feat/create-qa-agent-skill
**Estimated total complexity**: medium

## Objective

Create a new skill `create-qa-agent` that, when invoked, investigates the project, asks targeted questions about testing needs, inventories available testing skills/plugins/tools, and generates a professional QA/Test engineer agent in the native format of the current AI coding tool.

## Acceptance Criteria

- [x] `skills/create-qa-agent/SKILL.md` exists with YAML frontmatter and full prompt
- [x] Skill inventories existing skills/plugins/tools (Phase 1 — Preflight)
- [x] Skill asks targeted questions about testing frameworks, coverage goals, CI/CD integration (Phase 3)
- [x] Generates agent in native format of the current tool (Phase 4 — not a SKILL.md, a real agent)
- [x] Skill registered in `install.py` SKILLS list
- [x] README updated with the new skill entry

## Design Decision

During implementation, the design evolved. Originally planned to output a SKILL.md. Instead outputs a **native agent file** for the current tool (e.g., `.opencode/agents/qa-agent.md`, `.claude/agents/qa-agent.md`). The AI tool knows its own agent format — the skill just tells it what to create.

## Implementation Plan

## Step 1: Create skill directory and SKILL.md

**Files**: `skills/create-qa-agent/SKILL.md`
**Depends on**: none
**Estimated complexity**: medium
**Reversible**: yes

### What
Created the complete skill with phases:
- Phase 1: Preflight — inventory skills/plugins, scan tech stack
- Phase 2: Domain Research — explore testing landscape
- Phase 3: Domain Questions — ask about testing needs
- Phase 4: Generate Agent — create native agent file for current tool

### Why
Foundation for the agent generator.

### How to verify
File exists at correct path with all required phases.

### Risks
None.

## Step 2: Register in install.py

**Files**: `install.py`
**Depends on**: Step 1
**Estimated complexity**: trivial
**Reversible**: yes

### What
Add `("create-qa-agent", "Generate a professional QA/Test engineer agent prompt")` to the SKILLS list.

### How to verify
Skill appears when running `uv run install.py`.

### Risks
None.

## Step 3: Update README

**Files**: `README.md`
**Depends on**: Step 1
**Estimated complexity**: trivial
**Reversible**: yes

### What
Update the Agent Generators table with the new skill entry.

### How to verify
README renders correctly.

### Risks
None.

## Files Modified
| File | Change type | Notes |
|------|-------------|-------|
| `skills/create-qa-agent/SKILL.md` | create | Full skill with 4 phases |
| `install.py` | modify | Added to SKILLS list |
| `README.md` | modify | Added to Agent Generators table |

## Progress Log
- [21:45] Design finalized: generates native agent (not SKILL.md)
- [21:50] SKILL.md created with Preflight + Domain Research + Questions + Generate phases
- [21:50] install.py updated with all 8 new skills
- [21:50] README updated with Agent Generators section
