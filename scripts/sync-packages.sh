#!/usr/bin/env bash
# Sync all CursorFlow packages from .cursor (source of truth) to other agents.
#
# Targets:
#   .agents/  — Codex + Antigravity (commands → workflows)
#   .claude/  — Claude Code
#
# Usage:
#   ./scripts/sync-packages.sh
#   ./scripts/sync-packages.sh --dry-run
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${ROOT}/.cursor"
DRY_RUN=0

if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=1
fi

if [[ ! -d "${SRC}" ]]; then
  echo "error: missing source: ${SRC}" >&2
  exit 1
fi

# Rewrite Cursor paths to a target agent root + optional commands folder rename.
# Args: input_file output_file agent_root commands_dir_name
rewrite_file() {
  local src_file="$1"
  local dest_file="$2"
  local agent_root="$3"       # e.g. .agents or .claude
  local commands_name="$4"    # e.g. workflows or commands

  python3 - "$src_file" "$dest_file" "$agent_root" "$commands_name" <<'PY'
import pathlib, sys

src_path, dest_path, agent_root, commands_name = sys.argv[1:5]
text = pathlib.Path(src_path).read_text(encoding="utf-8")

# Longest / most specific replacements first
replacements = [
    (".cursor/commands", f"{agent_root}/{commands_name}"),
    (".cursor/uiux_reference", f"{agent_root}/uiux_reference"),
    (".cursor/skills", f"{agent_root}/skills"),
    (".cursor/rules", f"{agent_root}/rules"),
    (".cursor/docs", f"{agent_root}/docs"),
    (".cursorrules", ".agentsrules" if agent_root == ".agents" else "CLAUDE.md"),
    ("@.cursor/", f"@{agent_root}/"),
    (".cursor/", f"{agent_root}/"),
]

for old, new in replacements:
    text = text.replace(old, new)

dest = pathlib.Path(dest_path)
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(text, encoding="utf-8")
PY
}

# Copy a package directory, optionally rewriting text file contents.
# Args: relative_src_subdir dest_dir agent_root commands_name rewrite(0|1)
sync_package() {
  local rel="$1"
  local dest="$2"
  local agent_root="$3"
  local commands_name="$4"
  local do_rewrite="$5"
  local src_dir="${SRC}/${rel}"

  if [[ ! -d "${src_dir}" ]]; then
    echo "skip (missing): ${src_dir}"
    return 0
  fi

  if [[ "${DRY_RUN}" -eq 1 ]]; then
    echo "dry-run: ${src_dir} → ${dest} (rewrite=${do_rewrite})"
    return 0
  fi

  rm -rf "${dest}"
  mkdir -p "${dest}"

  # Copy tree; rewrite text files in place when requested
  while IFS= read -r -d '' file; do
    local rel_file="${file#${src_dir}/}"
    local out="${dest}/${rel_file}"
    mkdir -p "$(dirname "${out}")"
    case "${file}" in
      *.md|*.mdc|*.txt|*.prompt.md|*.csv|*.json|*.yml|*.yaml)
        if [[ "${do_rewrite}" -eq 1 ]]; then
          rewrite_file "${file}" "${out}" "${agent_root}" "${commands_name}"
        else
          cp "${file}" "${out}"
        fi
        ;;
      *)
        cp "${file}" "${out}"
        ;;
    esac
  done < <(find "${src_dir}" -type f -print0)

  echo "synced → ${dest}"
}

echo "source of truth: ${SRC}"

# --- Codex / Antigravity (.agents) ---
sync_package "rules"          "${ROOT}/.agents/rules"          ".agents" "workflows" 1
sync_package "commands"       "${ROOT}/.agents/workflows"      ".agents" "workflows" 1
sync_package "skills"         "${ROOT}/.agents/skills"         ".agents" "workflows" 1
sync_package "uiux_reference" "${ROOT}/.agents/uiux_reference" ".agents" "workflows" 1
# Docs describe all agents — copy verbatim (no path rewrite)
sync_package "docs"           "${ROOT}/.agents/docs"           ".agents" "workflows" 0

# --- Claude Code (.claude) ---
sync_package "rules"          "${ROOT}/.claude/rules"          ".claude" "commands" 1
sync_package "commands"       "${ROOT}/.claude/commands"       ".claude" "commands" 1
sync_package "skills"         "${ROOT}/.claude/skills"         ".claude" "commands" 1
sync_package "uiux_reference" "${ROOT}/.claude/uiux_reference" ".claude" "commands" 1
sync_package "docs"           "${ROOT}/.claude/docs"           ".claude" "commands" 0

# Keep old skills-only script name working via note
if [[ "${DRY_RUN}" -eq 0 ]]; then
  echo "done. edit under .cursor/, then re-run this script."
fi
