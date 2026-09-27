# Style 16 — Film Noir

Hard shadows and single sources of light. B/W with one accent color; the UI emerges from darkness like evidence under a lamp.

Best for: security, VPN, privacy (serious sibling of Midnight Playground), finance, investigation/mystery angles, legal-tech.

## Tokens

```ts
black "#060606"  white "#ECEBE6"  gray ramp only via shadows
accent "#D4A017" (amber) OR "#B32B2B" (blood red) — ONE only
Font: condensed slab/serif for titles (Bebas/Playfair SC), mono for case-file labels.
FPS 30.
```

Motion grammar: light does the animating. Spotlights sweep (`radial-gradient` position follows content), venetian blind shadow bands drift slowly, content reveals as light hits it — elements themselves barely move (opacity + 8px drift max). Slow dissolves (24–40 frames).

## Core mechanism

```tsx
// Spotlight = radial-gradient mask div positioned over the subject:
<div style={{position:"absolute",inset:0,
  background:`radial-gradient(420px 300px at ${spotX}% ${spotY}%, transparent 0%, rgba(6,6,6,.92) 70%)`}}/>
// spotX/spotY interpolated toward each element's `at` — light literally travels the scene.
// Venetian blinds: repeating-linear-gradient rotated -18deg, drifting 0.3px/frame,
//   as a multiply overlay at 25%.
// Content "caught in light": element opacity = f(spotDistance) — as spotlight
//   approaches, element fades in; light leaves, it fades back to 20%.
// Smoke: 3 large blurred divs drifting (translate slow, blur(60px), opacity .05).
// Screenshots: flat in a case-file folder card labeled "EXHIBIT A".
```

## Scene grammar (6–8 scenes, 100–140s — noir breathes)

S01: title in single spotlight cone, smoke drifts · S02: "THE CASE" file opens, problem typed on a dossier · S03–S06: each feature = an "EXHIBIT": light sweeps to a screenshot evidence card, amber/red annotation stamp · S07: light pulls wide → wordmark lit alone → tagline whispers in.

Transitions: light extinguishes (frame goes black 8 frames) then ignites on next scene.

## Audio

- Music: noir jazz — numpy: brushed swing kit (noise bursts soft, 70 BPM swing 12%), walking sine-bass line, muted trumpet-ish lead (saw + strong lowpass + vibrato), minor key.
- SFX: distant rain bed, match-strike on light ignitions, case-file slap.
- VO: low conspiratorial register (-3Hz pitch), measured, dramatic pauses. VN: ít từ, nhiều ngầm ý — "Họ đọc hết. Tất cả."

## Signature details

Light as the only "camera" · EXHIBIT numbering · blinds-shadow always present · smoke layer · single accent color discipline · black-frame scene transitions.

Anti-patterns: bright colors, bounce, fast cuts, exclamation energy, more than one light source visible, music with drums louder than a whisper.
