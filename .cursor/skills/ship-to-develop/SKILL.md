---
name: ship-to-develop
description: >-
  Create a temporary branch, commit all changes, open a PR into develop,
  merge it, then delete the temporary branch. Use when the user asks to
  ship/land work to develop, run /ship-to-develop, or
  branch → commit → PR → merge develop → delete branch.
---

# Ship to Develop

Run this end-to-end ship flow. If `.cursor/commands/ship-to-develop.prompt.md` (or this agent’s mirrored `commands/` / `.agents/workflows/` copy) exists, **read and follow that file**. Otherwise use the steps below.

## Flow

1. **Preconditions** — `git fetch`; ensure `develop` exists (ask before creating it from the default branch).
2. **Branch** — create `ship/<short-slug>` (or use a user-provided name) with the work to ship.
3. **Commit all** — stage intended changes (exclude secrets); commit with HEREDOC; match recent log style; no empty commits; no `--no-verify` unless asked; amend only under the usual safety rules.
4. **PR** — `git push -u origin HEAD`, then `gh pr create --base develop` with summary + test plan covering **all** commits on the branch.
5. **Merge** — `gh pr merge <n> --merge --delete-branch` (or squash/rebase if user asked). If blocked, stop and report the PR URL.
6. **Cleanup** — checkout `develop`, pull, delete local temp branch if still present.
7. **Report** — PR URL, branch name (deleted), confirm on up-to-date `develop`.

## Safety

- Never update git config; never interactive git (`-i`); never force-push `main` / `master` / `develop`.
- Do not commit `.env` / credentials / private keys.
- “Delete that new PR” means: merge into `develop` and delete the temporary head branch (remote + local).
