# Style 39 — Phone-in-Hand Mock

The product in someone's actual life. An illustrated/rendered hand holds the phone against ambient environments; scenes = places.

Best for: consumer, lifestyle, dating, food/delivery, transit — anywhere "in the moment" context sells.

## Tokens

```ts
environments: per-scene gradient+shapes suggesting place — cafe warm "#6B4A3A"/"#E8B98A", night-out "#2A1B4A"/"#FF6B9D", morning "#B8D4E8"/"#F5E6C8", gym "#2E3A45"/"#E8FF5C"
phone: dark bezel device + real screenshot
Font: lifestyle rounded sans (Poppins); casual.
FPS 30.
```

Motion grammar: ambient life — phone tilts ±3° idly in hand (pendulum sway ~0.3Hz); environment particles drift (steam, bokeh lights, leaves); thumb occasionally enters to "tap" (rounded rect swiping up 80px); scene change = hand swings phone out of frame, new environment washes in.

## Core mechanism

```tsx
// Hand: stylized — either a flat-illustration SVG hand gripping the device
//   (best: draw once in Figma-style paths, skin tone + sleeve), or a clean
//   vector "thumb arc" emerging bottom-right. Keep it tasteful/graphic, not
//   photoreal (photoreal hands = uncanny in motion graphics).
// Environment: 2–3 layers of place cues — big soft shapes + bokeh circles
//   (blur 30px colored dots), drifting slowly; optional recognizable prop
//   silhouettes (coffee cup, steering wheel top arc).
// Phone: idle sway rotate = sin(f/50)*2.5°, bob translateY sin(f/38)*5px.
// Thumbs-up taps: rounded pill slides in from bottom → tap ripple on screen.
// Screenshots: change by sliding the screen content (inside fixed bezel).
// Text captions float as environmental "cards" pinned near phone, slight parallax.
```

## Scene grammar (6–8 scenes, 90–120s)

S01: morning env — phone wakes, app opens · S02: problem shown in a boring gray env · S03–S06: each feature in a place it's used (commute, cafe, night, group hang) — environment tells WHERE, caption tells WHAT · S07: envs cycle rapidly past → settle home → logo + CTA.

Environment change IS the transition — phone swings out, world washes to new palette.

## Audio

- Music: warm pop 100–108 BPM — numpy: plucked chords, gentle bass, shaker; add env-ambience layer per scene (cafe murmur noise, night crickets = high sine pings quiet).
- SFX: tap ripples, sleeve-rustle on swings.
- VO: best-friend recommendation tone — "lúc đang đi làm nè…" contextual narration.

## Signature details

Environment-as-scene-changes · idle hand sway · bokeh drift · thumb taps with ripples · palette-per-place · the env-cycling recap before CTA.

Anti-patterns: photoreal hands, static phone (it must sway), environments detailed enough to distract (keep soft/suggestive), white studio background.
