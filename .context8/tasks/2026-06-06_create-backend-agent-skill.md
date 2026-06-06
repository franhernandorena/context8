# Task: Create Backend Developer Agent Generator Skill

**Date**: 2026-06-06
**Status**: Complete
**Branch**: feat/create-backend-agent-skill
**Estimated total complexity**: medium

## Objective

Create a new skill `create-backend-agent` that investigates the project, asks about backend stack and requirements, inventories available backend-related skills/plugins, and generates a professional Backend Developer agent prompt.

## Acceptance Criteria

- [ ] `skills/create-backend-agent/SKILL.md` exists with full prompt
- [ ] Skill inventories existing backend-related skills/plugins (API tools, ORMs, DB tools)
- [ ] Skill asks about: language/framework, API design, data layer, auth, error handling
- [ ] Generated agent prompt covers: coding standards, API patterns, error handling, performance
- [ ] Skill registered in `install.py`
- [ ] README updated

## Unknowns & Risks

| Unknown / Risk | Impact | Mitigation |
|----------------|--------|------------|
| Backend tech stacks vary widely | medium | Make skill ask about language/framework first |

## Implementation Plan

## Step 1: Create skill directory and SKILL.md

**Files**: `skills/create-backend-agent/SKILL.md`
**Depends on**: none
**Estimated complexity**: medium
**Reversible**: yes

### What
Create skill with phases for backend stack discovery, requirements gathering, and agent prompt generation.

### How to verify
File exists with all required phases.

### Risks
None.

## Step 2: Register in install.py

**Files**: `install.py`
**Depends on**: Step 1
**Estimated complexity**: trivial
**Reversible**: yes

### What
Add to SKILLS list.

### How to verify
Skill appears in installer.

### Risks
None.

## Step 3: Update README

**Files**: `README.md`
**Depends on**: Step 1
**Estimated complexity**: trivial
**Reversible**: yes

### What
Update Agent Generators table.

### How to verify
README renders correctly.

### Risks
None.
