# Style 13 — Blueprint

Engineering drawing come alive. Cyan-on-blue schematic lines, dimension arrows annotating UI, exploded device views — precision as beauty.

Best for: architecture/construction, CAD/3D tools, fintech infra, security, B2B, productivity for pros.

## Tokens

```ts
blue "#1B3A6B" (paper)  blueDeep "#142C52"
line "#7FB4E8" (cyan lines)  lineHi "#C9E6FF"  accent "#FFD166" (annotation amber — sparing)
Font: technical mono (JetBrains/IBM Plex Mono) for ALL labels; condensed sans for headline blocks.
FPS 30.
```

Motion grammar: drafting — lines extend from endpoints (scaleX 0→1, origin left), dimension markers slide along their line, crosshairs scan. Easing linear-ish (`Easing.bezier(0.3,0,0.7,1)`), deliberate, instrument-like. Elements "measure in", never bounce.

## Core mechanism

```tsx
// Dimension line = the signature atom:
const DimLine: React.FC<{x:number;y:number;w:number;label:string;at:number}> = ...
// renders: ←—————— "235mm" ——————→ ; line scaleX in, label fades at midpoint.
// Crosshair: vertical+horizontal hairlines meeting at a point that travels
//   scene→scene like a drafting cursor; leaves a trailing ghost.
// Exploded view: phone components as stacked layers offset along Y with
//   connector lines + part codes ("SCR-01").
// Grid: fine 40px + major 200px cyan lines at 8%/15% opacity, always visible.
// All corners get tick marks ⌐ ¬.
// Screenshot integration: framed inside a drawn rectangle with dimension
//   callouts ("1080×1920") and a section label ("FIG. 03 — LOCK SCREEN").
```

## Scene grammar (7–9 scenes, 100–140s)

S01: title block drafts itself (drawing table bottom-right: app name, scale 1:1, date) · S02: problem as "FAULT DIAGRAM" · S03–S07: each feature = a FIGURE: screenshot framed + dimensioned + annotated with leader lines; one scene is a full exploded device · S08: title block returns with stamp "APPROVED" + CTA.

Transitions: crosshair scans to next figure region; wipe = a drawn line sweeping.

## Audio

- Music: ambient synth pad + precise clicks — numpy: evolving pad (detuned saws through slow lowpass LFO), metronome tick 90 BPM low in mix, occasional sonar-blip.
- SFX: pencil-drag, plotter whir, camera-shutter on figure captures.
- VO: precise, calm engineer — measured pace, no slang. Technical-but-clear phrasing.

## Signature details

FIG. numbering per scene · dimension labels on EVERYTHING (even emotional beats: "trust: 100%") · corner ticks · title block persistent · crosshair travel transitions · amber "REVISION" stamp end card.

Anti-patterns: warm colors, handwriting fonts, bounce easing, decorative illustration, marketing hyperbole in VO.
