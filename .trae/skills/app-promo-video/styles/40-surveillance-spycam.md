# Style 40 — Surveillance / Spy Cam

The product seen through the eyes of a watcher — CAM overlays, green night-vision, target brackets — until the app itself beats the watcher. Privacy thriller energy.

Best for: security, VPN, privacy apps, encrypted messengers — the serious/darker sibling of Midnight Playground.

## Tokens

```ts
cam view: green-tinted "#0A1F0E" night vision OR monochrome "#111" cctv
overlay amber "#FFB000" for HUD text; red "#FF2B2B" for "DETECTED"
clean side: brand's real palette (revealed post-flip)
Font: HUD mono everywhere on cam side; brand font post-reveal.
FPS 30.
```

Motion grammar: surveillance mechanics — slow pan/zoom presets (camera "hunts" then locks), tracking brackets that lag then snap onto target (target moves 20 frames, brackets follow with 8-frame delay + overshoot), occasional signal noise bars.

## Core mechanism

```tsx
// Cam chrome (persistent overlay): "CAM 03" corner label, "● REC" blink,
//   timestamp rolling, battery icon, slight vignette + noise overlay (grain PNG,
//   animated via f%4 cycling).
// Tracking brackets: 4 corner brackets around a target element; brackets' frame
//   position = lerp of target pos at (f - 8) → lagging pursuit feel.
// Night vision: content rendered normal but wrapped in green tint overlay +
//   contrast boost (filter:"contrast(1.2) sepia(1) hue-rotate(70deg)" trick or
//   simply duotone-green coloring of cards).
// THE FLIP — the signature: mid-video, when the app's protection activates,
//   cam feed glitches hard (slice displacement + noise burst 10 frames) →
//   world resolves into clean branded UI. Watcher loses the target:
//   brackets search, find nothing, "SIGNAL LOST".
// Screenshots on cam side: framed as "captured intel" — tilted, green-tinted.
```

## Scene grammar (7–8 scenes, 90–120s)

S01: cam boots, sweeps a dark room, finds a phone · S02: problem = intercept — brackets lock onto a chat bubble, "READING…" · S03: THE FLIP — protection activates, glitch, clean world; brackets now find nothing · S04–S06: features demonstrated in clean UI while cam overlay "loses signal" progressively (HUD degrades, static grows) · S07: final cam view: static snow → logo cuts through → CTA "stay invisible".

## Audio

- Music: tension drone 60–70 BPM — numpy: detuned low sines beating, filtered noise swells, sub-thump heartbeat; post-FLIP music snaps to clean minimal techno (contrast = the payoff).
- SFX: cam servo whirs, lock-on chirp, static burst at flip, radio squelch.
- VO: hushed operative ("They're watching right now…") — low pitch -3Hz, then confident post-flip.

## Signature details

Lagging pursuit brackets · the mid-video GLITCH-FLIP (make it the emotional peak) · HUD degradation post-flip · "SIGNAL LOST" payoff text · persistent cam chrome.

Anti-patterns: the flip arriving late/soft (it must land hard), clean footage on cam side, playful colors, revealing clean UI before the flip.
