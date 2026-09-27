---
name: motion-graphics-promo
description: >-
  Generate cinematic, extremely kinetic motion-graphics promo videos for an app
  or product (Remotion + procedural audio, 15–60s, 16:9 + 9:16). Ships a
  ready-to-paste master prompt with a 100-style library, style auto-selection
  (pick best fit from the product/URL when the user doesn't choose), word-sync
  lyric mode, and a full research→script→animate→audio→render→QA workflow.
  Use when the user asks for a "motion graphics video", cinematic promo/trailer,
  a video "like this reference", wants a style picked automatically, or wants
  separate videos per product. Complementary to `app-promo-video` (which focuses
  on VO-driven story promos); this skill is the pure motion-graphics / beat-synced
  route.
---

# Motion Graphics Promo — cinematic style master prompt

Wraps `prompts/motion_graphics_master_prompt.md` (from the `promo_videos` repo)
as a reusable skill. The master prompt is the deliverable: fill its variables
block and paste everything below the line into any capable agent — it drives
research → direction → beat sheet → animation → procedural audio → Remotion
render → QA loop, all beat-locked.

## Contents

- `master_prompt.md` — the full paste-ready prompt (input variables, motion
  rules, 7-phase workflow, ~50 technique library, 100-style library, style
  auto-selection, audio spec, QA gates, worked example).
- `STYLES.md` — quick index of all 100 styles for skimming/overrides.

## When to use

- "make a promo/motion-graphics video for <product>" — with or without a style.
- A reference video/clip is provided → set `REFERENCE_VIDEO`; the agent
  self-analyzes frames and adopts that grammar (proven on the "lab instrument /
  kinetic lyric" style).
- "Generate videos for all my products, each different" → auto-selection +
  `USED_STYLES` uniqueness rule gives each product a contrasting style.

## How to use

1. Copy `master_prompt.md`, fill the `{{VARIABLES}}` block:
   `PRODUCT_NAME`, `PRODUCT_URL`, `DURATION_SECONDS`, `ASPECT_RATIOS`,
   `STYLE_DIRECTION` (`S## <name>`, free text, or leave `auto`).
2. Paste everything below the line into the target agent.
3. `STYLE_DIRECTION = auto` → the agent runs §4.6: fingerprints the product
   (category / voice / palette / core action / emotion), shortlists 3 styles
   from the mapping table, passes 4 gates (hook, readability, palette, casting),
   and documents the pick + 2 runners-up in `direction.md`. In batches it keeps
   `USED_STYLES` and never repeats a style.

## Requirements on the target agent

- Shell + Node.js (Remotion) + ffmpeg/ffprobe + Python with numpy.
- Web access to research `PRODUCT_URL` and pull real screenshots.

## Field notes (proven on promo_videos repo)

- Screenshots from store pages often ship with baked-in device chrome —
  wrapping them in a `Phone` bezel makes a phone-in-phone. Either crop the
  screen out, or swap to a thin rim matching the screenshot's own aspect.
- Keep one cue/timing JSON as the single source of truth — scenes AND the
  procedural audio generator both read it, so SFX land on animation beats.
- This machine (and most laptops) can't parallel-render Remotion — render
  sequentially. QA stills across the timeline before final renders.
- Audio target: ≈ −14 LUFS integrated, peak ≈ −0.8 dB, h264 + AAC, CRF 18.
- 60s structure that works: hook → drop ~5.5s → proof → feature chapters →
  build → second drop ~47s → lockup; keep real screenshots to ~10% of runtime,
  the rest pure animation.

## Files

- `master_prompt.md` — paste-ready master prompt (source of truth:
  `promo_videos/prompts/motion_graphics_master_prompt.md`).
- `STYLES.md` — 100-style index (auto-extractable via `grep '^**S'`).
