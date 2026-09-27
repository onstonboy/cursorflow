# App Promo Video — 50 Style Catalog (INDEX)

Each style = a distinct IMPLEMENTATION, not a reskin. This file is the **index** — read it to choose. Every style has a **full spec file** at `styles/NN-<slug>.md` (tokens, core-mechanism code, scene grammar, audio recipe, anti-patterns) — read that file to build.

Shared pipeline (script → edge-tts → numpy music → Remotion → asplit mix → whisper verify) always applies; only the visual/animation/audio technique changes.

Notation per entry: **vibe** · **fits** · **build** (the differentiating technique) · **signature** (motion/audio).

---

## A. Typography-led (words are the footage)

**01 — Minimalist Editorial.** Calm premium. Fits: wellness, finance-lite, premium tools. Build: flat ivory `#FAF8F4` bg, charcoal text, hairline rules; layout from a 12-col bento grid, cards are flat color blocks, zero gradients/shadows/particles; screenshots unframed with 1px border. Signature: only fades + 24px rises, Inter/Tiempos serif headline mix; felt-piano music 60 BPM; VO slow, whisper-adjacent.

**02 — Brutalist Terminal.** Raw engineering. Fits: devtools, security, CLI apps. Build: JetBrains Mono everything; borders via CSS `border:2px solid`, ASCII box-drawing decorations, visible 8px grid, registration marks in corners; elements snap in with `steps(4)` easing (no smooth tweens). Signature: red stamp labels rotate -6°, typewriter VO, glitch-hit SFX, square-wave music.

**03 — Kinetic Type.** Hype reel. Fits: entertainment, social, sports. Build: no components — one huge word/phrase per beat, per-letter stagger (index×2 frames), motion-blur via fast translate + `filter: blur()` fading; screenshots appear only in final 15% inside a phone. Signature: beat-locked cuts to 128 BPM phonk/electronic; VO punchy short lines; bg = flat color flashing per scene.

**04 — Swiss International.** Disciplined modernist. Fits: productivity, B2B SaaS, news. Build: visible thin grid lines as actual divs; strict baseline type (Helvetica/Inter Tight), red `#E30613` + black + white; exactly ONE accent may break the grid. Signature: wipes along grid axes only (translateX/Y), no rotation; metronome-tight minimal techno.

**05 — Duotone Halftone.** Bold poster. Fits: fitness, sports, music events apps. Build: two brand colors only; screenshots processed beforehand to 2-color halftone (imagemagick `-dither`); giant skewed numerals (-8°) as section markers. Signature: hard cuts on every beat, impact-VO, drum-heavy 140 BPM.

**06 — Countdown Teaser.** Pre-launch mystery. Fits: launches, waitlists. Build: split-flap numeral component (two halves, top flips via rotateX with backface-hidden); reveals nothing but numerals + one line of copy per beat; screenshot only in last 5s. Signature: ticking SFX, rising drone, VO sparse.

**07 — Broadcast News.** Information urgency. Fits: news, finance, sports scores. Build: lower-third nameplates slide in (translateX + skew), top ticker marquee via infinite translate, corner "bug" logo; feature cards framed as "segments" with red LIVE dot. Signature: punchy news-sting stingers between scenes, authoritative VO.

**08 — Meme/Changelog.** Self-aware comedy. Fits: consumer apps targeting Gen Z, indie apps. Build: Impact-font top/bottom captions on screenshots, record-scratch freeze frames (`playbackRate`-style jump cuts), intentionally abrupt holds, "wait that's it?" beats. Signature: VO conversational with jokes + self-deprecation, comedic pause timing, trap-lite beat.

---

## B. Tactile / analog material simulation

**09 — Paper Cutout.** Crafted warmth. Fits: kids, family, journaling. Build: every element a paper card — layered `box-shadow` for cut-edge depth, slight rotate ±2°; fake stop-motion: animate transforms in `steps()` and hold each pose 4–5 frames; paper grain overlay PNG (procedural noise). Signature: ukulele/glockenspiel 90 BPM, page-rustle SFX.

**10 — Risograph Collage.** Indie zine. Fits: creative tools, photo apps, fashion. Build: screenshots duplicated 3× with `mix-blend-mode: multiply` in cyan/magenta/yellow, offset 6–10px misregistration, heavy grain overlay; torn-edge masks via `clip-path` polygon. Signature: jazzy lo-fi 85 BPM, tape-stop transitions.

**11 — Doodle Sketch.** Friendly explainer. Fits: education, productivity, health. Build: SVG annotation layer over clean layouts — circles, arrows, underlines drawn via `strokeDashoffset` interpolate; "hand" pointer (SVG) follows the drawing; screenshots get doodled highlights. Signature: acoustic guitar, marker-squeak SFX, teacher-tone VO.

**12 — Chalkboard.** Classroom. Fits: learning, language, STEM apps. Build: dark green `#2D4A3E` textured bg, chalk font (Caveat/Kalam), white "dust" particles falling, chalk smear transitions (blur + wipe); diagrams draw like chalk strokes. Signature: soft piano, chalk-scratch SFX, warm VO.

**13 — Blueprint.** Engineering precision. Fits: architecture, CAD-adjacent, fintech infra, security. Build: cyan-on-blue `#1B3A6B` reversed palette; hairline dimension lines with arrows annotate UI; exploded phone mockup (parts offset along Z-fake); crosshair follows a scanning path. Signature: ambient synth pad, servo SFX, precise VO.

**14 — Origami Fold.** Elegant reveal. Fits: premium/lifestyle, meditation, design tools. Build: `perspective` + rotateX/rotateY folds — cards fold up from flat (rotateX -90→0 with transform-origin edge); shadows darken during fold for realism. Signature: shakuhachi/harp, paper-crease SFX, slow VO.

**15 — VHS / CRT.** Nostalgia. Fits: retro games, music, photo-filter apps. Build: every frame rendered normally then overlaid: RGB split (3 tinted copies, `mix-blend-mode: screen`, ±3px offset), horizontal tracking band scrolling, scanlines via repeating-linear-gradient, timestamp "PLAY ▶ 0:00:12" corner; whole video letterboxed 4:3 inside 16:9 at open, expands. Signature: synthwave 100 BPM, tape-wow pitch drift on music, VO slightly reverbed.

**16 — Film Noir.** Dramatic privacy/mystery. Fits: security, finance, thriller-genre apps. Build: strict B/W + one accent (amber); radial spotlight mask follows content, venetian-blind shadow bands (repeating-linear-gradient rotate 20°) drifting; smoke haze via blurred slow divs. Signature: jazz bass + brushed drums 70 BPM, low conspiratorial VO.

**17 — Scrapbook Polaroid.** Personal memory. Fits: photo, journal, family apps. Build: screenshots cropped into polaroid frames (white padded card, handwriting caption), drop onto "desk" bg with rotate + shadow; tape strips, pins; camera slowly pans/zooms across the desk (one big translated container). Signature: warm folk 100 BPM, soft shutter SFX.

**18 — Comic Manga.** Action energy. Fits: gaming, social, manga/anime-adjacent apps. Build: thick black panel borders slam in sequence; speed-line background (conic-gradient repeat) behind feature cards; screentone dot fills; "ゴゴゴ"-style impact words. Signature: taiko-hit transitions, excited VO, 150 BPM.

---

## C. Motion-architecture (structure IS the style)

**19 — Isometric World.** Systemic product. Fits: smart-home, finance ecosystems, productivity suites. Build: a ground plane `transform: rotateX(55deg) rotateZ(45deg)`; cards/screens stand on it as extruded slabs (3 stacked offset copies = fake depth); camera = single container translating/zooming across the iso map visiting 5 "stations". Signature: cozy synth 95 BPM, pop SFX on each station.

**20 — Infinite Zoom.** Wow-factor montage. Fits: photo/AI/creative apps. Build: nested `AbsoluteFill`s each scaled to fill parent at a focal point; every scene ends zoomed 6–8× into a detail that IS the next scene's start (plan zoom targets at design time). Signature: continuous rising pad, whoosh per transition, no hard cuts.

**21 — Endless Feed Dive.** Social-native. Fits: social, content, dating apps. Build: cards of fake-but-branded content scroll vertically past camera (translateY), camera accelerates then "dives" INTO one card which expands to reveal real screenshot; streak of like-hearts trail behind. Signature: hyperpop 150 BPM snippets, swoosh, energetic VO.

**22 — Split-Screen Before/After.** Problem→solution clarity. Fits: utilities, cleaners, health, finance. Build: a vertical divider bar with handle glyph sweeps left→right; left side desaturated/problem, right side branded color/solution; mid-video the ratio animates 50/50→20/80. Signature: whoosh on each wipe, ticking→resolved chord shifts.

**23 — Micro-Interaction Montage.** Craft-obsessed. Fits: design-forward apps, premium consumer. Build: extreme close-ups only — crop screenshots 300–400% on ONE control (a toggle, a keyboard key, a FAB); each beat = macro detail + click/haptic SFX + one word; VO minimal. Signature: silence-forward mix, ASMR UI sounds, sparse piano.

**24 — Split-Flap Departure Board.** Retro info display. Fits: travel, transit, events. Build: character-flip component (like 06 but per-CHARACTER cascade across whole words); route-style rows list features; screenshot arrives as a "destination". Signature: flap-click cascade SFX, upbeat lounge.

**25 — Game-Parody Runner.** Features as levels. Fits: habit, finance gamified, kids, fitness. Build: side-scrolling world (parallax 3 layers), features as floating "items" the avatar (product mascot/icon) collects; HUD = hearts/coins counting real benefits; level-complete jingle between scenes. Signature: chiptune 140 BPM (numpy square+triangle waves), 8-bit SFX.

**26 — Domino Chain.** Cause→effect demo. Fits: automation, workflow, integration apps. Build: cards/tiles placed along a path; each "falls" (rotate ±70° origin-bottom) triggering next with 4-frame delay; chain passes through screenshots that spin into place. Signature: clack SFX per tile, marimba groove.

**27 — Orbit Diagram.** Connected features. Fits: suites, ecosystems, platforms. Build: product icon center; feature nodes orbit on circular paths (rotate container + counter-rotate node); zoom into a node → it expands to screenshot scene; pull back out for next node. Signature: ambient orbit hum, whoosh in/out.

**28 — Storybook Page-Turn.** Narrative. Fits: kids, sleep stories, reading apps. Build: book metaphor — each scene a page, transition = rotateY from right edge with page shadow curve (gradient sweep during turn); watercolor-flat illustrations (flat shapes + soft noise). Signature: music-box, page-turn SFX, storyteller VO pace.

---

## D. Dimensional / light-play

**29 — Glassmorphism Aurora.** Premium soft. Fits: finance premium, health, AI assistants. Build: animated gradient blobs behind; every card `backdrop-filter: blur(18px)` + `rgba(255,255,255,0.08)` fill + 1px inner-highlight border; screens float inside frosted frames, parallax layers at 3 depths. Signature: airy pad 75 BPM, soft VO.

**30 — Claymorphism 3D-Look.** Squishy friendly. Fits: kids, habit, casual consumer. Build: simulated clay via stacked shadows (`inset 4px 4px 8px white + inset -4px -4px 8px rgba(0,0,0,.15) + drop`), pastel palette, rounded-3xl everything; squash-and-stretch entrances (scaleX/scaleY overshoot). Signature: bubbly synth-pop, boing SFX, giggly VO.

**31 — Three.js Device Orbit.** Flagship-cinematic. Fits: premium flagship apps, fintech, health hardware companions. Build: `@remotion/three` + react-three-fiber: phone mesh (box + extruded bezel), screenshots as textures on the face; camera dollys/orbits with `CameraShake`-style drift; env lighting via gradient env-map; scenes alternate orbit shots vs full-screen feature typography. Signature: orchestral-hybrid swell, sub-bass hits.

**32 — Hologram Float.** Futuristic. Fits: AI, AR, devtools, space/science apps. Build: UI/screens float tilted on dark bg; cyan-magenta edge chromatic offset; scanline sweep travels down each card; bloom via blurred copy beneath; elements bob with sin(t) ±6px. Signature: airy synthwave + shimmer SFX, slightly reverbed VO.

**33 — AR Desk Overlay.** Product in your space. Fits: utilities, camera, home, education. Build: background = subtle radial gradient "room" + fake vignette + handheld drift (random-walk translate ±4px); UI cards pinned to fake perspective floor grid, cast soft contact shadow; hand-cursor taps trigger ripples. Signature: clean minimal electronic, tap SFX.

**34 — Neon Arcade.** Night energy. Fits: music, nightlife, gaming, dating. Build: deep `#0A0014` bg; all strokes glow via stacked `text-shadow`/`box-shadow` (0 0 8, 0 0 24, 0 0 48); perspective grid floor scrolling toward horizon; chrome-text headline (gradient metal). Signature: synthwave 110 BPM, laser zaps.

**35 — Liquid Morph.** Organic fluid. Fits: wellness, period/health, drink/food, sensual brands. Build: blob shapes via animated `border-radius` (8-value asymmetric, interpolate between keyframe shapes) morphing between feature icons/colors; metaball merge illusion via two blurred circles converging then deblur. Signature: liquid ambient, drop SFX, slow VO.

**36 — Particle Constellation.** Tech-poetic. Fits: AI, network, data, security. Build: seeded pseudo-random dots + lines (pure divs, no canvas); particles fly from scatter → assemble into logo/screenshot silhouette (interpolate each dot scatter→target with per-dot delay); slight connect-line flicker. Signature: ambient pads swell at assembly, data-blip SFX.

---

## E. Camera / capture simulation (feels "shot", not animated)

**37 — Live Cursor Demo.** Product truth. Fits: SaaS, productivity, any "show don't tell" product. Build: REAL screen capture (record simulator walkthrough) as `<Video>`; overlay SVG cursor following a scripted spline (cubic-bezier waypoints), click = ripple + state-change synced to footage; punch-in zooms (scale + translate) on detail moments. Signature: minimal beat, click/keystroke SFX, explainer VO.

**38 — Documentary Handheld.** Authentic startup-story. Fits: mission-driven, health, education, indie. Build: entire video inside a slight random-walk handheld transform (±0.6% translate/rotate, low-freq noise); rack-focus moments (blur 6px→0 pulls); interview lower-thirds "FEATURE — 01"; screenshots pushed in with Ken Burns drift. Signature: acoustic ambient, room-tone, intimate VO.

**39 — Phone-in-Hand Mock.** Real-world context. Fits: consumer, lifestyle, dating, food. Build: hand-drawn SVG/PNG hand holding phone frame; background = blurred gradient "environment" that changes per scene (cafe warm, night purple); phone tilts slightly; UI screenshots slide into the phone screen. Signature: pop 105 BPM, ambient café noise low in mix.

**40 — Surveillance/Spy Cam.** Thriller privacy angle. Fits: security, VPN, privacy apps — darker sibling of Midnight Playground. Build: corner "CAM 03 ● REC" overlays, green-tinted night-vision gradient on mock "captured" screens, target-lock brackets tracking a chat bubble; reveal flips to clean branded UI. Signature: tension drones, UI beep locks, hushed VO.

**41 — Projection Room.** Gallery screening. Fits: portfolio, creative, photo/video apps. Build: dark room; scenes projected on a wall plane (perspective-skewed container, slight barrel feel via border-radius shadow), dust motes in light cone; cuts like a slide projector (white flash + clunk). Signature: reverb-heavy piano, projector-clack SFX.

**42 — Weather Window.** Mood = weather. Fits: weather (obviously), mindfulness, journal. Build: each scene a sky gradient (dawn/noon/dusk/storm) with parallax cloud layers (translucent blobs at 3 speeds), occasional rain streaks or sun rays; content on translucent pane "window"; state changes match feature mood. Signature: ambient nature bed, gentle VO.

---

## F. Data / system realism

**43 — Fintech Trust.** Clean authority. Fits: banking, investing, insurance, expense. Build: light theme `#F6F8FB`; animated SVG line/bar/donut charts (strokeDashoffset + path morph), number count-ups with `interpolate`; card components get subtle top-border accent; screenshot inside slim device with chart echoes behind. Signature: confident minimal electronic 90 BPM, clear VO, coin-tick SFX.

**44 — Broadcast Dashboard.** Live ops. Fits: analytics, sports, monitoring, trading. Build: multi-panel grid that rearranges (grid cells animate FLIP-style via measured translates); each panel a mini visualization; status LED dots pulse; big KPI numerals roll. Signature: pulses on data tick, VO terse.

**45 — ASCII Cinema.** Dev poetry. Fits: devtools, CLI, hacker/security. Build: PREPROCESS screenshots to ASCII art (python: resize→luminance→char map, output to txt); render mono `<pre>` that types itself; color = phosphor green or amber; transitions = screen clear + retype. Signature: hum + fan noise, modem SFX, VO optional (often text-only works).

**46 — Diff/Patch Reveal.** Engineering audience. Fits: devtools, API products. Build: content presented as a "diff" — before-lines slide left and fade while after-lines slide in green-highlighted; line-number gutter; commit-hash scene markers (`a1b2c3 — feat: onboarding`). Signature: keyboard clacks, subtle synth pad.

**47 — Node Graph Flow.** System thinking. Fits: automation, integration, no-code, AI pipelines. Build: features as labeled nodes connected by animated bezier paths (SVG path `strokeDasharray` flow dashes); packet dots travel along edges triggering node "activation" (glow + screenshot popover). Signature: plucky electronic, packet-zip SFX.

---

## G. Emotion / audience-shaped

**48 — Sleep Breath.** Pre-bed calm. Fits: sleep, meditation, anxiety, baby apps. Build: EVERYTHING moves at breathing tempo — a single master sine `Math.sin(f/90)` drives scale 1→1.03, opacity 0.85→1, glow intensity; indigo-deep palette; max one idea per 10s; VO at ~85% speed with long pauses. Signature: 432Hz-ish drone pad, no percussion, ocean noise.

**49 — Fitness Pulse.** Sweat energy. Fits: fitness, sports, dance. Build: beat-detection-fake — all motion quantized to 132 BPM grid; big counters roll for stats; screen "shakes" ±3px on drop moments; progress ring fills per benefit; color flashes on beat. Signature: EDM/phonk, countdown VO shout, airhorn-lite.

**50 — Cozy Home Evening.** Comfort domestic. Fits: food/recipe, home, family, dating-lite. Build: warm palette (cream/terracotta/olive), lamp-glow radial vignette flickering subtly, steam particles rising (blurred divs), content on soft cushions of whitespace; scenes "settle" — everything lands and stays, no exits. Signature: lo-fi with vinyl + rain, warm close-mic VO.

---

## Choosing quickly

| App genre | Try first |
|---|---|
| Social/Gen Z utility | 00 Midnight Playground, 08, 21 |
| Fintech | 43, 29, 13 |
| Health/wellness | 48, 35, 01, 42 |
| Fitness | 49, 05, 03 |
| Kids/education | 09, 12, 28, 30 |
| Devtools/security | 45, 02, 40, 36 |
| AI | 36(→32), 32, 47, 27 |
| Photo/creative | 10, 41, 17, 20 |
| Travel/food | 24, 22, 50 |
| News/finance-data | 07, 44, 04 |
| Premium flagship | 31, 23, 29 |
| Gaming/entertainment | 34, 18, 25, 03 |
| Dating/social | 21, 34, 39 |
| Productivity/SaaS | 37, 04, 01, 26 |
