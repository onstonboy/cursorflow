# Style 21 — Endless Feed Dive

Social-native storytelling. The camera swims through an infinite vertical feed of content cards, accelerates, then dives INTO one card that becomes the app's real UI.

Best for: social, content/community, dating, creator-economy, feed-based products.

## Tokens

```ts
bg: brand-dark gradient "#10101E"→"#1A1230" (deep, lets cards glow)
cards: dark surfaces "#1E1E2E" + accent gradient avatars
accent: brand gradient (2 stops)
Font: modern rounded sans (Inter/Poppins 600); UI text small, captions big.
FPS 30.
```

Motion grammar: scroll physics — feed `translateY` with velocity that eases up/down; cards have subtle parallax (inner content moves 8% slower); the dive = scale toward a card with `transform-origin` at card center + radial mask expand.

## Core mechanism

```tsx
// Feed column: N cards (7–10), each 340px, translateY = -(f * speed) wraps.
// Camera speed: interpolate velocity over the dive — fast scroll (motion-blur via
//   duplicate ghost offsets ±20px at 15% opacity) then decelerate onto target card.
// The dive: as camera approaches target card, card scales to fill frame:
//   const d = interpolate(f,[diveStart,diveEnd],[0,1],easing easeInOutCubic)
//   worldScale = 1 + d*4 ; worldOrigin at card center; card content crossfades
//   from "post preview" to REAL screenshot as scale crosses ~2.5.
// Cards' like-buttons pulse, comments tick up — ambient micro-motion on every card.
// After the feature plays, reverse: zoom out to feed, resume scroll, dive again.
```

## Scene grammar (6–8 scenes, 90–130s)

S01: surface INTO the feed mid-scroll, cards blur past · S02: slow onto a "problem post" · S03–S06: dive into posts where each post IS a feature demo (dive → full-screen screenshot moment → back out to feed) · S07: feed scrolls to a post that's the CTA ("Follow/download" card) → dive → end card.

Every feature revealed THROUGH a post — the frame device never breaks.

## Audio

- Music: hyperpop/future-bass 140–150 BPM — numpy: detuned supersaw chords (5 saws ±0.8%), sidechained pump (duck pad 8th-note), glitter arps.
- SFX: scroll whoosh rises with speed, dive "sub-drop" (sine sweep 200→40Hz), notification pings scattered.
- VO: hyped casual — sounds like a creator narrating their own app. Fast, warm, fandom vocabulary.

## Signature details

Scroll-blur ghosts on cards · dive = the only transition · ambient like/comment ticks on every card · CTA exists as a post in-feed · velocity easing on scroll, never linear.

Anti-patterns: static cuts, formal captions, empty feed (cards must feel alive), breaking the "we're inside a feed" illusion.
