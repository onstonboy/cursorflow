# Style 49 — Fitness Pulse

Gym-energy promo. Every motion quantized to a 132 BPM grid; counters roll, rings fill, the frame shakes on drops. The video does cardio.

Best for: fitness, running, sports, dance, challenge/streak apps, nutrition with numbers.

## Tokens

```ts
bg "#0D0D0F"  accent: volt "#D4FF00" + performance red "#FF3B30"
big numbers: condensed 800–900, tabular-nums
Font: display condensed (Anton/Archivo Black) + mono for metrics.
FPS 30. BEAT = FPS*60/132 ≈ 13.6 frames — quantize everything.
```

Motion grammar: beat-quantized — every entrance/exits lands ON beat (at = round(beatN * BEAT)); screen shake ±4px for 3 frames on drop beats; elements pulse scale 1→1.06 on every kick; motion is explosive: in ≤8 frames, hold, out hard.

## Core mechanism

```tsx
const BEAT = 30*60/132;
const at = (b:number)=>Math.round(b*BEAT); // schedule on the grid, always
// Kick-synced pulse: const kick = 1 + 0.05*Math.max(0,Math.sin((f%BEAT)/BEAT*Math.PI*2 + π)) — decaying bump each beat.
// Shake: on drop frames, world translate = rng(±4px) for 3 frames.
// Rolling counter: digits scroll vertically — each digit a column translating
//   to target with 4-frame stagger (odometer).
// Progress ring: circle strokeDashoffset fills on beat hits (quarter-beat
//   chunks — feels physical).
// Screenshots: slam in with zoom-punch (scale 1.25→1, 6 frames) + tilt ±3°,
//   framed raw — border 3px volt, offset shadow, no radius.
// Rep-counting: benefits literally counted like reps ("01! 02! 03!").
```

## Scene grammar (8–12 beats, 60–100s — intense, short)

S01: countdown 3-2-1 slam (each numeral on beat) → drop · S02: problem on backbeat · S03–S08: feature-per-beat-block: counters rolling, rings filling, screenshots punching in; each block ends with a "REP" count · S09: personal-record card → CTA slammed like a finish line.

Energy budget: peaks and breathers — don't hold max intensity (build 2-bar phrases, mini-drops).

## Audio

- Music: EDM/phonk 128–135 BPM — numpy: sidechained saw bass pumping, hard kick (saturated sine click + decay), riser noise sweeps per drop, airhorn-lite (saw stack burst) once.
- SFX: count tick (woodblock-ish), plate-clang on PRs, whistle on transitions.
- VO: hype-coach — loud-ish, clipped phrases ("One. More. Feature."), lands ON beats. Or minimal captions + music leads.

## Signature details

Beat-quantized everything (off-beat elements look broken here) · kick-synced scale pulse · odometer counters · ±4px drop shakes · rep-counted benefits · PR-card finale.

Anti-patterns: off-beat motion, soft ease curves, slow builds, pastel, quiet SFX, long holds (nothing holds longer than 2 bars).
