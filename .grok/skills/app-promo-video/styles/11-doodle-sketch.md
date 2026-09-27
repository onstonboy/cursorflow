# Style 11 — Doodle Sketch

Friendly whiteboard explainer. Everything is "drawn" live — circles scribble around features, arrows point at screenshots, annotations hand-write themselves.

Best for: education, productivity, health explainers, B2B onboarding, "how it works" promos.

## Tokens

```ts
bg "#FEFEFB" (paper white)
ink "#2B2B2B"  accent "#FF5C38" (marker red) + "#2B7FFF" (pen blue)
Font: content grotesk (Inter) for body; annotations in handwriting font (Caveat/Gochi Hand).
FPS 30.
```

Motion grammar: draw-on — SVG `strokeDasharray`/`strokeDashoffset` animated via interpolate. Strokes draw at human hand speed (~80–120px of path per 10 frames), slightly wobbly (double-stroke offset copy at 30% opacity for sketch feel).

## Core mechanism

```tsx
const Stroke: React.FC<{d:string; at:number; color?:string; w?:number}> = ({d,at,color=accent,w=5}) => {
  const f = useF();
  const L = 2000; // pathLength normalized
  const t = interpolate(f,[at,at+30],[0,1],{extrapolateLeft:"clamp",extrapolateRight:"clamp"});
  return <>
    <path d={d} stroke={color} strokeWidth={w} fill="none" strokeLinecap="round"
      pathLength={L} strokeDasharray={L} strokeDashoffset={L*(1-t)}/>
    <path d={d} stroke={color} strokeWidth={w*0.6} fill="none" opacity={0.3}
      transform="translate(2,-1.5)" pathLength={L} strokeDasharray={L}
      strokeDashoffset={L*(1-t)}/>
  </>;
};
// Pre-build path strings: circle-scribble (2 overlapping ellipses), arrow (line + head),
// underline (wavy path), asterisk, check. A "pen cursor" SVG sits at the stroke's
// current end point (getPointAtLength approximated by interpolating endpoints or
// placing a dot that travels a simplified path).
// Handwritten text: chars appear with slight per-char rotate ±3° (not typed — drawn feel).
```

## Scene grammar (7–9 scenes, 90–130s)

S01: title scribbles itself + underline stroke · S02: problem framed in a scribbled box · S03–S07: screenshot slides in clean → doodles annotate it (circle the key control, arrow + handwritten note "chỉ 1 chạm!") — annotation IS the narration · S08: big checkmark drawn + CTA handwritten.

The pen never stops moving — constant micro-doodles in margins.

## Audio

- Music: acoustic guitar/folk 95–105 BPM — numpy: plucked sine-triads, alternating bass, light shaker (filtered noise 16ths).
- SFX: marker squeaks (short sine chirps 1.2–2kHz, random ±10% pitch) at every stroke start.
- VO: explainer tone — clear, friendly teacher. Pacing synced so each VO phrase lands as its stroke completes.

## Signature details

Double-stroke wobble · pen cursor traveling · margin doodles (stars, arrows) · handwritten VN annotations ("xem nè!", "đỉnh chưa") · check-mark flourish ending.

Anti-patterns: straight perfect lines, filled solid arrows, typed annotation fonts, dark themes, formal VO.
