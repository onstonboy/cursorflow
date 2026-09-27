# Style 22 — Split-Screen Before/After

Problem vs. solution, literally side by side. A draggable-looking divider sweeps across the frame; the gray world gets replaced by the branded one.

Best for: utilities, cleaners/optimizers, health transformations, finance (debt→savings), any "life before/after" story.

## Tokens

```ts
left (before): desaturated world — gray "#9AA0A8", "#D8DBDE" surfaces, muted
right (after): full brand color
divider: brand accent bar 6px + circular handle with ⇄ glyph
Font: clean sans (Inter); claims set as paired statements.
FPS 30.
```

Motion grammar: the divider IS the protagonist — it slides horizontally (`translateX` with `Easing.inOut` 40–60 frames), revealing the after-side via `clipPath: inset()`. Within each side, micro-motion contrast: before-side items sag/stutter (rough eased), after-side items pop crisply (spring).

## Core mechanism

```tsx
// Two stacked full scenes; the after layer clipped by divider position:
const Split: React.FC<{split:number /*0..1*/}> = ({split}) => <>
  <BeforeScene/>   {/* full frame, gray world */}
  <AbsoluteFill style={{clipPath:`inset(0 0 0 ${split*100}%)`}}>
    <AfterScene/>  {/* branded world wipes in from the left edge */}
  </AbsoluteFill>
  {/* divider bar + handle at x = split*width */}
</>;
// Moment of change: divider sweeps at the VO beat flip — one continuous wipe.
// Paired elements: same card exists both sides (chaotic vs calm) — align positions
//   so the wipe morphs each element in place.
// Scene-end beat: divider slams to 100% (after wins) or holds a 20/80 ratio.
```

## Scene grammar (6–8 scenes, 90–120s)

S01: full gray "before" world, divider at 0% · S02: divider peeks in — audience sees the after-world exists · S03–S06: paired transformations: same layout both sides (messy inbox → clean, manual → auto, anxious → calm), divider sweeps per feature on VO flip · S07: divider to 100%, brand color floods, CTA both-badge.

The divider's position tracks the STORY: nudge it 10%→…→100% across the video as a progress metaphor.

## Audio

- Music: two-literal-modes — before = detuned/muted version (lowpass 0.03), after = same motif bright (add hats + raise pad an octave). Crossfade follows divider position. Numpy: render both layers, mix by split ratio per-frame.
- SFX: slide swoosh on sweeps, satisfying click when handle locks.
- VO: contrast phrasing — "Trước đây: … Giờ thì …" pacing rides the wipe.

## Signature details

Same-element-both-sides alignment (the money shot) · divider nudged as progress bar · audio crossfade tied to split position · full-flood finale.

Anti-patterns: sides that don't share layout, asymmetric unrelated imagery, forgetting the handle, starting at 50/50 (start at 0 — the before world must be the world).
