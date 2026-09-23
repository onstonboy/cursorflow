---
agent: agent
---

# Ship to Develop

**AI Role:** Run the full local → develop ship flow in one pass: create a branch, commit all changes, open a PR into `develop`, merge that PR, then delete the temporary branch (PR head).

Use when the user asks to ship, land, or push work to `develop` via this command (`/ship-to-develop` or equivalent).

---

## CRITICAL: Execution Rules

**⚠️ AI MUST FOLLOW THESE RULES:**

1. Execute **all** steps in order. Do not stop after commit or PR creation unless a step fails.
2. **Base branch is `develop`** unless the user names a different target.
3. Use `gh` for all GitHub PR operations. Use git for branch/commit/push/cleanup.
4. **Never** update git config. **Never** use interactive git flags (`-i`). **Never** skip hooks (`--no-verify`, etc.) unless the user explicitly asks.
5. **Never** force-push to `main` / `master` / `develop`. Warn and stop if that would be required.
6. Do **not** commit secrets (`.env`, credentials, private keys). Warn and exclude them.
7. If there is nothing to commit and no unpushed commits worth shipping, stop and say so — do not create an empty commit or empty PR.
8. After a successful merge, **delete the temporary feature branch** (remote + local) and leave the user on an up-to-date `develop`.
9. Return the PR URL when done (even though the PR will be merged/closed).

---

## Defaults

| Setting | Default |
|---------|---------|
| Target / base branch | `develop` |
| Temporary branch prefix | `ship/` |
| Merge strategy | `gh pr merge --merge --delete-branch` |
| Push | `git push -u origin HEAD` |

Optional user overrides (apply if stated in the invoking message):

- Branch name
- Commit message
- PR title / body
- Base branch (if not `develop`)
- Merge method: `--merge` (default), `--squash`, or `--rebase`

---

## Workflow

### Step 0: Preconditions

Run in parallel:

```bash
git status
git branch -a
git remote -v
git rev-parse --abbrev-ref HEAD
```

Then ensure `develop` exists locally or remotes:

```bash
git fetch origin
git show-ref --verify --quiet refs/heads/develop \
  || git show-ref --verify --quiet refs/remotes/origin/develop
```

**If `develop` is missing:**

1. Tell the user `develop` does not exist.
2. Ask whether to create `develop` from `main`/`master` (or the default branch) and continue, or abort.
3. Do **not** invent a different base without confirmation.

**Working tree:**

- If already on a dedicated ship/feature branch the user wants to keep, reuse it (skip Step 1 create).
- Otherwise proceed to create a new temporary branch.

---

### Step 1: Create temporary branch

If not already on a suitable branch:

```bash
git checkout develop
git pull origin develop
git checkout -b ship/<short-slug>
```

**Branch name rules:**

- Prefer user-provided name.
- Else derive a short slug from the change summary (kebab-case), e.g. `ship/update-sync-script`.
- Keep it unique; if the name exists, append a short suffix (e.g. `-2` or a date).

If the user is mid-feature on another branch with the changes already there, **do not** reset — create the ship branch from current HEAD (or rename only if the user asked). Prefer:

```bash
git checkout -b ship/<short-slug>
```

from the current commit when that preserves uncommitted / current work.

---

### Step 2: Commit all relevant changes

Follow the repo commit protocol:

1. In parallel:

```bash
git status
git diff
git diff --staged
git log -5 --oneline
```

2. Stage relevant files (all intended work; exclude secrets):

```bash
git add -A
# then unstage any secret/credential files if present
```

3. Draft a concise 1–2 sentence commit message focused on **why**, matching recent `git log` style.

4. Commit via HEREDOC:

```bash
git commit -m "$(cat <<'EOF'
Commit message here.

EOF
)"
```

5. If the commit fails due to a pre-commit hook:

- Fix the issue.
- Create a **new** commit (do not amend unless the user explicitly asked **and** amend safety rules below are all met).

**Amend only when all are true:**

- User explicitly requested amend, **or** the commit succeeded but a hook auto-modified files that must be included.
- HEAD commit was created by you in this conversation.
- Commit has **not** been pushed to remote.

6. Re-run `git status` and confirm a clean (or intentionally residual) tree before continuing.

**If nothing to commit:** skip this step only when there are already commits on the branch that are not in `develop`; otherwise stop.

---

### Step 3: Push and create PR into `develop`

1. Push:

```bash
git push -u origin HEAD
```

2. Create the PR with `gh`, base = `develop`:

```bash
gh pr create --base develop --title "the pr title" --body "$(cat <<'EOF'
## Summary
<1-3 bullet points>

## Test plan
- [ ] <checklist>

EOF
)"
```

3. Capture and keep the PR URL / number for later steps.

Analyze **all** commits that will be included (`git log develop...HEAD` / `git diff develop...HEAD`) — not only the latest commit — when writing the summary.

---

### Step 4: Merge PR into `develop`

Merge immediately (this flow is ship-and-land, not review-wait):

```bash
gh pr merge <PR_NUMBER> --merge --delete-branch
```

Use `--squash` or `--rebase` only if the user requested that method.

If merge is blocked (reviews, CI, conflicts):

1. Report the blocker clearly.
2. Do **not** bypass required checks unless the user explicitly asks and `gh` allows it for that repo.
3. Stop; leave the PR open and report the URL.

---

### Step 5: Delete temporary branch / clean up

`gh pr merge --delete-branch` removes the **remote** head branch. Finish local cleanup:

```bash
git checkout develop
git pull origin develop
git branch -d ship/<short-slug> 2>/dev/null || true
# if still present only remotely somehow:
git push origin --delete ship/<short-slug> 2>/dev/null || true
git status
git log -3 --oneline
```

**Meaning of “delete that new PR” in this command:** the temporary PR is **merged into `develop`**, its **head branch is deleted**, and local leftovers of that ship branch are removed. Do not leave the temporary branch checked out.

---

### Step 6: Report

Return a short completion report:

- Temporary branch name (deleted)
- Commit subject(s)
- PR URL (merged)
- Confirm current branch is `develop` and includes the merge
- Any files skipped (e.g. secrets) or blockers

---

## Failure handling

| Failure | Action |
|---------|--------|
| No `develop` | Ask before creating from default branch |
| Nothing to ship | Stop; no empty commit/PR |
| Secrets in staging | Unstage, warn, continue without them if remaining changes exist |
| Push rejected | Fix/rebase onto latest `develop` only with user-safe non-destructive steps; never force-push protected bases |
| PR create fails | Fix auth/remote issue; do not claim success |
| Merge blocked | Leave PR open; report URL + blocker |
| Hook failed commit | Fix → **new** commit (no casual amend) |

---

## Definition of Done

- [ ] Temporary branch created (or explicitly reused)
- [ ] All intended changes committed (no secrets)
- [ ] PR opened against `develop`
- [ ] PR merged into `develop`
- [ ] Remote temporary branch deleted
- [ ] Local temporary branch deleted (if present)
- [ ] Working tree on up-to-date `develop`
- [ ] PR URL reported to the user
