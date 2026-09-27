# Style 26 — Domino Chain

Cause→effect visualized. Tiles topple in sequence; each falling tile triggers the next feature reveal — automation made physical.

Best for: automation, workflow, integration/no-code, IFTTT-like products, CI/CD, "set it and forget it" apps.

## Tokens

```ts
bg: warm neutral studio "#E8E4DC" or deep "#191B1F"
tiles: matte color cards (brand palette), engraved face glyphs
accent: brand color on the "trigger" tile and CTA
Font: clean sans labels ON tiles; mono for chain-step numbers.
FPS 30.
```

Motion grammar: rigid topple — each tile `rotate(0→72°)` around bottom edge via `transform-origin: bottom`, `Easing.in` (accelerating like gravity), lands with dust puff + camera micro-shake (2px, 6 frames). Gap between tiles ~1.1× height so falls read clearly.

## Core mechanism

```tsx
const Tile: React.FC<{at:number; label:string; children}> = ({at,...}) => {
  const f = useF();
  const a = interpolate(f,[at,at+10],[0,72],{easing:Easing.in(Easing.quad),
    extrapolateLeft:"clamp",extrapolateRight:"clamp"});
  return <div style={{transformOrigin:"50% 100%", transform:`rotate(${a}deg)`}}>…</div>;
};
// Chain scheduler: tile i starts when i-1 reaches ~55° (at_i = at_{i-1} + 7).
// Camera: gentle pan FOLLOWING the fall wave (translateX keeps impact point
//   at ~60% frame width) — the camera chases the action.
// Payload tiles: some tiles carry a screenshot card on their back — revealed
//   when the tile lands (screenshot flips up from the fallen tile via nested
//   rotate from its top edge).
// Shake: world container translate ±2px decaying on each impact.
```

## Scene grammar (5–8 scenes, 80–110s)

S01: single trigger tile pushed by a finger-cursor — chain begins · S02–S06: the chain travels through the feature set; payload tiles reveal screenshots when they land; occasionally chain splits (two branches = parallel automations) · S07: final tile lands on a big CTA button tile → rings a "done" chime → wordmark.

One continuous chain ideally; re-anchoring cuts allowed between "setups".

## Audio

- Music: marimba/percussive groove 100 BPM — numpy: wooden plucks (sine + 3rd harmonic, fast decay), log-drum bass, shaker.
- SFX: THE clack (filtered wood-block click ~60ms) per tile + low thud on land + camera-shake rumble; a wind-up creak for the first push.
- VO: cause-effect narration — "Điều này xảy ra… nên điều này xảy ra." Medium pace, satisfied tone.

## Signature details

Gravity-accelerated topple (never constant speed) · impact dust + shake · payload screenshots on fallen tiles · camera chasing the wave · split chains · final tile pressing the CTA like a button.

Anti-patterns: tiles that float/rotate wrong axis, uniform fall speed, no impact feedback, static camera (must chase), breaking the chain with fades.
