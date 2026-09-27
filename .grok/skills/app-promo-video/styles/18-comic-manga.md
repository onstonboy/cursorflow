# Style 18 — Comic / Manga

Action-manga energy. Panels slam in, speed lines radiate, screentone fills, giant sfx typography — the app story told like a fight scene.

Best for: gaming, anime/manga apps, social with playful conflict ("you vs boring chats"), Gen Z entertainment.

## Tokens

```ts
paper "#F7F3EA"  ink "#141414"  screentone: radial dots via repeating-radial-gradient
accent "#FF3355" (impact red) + "#FFD400" (flash yellow)
Font: heavy condensed display for SFX words (Anton), bold sans for dialog, mono for panel labels.
FPS 30.
```

Motion grammar: panels SLAM — scale 1.4→1 in 5 frames + 2px translate shake on impact; speed-line bursts scale from 0 behind the focal point; zoom punches into panels. Everything violent-fast (≤8 frames) then holds.

## Core mechanism

```tsx
// Manga panel: thick 6px ink border, slight rotate ±1.5°, drop shadow offset 8px
//   (hard offset, no blur — print style).
// Speed lines bg: conic-gradient thin rays, opacity pulse on impact frames:
<div style={{background:`repeating-conic-gradient(from ${rot}deg,
  #141414 0deg 0.8deg, transparent 0.8deg 4deg)`, opacity:pulse}}/>
// Impact SFX text: giant outlined glyph ("ドン!" or "BÙM!") scale 0→1.15→1 in
//   8 frames, flash yellow fill, red stroke, rotate -8°.
// Screentone fill: any flat area gets repeating-radial-gradient dots at 40%.
// Reading order: panels enter in manga order (right→left) or western (left→right)
//   — pick one and stay consistent; number them subtly.
// Screenshots: pasted INTO panels like pasted artwork (still 6px ink border).
```

## Scene grammar (8–11 beats, 60–100s — fast cuts)

S01: title page — logo exploded across a panel with speed lines · S02: "the enemy" = boring chat screen in a dark panel · S03–S07: each feature = an action beat: caption box ("LIÊN HOÀN ĐẤM:"), SFX glyph, screenshot panel slam · S08: final spread — hero shot of app, "TO BE CONTINUED…" + CTA.

Transitions: hard panel cuts; occasionally a white flash frame.

## Audio

- Music: taiko + punk energy 140–150 BPM — numpy: taiko hits (saturated sine-thump + noise), driving 8th-note bass, shamisen-ish pluck (saw + fast decay + slight bend).
- SFX: impact boom per slam, whoosh on panel entries, crowd "ohhh" stinger at reveals.
- VO: hyped announcer or deadpan-vs-chaos contrast. Short bursts only — SFX text carries the punchlines.

## Signature details

Ink-bordered panels · speed-line pulses · giant SFX glyphs with flash fill · screentone on flats · "TO BE CONTINUED" cliffhanger CTA · motion = slam+hold, never glide.

Anti-patterns: soft shadows, rounded corners, gentle easing, long fades, quiet SFX, paragraphs of copy inside panels.
