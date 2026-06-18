---
name: repo-cleanup
version: 1.0.0
description: Reviews local repo branches, automatically cleans up your own merged branches and asks permission before touching others' branches. Keeps .context8/repo-branches.md updated with project conventions.
---

# Repo Cleanup — Safe Git Branch Cleanup

## Overview

Scans repository branches, classifies them by authorship, and cleans up safely:
your own merged branches are deleted automatically with `git branch -d`; other
people's merged branches require explicit permission. Maintains a reference file
(`.context8/repo-branches.md`) with protected branches, tags, and detected
patterns, which other skills (task-do, deploy-plan, release) can consult.

## When to use

- Periodically to keep the local repository clean
- After merging several PRs
- Before starting a new feature (to avoid confusion from stale branches)
- Any git maintenance session

## When NOT to use

- In repositories where you don't have write permissions
- In the middle of an unresolved rebase or merge conflict
- If there are uncommitted changes (stash does not protect against branch -d)

## Output

- Your own merged branches deleted
- `.context8/repo-branches.md` created or updated
- Inline report with summary of actions taken, pending approvals, and unmerged branches

## Full Prompt

# REPO CLEANUP — Safe Branch Cleanup

## Rule: Always use `-d` (safe). `-D` only with explicit user approval.

---

## Phase 1 — Load Repository Conventions

### 1.1 Identify git user

```bash
GIT_USER_NAME=$(git config user.name)
GIT_USER_EMAIL=$(git config user.email)
echo "User: $GIT_USER_NAME <$GIT_USER_EMAIL>"
```

### 1.2 Create or read `.context8/repo-branches.md`

```bash
mkdir -p .context8
```

If the file doesn't exist, create it with the structure below. If it exists,
load it to respect already-documented conventions.

```markdown
# Repo Branches — Branch and Tag Conventions

## Protected Branches
List of branches that are NEVER deleted. Auto-detected.

- `main`
- `develop`
- [add others detected]

## Git User
- **Name**: [git config user.name]
- **Email**: [git config user.email]

## Branch Naming Patterns
Patterns detected in existing branches (for authorship classification).

- `fran/*` — main user's branches

## Tags
| Tag | Date | Purpose |
|-----|------|---------|
| v1.0.0 | 2024-01-01 | First release |

## Cleanup History
| Date | Deleted branches | Pending branches |
|------|------------------|------------------|
| YYYY-MM-DD | N | M |

## Notes
[Additional information about the project's branching flow.]
```

### 1.3 Detect default branch and other protected ones

```bash
# Default branch (main or master)
git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@.*/@@' || echo "main"

# All branches with commits from 2+ people = candidate protected branches
```

### 1.4 List existing tags

```bash
git tag --sort=-creatordate | head -20
```

For each tag, record purpose:
```bash
git log --oneline <tag> -1
```

If the tag is not documented in `.context8/repo-branches.md`, add it.

---

## Phase 2 — List and Classify Branches

### 2.1 Branches merged into each protected branch

```bash
for branch in main develop; do
  echo "=== Merged into $branch ==="
  git branch --merged "$branch" | grep -v "^\*\|^  $branch$" | sed 's/^..//'
done
```

### 2.2 Remote fetch to detect branches already deleted upstream

```bash
git fetch --prune 2>&1 || true
```

### 2.3 Classify by authorship

For each merged branch (excluding protected branches):

- Get unique commit authors of the branch:
  ```bash
  git log origin/main..<branch> --format="%an <%ae>" | sort -u
  ```
  or, if the branch is already fully merged, use `git log` with an appropriate
  range.

- **Own**: all commits are from `$GIT_USER_NAME` / `$GIT_USER_EMAIL`
- **Other**: any commit from someone else
- **Unclear authorship**: treat as other (safer)

---

## Phase 3 — Clean Up Own Merged Branches

### 3.1 For each own branch merged into `main` or `develop`:

```bash
git branch -d <branch>
```

Confirm deletion:
```bash
git branch -a | grep <branch> || echo "Deleted successfully"
```

Notify the user:
`→ Deleted: <branch> (own, merged)`

### 3.2 Error handling

If `git branch -d` fails because the branch is not fully merged:
- Verify manually with `git merge-base --is-ancestor <branch> <protected>`
- If truly not merged: move to "unmerged" list (Phase 5)
- If merged but git doesn't recognize it (complex merge): list as pending

---

## Phase 4 — Other People's Merged Branches (Ask Permission)

### 4.1 Show other people's merged branches

List each other's merged branch with its main author and last commit date:

```bash
git log --format="%an <%ae> — %ci" <branch> -1 | head -1
```

### 4.2 Ask for explicit permission

Present to the user:

```
═══ Other people's merged branches — require approval ═══
  1. feature/xyz  (author: other@dev.com, last commit: 2024-03-01)
  2. fix/abc      (author: other@dev.com, last commit: 2024-02-15)
  3. ...

What do you want to do?
  [number(s)] — delete specific branches (with safe -d)
  all          — delete all (with safe -d)
  force <n>    — delete with -D (force, only if -d fails)
  skip         — delete none, leave as is
  review <n>   — open branch review before deciding
```

Do NOT execute any action without user response.

If the user authorizes:

```bash
git branch -d <branch>
```

If `-d` fails and the user asked for `force`:

```bash
git branch -D <branch>
```

---

## Phase 5 — Unmerged Branches (Informational Only)

### 5.1 List branches not merged into any protected branch

```bash
git branch --no-merged main
git branch --no-merged develop
```

### 5.2 Calculate age

```bash
git log --format="%ci" <branch> -1
```

### 5.3 Display informational summary

```
═══ Unmerged branches (NOT touched) ═══
  - fix/wip          (last commit: 2024-06-10 — 7 days ago)
  - experiment/foo   (last commit: 2024-03-01 — 108 days ago)
```

Do not offer to delete them. Inform only. If the user asks about a specific one,
then discuss.

---

## Phase 6 — Update `.context8/repo-branches.md`

### 6.1 Update protected branches

If new protected branches were discovered during execution, add them to the file.

### 6.2 Add newly detected tags

Any tag that was not documented in Phase 1, add it with its purpose inferred from
the commit message.

### 6.3 Record cleanup history

Add a row to the **Cleanup History** table:

```
| YYYY-MM-DD | N own deleted, N other pending | N |
```

### 6.4 Commit the updated file

```bash
git add .context8/repo-branches.md
git commit -m "docs(repo-branches): update after branch cleanup"
```

---

## Completion Checklist

- [ ] `.context8/repo-branches.md` exists with protected branches, tags, and user identity
- [ ] Own merged branches deleted with `-d`
- [ ] Other people's merged branches: user asked (approved or deferred)
- [ ] Unmerged branches listed informatively
- [ ] Cleanup history updated
- [ ] No `-D` used without explicit authorization
- [ ] Protected branches left intact

---

## Rules

- **Always** `git branch -d` (safe). `-D` only with explicit user permission.
- **Never** delete protected branches (main, develop, and documented ones).
- **Never** delete other people's branches without asking.
- **Always** notify the user of actions taken.
- **Never** touch unmerged branches — only report their existence.
- If the user says "skip" in Phase 4, leave all other people's branches as they are.
- Write all documentation in English.
