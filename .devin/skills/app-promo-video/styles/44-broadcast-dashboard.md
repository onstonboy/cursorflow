# Style 44 — Broadcast Dashboard

Mission-control live board. A multi-panel grid that rearranges itself FLIP-style, live visualizations in every cell, status LEDs pulsing.

Best for: analytics, monitoring, trading, sports-data, ops/devops tools.

## Tokens

```ts
bg "#0A0F1A"  panel "#111827"  line "#1E2A3A"
green "#22C55E"  amber "#F59E0B"  red "#EF4444"  data "#38BDF8"
Font: mono for all values (tabular), condensed sans for panel titles.
FPS 30.
```

Motion grammar: rearrangement — panels slide to new grid positions when layout changes (animate left/top via measured FLIP); values tick/refresh on staggered intervals; LEDs pulse 12-frame cycles; chart lines scroll (translateX loop).

## Core mechanism

```tsx
// FLIP rearrange: panels have slot positions list per "mode"; on mode change
//   each panel interpolates left/top/w/h over 24 frames easeInOut —
//   satisfying layout-shuffle (the signature move).
// Live values: const v = base + Math.sin(f/17+seed)*amp + tick updates;
//   round + tabular mono; occasionally a cell flashes on update (bg
//   brightness spike 4 frames).
// Sparkline strips: tiny SVG polylines with translateX scroll inside cells.
// LED dot: borderRadius 50%, boxShadow color-glow, opacity sine-pulse.
// Screenshots: one panel IS the app — expands from a cell to a hero panel
//   (FLIP to 2×2 slot) while others compress — hierarchy shift as reveal.
// Status feed: bottom strip logging events ("sync ok", "alert resolved").
```

## Scene grammar (7–9 scenes, 90–120s)

S01: board boots — panels flicker on one by one, LEDs stabilize · S02: chaos mode — problem = panels all red/alerting · S03–S06: app engages: board reorganizes around the app panel (FLIP), alerts resolve one by one (red→green), each feature a panel cluster · S07: "ALL SYSTEMS" green state → logo cell expands → CTA.

The board tells the story via STATE — colors, statuses, rearrangement.

## Audio

- Music: pulsing electronic 110 BPM — numpy: sequenced bass 16ths, arp ticks, pad underneath; add urgency shift (key + intensity) during chaos scene.
- SFX: data-tick per value update (quiet), alert ping on red, resolve-chime on green, layout-shift whoosh on FLIPs.
- VO: terse ops-voice or none — the board can narrate itself; if used, clipped mission-control delivery.

## Signature details

FLIP layout rearranges · staggered LED boot · chaos→resolution arc via panel colors · app panel expanding to hero · bottom event-feed strip always running.

Anti-patterns: decorative panels that don't change state, static values, smooth slow motion (ops moves snap), missing the chaos→order arc.
