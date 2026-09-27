# Style 25 — Game-Parody Runner

The app demo disguised as gameplay. Side-scrolling world, features as collectible items, benefits as score — marketing video as a fake speedrun.

Best for: habit/productivity gamified apps, kids, finance with goals, fitness — or any app willing to be silly.

## Tokens

```ts
sky gradient per "level"  ground "#6B4F2E"-ish or neon platform — pick theme per app
HUD: pixel font (Press Start 2P / VT323) for score/hearts; content sans for labels
accent: coin-gold "#FFD23F"
FPS 30.
```

Motion grammar: platformer physics — constant forward scroll (parallax 3 layers: far 0.3×, mid 0.6×, front 1×); mascot/icon bobs and "jumps" (parabolic arc, squash on land); collectibles spin (rotateY via scaleX osc or sprite-swap ±).

## Core mechanism

```tsx
// World scrolls, camera fixed: world translateX = -(f * speed).
// Mascot = product icon with leg-less bounce: translateY = -abs(sin) arc,
//   squash scaleY 0.85 on landing, stretch 1.1 mid-jump.
// Collect: item near mascot → sparkle burst (8 dots radial) + item flies to HUD
//   (interpolate item→hud position) + score counter ticks +100 with pop.
// Level transitions: "LEVEL 2" banner cards + palette swap (sky hue shift).
// Screenshots: presented as "POWER-UP KIOSKS" — framed signposts the mascot
//   stops at; camera punches in to show the screen, then resumes run.
// Enemies = the problem: gray "boring blocks" that get bonked → shatter particles.
```

## Scene grammar (6–9 scenes, 80–120s)

S01: "PRESS START" → title drops pixel-style · S02: Level 1 = problem world, mascot dodges "boring" enemies · S03–S07: each level = a feature; collectibles = benefits; kiosk = real screenshot; boss-mid = the hesitation to switch, defeated · S08: results screen — score tally = benefit recap → "INSERT COIN = TẢI NGAY" CTA.

Score always visible, climbing — the benefit counter.

## Audio

- Music: chiptune 140 BPM — numpy: square-wave lead (`np.sign(sin)`) melody + triangle bass + noise drums; loop 4 bars; pitch-bend coin sound = sine gliss up.
- SFX: coin (B5→E6 arp), jump chirp, damage buzz, level-up jingle (4-note rise).
- VO: optional announcer-hype or none — HUD text often carries it.

## Signature details

Parallax 3-layer scroll · squash-and-stretch mascot · collectibles that fly to HUD · level banners · score = benefit counter · boss-beat = objection handling.

Anti-patterns: realistic rendering, slow motion, missing HUD, collecting nothing (items must visibly count), forgetting the results-screen recap.
