# Task: Create Cloud Architect Agent Generator Skill

**Date**: 2026-06-06
**Status**: Complete
**Branch**: feat/create-cloud-agent-skill
**Estimated total complexity**: medium

## Objective

Create a new skill `create-cloud-agent` that investigates the project, asks about cloud provider, infrastructure requirements, and cost constraints, inventories available cloud-related skills/plugins, and generates a professional Cloud Architect agent prompt.

## Acceptance Criteria

- [ ] `skills/create-cloud-agent/SKILL.md` exists with full prompt
- [ ] Skill inventories existing cloud/infra skills/plugins (Terraform, Pulumi, k8s, MCP servers)
- [ ] Skill asks about: cloud provider, services needed, scaling requirements, budget, compliance
- [ ] Generated agent prompt covers: architecture design, cost optimization, security, reliability, IaC
- [ ] Skill registered in `install.py`
- [ ] README updated

## Unknowns & Risks

| Unknown / Risk | Impact | Mitigation |
|----------------|--------|------------|
| Multi-cloud vs single-cloud preference | medium | Ask user preference |
| Cost constraints vary | low | Include budget questions in skill |

## Implementation Plan

## Step 1: Create skill directory and SKILL.md

**Files**: `skills/create-cloud-agent/SKILL.md`
**Depends on**: none
**Estimated complexity**: medium
**Reversible**: yes

### What
Create skill with phases for cloud infrastructure discovery, requirements gathering, and agent prompt generation.

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
