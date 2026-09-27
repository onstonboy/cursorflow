# Style 36 — Particle Constellation

Tech-poetic assembly. Thousands of points of light fly from chaos into formation — assembling the logo, the UI, the meaning — connected by faint lines.

Best for: AI, data, network, security, research products — "emergence" as the visual metaphor.

## Tokens

```ts
void "#070A14"  particles: "#9FD8FF"–"#FFFFFF" ramp + accent "#6E5FFF"
lines: rgba(159,216,255,0.15)
Font: light-tech sans (Space Grotesk 300/500); sparse.
FPS 30.
```

Motion grammar: scatter→assemble — each particle interpolates from a random scatter position to its formation target with staggered delays (i%40 frames); slight orbit wobble post-assembly; dispersal = reverse with swirl.

## Core mechanism

```tsx
// N≈150–400 particles (divs work fine at this count; no canvas needed).
// Deterministic seed: pos_i = hash(i) — must be stable across frames.
// Target positions for formation shapes:
//   - text/logo: render the text once, sample positions = precompute a list of
//     coordinates along letters (approximate via grid of point offsets)
//   - screenshot silhouette: grid of points clipped to rectangle aspect
//   - icon shapes: parametric (circle = angle*r, etc.)
// p_i(t) = scatter_i + (target_i - scatter_i) * ease(clamp((f - delay_i)/DUR))
// Connections: skip true nearest-neighbor — fake it: draw ~60 fixed lines
//   between pre-paired particle indices, opacity by formation progress.
// Depth: 30% of particles slightly defocused (blur 2px, dimmer) = bokeh.
// Assembled screenshot: particles hold formation ~30 frames then the REAL
//   screenshot fades in ON TOP of the formation, particles scatter away.
```

## Scene grammar (6–8 scenes, 90–130s)

S01: void → particles stream in from edges → assemble logo · S02: dispersal → reform as problem glyph (broken chain / eye) · S03–S06: assemble each feature's icon shape → real screenshot materializes on top · S07: all particles form a constellation map = the app, then settle into wordmark + CTA points.

## Audio

- Music: ambient pads + delicate arps 85–95 BPM — numpy: evolving sine pads w/ harmonic swells, glass-pluck arp (high sine, long decay), swell crescendo timed to each assembly completion.
- SFX: shimmer on formation (filtered noise swell), data-blips on connections.
- VO: poetic-technical — short resonant phrases timed to assembly completions.

## Signature details

Formation-then-materialize rhythm (particles form shape → real asset appears) · bokeh depth · swell-per-assembly music sync · final constellation-into-logo.

Anti-patterns: canvas-less flicker (seed everything), unbounded particle counts (>500 divs = slow render), particles never settling, random motion without purpose.
