# Style 29 — Glassmorphism Aurora

Premium soft-tech. Frosted glass cards float over a living aurora gradient; content sits behind blur with inner-light edges.

Best for: premium fintech, health, AI assistants, weather, subscription "pro" tiers — quiet luxury.

## Tokens

```ts
bg: animated aurora — layered radial-gradients "#1A0B3D","#0E3A5C","#3B0E4E" drifting slowly
glass: rgba(255,255,255,0.08) fill + backdrop-filter blur(18px) + 1px rgba(255,255,255,.18) border + inner highlight top edge
ink "#F2F0FA"  muted "#B8B2D4"
Font: clean geometric (Inter/Poppins 400–600), letterSpacing relaxed.
FPS 30.
```

Motion grammar: buoyancy — glass cards float up ±8px on offset sine phases; entrances = rise 60px + blur(20→0) + scale .96→1 over 40 frames; aurora blobs drift on 20s+ cycles. Everything glides; nothing snaps.

## Core mechanism

```tsx
// Aurora layer: 3–4 large radial-gradient blobs, each translating slowly along
//   a Lissajous path (sin/cos with different periods); occasional hue breathe.
const blob = (x,y,r,color,phase) => radial-gradient… at animated positions.
// Glass card recipe (the whole style):
background:"rgba(255,255,255,0.07)", backdropFilter:"blur(18px) saturate(1.4)",
border:"1px solid rgba(255,255,255,0.16)", borderRadius:28,
boxShadow:"inset 0 1px 0 rgba(255,255,255,.25), 0 30px 60px -20px rgba(0,0,0,.4)"
// Parallax: 3 depth layers — bg blobs (0.3×), cards (1×), foreground sparkle
//   dust (1.4×) moving against camera drift.
// Screenshots: inside glass frames — screenshot sits BEHIND frosted border
//   card; screen content fully visible, frame is the glass.
// Light edge: rotate a conic-gradient border highlight slowly for "premium"
//   shimmer on ONE hero card only.
```

## Scene grammar (7–9 scenes, 100–140s)

S01: aurora blooms → logo materializes in blur · S02: problem as a foggy card clearing up · S03–S07: each feature = a glass panel floating in at a different depth; screenshots in glass frames; specular edge highlight on the hero feature · S08: all cards recede → single glass pill CTA glowing center.

Transitions: cards sink back into blur (opacity + blur leave), new ones float up.

## Audio

- Music: airy pad 72–78 BPM — numpy: stacked detuned sines w/ slow LFO lowpass, occasional bell tones (sine + long decay), no drums or barely brushed hat.
- SFX: soft glass "ting" on card landings, airy whoosh.
- VO: calm premium — smooth, unhurried, low dynamic range. Slight reverb on VO fits.

## Signature details

Backdrop-blur everywhere (never flat fills) · three-depth parallax · ONE shimmering conic-border hero card · buoyant float loops · aurora that never stops moving.

Anti-patterns: opaque cards, hard edges <20px radius, fast cuts, dark flat backgrounds (aurora must live), more than 3 glass cards on screen.
