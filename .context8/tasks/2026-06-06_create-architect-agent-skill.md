# Task: Create Software Architect Agent Generator Skill

**Date**: 2026-06-06
**Status**: Complete
**Branch**: feat/create-architect-agent-skill
**Estimated total complexity**: medium

## Objective

Create a new skill `create-architect-agent` that investigates the project, asks about architecture constraints and goals, inventories available architecture documentation tools, and generates a professional Software Architect agent prompt.

## Acceptance Criteria

- [ ] `skills/create-architect-agent/SKILL.md` exists with full prompt
- [ ] Skill inventories existing skills/tools for architecture documentation
- [ ] Skill asks about: architecture patterns, tech stack decisions, scalability requirements, trade-offs
- [ ] Generated agent prompt covers: architecture design, ADRs, trade-off analysis, system design docs
- [ ] Skill registered in `install.py`
- [ ] README updated

## Unknowns & Risks

| Unknown / Risk | Impact | Mitigation |
|----------------|--------|------------|
| Should it generate C4 diagrams or ADRs? | medium | Ask user preferences |
| Different projects need different architecture detail levels | low | Make the skill adaptive |

## Implementation Plan

## Step 1: Create skill directory and SKILL.md

**Files**: `skills/create-architect-agent/SKILL.md`
**Depends on**: none
**Estimated complexity**: medium
**Reversible**: yes

### What
Create the complete skill with phases covering architecture exploration, constraint gathering, and agent prompt generation.

### Why
Foundation for the agent generator.

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
Add `("create-architect-agent", "Generate a professional Software Architect agent prompt")` to SKILLS list.

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
