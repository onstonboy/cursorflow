# Style 12 — Chalkboard

Classroom nostalgia. Dark green slate, chalk handwriting, dust motes, diagrams sketched in white — learning made warm.

Best for: education, language learning, STEM, kids' learning, course platforms.

## Tokens

```ts
board "#2D4A3E" (deep slate green) — texture: subtle noise + faint erased-chalk smudges (low-opacity white blurs)
chalk "#F2EFE4"  accents: chalk-yellow "#F0D97C", chalk-pink "#EFA9B8", chalk-blue "#A9C9E8"
Font: handwriting (Caveat/Kalam) for everything written; mono never appears.
FPS 30.
```

Motion grammar: chalk-write — strokes draw on via dashoffset (same mechanism as Doodle) BUT with chalk texture: `stroke-linecap:round` + rough edges (overlay noise-masked stroke or slight per-frame width jitter); letters appear character-by-character with ±4° rotate; dust puffs on "erasing" transitions.

## Core mechanism

```tsx
// Chalk stroke: draw-on path + graininess via a second dashed overlay:
<path stroke={chalk} strokeWidth={7} strokeDasharray={`${L}`} strokeDashoffset={L*(1-t)}
  filter="url(#chalkRough)"/>   // feTurbulence displacement ~1.5 for crumbly edge
// Eraser transition: a rounded-rect "eraser" div travels across, leaving
// a half-opacity smear region; drawn content fades with blur 0→3 + dust particles.
// Dust: 40 small white dots drifting down (seeded positions), opacity twinkle.
// Screenshots: pasted INTO the board like paper on a board — slight rotate,
//   white "tape" corners, then chalk annotations point at it.
```

## Scene grammar (7–8 scenes, 90–120s)

S01: lesson title chalks itself + underlined twice · S02: problem as a "?" diagram · S03–S06: today's "lesson" — screenshot taped to board, chalk arrows + annotations circling features, a stick-figure celebrating · S07: "Quiz!" playful recap card · S08: "Class dismissed → Tải app" + bell.

Transitions: eraser wipe (with dust puff).

## Audio

- Music: gentle piano+clarinet feel — numpy: soft sine-triad melody 75 BPM, no drums except a soft brush-swish (lowpassed noise) on beats 2/4.
- SFX: chalk scratch (filtered noise bursts, 200–400ms, bandpass ~3kHz — keep QUIET), board tap, school bell at end.
- VO: friendly teacher/older-sibling energy, clear enunciation, patient pace (-2%).

## Signature details

Chalk texture displacement on strokes · dust motes always falling · tape-cornered screenshots · underlined-emphasis chalk strokes · "today's lesson" framing per feature.

Anti-patterns: neon, mono fonts, dark-mode navy (this board is GREEN), sharp digital edges, fast cuts.
