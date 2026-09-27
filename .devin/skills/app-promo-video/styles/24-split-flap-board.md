# Style 24 — Split-Flap Departure Board

Airport-board nostalgia at word scale. Whole lines cascade-flip into place, character by character — every message feels "announced".

Best for: travel, transit, events, itinerary/booking apps, countdown-adjacent promos (companion to #06 but full-video).

## Tokens

```ts
bg "#14161A"  cell "#1E2126"  char "#E8E4D8"  accent: brand color on status cells
Font: condensed mono/sans per cell — all cells same width (tabular discipline).
FPS 30.
```

Motion grammar: character cascade — each glyph spins through a few faces before settling (digit flaps 2–3 quick flips over 8 frames; letter flips show 2–3 random chars then the real one). Cells settle left→right with 1-frame offset per cell → rolling clack wave.

## Core mechanism

```tsx
const FlapChar: React.FC<{ch:string; at:number}> = ({ch,at}) => {
  const f = useF();
  // spin phase: cycles through GLYPHS pool for 6 frames, then locks to ch
  const pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  const spinning = f >= at && f < at+8;
  const shown = spinning ? pool[(f*3+at)%pool.length] : ch;
  const rot = spinning ? -70 : interpolate(f,[at+7,at+10],[-70,0],{clamp});
  // render char in cell with hinge line at 50% + slight rotateX during spin
};
// A ROW = word array of FlapChar, at_i = base + i*1. Row clack = audio SFX
//   noise burst ~120ms rolled at same cadence.
// Status cells: colored cell blocks ("ON TIME" green) flip identically.
// Board chrome: header row ("DEPARTURES"), thin rules, row divider lines.
```

## Scene grammar (7–9 scenes, 80–110s)

S01: empty board → rows cascade filling "MORSEY — DEPARTING NOW" style title · S02: "DELAYED" stamp on the problem row (red status cell) · S03–S07: feature rows as departures — "FEATURE …… PLATFORM 3 …… BOARDING" with status flips to green; screenshot arrives framed as an ad panel ON the board wall · S08: all rows collapse→ final line "TẢI NGAY — GATE CLOSING" + store cells.

Transitions: whole board blur-flips (all cells spin once, show new content).

## Audio

- Music: upbeat lounge/bossa 105–115 BPM — numpy: brushed kit, walking bass, muted guitar chords (short sine-pluck stabs).
- SFX: THE clack cascade — rolled noise bursts matched per-cell (essential; flap without clack is dead), PA-ding before announcements.
- VO: optional PA-style announcer (bandpass EQ 500–3000 + reverb = tannoy) reading departures — "Now boarding: tính năng mới."

## Signature details

Per-cell cascade timing · hinge line detail · status cells flipping red→green · whole-board re-flip transitions · PA-VO processing.

Anti-patterns: non-uniform cell widths, smooth fades instead of flips, missing clack SFX, modern UI fragments inside cells (board is text-only; screenshots live in wall panels).
