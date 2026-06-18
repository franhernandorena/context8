---
name: tag-create
version: 1.0.0
description: Creates git tags based on changes since the last tag. Reads conventions from .context8/repo-branches.md, analyzes commits, suggests the next version number (semver), and asks for confirmation before creating.
---

# Tag Create — Git Tag Creation

## Overview

Reads the repository conventions from `.context8/repo-branches.md` (created
by `repo-cleanup`), analyzes changes since the last tag, classifies the type
of changes (fix, feature, breaking), suggests the next version number, and
asks for confirmation before creating the tag with a descriptive message.

## When to use

- After merging significant changes
- Before a release
- When you want to mark a point in history with a semver tag

## Output

- Tag created in the local repository
- `.context8/repo-branches.md` updated with the new tag
- Tag push if the user authorizes it

## Full Prompt

# TAG CREATE — Create Git Tag

---

## Phase 1 — Load Repository Conventions

### 1.1 Read existing tags

```bash
git tag --sort=-creatordate | head -20
```

### 1.2 Read `.context8/repo-branches.md`

```bash
cat .context8/repo-branches.md 2>/dev/null || echo "Does not exist — will be created at the end"
```

Extract: tag format used historically (v0.0.0, v0-0-0, etc.),
and latest documented versions.

### 1.3 Latest tag

```bash
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "no-tag")
echo "Latest tag: $LAST_TAG"
```

---

## Phase 2 — Analyze Changes Since the Last Tag

### 2.1 Change log

```bash
if [ "$LAST_TAG" != "no-tag" ]; then
  git log "$LAST_TAG"..HEAD --oneline --no-decorate
else
  git log --oneline --no-decorate | tail -20
fi
```

### 2.2 Classify changes

Read each commit message and classify:

| Type | Indicator | Example | Version bump |
|------|-----------|---------|-------------|
| **Breaking** | `!`, `BREAKING CHANGE`, `feat!:` | `feat!: API change` | Major (X+1.0.0) |
| **Feature** | `feat:`, `feature:`, `feat(` | `feat(auth): login with Google` | Minor (0.X+1.0) |
| **Fix** | `fix:`, `fix(`, `bugfix:`, `hotfix:` | `fix: null pointer in login` | Patch (0.0.X+1) |
| **Docs/Chore** | `docs:`, `chore:`, `refactor:`, `test:` | `docs: update README` | No change |

### 2.3 Generate change summary

```
Commits since v1.0.0 (5 commits):
  ✨ feat: login with Google
  🐛 fix: null pointer in login
  📚 docs: update README
  ✨ feat: logout endpoint
  🔧 chore: clean dependencies

Classification:
  - Breaking:  0
  - Features:  2
  - Fixes:     1
  - Chore/doc: 2
```

---

## Phase 3 — Suggest Next Tag

### 3.1 Calculate suggested version

Apply semver according to classification:

```
REASONING:
  Previous tag: v1.0.0
  Breaking:  0 → no major change
  Features:  2 → bumps minor (+1)
  Fixes:     1 → ignored (minor already bumped)

  Suggested version: v1.1.0
```

### 3.2 Respect historical format

If historical tags use `v0-0-0` (hyphens), suggest `v1-1-0`.
If they use `v0.0.0` (dots), suggest `v1.1.0`.

### 3.3 Show proposal to user

```
═══ Tag Proposal ═══

  Suggested tag:  v1.1.0
  Format:         v<major>.<minor>.<patch> (semver)

  Commits since v1.0.0:
    ✨ feat: login with Google
    🐛 fix: null pointer in login
    📚 docs: update README
    ✨ feat: logout endpoint

  Suggested message:
    v1.1.0 — New Google login, logout endpoint, fix null pointer

Confirm?
  [Enter]      — create tag with suggested name and message
  <name>       — create tag with a different name (type what you want)
  <message>    — create tag with the suggested name but different message
  skip         — cancel
```

---

## Phase 4 — Create Tag

### 4.1 Create local tag

```bash
git tag -a <tag-name> -m "<tag-message>"
```

### 4.2 Verify

```bash
git tag --sort=-creatordate | head -5
git log --oneline <tag-name> -1
```

### 4.3 Ask about push

```
Tag v1.1.0 created locally.
Push to remote?
  [y/N]
```

If the user says yes:

```bash
git push origin <tag-name>
```

---

## Phase 5 — Update `.context8/repo-branches.md`

Add the new tag to the tags table:

```markdown
| v1.1.0 | YYYY-MM-DD | Google login, logout endpoint, fix null pointer |
```

```bash
git add .context8/repo-branches.md
git commit -m "docs(repo-branches): add tag v1.1.0"
```

Only commit if the file exists.

---

## Rules

- Never create a tag without user confirmation.
- The tag message must be descriptive, not generic like "release".
- If there are no previous tags and the format cannot be determined, use dots (v0.1.0).
- If there are no changes since the last tag, report it and suggest nothing.
- Write all documentation in English.
