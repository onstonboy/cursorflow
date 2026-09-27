# Style 35 — Liquid Morph

Organic fluid identity. Everything is blobs that stretch, merge, and morph — features literally flow into each other.

Best for: wellness, period/health, hydration, sleep, sensual or soft brands, baby products.

## Tokens

```ts
bg: deep calm "#1A1030" or dawn "#F8E8E0"
liquids: flowing gradient pair e.g. "#7B5FE8"→"#E87BA8", "#5FE8D4"→"#7B9FE8"
ink: soft white "#F5F0FA"
Font: rounded soft sans (Nunito/Quicksand), low weights.
FPS 30.
```

Motion grammar: morphing — `border-radius` interpolation between blob shapes (8-value asymmetric radius, e.g. `"60% 40% 55% 45% / 50% 55% 45% 50%"` → next keyframe), continuous slow morphing even at rest (±10% radius wander); merge illusion via `filter: blur()` + contrast trick on a wrapper.

## Core mechanism

```tsx
// Breathing blob:
const morphR = (f:number, seed:number) => {
  const w=(a:number)=>Math.sin(f/45+seed*3+a)*12;
  return `${50+w(0)}% ${50-w(0)}% ${50+w(1)}% ${50-w(1)}% / ${55+w(2)}% ${50-w(2)}% ${55+w(3)}% ${45+w(3)}%`;
};
// GOOEY MERGE — the signature: wrap merging blobs in a container with
//   filter: blur(14px) contrast(20) against matching bg → metaball effect.
//   Inside container, blobs are flat-colored circles that drift together.
// Flow transitions: scene ends as blobs merge into one → splits into next
//   scene's shapes — content never "leaves", it transforms.
// Screenshots: masked inside a slowly-morphing blob (overflow hidden on the
//   morphing radius) — screen surface ripples with the blob.
// Surface detail: highlight ellipse at top-left 25% opacity inside blob.
```

## Scene grammar (6–8 scenes, 90–130s — flows slow)

S01: droplets merge into logo blob · S02: problem = rigid cube blob that resists, dissolves · S03–S06: feature blobs morph between icon silhouettes (drop→shield→chat→heart shapes via radius tricks) with screenshot surfaces · S07: all blobs merge into calm pool → logo surfaces → CTA ripple.

Everything transforms; nothing enters/exits by cut or wipe.

## Audio

- Music: liquid ambient 70–80 BPM — numpy: filtered sine pads with slow attack, occasional water-drop notes (sine with pitch-drip: f drops 20% over 200ms), deep warm sub.
- SFX: droplet plinks, merge "blurp" (filtered noise blob), gentle ripple shimmer.
- VO: ASMR-adjacent — soft, slow (-5%), soothing; or text-only with type materializing inside blobs.

## Signature details

Gooey blur+contrast merges · always-morphing rest state · screenshots inside living blobs · transform-not-cut transitions · droplet SFX.

Anti-patterns: straight lines, sharp corners, hard cuts, fast pacing, geometric grids, stopping the morph (blobs never freeze).
