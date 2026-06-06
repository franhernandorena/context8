# Task: Create Database Expert Agent Generator Skill

**Date**: 2026-06-06
**Status**: Complete
**Branch**: feat/create-database-agent-skill
**Estimated total complexity**: medium

## Objective

Create a new skill `create-database-agent` that investigates the project, asks about database stack, schema complexity, and performance requirements, inventories available DB-related skills/plugins, and generates a professional Database Expert agent prompt.

## Acceptance Criteria

- [ ] `skills/create-database-agent/SKILL.md` exists with full prompt
- [ ] Skill inventories existing DB skills/plugins (ORM tools, migration tools, query analyzers)
- [ ] Skill asks about: database type, schema design, query patterns, migration strategy, performance
- [ ] Generated agent prompt covers: schema design, query optimization, migrations, indexing, backup
- [ ] Skill registered in `install.py`
- [ ] README updated

## Unknowns & Risks

| Unknown / Risk | Impact | Mitigation |
|----------------|--------|------------|
| Diverse database technologies | medium | Make skill detect and adapt |
| Performance optimization varies by workload | low | Include workload pattern questions |

## Implementation Plan

## Step 1: Create skill directory and SKILL.md

**Files**: `skills/create-database-agent/SKILL.md`
**Depends on**: none
**Estimated complexity**: medium
**Reversible**: yes

### What
Create skill with phases for database stack discovery, requirements gathering, and agent prompt generation.

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
