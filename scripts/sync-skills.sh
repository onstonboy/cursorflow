#!/usr/bin/env bash
# Deprecated alias — use sync-packages.sh (skills + rules + commands + uiux + docs).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec "${ROOT}/scripts/sync-packages.sh" "$@"
