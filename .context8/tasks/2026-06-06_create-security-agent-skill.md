# Task: Create Security Engineer Agent Generator Skill

**Date**: 2026-06-06
**Status**: Complete
**Branch**: feat/create-security-agent-skill
**Estimated total complexity**: medium

## Objective

Create a new skill `create-security-agent` that investigates the project, asks about security requirements, compliance needs, and threat model, inventories available security-related skills/plugins, and generates a professional Security Engineer agent prompt.

## Acceptance Criteria

- [ ] `skills/create-security-agent/SKILL.md` exists with full prompt
- [ ] Skill inventories existing security skills/plugins (SAST, DAST, dependency scanners, MCP tools)
- [ ] Skill asks about: compliance standards, threat model, security testing, incident response
- [ ] Generated agent prompt covers: security review, vulnerability assessment, compliance, secure coding
- [ ] Skill registered in `install.py`
- [ ] README updated

## Unknowns & Risks

| Unknown / Risk | Impact | Mitigation |
|----------------|--------|------------|
| Compliance requirements vary by industry | medium | Ask about industry and compliance standards |
| Security tooling landscape is broad | low | Include tool detection in skill phases |

## Implementation Plan

## Step 1: Create skill directory and SKILL.md

**Files**: `skills/create-security-agent/SKILL.md`
**Depends on**: none
**Estimated complexity**: medium
**Reversible**: yes

### What
Create skill with phases for security stack discovery, requirements gathering, and agent prompt generation.

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
