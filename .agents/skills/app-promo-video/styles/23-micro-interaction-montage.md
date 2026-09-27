# Style 23 — Micro-Interaction Montage

Craft worship. Extreme close-ups of single UI details — a toggle, a keypress, a slider — each with its click sound. For products where the feel IS the feature.

Best for: design-forward apps, premium consumer, keyboard/utility apps, camera UIs, anything tactile.

## Tokens

```ts
bg: deep neutral "#0E0E10" or soft "#F4F3EF" (match app's theme)
light: dramatic top-light gradient behind each macro subject
Font: minimal captions only — tiny mono labels ("haptic · toggle"), letting UI breathe.
FPS 30.
```

Motion grammar: macro stillness + micro life — camera nearly locked (2–4px drift), the DETAIL animates: toggle thumb slides, keycap depresses (scaleY 0.92 + shadow), slider fills. Every motion is the UI's real affordance, exaggerated by scale.

## Core mechanism

```tsx
// Macro shot = 300–450% crop: recreate the control as a React component at huge
//   scale (don't upscale screenshot pixels — rebuild the toggle/key/slider as
//   styled divs, then it stays crisp). Real screenshots only in 1–2 wide shots.
const Keycap: React.FC = () => {
  // 340px keycap: border-radius 24, inner shadow; on press frame:
  //   scaleY 0.9, inner shadow deepens, "click" SFX lands.
};
// Sequence per shot: detail enters (scale .92→1, 20 frames) → idle 8 frames →
//   ACTUATE (the interaction, 6–10 frames) → consequence glow (checkmark pulse /
//   ripple 30 frames) → cut.
// Focus breathing: subtle blur 0→1.5px oscillation selling "macro lens".
// Light sweep: a slow specular highlight band travels across the control.
```

## Scene grammar (8–12 shots, 60–100s — short, rhythmic)

S01: pull out from a macro pixel-texture to reveal we're inside the app · S02–S08: one control per shot — toggle flicks, slider drags, keypress, drag-reorder; each cut lands ON the click · S09: first FULL screenshot (context payoff — "oh that's the app") · S10: logo macro → pull out → CTA.

Rhythm: actuation → consequence → cut, 60–80 frames per shot.

## Audio

- Music: near-silent — sparse piano notes or sub pulse, tons of air. The SFX are the soundtrack.
- SFX: REAL-feeling UI sounds are mandatory: click (2ms noise transient + 800Hz ping), haptic thunk (60Hz sine burst), swipe shh (noise sweep). Each lands exactly on actuation frame.
- VO: whisper-close or absent entirely. If present: one whispered phrase per 2 shots.

## Signature details

Controls rebuilt at 300%+ scale (never pixel-blown) · actuation-frame SFX sync · focus breathing · the delayed wide-shot reveal · near-silence between clicks.

Anti-patterns: upscaled blurry screenshots, background music louder than clicks, more than one control per shot, showing full UI too early.
