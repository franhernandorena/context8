# Task: Create DevOps/SRE Agent Generator Skill

**Date**: 2026-06-06
**Status**: Complete
**Branch**: feat/create-devops-agent-skill
**Estimated total complexity**: medium

## Objective

Create a new skill `create-devops-agent` that investigates the project, asks about CI/CD, infrastructure, monitoring, and incident response, inventories available DevOps-related skills/plugins, and generates a professional DevOps/SRE agent prompt.

## Acceptance Criteria

- [ ] `skills/create-devops-agent/SKILL.md` exists with full prompt
- [ ] Skill inventories existing DevOps skills/plugins (CI/CD tools, monitoring, k8s, IaC tools)
- [ ] Skill asks about: CI/CD pipeline, hosting infrastructure, monitoring/alerting, incident response
- [ ] Generated agent prompt covers: pipeline management, infrastructure automation, observability, SLOs
- [ ] Skill registered in `install.py`
- [ ] README updated

## Unknowns & Risks

| Unknown / Risk | Impact | Mitigation |
|----------------|--------|------------|
| DevOps tooling varies hugely | medium | Ask about specific tools in use |
| SRE maturity level varies | low | Include maturity assessment questions |

## Implementation Plan

## Step 1: Create skill directory and SKILL.md

**Files**: `skills/create-devops-agent/SKILL.md`
**Depends on**: none
**Estimated complexity**: medium
**Reversible**: yes

### What
Create skill with phases for DevOps stack discovery, requirements gathering, and agent prompt generation.

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
