# Style 28 — Storybook Page-Turn

A fairy tale told from an open book. Each scene is a page; turning the page is the transition. Warm, narrative, made for bedtime-adjacent products.

Best for: kids, sleep stories, reading apps, family products, gentle wellness brands.

## Tokens

```ts
desk "#7A5C42" or night "#3A3450" (book rests on it)
page "#FBF6EA"  pageEdge "#E8DCC8"  ink "#4A3F30"
illustration palette: watercolor-flat — "#E8A2B8","#A2C8E8","#B8D9A8","#F0D98C"
Font: storybook serif (Gentium/Merriweather italic) body; display serif title.
FPS 30.
```

Motion grammar: the page turn — right page rotates `rotateY(0→-180°)` around spine (transform-origin left edge, perspective 2000px), with a traveling shadow gradient across both pages and slight page curl (the turning page skews/gradients mid-turn). Content on pages is gentle: elements rise 20px, illustrations drift ±4px.

## Core mechanism

```tsx
// Book: two page halves + turning page layer between them:
<Spine shadow/> <LeftPage/> <TurningPage rotateY={a}/> <RightPage/>
// TurningPage carries next-scene content on its back face
//   (rotateY 180 = you're seeing the back = next page's left side).
// During turn: page brightness = 1 - sin(progress*π)*0.25 (shadow mid-air).
// Illustrations: flat shapes + soft noise texture (opacity .12) for watercolor feel.
// Screenshots: pasted as "tipped-in plates" — small framed screenshots with a
//   caption rule, like illustrated plates in old books.
// Marginia: tiny stars/moons/flower doodles animate in page corners.
// "Once upon a time" opener types in serif italic.
```

## Scene grammar (6–8 pages, 100–140s — gentle pacing)

P01: cover page — embossed title + crest · P02: "once upon a time" — the problem as a little storybook village · P03–P06: each feature = a storybook chapter page (chapter numeral "Chapter Three — The Secret Words"), plate screenshot + illustration · P07: "and they chatted happily ever after" → endpaper CTA page (dark paper, gold-foil-looking logo).

Each page holds 15–22s; turns every scene.

## Audio

- Music: music-box/celesta + strings — numpy: plucked sine-triangle melody with bell overtones (3rd harmonic), soft string pad, 72 BPM, 3/4 waltz feel.
- SFX: page-turn rustle (filtered noise sweep 400ms) at every turn — essential.
- VO: storyteller — warm, slow (-5%), gentle drama; "Ngày xửa ngày xưa…" openers work beautifully.

## Signature details

Page-shadow mid-turn · back-face content on turning page · "Chapter N" framing per feature · watercolor noise on flats · tipped-in plates for screenshots · gold endpaper finale.

Anti-patterns: hard cuts (book never closes until the end), sans-serif body text, neon, fast motion, more than one page turn animating at once.
