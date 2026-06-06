# Task: Create Frontend Developer Agent Generator Skill

**Date**: 2026-06-06
**Status**: Complete
**Branch**: feat/create-frontend-agent-skill
**Estimated total complexity**: medium

## Objective

Create a new skill `create-frontend-agent` that investigates the project, asks about frontend stack, design system, and UI requirements, inventories available frontend skills/plugins, and generates a professional Frontend Developer agent prompt.

## Acceptance Criteria

- [ ] `skills/create-frontend-agent/SKILL.md` exists with full prompt
- [ ] Skill inventories existing frontend skills/plugins (component libraries, design tools, testing)
- [ ] Skill asks about: framework, styling approach, state management, component patterns, a11y
- [ ] Generated agent prompt covers: component architecture, styling conventions, a11y, testing
- [ ] Skill registered in `install.py`
- [ ] README updated

## Unknowns & Risks

| Unknown / Risk | Impact | Mitigation |
|----------------|--------|------------|
| Frontend frameworks and tools vary | medium | Make skill ask about framework first |
| Design system integration complexity | low | Include design system questions in skill |

## Implementation Plan

## Step 1: Create skill directory and SKILL.md

**Files**: `skills/create-frontend-agent/SKILL.md`
**Depends on**: none
**Estimated complexity**: medium
**Reversible**: yes

### What
Create skill with phases for frontend stack discovery, requirements gathering, and agent prompt generation.

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
