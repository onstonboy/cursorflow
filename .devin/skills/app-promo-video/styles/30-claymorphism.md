# Style 30 — Claymorphism

Soft 3D clay blobs that squash and stretch. Chunky rounded shapes with inner+outer shadow stacks simulating hand-molded clay — cute with real dimension.

Best for: kids, habit trackers, casual consumer, finance-for-everyone, playful brands.

## Tokens

```ts
bg "#EDE8F5" or per-brand pastel field
clay set: "#FFB6C8","#A8D8FF","#B8E8B0","#FFD9A0","#D8C8F8" + brand color
ink "#3D3450"
Font: chunky rounded (Baloo 2 / Nunito 800) — weight sells clay.
FPS 30.
```

Motion grammar: squash & stretch — entrances `scale(0.6→1.08→1)` with `Easing.elastic` or spring (Remotion `spring({damping:8})`); shapes wobble (scaleX/scaleY counter-oscillate ±4% at ~0.5Hz); landings squash flat 0.85 then recover.

## Core mechanism

```tsx
// The clay recipe — stacked shadows simulate depth:
const clay = (base:string) => ({
  background: base,
  borderRadius: 32,
  boxShadow: `inset 4px 4px 10px rgba(255,255,255,.75),
              inset -6px -6px 14px rgba(60,40,90,.18),
              0 18px 36px -10px rgba(60,40,90,.28)`,
});
// + a top-left "light" blob: blurred white ellipse inside at 40% for specular.
// Squash-stretch entrance:
const s = spring({frame: f-at, fps, config:{damping:8, mass:1, stiffness:120}});
scale = interpolate(s,[0,1],[0.5,1]); 
// wobble: scaleX = 1+sin(f/9+seed)*0.04; scaleY = 1-sin(f/9+seed)*0.04 (counter-phase = volume preserved)
// Screenshots: embedded as "windows" inset INTO clay shapes — inner shadow ring,
//   screen slightly recessed (scale .97 + inset shadow).
// Buttons: press = scale .9 + shadow flattens (outer shadow shrinks — pressed into table).
```

## Scene grammar (7–9 scenes, 90–120s)

S01: clay logo blobs merge together into wordmark · S02: problem = gray clay block that's sad (slumps) · S03–S07: each feature = clay playset — blob character + screenshot window + chunky label; blobs bounce-greet each other · S08: all clay pieces stack into a trophy → CTA clay button that presses itself.

Clay elements should feel weighty-then-light: impact squash, then floaty wobble.

## Audio

- Music: bubbly synth-pop 100–115 BPM — numpy: round bass (sine + saturation), bouncy plucks, whistle-y lead (sine + vibrato), upbeat kick pattern.
- SFX: boing on springs (sine pitch-drop-up), squish on squash (noise+lowpass burst), pop on buttons.
- VO: playful, smiley — kid-friendly energy without babytalk; moderate pace.

## Signature details

Volume-preserving squash/stretch · inner+outer shadow stack (the clay recipe) · specular light blob top-left · recessed screenshot windows · elastic springs with damping ~8.

Anti-patterns: hard shadows, thin fonts, monochrome schemes, linear motion (everything springs), clay shapes without the inner shadow (reads flat).
