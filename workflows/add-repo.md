# ADD REPO — Add a New Repository to an Existing Workspace

## RULE: The workspace must already be bootstrapped (`workflows/init.md` complete). No code changes. Documentation only.

Use this when adding a new child repo to a workspace that already has a root `md_docs/` and `WORKSPACE_OVERVIEW.md`.

---

## Phase 1 — Verify Workspace State

### 1.1 Confirm workspace is bootstrapped
```bash
ls md_docs/
cat md_docs/README.md
```

If `md_docs/` does not exist or `WORKSPACE_OVERVIEW.md` is missing: stop and run `workflows/init.md` first.

### 1.2 Identify the new repo
```bash
find . -maxdepth 2 -name ".git" -type d | sed 's|/.git||' | sort
```

Confirm the new repo's path. Check it does not already appear in `md_docs/README.md`.

### 1.3 Check for existing documentation in the new repo
```bash
find [new-repo-path] -name "md_docs" -type d
find [new-repo-path] -name "*.md" -maxdepth 2 | sort
```

---

## Phase 2 — Explore the New Repo

Work from inside the new repo directory for this phase.

### 2.1 Directory structure
```bash
find . -not -path '*/node_modules/*' -not -path '*/.git/*' \
       -not -path '*/__pycache__/*' -not -path '*/.venv/*' \
       -not -path '*/dist/*' -not -path '*/build/*' \
       | sort | head -120
```

### 2.2 Root configuration files
Read every config file present:
- package.json / package-lock.json / yarn.lock / pnpm-lock.yaml
- pyproject.toml / setup.py / requirements*.txt / Pipfile
- dbt_project.yml / profiles.yml
- Cargo.toml / go.mod / build.gradle / pom.xml
- tsconfig.json / .eslintrc* / .prettierrc* / ruff.toml / .flake8
- docker-compose*.yml / Dockerfile*
- .env.example / .env.template (NEVER .env itself)
- Makefile / justfile / taskfile.yml

### 2.3 Git history
```bash
git log --oneline -30
git branch -a
git remote -v
```

### 2.4 CI/CD pipelines
Read every file in:
- .github/workflows/
- .gitlab-ci.yml / cloudbuild.yaml / .circleci/config.yml / bitbucket-pipelines.yml

### 2.5 Existing documentation
```bash
find . -name "*.md" -not -path '*/node_modules/*' | sort
```
Read every .md file found.

### 2.6 Test suite
```bash
find . \( -name "test_*.py" -o -name "*_test.py" -o -name "*.test.ts" \
          -o -name "*.spec.ts" -o -name "*.test.tsx" -o -name "jest.config*" \
          -o -name "pytest.ini" -o -name "vitest.config*" \) \
     -not -path '*/node_modules/*' | sort | head -40
```

### 2.7 Entry points & main modules
Identify and read:
- Main app entry (main.py / app.py / index.ts / server.ts / main.rs / cmd/)
- Router definitions
- Core models / schemas / types
- Database migrations directory

### 2.8 Infrastructure & cloud
Read any IaC files: terraform/ / pulumi/ / cdk/ / serverless.yml / kubernetes/ / k8s/

---

## Phase 3 — Create Per-Repo md_docs/

Inside the new repo, create:
```
[new-repo]/md_docs/
├── README.md
├── AGENT_CONTEXT.md
├── AGENT_SYSTEM_PROMPT.md
├── PROJECT_OVERVIEW.md
├── architecture/
│   ├── data_flow.md
│   ├── key_patterns.md
│   ├── module_map.md
│   └── infrastructure.md
└── tasks/
```

### AGENT_CONTEXT.md
Must include ALL sections:

```markdown
# Agent Context — [repo name]

## Tech Stack
## Architecture
## Directory Structure (annotated)
## Entry Points
## Data Flow
## Key Modules & Their Responsibilities
## Core Design Patterns & Conventions
## Configuration & Environment
## Database & Schema
## External Integrations & APIs
## Testing Strategy
## CI/CD Pipeline
## Known Constraints & Gotchas
## Workspace Relationships
[How this repo connects to others in the workspace: API calls, shared DB, events, packages]
```

### AGENT_SYSTEM_PROMPT.md
Ready-to-paste system prompt:
- Project in 2–3 sentences
- Tech stack
- Primary workflow: `read projects/continue.md → read AGENT_CONTEXT.md → check tasks/`
- Top 3–5 conventions to follow strictly
- What NOT to do
- Reference to workspace: `"This repo is part of workspace [name]. Cross-repo context: ../../md_docs/WORKSPACE_OVERVIEW.md"`

### PROJECT_OVERVIEW.md
1-page: what it does, who uses it, key architectural decisions, current state, next priorities.

### architecture/data_flow.md
Full lifecycle of a request from entry to exit.

### architecture/key_patterns.md
Naming, module boundary rules, error propagation, logging, how to add features, anti-patterns.

### architecture/module_map.md
ASCII or mermaid map of main modules and dependencies.

### architecture/infrastructure.md
Cloud services, env vars (name + purpose + example — no real secrets), container setup, local run, deploy.

### Update repo README.md
Add:
```markdown
## Agent Documentation

This repo is part of the **[workspace name]** workspace.
See [`md_docs/README.md`](md_docs/README.md) for the full agent documentation index.
For cross-repo context: [`../../md_docs/WORKSPACE_OVERVIEW.md`](../../md_docs/WORKSPACE_OVERVIEW.md)
```

---

## Phase 4 — Update Root md_docs/

### 4.1 Update md_docs/README.md
Add the new repo to the repo table:
```markdown
| [repo name] | ./[path] | [one-line purpose] | [path/md_docs/README.md] |
```

### 4.2 Update md_docs/WORKSPACE_OVERVIEW.md
- Add the new repo to the **Repos** table.
- Document any cross-repo relationships discovered (API contracts, shared DB, events, shared packages).
- Update **Shared Infrastructure** if the new repo shares infra with existing repos.
- Update **Known Cross-repo Constraints & Gotchas** if applicable.

---

## Completion Checklist

- [ ] New repo fully explored (all Phase 2 steps complete).
- [ ] Per-repo `md_docs/` created with all required files.
- [ ] `AGENT_CONTEXT.md` has all sections populated (no placeholder text).
- [ ] `AGENT_SYSTEM_PROMPT.md` is ready to paste.
- [ ] Repo's `README.md` references its `md_docs/` and the root `md_docs/`.
- [ ] Root `md_docs/README.md` repo table updated.
- [ ] `WORKSPACE_OVERVIEW.md` updated with new repo and any cross-repo relationships.
- [ ] All documentation written in English.
- [ ] No secrets or .env values written to any file.

---

## Rules
- Per-repo `md_docs/` must be fully self-contained. Agent working on this repo must not need to read other repos.
- Document what exists, not what should exist.
- If a section has no content, write: "None currently. [Reason if known]."
- Never skip a Phase 2 step because the repo "looks simple."
- If MCP tools are available (GitHub, Linear, Jira): check for existing issues and reference them.
