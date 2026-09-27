# Style 45 — ASCII Cinema

Dev poetry. Screenshots and scenes rendered entirely as ASCII art that types itself — phosphor terminals as cinema.

Best for: devtools, CLI products, hacker/security, APIs — audiences who read code for pleasure.

## Tokens

```ts
phosphor green "#33FF66" on "#050805" OR amber "#FFB000" on "#120A02" — pick one ramp
mono font REQUIRED for grid alignment: JetBrains Mono / IBM Plex Mono, lineHeight exact 1.0
chars ramp: " .:-=+*#%@" (light→dense)
FPS 30.
```

Motion grammar: typing — text/art appears 2–6 chars per frame left-to-right or in random "decode" order; cursor block █ blinks `f%16<8`; transitions = screen clear (instant) or scroll-up.

## Core mechanism

```tsx
// PREPROCESS screenshots → ASCII (run once, commit .txt files):
// python: img → grayscale → resize to ~96 cols wide (aspect-corrected ×0.5)
//   → map luminance to ramp chars → save .txt per screenshot.
// Render: <pre style={{fontFamily:mono, lineHeight:1, fontSize:14,
//   letterSpacing:0}}>{visibleSlice}</pre>
// Type-on: visibleSlice = art.slice(0, charsShown) where
//   charsShown = (f-at)*4 — image "prints" itself.
// Better: decode-order — chars appear in shuffled index order (deterministic
//   seeded shuffle) for a "resolving" effect.
// Structure all scenes as terminal screens: prompt lines "$ app --demo",
//   output blocks, blinking cursor, occasional [OK] status stamps.
// Column discipline: art width fixed (e.g. 96 cols), everything monospace grid.
```

## Scene grammar (7–9 scenes, 90–130s)

S01: boot text types → ASCII logo resolves char-by-char · S02: problem as a leaked log (`>> READ BY: everyone`) · S03–S07: features = ASCII-art screenshots decoding in + typed captions; maybe an ASCII animation (progress bars, spinner) · S08: `$ install` → fake progress bar fills → "done." → URL in ASCII box.

## Audio

- Music: minimal hum — numpy: mains-hum 60Hz + soft pad, modem-ish blips; keep it thin (terminal silence is the aesthetic).
- SFX: fan hum bed, keyclicks during typing (essential — typing without clicks dies), beep on [OK], dial-up-lite chirp at connect.
- VO: OPTIONAL — this style often lands harder with text + SFX only. If used: deadpan hacker monotone.

## Signature details

Real ASCII-converted screenshots (preprocessed, not faked) · decode-order reveals · blinking block cursor · exact mono grid alignment · `[OK]`/`[DONE]` stamps · silence-forward audio.

Anti-patterns: proportional fonts breaking columns, smooth fades (terminals don't fade), ASCII drawn by hand (must be converted), color — two-tone only.
