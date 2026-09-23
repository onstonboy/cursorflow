---
name: ship-to-main
description: >-
  Create a temporary branch, commit all changes, open a PR into main,
  merge it, then delete the temporary branch. Use when the user asks to
  ship/land work to main, run /ship-to-main, or
  branch → commit → PR → merge main → delete branch.
---

# Ship to Main

Run this end-to-end ship flow. If `.cursor/commands/ship-to-main.prompt.md` (or this agent’s mirrored `commands/` / `.agents/workflows/` copy) exists, **read and follow that file**. Otherwise use the steps below.

Resolve base as `main`, or `master` if `main` is missing and `master` is the default. Call that branch `BASE` below.

## Flow

1. **Preconditions** — `git fetch`; ensure `BASE` exists (ask if neither `main` nor `master` exists).
2. **Branch** — create `ship/<short-slug>` (or use a user-provided name) with the work to ship.
3. **Commit all** — stage intended changes (exclude secrets); commit with HEREDOC; match recent log style; no empty commits; no `--no-verify` unless asked; amend only under the usual safety rules.
4. **PR** — `git push -u origin HEAD`, then `gh pr create --base BASE` with summary + test plan covering **all** commits on the branch.
5. **Merge** — `gh pr merge <n> --merge --delete-branch` (or squash/rebase if user asked). If blocked, stop and report the PR URL.
6. **Cleanup** — checkout `BASE`, pull, delete local temp branch if still present.
7. **Report** — PR URL, branch name (deleted), confirm on up-to-date `BASE`.

## Safety

- Never update git config; never interactive git (`-i`); never force-push `main` / `master` / `develop`.
- Do not commit `.env` / credentials / private keys.
- “Delete that new PR” means: merge into `BASE` and delete the temporary head branch (remote + local).
