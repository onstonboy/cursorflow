# Style 09 — Paper Cutout

Handcrafted stop-motion warmth. Layered paper cards with real-feeling shadows and a 6fps jitter that makes everything feel touched by hands.

Best for: kids, family, journaling, habit, cooking, education apps.

## Tokens

```ts
bg "#F5EDE0" (kraft) or "#EAF2EC" (sage paper)
papers: "#FFFDF7", "#F7D78A", "#E8A798", "#A8C8B8", "#9BB8D9" — muted craft set
ink "#3E3529"
Font: rounded friendly — Baloo 2 / Quicksand 600+ for headlines; handwriting (Caveat) for labels.
FPS 30.
```

Motion grammar: **stop-motion sim** — quantize ALL animation: `const fq = Math.floor(f/4)*4` applied to every animated value (8fps effective). Poses hold and "settle" ±1°. Entrances: paper drops in from top with rotate ±3° and shadow growing.

## Core mechanism

```tsx
// Paper card = layered shadows that read as cut edges:
const paperShadow = "0 1px 0 rgba(0,0,0,.10), 0 8px 0 -4px rgba(0,0,0,.08), 0 24px 32px -12px rgba(62,53,41,.25)";
// EVERYTHING through the jitter quantizer:
const fq = Math.floor(f/4)*4;  // use fq everywhere you'd use f
// Slight per-element rotation offset (deterministic): rot = ((i*13)%7)-3 degrees
// Transitions: a hand-torn edge band wipes across (clip-path with jagged polygon —
//   generate 24-point irregular polygon at module level, frozen seed).
// Texture: fixed noise overlay PNG (generate 256px noise tile via numpy → png) at
//   multiply blend, opacity 0.35, covering full frame.
```

## Scene grammar (7–9 scenes, 90–130s)

S01: paper logo assembles — pieces drop/slide in one by one · S02: problem as a "messy desk" · S03–S07: features on colored paper cards pinned/taped to a cork or kraft board; screenshots inside paper frames with tape corners · S08: heart/star cutouts float up (emotion) · S09: logo card + stitched-button CTA ("Tải về" on a paper button).

Transitions: torn-paper wipe (jagged clip-path travels across frame).

## Audio

- Music: ukulele/glockenspiel/kalimba 85–95 BPM — numpy: short plucky sines with fast decay (0.3s), 2-3 harmonics, simple I–V–vi–IV.
- SFX: paper rustle (filtered noise swells 80ms), scissor-snips on cuts, tape-pull on screenshot placement.
- VO: warm, smiley, storytime pace (-3%).

## Signature details

Tape corners on screenshots · pins/brads holding cards · the fq=4-frame quantization everywhere · torn-edge wipes · slight paper curl on card edges (small rotateX at top edge).

Anti-patterns: smooth 30fps motion, neon colors, sharp 90° corners on shapes, digital glow effects, gradients other than subtle paper shade.
