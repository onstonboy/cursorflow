#!/usr/bin/env bash
# Sync all CursorFlow packages from .cursor (source of truth) to other agents.
#
# Targets:
#   .agents/     — Codex + Antigravity (commands → workflows)
#   .claude/     — Claude Code
#   .devin/      — Devin CLI
#   .trae/       — Trae
#   .grok/       — Grok (xAI)
#   .opencode/   — OpenCode
#   .qwen/       — Qwen Code
#   .kimi-code/  — Kimi Code CLI
#   .omp/        — Oh My Pi (omp)
#   .pi/         — Pi coding agent
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
  local agent_root="$3"
  local commands_name="$4"

  python3 - "$src_file" "$dest_file" "$agent_root" "$commands_name" <<'PY'
import pathlib, sys

src_path, dest_path, agent_root, commands_name = sys.argv[1:5]
text = pathlib.Path(src_path).read_text(encoding="utf-8")

root_md = {
    ".agents": "AGENTS.md",
    ".claude": "CLAUDE.md",
    ".devin": "AGENTS.md",
    ".trae": "AGENTS.md",
    ".grok": "AGENTS.md",
    ".opencode": "AGENTS.md",
    ".qwen": "QWEN.md",
    ".kimi-code": "AGENTS.md",
    ".omp": "AGENTS.md",
    ".pi": "AGENTS.md",
}.get(agent_root, "AGENTS.md")

replacements = [
    (".cursor/commands", f"{agent_root}/{commands_name}"),
    (".cursor/uiux_reference", f"{agent_root}/uiux_reference"),
    (".cursor/skills", f"{agent_root}/skills"),
    (".cursor/rules", f"{agent_root}/rules"),
    (".cursor/docs", f"{agent_root}/docs"),
    (".cursorrules", root_md),
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

# Sync the standard package set for one agent root.
# Args: agent_root commands_dir_name [packages...]
# packages default: rules commands skills uiux_reference docs
# Special: pass "commands:workflows" style already handled via commands_dir_name
sync_agent() {
  local agent_root="$1"
  local commands_name="$2"
  shift 2
  local packages=("$@")
  if [[ ${#packages[@]} -eq 0 ]]; then
    packages=(rules commands skills uiux_reference docs)
  fi

  echo "--- ${agent_root} ---"
  local pkg dest do_rewrite
  for pkg in "${packages[@]}"; do
    do_rewrite=1
    case "${pkg}" in
      docs) do_rewrite=0 ;;
    esac
    if [[ "${pkg}" == "commands" ]]; then
      dest="${ROOT}/${agent_root}/${commands_name}"
    else
      dest="${ROOT}/${agent_root}/${pkg}"
    fi
    sync_package "${pkg}" "${dest}" "${agent_root}" "${commands_name}" "${do_rewrite}"
  done
}

echo "source of truth: ${SRC}"

# Codex / Antigravity
sync_agent ".agents" "workflows"

# Claude Code
sync_agent ".claude" "commands"

# Devin — native rules + skills; commands imported from .claude when present
sync_agent ".devin" "commands" rules skills uiux_reference docs

# Trae
sync_agent ".trae" "commands"

# Grok — rules + skills; slash workflows live as skills
sync_agent ".grok" "commands" rules skills uiux_reference docs

# OpenCode
sync_agent ".opencode" "commands"

# Qwen Code
sync_agent ".qwen" "commands"

# Kimi Code — skills are first-class; keep rules/commands/uiux for AGENTS.md pointers
sync_agent ".kimi-code" "commands"

# Oh My Pi (omp)
sync_agent ".omp" "commands"

# Pi coding agent
sync_agent ".pi" "commands" rules skills uiux_reference docs

if [[ "${DRY_RUN}" -eq 0 ]]; then
  # OpenCode: point instructions at mirrored rules (additive; no secrets)
  OPENCODE_JSON="${ROOT}/.opencode/opencode.json"
  if [[ ! -f "${OPENCODE_JSON}" ]]; then
    cat > "${OPENCODE_JSON}" <<'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    ".opencode/rules/**/*.md",
    ".opencode/rules/**/*.mdc"
  ]
}
EOF
    echo "wrote → ${OPENCODE_JSON}"
  fi

  echo "done. edit under .cursor/, then re-run this script."
fi
