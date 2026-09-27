# Style 20 — Infinite Zoom

One unbroken dive. Every scene zooms into a detail of the previous frame — a screenshot's button becomes a doorway into the next scene. Mesmerizing, impossible-looking.

Best for: photo/AI/creative apps, fractal/data products, any brand wanting a "wow" demo reel.

## Tokens

```ts
bg: deep space "#0A0A12" between zoom layers
accent: brand color as the "portal glow"
Font: minimal — short labels only, appears floating within layers.
FPS 30.
```

Motion grammar: continuous exponential zoom — NEVER linear. Scale multiplies ~4–8× per scene over 60–90 frames using `interpolate` on a log curve: `scale = Math.pow(k, t)`. At zoom boundaries, next scene is nested INSIDE the focal element and fades in as scale crosses ~1.5.

## Core mechanism

```tsx
// Nested layers approach: LayerStack of N scenes, each child rendered inside
//   parent's focal element at small scale; parent scales up around it.
const ZoomLayer: React.FC<{t:number; children}> = ...
// Compute camera: z = Math.pow(ZOOM_K, f/FRAMES_PER_LAYER)
// Current layer index i = floor(log_k(z)); local zoom = z / k^i
// Simpler discrete version: each scene is full-frame content that ends scaled
//   6× into focal point; next scene starts inside that focal element at 1/6 scale
//   and the PARENT container zoom does the handoff. Plan focal points at design
//   time: e.g. camera dives into (0.62, 0.41) of each frame.
// Portal edge: at transition the focal element gets accent glow ring (scale-up +
//   blur(2)) so the "doorway" reads.
// Keep mid-detail renderable: scenes must look good at 1× AND when 6× cropped —
//   put the focal element on its own layer.
```

## Scene grammar (6–8 layers, 80–120s)

S01: logo/city overhead → dive into a glowing dot · S02–S06: each layer = a scene whose focal element (a button, a QR cell, an icon, a photo inside the screenshot) contains the NEXT scene — dive → resolve → content plays → dive again · S07: reverse! zoom all the way back out through every layer (fast) → logo. The reverse-out is the signature ending.

Transitions: literally impossible to see — that's the point.

## Audio

- Music: continuous rising ambient — numpy: shepard-tone-ish illusion (stacked sine glissandi cycling pitch classes), pad swells at each portal, sub drop at the reveal.
- SFX: whoosh per portal (bandpass noise sweep 300ms), heartbeat pulse under everything.
- VO: dreamy, minimal — short phrases that land right as each portal resolves.

## Signature details

Exponential (never linear) zoom · accent-glow portal rings · focal points designed INTO the layouts · the full reverse-zoom finale · scene count visible as "depth meter" corners (optional).

Anti-patterns: any hard cut, linear zoom (looks broken), focal elements that are blurry at 6× (render them crisp — zoom target must be a real element, not pixels), busy edges at focal points.
