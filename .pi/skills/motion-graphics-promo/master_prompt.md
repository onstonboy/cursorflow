# MASTER PROMPT — Cinematic, High-Density Motion Graphics Video (Agent Edition)

> Copy everything below the line into your AI agent. Fill in the `{{VARIABLES}}` block first.
> The agent must have: a shell, file write access, Node.js ≥ 18, ffmpeg, Python 3 (numpy), and web access.

---

## 0. INPUT VARIABLES (fill these in)

```
PRODUCT_NAME       = {{e.g. "MaskShot"}}
PRODUCT_URL        = {{e.g. https://maskshot.chuongle.dev}}
EXTRA_SOURCES      = {{store links, local repo path, screenshot folder, brand guide — or "none"}}
DURATION_SECONDS   = {{15 | 30 | 45 | 60}}
ASPECT_RATIOS      = {{"16:9 1920x1080" and/or "9:16 1080x1920" and/or "1:1 1080x1080"}}
FPS                = {{30 or 60 — default 30}}
LANGUAGE           = {{on-screen text language, default English}}
STYLE_DIRECTION    = {{optional preset name from §4.3 or §4.5 (e.g. "S7 Liquid Chrome"), free text, or "auto" / empty → run the §4.6 detection procedure}}
REFERENCE_VIDEO    = {{optional path/URL — if given, extract frames (ffmpeg fps=1 contact sheet + full-res keyframes), analyze its palette/type/motion/transition grammar, and adopt it as the style direction while keeping all content product-specific}}
VOICEOVER          = {{none | TTS | provided file}}   (default: none — music + SFX only)
MUSIC              = {{procedural (default, zero licensing risk) | provided file path}}
OUTPUT_DIR         = {{e.g. ./out}}
```

---

## 1. ROLE & MISSION

You are a **senior motion designer + creative director + front-end engineer** in one. You make award-level, cinematic, **extremely kinetic** motion graphics in code. Your job is to research `{{PRODUCT_NAME}}`, write the script yourself, design a visual system, animate it frame-by-frame, score it with music and sound effects, render it, and QA it until it looks like a top-tier agency made it.

The target feel: **"dopamine-dense" motion design**. Every frame is alive. There is always something moving, always a layer drifting, always a camera move, always a next beat arriving. The viewer should feel they *cannot look away* and that there is more detail than they can absorb in one viewing — yet the message stays crystal clear. Think Apple keynote product films × Buck/ManvsMachine kinetic type × high-end SaaS launch videos — or, if a reference video is provided, match its observed style (see §4.4).

**100% motion graphics.** No stock footage, no live action, no AI-generated video clips, no talking heads. Everything is designed and animated: typography, shapes, UI, icons, particles, 3D-ish planes, data, real product screenshots placed in animated device frames.

Work autonomously. Do not stop to ask questions unless a required input is literally missing. When unsure, make the bold, tasteful choice and document it.

---

## 2. NON-NEGOTIABLE MOTION RULES (the "always moving" contract)

These are hard rules. Treat violations as bugs.

1. **Zero dead frames.** On every single frame, at least **3 independent things** are moving (e.g. camera drift + background particles + a foreground element). Check this during QA by sampling random frames.
2. **No static hold longer than 8 frames (@30fps)** on any hero element. Even "hold" moments get a slow push-in (scale 1.00 → 1.04), a drift (2–6 px/s), a shimmer, or a breathing glow.
3. **The camera never stops.** Wrap every scene in a virtual camera with continuous micro-movement: slow dolly (scale), subtle pan, slight rotateX/rotateY in perspective, plus hard camera moves (whip, zoom-through, push) on transitions.
4. **Every element enters AND exits with animation.** Nothing pops in or disappears on a cut. No fade-only entrances for hero elements — use masks, scale+blur, slides, per-letter reveals, path draws, flips, morphs.
5. **New visual idea every 1.0–2.5 seconds.** A 15s video contains **8–14 distinct beats**; a 30s video 16–26 beats. A "beat" = a new composition, new text, new device state, or major transformation.
6. **Transitions are designed, never default.** Minimum 70% of scene changes must be *motivated* transitions (match-cut, element morphs into next scene, zoom-through a shape, whip-pan with motion blur, mask wipe using a brand shape, light flash on a musical hit). Plain crossfades are allowed at most once per video.
7. **Layered depth on every shot**: minimum 4 layers — (a) animated background (gradient field / grid / noise), (b) mid-ground graphic system (shapes, lines, particles), (c) hero content (type/UI/device), (d) foreground accents (bokeh, sparks, light streaks, grain, vignette). Each layer moves at a different speed (parallax ratio roughly 0.2 / 0.5 / 1.0 / 1.4).
8. **Everything is on the beat.** Pick a BPM (typically 110–128). All major hits land on beats; sub-animations land on 1/2 or 1/4 beats. Every visual impact has a matching sound effect within ±1 frame.
9. **Stagger everything.** Lists, letters, tiles, particles, and UI rows animate with staggered offsets (1–3 frames apart), never all at once.
10. **Overshoot and settle.** Hero entrances use springs or back-out easing with visible overshoot (5–15%) and settle. Nothing moves linearly except continuous drifts, tickers, and rotations.
11. **Motion blur on fast moves.** Anything moving > ~40 px/frame gets directional blur (CSS `filter: blur()` scaled by velocity, or smear frames / duplicated trailing copies at decreasing opacity).
12. **Readability beats spectacle.** Every text line stays fully readable for at least `0.25s + 0.06s × word_count` before it starts exiting. Max ~7 words per line on screen at once, max 3 lines.

---

## 3. PHASE 1 — RESEARCH (do this before any design)

1. Open `{{PRODUCT_URL}}` and every relevant subpage. Also read `{{EXTRA_SOURCES}}`.
2. Extract and write to `research.md`:
   - One-sentence product definition (what it is, for whom).
   - The **core pain** it solves and the **core promise**.
   - 3–5 key features, each rewritten as a punchy 2–5 word headline + one 6–10 word support line.
   - Hard proof points: numbers (downloads, ratings, users, speed, counts of features, languages, % metrics). Never invent numbers. If none exist, use product-true quantities (e.g. "3 taps", "0 uploads", "18 effects").
   - Brand tokens: primary/secondary colors (sample from logo & UI), fonts if identifiable, icon style, tone of voice.
   - Available real assets: app icon, logo, screenshots (download highest resolution available; for App Store images replace the size suffix with a large size such as `1290x2800bb.png`).
3. Asset hygiene:
   - If screenshots are marketing frames with a phone already drawn in, **crop out only the screen** so you can place it in your own device frame. Measure crop boxes carefully (draw a percentage grid over the image, then crop). Never show a phone inside a phone.
   - Store every asset under `public/<project>/` with clean names (`icon.png`, `scr_1.png` …).
   - Never use emoji glyphs in renders (headless Chromium often can't draw them) — use SVG icons.

---

## 4. PHASE 2 — CREATIVE DIRECTION

Write `direction.md` containing:

### 4.1 Concept
- A **one-line creative concept** that turns the product's function into a visual metaphor (e.g. privacy app → "a laser scan that finds secrets and stamps them out"; habit app → "tiles that flip alive"; decision app → "the wheel decides"). The opening 3–4 seconds must *dramatize the product's core action* with pure graphics — this is the hook.
- The emotional arc: **Tension/Problem → Reveal/Drop → Proof → Features → Promise → Brand lockup**.

### 4.2 Visual system
- **Palette**: 1 background base, 2 accents (gradient-capable), 1 "flash" color (for impact frames), text + muted text. Define light or dark theme to match the brand.
- **Typography**: exactly 1 display face + 1 body face (Google Fonts). Choose a display face with character that fits the product (e.g. Orbitron for LED/tech, Fraunces for playful premium, Instrument Serif for inspirational, Space Grotesk for dev/privacy, Barlow Light for Metro/minimal, Fredoka/Baloo for playful games, Nunito for soft/family). Define a type scale: hero 140–300 px, headline 90–120 px, kicker 24–30 px with wide letter-spacing (6–10 px), body 30–40 px (values for 1080-short-side; scale by `min(width,height)/1080`).
- **Graphic language**: choose 3–5 recurring motifs (e.g. dot grid, rounded pills, thin 1px lines, rings/shockwaves, glowing particles, brackets, crosshairs, scanlines, blobs). Reuse them everywhere for cohesion.
- **Texture**: film grain overlay (animated noise, 5–8% opacity, overlay blend), vignette, soft glow on accents, optional chromatic aberration only on impact frames.
- **Motion language**: define the signature easing set (see §7) and 2–3 signature moves unique to this video (e.g. "everything implodes into a glowing dot then bursts", "letters drop in like LED pixels", "cards flip on every downbeat").

### 4.3 Style presets (quick table — for the full library and auto-selection see §4.5–4.6)
| Preset | Look | Signature motion |
|---|---|---|
| Dark Tech Neon | near-black, electric accent, glow, grid | scanlines, glitch slices, laser sweeps, HUD brackets |
| Swiss Kinetic | off-white/black, one bold color, huge grotesk type | hard mask wipes, type as layout, grid snaps |
| Soft 3D Pastel | pastel gradients, rounded glossy shapes | squash & stretch, bouncy springs, floating objects |
| Luxury Editorial | black/ivory/gold, serif display | slow elegant push-ins, light sweeps, letter-spacing breathes |
| Retro Terminal | green/amber on black, mono font | typewriter, cursor blink, scramble decode, CRT flicker |
| Playful Arcade | saturated primaries, chunky rounded type | pops, counters, confetti, coin bursts, screen shakes |
| Calm Wellness | light warm neutrals, soft greens/blues | gentle floats, breathing scale, soft ripples, no shakes |
| **Lab Instrument / Kinetic Lyric** ⭐ | near-black, 1px white technical linework, one hot accent (orange/red), mono data readouts | word-by-word lyric sync, HUD panels, schematics, chromatic aberration, glitch crops (see §4.4) |

### 4.4 Observed reference style — "Lab Instrument / Kinetic Lyric"
Use this when the reference video is the dark, technical, lyric-synced style (verified from frame analysis):

- **Canvas**: pure near-black (#050505). Fine animated film grain + vignette. Frame corners carry thin **viewfinder/crop-mark brackets** that sometimes subtly re-frame.
- **Technical linework backgrounds**: rotating polar/radar plot grids with degree markings and glowing radial axes; topographic contour fields (concentric elevation rings that slowly morph); dotted construction lines connecting elements; blueprint schematics of objects/creatures drawn in thin glowing strokes with joint nodes, like engineering rigging diagrams; wireframe figures shaded with topographic banding; a recursive "endless tiled corridor" room built from repeating white cell outlines in 3-point perspective.
- **Type**: heavy grotesk display, all-caps, tight leading. Words appear **one or two at a time, exactly on the lyric/spoken beat**, then accumulate or swap. One word per phrase is accented (solid orange) or outlined/glitch-struck. Occasional giant words cropped by the frame edge, mirrored copies, or words rotated upside-down. Subtle **chromatic aberration** (RGB fringe) on type at all times; stronger on impacts.
- **Instrumentation HUDs**: monospace panels that look like a running experiment — token-probability tables (`p(next|context)` with per-token % bars), a glowing "P(doom) 0.14" readout, checkpoint tables, an oscilloscope waveform trace, corner metadata (`PROMPT 01 · T 0.7 · top-p 0.95 · seed 0x2A`). Numbers tick/flicker as if live. For a product video, feed these panels **real product data** (stats, feature counts, live-looking values) instead of fake ML internals.
- **Terminal moments**: a `>` prompt types the current line character-by-character with a block cursor, key-click SFX, then the line graduates into big display type.
- **Collage inserts**: occasional flat/iconic object (e.g. a balloon with a smiley) rendered in a contrasting style, framed by thin annotation lines.
- **Camera**: constant slow push/rotate on the technical fields; hard flips between diagram views; occasional violent zooms into a chart element that becomes the next scene. Small chromatic-aberration pulses on every downbeat.
- **Transitions**: flash/leak bursts, zoom-through into a plot axis or waveform, schematic morphing into the next diagram, type staying on screen while the entire background system swaps under it.
- **Density**: every corner of the frame has micro-information (readouts, tick marks, annotations) — but hero type stays dominant and readable.

### 4.5 Extended style library — 100 signature directions

Full specs like §4.4. Pick ONE as the primary style (a second may contribute 1–2 borrowed moves). Every style still obeys §2 — always moving, camera never still, every hit on beat. S1–S10 have long-form specs; S11–S100 use the same fields compressed into one paragraph each (Canvas / Graphics / Type / Signature moves / Transitions / Audio / Best for).

**S1 · Exploded Blueprint.** Canvas: blueprint cyan `#0B3B5E` or warm drafting paper `#EDE4D3`; white/sepia linework, one accent thread (red correction pencil). Graphics: the product's UI drawn as an **axonometric exploded assembly** — panels, nav bars, cards float apart along the Z axis with dimension lines (`↔ 390pt`, `↕ 844pt`), part numbers in circles, and a "BILL OF MATERIALS" parts list that ticks off items as they slot in. Type: stenciled technical caps + hand annotation script. Signature moves: assemblies exploding/recombining on the beat, dimension arrows sliding to measure things, a compass drawing arcs that become scene elements, section-cut wipes. Transitions: fold-up like a drafting sheet turning; zoom along a dimension line into the next part. Audio: precise mechanical clicks, pencil scratches, ruler taps, paper rustle, metronomic ticks. Best for: productivity, dev-tools, finance, anything "engineered".

**S2 · Paper Craft Cutout.** Canvas: kraft/cream paper with visible fiber grain; spot colors as printed ink. Everything looks **cut from paper** — slightly rough edges, drop shadows 2px below, masking-tape corners, staple pins, torn-edge reveals. Type: bold display face "printed" on paper scraps that are taped/dropped into frame; occasional rubber-stamp words pressed with a twist. Signature moves: stop-motion timing (move in 2s and 3s — hold poses 2–3 frames), hand-like nudges, fold-out tabs, pop-up layers lifting on paper springs, characters/cards sliding as if pushed by an off-screen finger. Transitions: a hand swipes the scene away like a scrapbook page; new scene folds in. Audio: paper slides, scissor snips, tape peels, stamp thunks, gentle lo-fi music. Best for: family, journaling, recipes, habit/lifestyle, kids.

**S3 · Neon Nocturne.** Canvas: wet-night near-black with deep blue/indigo grade; hot pink/cyan/lime neon accents reflecting on an implied wet floor (mirror-glow gradients at the bottom of frame). Graphics: neon tube outlines that flicker on letter-by-letter with buzz SFX; rain streak particles; light leaks and anamorphic flares crossing the frame on impacts; chrome signage panels with humming transformers. Type: neon tube lettering (drawn-on stroke animation) + small mono "OPEN 24H"-style captions. Signature moves: slow cinematic lateral dolly; neon elements flickering alive one by one; reflections warping; a car-headlight sweep that wipes the scene. Transitions: flare burns white → next sign buzzes on; rain-wipe; shutter drag with motion-trail neon. Audio: synthwave/retrowave pad, analog hum, neon buzz, distant rain, low whooshes. Best for: music, nightlife, dating, games, dark-mode products.

**S4 · Data Garden.** Canvas: soft deep green-black or warm loam; ivory + living green + one bloom color. Graphics: **everything grows** — vines creep along ruled paths and bloom into UI cards; nodes sprout as stems and connect into networks; particles swarm like spores/fireflies; charts are grown (a bar rises like a stalk, rings open like petals); concentric ring systems pulse like growth rings. Type: elegant serif or soft grotesk revealed by growing stems/underlines; labels attached to leaves. Signature moves: time-lapse growth (vines draw themselves with leaf sprout accents on each beat), flowers blooming as data points, roots spreading under stats, a whole scene composting into the next. Transitions: growth — a vine from the old scene becomes the spine of the new one; bloom-out white flash. Audio: plucked acoustic tones, soft chimes, birdsong textures, gentle swelling pads. Best for: wellness, mindfulness, gardening, habit-trackers, health, education.

**S5 · Retro Broadcast.** Canvas: living inside a TV — slight barrel vignette, scanlines, chroma fringe, noise. Graphics: the video runs as a **channel-surf**: each scene is a "channel" (CH-01 FEATURE, CH-02 STATS) with a channel-bug in the corner and a timestamp; broadcast test cards, color bars, "PLEASE STAND BY" slates between acts; 4:3-safe inner frame that occasionally punches out to full frame on impacts. Type: VHS-title font + broadcast lower-thirds, tracking-glitch offsets, closed-caption strips that type live. Signature moves: channel-flip zaps (snare + static burst), horizontal sync slips (image shears and rolls), tracking noise bands crawling, rewind/fast-forward stutters, VCR pause freeze with jitter. Transitions: literally change the channel — static burst, sync roll, new scene tunes in. Audio: filtered TV-speaker music that widens to full stereo at the drop, static bursts, channel clicks, tape hiss. Best for: entertainment, retro/lo-fi products, anything with personality.

**S6 · Riso Press.** Canvas: warm off-white; two spot inks (e.g. fluorescent pink + blue, or red + black) that **misregister** — layers deliberately offset 2–6px, overprinting to create a third color where they cross. Graphics: halftone-dot shading, ink squeeze edges, photocopy grain, registration marks, crop ticks, and a visible "second pass" where a layer re-prints slightly shifted. Type: huge condensed caps locked to a visible grid; words print twice with a few px offset; type fills with rolling halftone gradients. Signature moves: print-head passes (a bar sweeps and the graphic inks in behind it), misregistration drifts, ink-flood fills, layers peeling like fresh prints. Transitions: the sheet lifts off the drum to reveal the next print; a color pass wipes the frame. Audio: press clunks, roller swipes, ink hiss, rhythmic machine pulse that doubles as the beat. Best for: design tools, editorial/readers, creative apps, zine-culture products.

**S7 · Liquid Chrome.** Canvas: deep charcoal-to-black gradient; liquid metal (mercury/chrome) with razor highlights; one saturated accent (electric violet or acid green) refracting through the metal. Graphics: chrome blobs that morph, merge, and split; ribbons of liquid metal that form UI panels; refraction bands where background lines bend behind surfaces; specular streaks sweeping across on every beat. Type: type that extrudes from liquid metal — letters surface from a mercury pool, or chrome words pour and freeze. Signature moves: blob merge/split transitions, slow-mo splash ripples timed to bass, surface tension wobble on every pop, mirror flips. Transitions: the whole scene melts into a pool, a new scene condenses out of it; a droplet drops → ripple → reframed. Audio: deep sub pulses, metallic shimmers, glassy FM bells, slowed cinematic hits. Best for: premium/finance, AI products, wearables, anything "sleek flagship".

**S8 · Pop-Up Diorama.** Canvas: warm lit space (dark-to-warm gradient or paper-cream); flat-shaded isometric miniatures that **unfold like a pop-up book** — floors fold up from flat, walls hinge open, furniture/characters rise on paper tabs. Graphics: the product's world built as little diorama rooms (a "lesson room", a "streak garden", a "data workshop") on a visible stage; pull-tabs slide elements in; strings/pivots visible like a paper theater. Type: storybook display serif on folded banners; captions on little easel cards. Signature moves: fold-up builds on the beat (floor unfolds → walls → props → confetti from a pop tab), scenes closing flat and a new page flipping over, spotlights tracking inside each diorama. Transitions: page-turn — the whole diorama folds flat as the next page's stage rises. Audio: music-box or toy-orchestra cues, page flips, cardboard pops, small whooshes, tiny bell accents. Best for: kids, education, story apps, cozy/wholesome products.

**S9 · Survey Map.** Canvas: midnight cartographic navy or topo parchment; contour lines, coordinate crosshairs, grid squares, legend blocks with swatches. Graphics: the story is a **map survey** — camera top-down, cruising over terrain that is actually the product's features; route polylines draw themselves between landmark pins; each feature is a pin that drops with a bounce + elevation tag; a compass rose and scale bar live in the corner; distance rings radiate from waypoints. Type: cartographic caps + coordinate mono (`37°48'N 122°24'W` style readouts that count up as the camera moves). Signature moves: smooth map zooms (continent → city scale), pin drops with ring pulses, route lines drawing and animating dashes, terrain cross-section cuts, a "satellite sweep" line scanning features on. Transitions: relentless zoom — dive into a pin until its label fills the frame, pull back on the next map. Audio: ambient drone pads, sonar pings, radio beeps, paper-map rustle, deep "dive" whooshes on zooms. Best for: travel, delivery, fitness-tracking, logistics, real-estate, geo products.

**S10 · Monument Type.** Canvas: fog gradient (warm grey → black or ivory → stone); dramatic top light. Graphics: **letterforms as architecture** — a single giant word is the set; the camera orbits it like a monument while product UI floats in the letters' counter-spaces; stone/metal texture, dust motes in god-rays, small annotation lines scaling the letters ("height 47m"). Type: the message IS the 3D space — one word per scene carved monumental; secondary copy on floating marble slabs. Signature moves: slow orbital crane shots, letters assembling from stone blocks slamming into place (one per beat), letters crumbling/eroding into the next word, shadow of the word sweeping the floor as light moves. Transitions: the camera flies through a letter's counter into the next monument; a word topples into dust that forms the next scene. Audio: cathedral reverb, stone impacts, low choir/brass swells, deep rumbles — scored like a film trailer. Best for: flagship launches, finance, security, anything that should feel "epic/inevitable".

#### Materials & physics — S11–S20

**S11 · Stained Glass Cathedral.** Canvas: candlelit near-black; jewel tones (ruby, cobalt, amber, emerald) glowing like backlit glass, divided by black lead cames. Graphics: every UI element and word is **built as stained glass** — lead outlines draw first, then colored panes pour in and light up; sun shafts shift color as the camera pans; dust glitter in the shafts. Type: blackletter/roman caps formed by lead lines, then filled with glass color word by word. Signature moves: panes igniting in sequence on the beat, camera push through a giant rose window, candle-flicker luminance modulation. Transitions: a pane swings open like a door → next window; light-source sweep re-lights the next scene. Audio: choir pads, distant organ, glass dings, candle-room reverb. Best for: heritage brands, meditation, books/stories, craft products.

**S12 · Origami Fold.** Canvas: flat matte color fields with soft paper shadows; palette of folded-paper duo-tones. Graphics: everything **folds into existence** — a flat sheet creases along animated fold-lines and locks into cranes, boxes, panels; UI cards are folded paper constructions with visible crease maps. Type: caps formed by ribbon folds (each letter bends like a paper strip). Signature moves: reverse-fold reveals, whole scenes collapsing flat then re-folding into the next subject, unfold-chains across the screen on the beat. Transitions: the scene folds itself into an airplane/box and flies/slides off; the next scene unfolds from it. Audio: crisp paper folds, origami snaps, soft marimba, light air whooshes. Best for: education, kids, craft, minimal brands.

**S13 · Clay Lab.** Canvas: warm studio sweep; plasticine palette with visible fingerprints and tool marks. Graphics: **hand-molded clay** forms — blobs squash, stretch, get pinched and thumb-pressed into UI cards, buttons, mascots; wire-cutter slices reveal layers; coil-built letters. Type: thumb-pressed clay letterforms that squish when "touched". Signature moves: squash-and-stretch on every beat, fingers never shown but deforms imply them, stop-motion 2s timing, turntable slow-rotations of finished models. Transitions: a hand smears the scene flat into a new lump that rises as the next scene. Audio: squishes, pats, pops, soft playful percussion. Best for: kids, food, playful/cozy products.

**S14 · Kinetic Sand & Terrain.** Canvas: warm sand-beige or night-desert; raking light for relief. Graphics: **sand that behaves like liquid terrain** — dunes pile and get carved into shapes, lines of UI get raked into the surface, objects emerge as wind strips sand away, a buried screen is excavated brushstroke by brushstroke. Type: letters raked into the sand by a stylus, then eroded. Signature moves: excavation reveals, dune-pile builds, wind-streak erosion wipes, ripple pulses on each beat like footsteps. Transitions: sandstorm wipes; a gust uncovers the next scene. Audio: granular hiss, wind beds, soft tribal percussion, chime grains. Best for: travel, outdoor, history, wellness.

**S15 · Ferrofluid.** Canvas: black void; ink-black ferrofluid spikes lit with rim light; one neon accent in reflections. Graphics: **magnetic liquid** — smooth pools spike into crystalline cones on every beat; UI cards sit on ferrofluid pedestals that pulse with the bass; magnetic field lines drawn around elements. Type: liquid spike lettering that sharpens/softens with the music. Signature moves: beat-synced spike blooming, blobs climbing an invisible magnet, surface standing-waves. Transitions: the fluid drops flat and re-spikes into the next layout. Audio: deep analog synth drones, magnetic zaps, sub drops, metallic gurgles. Best for: audio apps, speakers, AI, science/edgy products.

**S16 · Loom Weave.** Canvas: dark loom-room or linen field; thread colors per brand. Graphics: **threads interlace** — warp lines stretch first, weft shuttles across on the beat, weaving fabric panels that ARE the UI cards; a selvage edge frames the viewport; stitch counters tick like a pattern draft. Type: cross-stitch lettering stitched on grid cells. Signature moves: shuttle passes with each snare, fabric panels tightening, loose threads pulling a new scene in. Transitions: the fabric rolls off like a finished bolt revealing the next weave. Audio: loom clacks in rhythm, thread whispers, folk string plucks. Best for: fashion, craft, heritage, slow-living products.

**S17 · Kiln Ceramic.** Canvas: studio warm-grey; glazed-ceramic palette (celadon, tenmoku, cobalt). Graphics: forms **thrown on a wheel** — clay cylinders spin and are pulled upward into vessels and panels on the beat; glaze pours and drips; kiln-fire glow transitions; crackle-glaze reveal lines spread like lightning. Type: sgraffito lettering scratched through slip. Signature moves: wheel-spin builds, glaze-drip fills, crackle reveals on impact frames. Transitions: a vessel is lifted → the next scene is inside it. Audio: pottery-wheel hum, wet clay slaps, kiln rumble, bell-like ceramic taps. Best for: food, coffee, home goods, mindful products.

**S18 · Parade Balloon.** Canvas: sky-blue or dawn gradient; huge soft matte balloons. Graphics: **everything inflates** — logos, letters, UI cards blow up with a rubbery bounce and float tethered; balloon knots, ribbon strings, subtle vinyl shine; some elements deflate and flap away. Type: balloon letterforms inflating one by one. Signature moves: pump-up bounces synced to kick, gentle buoyant float physics, tether-string pulls yank scenes in. Transitions: a balloon pops → confetti → next scene; or the camera tilts up following a rising balloon into the next sky. Audio: air pumps, rubbery boings, parade drums, cheerful brass. Best for: celebration, events, kids, cheerful consumer apps.

**S19 · Domino Rally.** Canvas: clean studio floor, macro lens feel; dominoes as the design unit. Graphics: **chain reactions** — domino lines topple across the frame spelling letters, knocking into ramps, releasing balls that trigger next elements; UI tiles stand up and fall in cascades. Type: rows of dominoes topple to reveal letters underneath. Signature moves: traveling topple waves on the beat, splits and merges of chains, camera tracking along the falling line. Transitions: the last domino knocks over the next scene's first element. Audio: dense rhythmic clacking, ramp rolls, percussive impacts, crowd-pleaser crescendos. Best for: fun/casual apps, games, productivity ("one tap starts everything").

**S20 · Clockwork Escapement.** Canvas: brass-on-dark horological palette; engraved plates. Graphics: **visible mechanics** — gears mesh, an escapement ticks the beat literally, springs coil, levers trip; UI cards are mounted on gear trains; jewel bearings and Roman-numeral chapter rings. Type: engraved serif caps etched onto brass plates. Signature moves: tick-tock beat-lock (escapement IS the metronome), gear-train builds, mainspring-release bursts. Transitions: a hatch opens mechanically, plates rotate like a tourbillon. Audio: precise ticks, gear whirs, chimes, slow cinematic swell under the mechanics. Best for: finance, productivity, luxury, precision products.

#### Retro & analog media — S21–S30

**S21 · Arcade CRT.** Canvas: dark arcade glow; chunky pixels, sprite grids, scanlines, slight CRT bulge. Graphics: **8/16-bit sprites** — pixel art versions of the app's screens jump onto platforms, coins pop stats, HUD score counters tick up, lives/levels as UI; occasional hi-res "cutscene" panel for the real screenshot. Type: pixel font, blink cursors, "INSERT COIN" pulses. Signature moves: sprite jumps landing on kick, coin-burst particle pops, screen-shake on combo, parallax platform layers. Transitions: level-complete iris-out, "GET READY" cards, warp-pipe dives. Audio: chiptune lead + noise drums, coin arps, jump zips, level fanfares. Best for: games, playful tools, retro-flavored products.

**S22 · Photocopy Punk.** Canvas: Xerox black-and-white plus one day-glo accent; heavy toner grain, edge burn, streak artifacts. Graphics: **collaged photocopies** — screens and words look machine-copied, slightly skewed, with toner shadows; torn edges, highlighter marks, rubber stamps, staple holes. Type: ransom-note cut caps + marker scrawl; type gets re-copied and degrades each pass. Signature moves: copy-machine light-bar sweeps that "print" the scene, repeat-copy drift (image recopied 3× more distorted each time), tape-down pastes on beat. Transitions: a fresh sheet feeds through and covers the last. Audio: machine hum + scan buzz, paper feeds, raw punk guitars or distorted drum machine. Best for: zine/skate/indie products, music, anti-polish brands.

**S23 · Cassette Rewind.** Canvas: dark shelf-lit room; warm tape-brown, neon label colors, handwritten stickers. Graphics: **tape decks and labels** — cassettes slide in and clunk, reels visibly spin, tape spaghetti unspools into lines that become charts; tracklist cards typewriter-stamped; VU needles bounce on the beat. Type: label-maker caps + marker handwriting on cassette J-cards. Signature moves: reel-spin sync to tempo, fast-forward squeal transitions, tape-ribbon trails drawing shapes. Transitions: tape pull — the magnetic ribbon drags the frame into the next scene. Audio: tape hiss bed, warm lo-fi beat, motor whirs, sped-up chipmunk rewind stingers. Best for: music, notes/journals, nostalgic products.

**S24 · Darkroom.** Canvas: safelight red glow; chemistry trays, hanging prints. Graphics: **photos develop live** — blank paper slides into developer and the app's screenshot fades up through chemical murk; prints hang on a line and drip; contact-sheet grids; dodge/burn masks sweep. Type: darkroom instruction labels + timer readouts. Signature moves: develop-in reveals (30%→100% density), hanging-print pegs dropping one per beat, enlarger light cone flickers. Transitions: the print sinks into fixer; a fresh sheet drops in. Audio: chemical sloshes, timer dings, dark ambient drone, photo-etcher hum. Best for: photo apps, galleries, film-flavored products.

**S25 · FM Dial.** Canvas: night-drive dashboard glow; amber/orange dial-light palette. Graphics: **a radio tuner crossing frequencies** — each station is a scene; the needle sweeps, static crackles between stations, frequency readout rolls; signal-strength meters pulse; station IDs flash like call letters. Type: LED-segment numerals + condensed broadcast caps. Signature moves: dial sweeps riding a slide-whistle gliss, station lock-in clicks on beat, signal bars pumping. Transitions: tuner blow-by — scene smears into static then locks onto the next frequency. Audio: radio static bursts, slide-tone glissandi, each "station" hints a different genre for 1s, main track filters in/out like reception. Best for: audio/music, podcasts, travel, night products.

**S26 · Typewriter Bureau.** Canvas: desk lamp over paper; cream + ink black + correction-fluid white. Graphics: **mechanical typebars strike** — letters physically stamp onto a rising sheet; carriage slides return left with a ding; paper rolls up revealing the next line/screen; margin bells, ribbon reversals, Wite-Out smears that erase mistakes. Type: monospaced typewriter face; the cursor blocks advance letter by letter. Signature moves: machine-gun letter stamps riding a fast rhythm, carriage-return whips between scenes, x'd-out corrections. Transitions: carriage return hurls the paper up into the next scene. Audio: key clacks, dings, carriage zip — percussion built from typing. Best for: writing/journal/notes apps, newsletters, retro-professional.

**S27 · Noir Venetian.** Canvas: hard black-and-white + one neon accent; smoke, venetian-blind light bars. Graphics: **shadow-play detective framing** — blinds cut light bars across screens, silhouettes pass, a desk lamp swings, case files and photo-evidence boards connected by red string; smoke drifts through light cones. Type: condensed 40s film-title caps, typewritten case labels. Signature moves: blind-shadow sweeps wipes, lamp-swing reveals, evidence-pin strings drawing connections on beat. Transitions: the lamp swings past black into the next scene's light. Audio: upright bass, brushed drums, sax stabs, rain on the window. Best for: security/privacy, mystery/story, finance-noir products.

**S28 · Mirrorball Disco.** Canvas: midnight dance floor; faceted reflections scatter. Graphics: **a giant mirrorball** spins overhead throwing light squares across everything; UI cards are lit dance-floor tiles igniting underfoot; disco spotlights cross beams; glitter particles everywhere. Type: chrome-disco caps (70s swashes) with moving facet reflections. Signature moves: tile-floor ignitions rippling on beat, mirrorball speckle sweeps, bounce-ball camera bob. Transitions: spotlight cross-fade through a light burst; camera dives through a mirrorball facet. Audio: four-on-the-floor disco/funk, claps, string stabs, hi-hat sizzle. Best for: social, dating, events, lifestyle, celebratory.

**S29 · Vinyl RPM.** Canvas: turntable top-down; matte black vinyl, colored label, dust sparkles. Graphics: **groove lines as data** — the record's grooves carry the UI; the tonearm tracks across tracks like chapters; label spins with the brand mark; groove spirals animate like waveform rings; speed shifts 33→45 on the drop. Type: label-print caps that rotate with the record. Signature moves: scratch-stutter transitions, runout-groove clicks, radial track divisions lighting up per section. Transitions: needle drop → groove ride → next track band. Audio: crackle bed, warm vinyl-filtered funk/soul, needle-drop thump, scratch accents. Best for: music/audio apps, DJ tools, warm-analog brands.

**S30 · Office 1994.** Canvas: beige cubicle-lit; fax paper, post-its, desk supplies. Graphics: **office machinery choreography** — dot-matrix printers chatter out charts line by line, post-its slap onto a whiteboard forming diagrams, rolodex flips feature cards, stamp pads slam APPROVED, in-trays stack. Type: dot-matrix and memo stamp faces; "INTERNAL MEMO" header. Signature moves: printer-head passes printing the scene, post-it slaps on beat, stamp slams on impacts. Transitions: a document is yanked off screen; a fax scrolls the next one in. Audio: printer chatter rhythm, phone rings, fax handshake tones, elevator-music pads. Best for: B2B/productivity played with irony, retro-comic products.

#### Organic & natural — S31–S40

**S31 · Ink in Water.** Canvas: bright water-white or deep tank-black; pigment colors bloom. Graphics: **real ink dispersal physics** — colored ink drops plunge and mushroom-cloud into soft billows that resolve into UI shapes; tendrils draw connecting lines; pigment drifts slowly with current. Type: serif forms condensing out of the ink cloud, then dissolving. Signature moves: drop impacts on the beat (slow-mo plume), ink-tendril underlines, pigment storms behind panels. Transitions: a drop of the NEXT scene's color plunges through the current frame. Audio: submerged whooshes, deep muffled pulses, glass harp tones, air bubbles. Best for: meditation, wellness, art/photo, beauty.

**S32 · Reef Glow.** Canvas: deep-sea gradient; bioluminescent cyan/violet/lime on near-black; particulate marine snow. Graphics: **bioluminescent organisms as UI** — jellyfish pulse open into cards, light-fish shoals form arrows and charts, coral structures grow headers; oxygen bubble counters rise. Type: glowing aqua caps flickering like lure-light. Signature moves: lure-flicker reveals, shoal morphs (fish reorganize into icons on beat), jellyfish pulse transitions. Transitions: the camera sinks deeper — light fades, new bioluminescent scene ignites below. Audio: deep ambient pads, sonar blips, underwater muffled beats, creature chirps. Best for: night/sleep apps, ambient products, science, anything calm-deep.

**S33 · Hive Mind.** Canvas: warm honey-gold + amber + dark wax cells. Graphics: **hexagon comb systems** — hex cells build outward on the beat, filling with content like honey; bee-dot swarms ferry elements cell to cell; waggle-dance arrows point at features; honey dip-fills rise inside cells. Type: rounded hex-grid caps that slot into cells. Signature moves: comb-expansion builds, swarm relocation transitions, drip-fill meters. Transitions: the swarm lifts everything away and re-deposits the next scene. Audio: soft buzzing harmony beds, piped high-frequency bee chirps, warm honeyed Rhodes. Best for: community, productivity, food, ecosystem products.

**S34 · Aurora Field.** Canvas: night tundra dark; aurora greens/teals/violets. Graphics: **curtains of light** — slow ribbon fields fold across the sky and become graphic elements (a curtain flattens into a chart, splits into panels); stars drift; ground contour lines glow. Type: thin elegant caps that shimmer as aurora light passes behind them. Signature moves: ribbon-fold scene reveals, light-curtain wipes, starfield parallax drifts. Transitions: a ribbon sweeps across frame leaving the next scene behind it. Audio: ethereal pads, glass harmonics, low wind, whale-song swells. Best for: sleep, meditation, travel, premium/calm.

**S35 · Cloud Chamber.** Canvas: dark science-void; vapor trails in white/electric colors. Graphics: **particle physics made visible** — charged trails streak through a supersaturated chamber, curving and colliding; collision points burst into sparks that form UI elements; ionization tracks linger and fade. Type: thin physics-annotation caps + event labels (`e⁻ event 042`). Signature moves: collision bursts on hits, trail-writing elements, decay spirals. Transitions: a collision flash floods the chamber white → reset → next event. Audio: Geiger ticks, particle zaps, airy synth drones, impact shimmers. Best for: science, AI, data, experimental products.

**S36 · Herbarium.** Canvas: archive-cream mounting paper; dried-flower palette. Graphics: **pressed specimens** — the app's features mounted like botanical plates with Latin-style labels, stitch pins, tape corners; stems press flat under glass; pressed-flower ornaments bloom at corners. Type: engraved botanical-plate serif + collector's handwriting. Signature moves: specimen cards sliding in on a grid, magnifier hover zooms, page-turn of the specimen book. Transitions: folio page turns. Audio: page rustles, archive drawers, soft chamber strings, nature room tone. Best for: journals, plant/wellness, archival/elegant products.

**S37 · Murmuration.** Canvas: dusk gradient (peach → violet); thousands of dark bird-dots. Graphics: **a flock that is the graphic system** — the swarm forms letters, arrows, pie charts, then dissolves; density waves ripple through the flock; a straggler-line trails behind punctual elements. Type: the flock literally spells the headline, holds 1s, scatters. Signature moves: shape-snap morphs on beat, predator-panic scatters on impacts, swirl-into-form transitions. Transitions: flock pours off frame left and re-enters as the next shape from right. Audio: wing-whoosh textures, distant calls, airy strings — the flock's motion drives stereo movement. Best for: social, AI/collective, environment, anything about "many → one".

**S38 · Tideline.** Canvas: wet-sand shoreline tones; foam white, kelp green, water blue-grey. Graphics: **the tide delivers** — waves wash in and deposit shells/objects/UI cards on the sand, then retract; tide-line typography is written in foam then erased; sandpipers of light dart past. Type: foam-lettering caps that partially wash away each wave. Signature moves: wave-cycle reveals (in on beat, out on offbeat), deposited-item pops, sand-suction wipes. Transitions: a big set-wave floods the frame; it drains into the next scene. Audio: real wave cycles as rhythm, gull calls, shore-suck textures, gentle guitar/piano. Best for: travel, mindfulness, wellness, coastal/calm.

**S39 · Terrarium Macro.** Canvas: under-glass miniature world; moss green, dew sparkle, soft bokeh. Graphics: **macro miniature** — tiny landscape where dewdrops are magnifier lenses over UI details; mushroom caps carry labels; miniature figures walk the moss; rain drips overhead. Type: little engraved garden markers + engraved label plates. Signature moves: dew-lens zoom reveals, time-lapse sprout pops on beat, raindrop percussion hits. Transitions: the camera passes through the glass into the next miniature. Audio: micro-percussion (dew drops, leaf taps), music-box melody, humid ambience. Best for: plant/nature, family, cozy, miniature-charm products.

**S40 · Ember Night.** Canvas: campfire-night dark; warm orange sparks on deep brown-black. Graphics: **embers and fireflies** — sparks swirl up from below frame and assemble into words/panels then scatter; firefly constellations connect features; heat shimmer distorts the background. Type: letters smolder — form as glowing embers, cool to ash-grey, reignite. Signature moves: ember-swarm assemblies on beat, glow-pulse with the music's warmth, spark scatter transitions. Transitions: a gust blows the embers into the next configuration. Audio: fire crackle percussion, warm acoustic guitar/harmonium, night crickets, deep soft kicks. Best for: outdoor, camping, storytelling, warm-community products.

#### Data & digital — S41–S50

**S41 · Phosphor Terminal.** Canvas: deep CRT black; green/amber phosphor glow with bloom + scanlines + slight curvature. Graphics: **everything is a terminal** — prompts type commands that literally build the scenes (`$ deploy --features`), ASCII/box-drawing UI frames, progress bars, man-page layouts, cursor blinking; occasional vector-graphics bursts (wireframe plots). Type: glowing monospace only — hierarchy by brightness + weight. Signature moves: typewriter command lines whose execution explodes into visuals, ASCII-art morphs, phosphor persistence trails. Transitions: `clear` — screen wipes to prompt, next scene compiles. Audio: modem chirps, hard-drive ticks, subdued darkwave synthline. Best for: dev-tools, AI/CLI products, security, technical audiences.

**S42 · Neural Mesh.** Canvas: near-black violet; node glow (cyan/magenta) with connection edges. Graphics: **a firing network** — nodes pulse in cascades, edges carry light packets, clusters form the app's feature shapes (a mesh that IS a brain forming a phone icon, a chart, a word); activation heat-maps. Type: thin futuristic caps over the mesh; node labels as tiny weights (`w=0.87`). Signature moves: signal-propagation pulses on beat, cluster-snap morphs, camera weaving through the lattice. Transitions: the mesh reorganizes — camera keeps moving while edges rewire into the next diagram. Audio: granular synth pulses, neural blips, deep processing drones, swarm textures. Best for: AI/ML, analytics, network products.

**S43 · Voxel Metropolis.** Canvas: dusk-lit isometric city palette. Graphics: **voxel cubes stack a city** — buildings rise cube-by-cube on the beat (each building = a feature), streets light up, tiny voxel cars/people animate, helicopter-camera orbits; UI panels are billboard facades. Type: voxel-built letterforms + rooftop signage. Signature moves: block-cascade construction, traffic-flow pulses, demolition/rebuild transitions. Transitions: crane-camera swings to the next district. Audio: plucky synth construction ticks, low city rumble, satisfying block-clack percussion. Best for: games, city/logistics, builders, playful-data.

**S44 · Datamosh.** Canvas: the corrupted digital image itself — smeared chroma, block artifacts, I-frame breakage. Graphics: **intentional compression chaos** — scenes pixel-sort into streaks, macroblock ghosts of the last scene bleed into the next, colors shear along JPEG block boundaries; HUD "corruption %" readouts. Type: heavy glitch type — letters tear horizontally, channel-split, occasionally snap clean for readability. Signature moves: datamosh smears on every transition, pixel-sort wipes, buffer-stutter freezes mid-motion. Transitions: the frame literally corrupts into the next one — never clean cuts. Audio: bitcrushed beats, sample-rate stutters, modem noise, corrupted-audio stingers resolving to clean hits. Best for: edgy/music/streetwear, anti-corporate, experimental.

**S45 · PCB Etch.** Canvas: solder-mask green or black; copper-trace gold, silkscreen white. Graphics: **circuit-board as city map** — traces route between pads forming the layout; solder dots pop like rivets; signal pulses race along traces lighting components (each component = a feature); silkscreen labels in monospace. Type: PCB silkscreen caps (`C47`, `U12` style references as annotations). Signature moves: trace-draw reveals on beat, signal-pulse races, component stamp-downs. Transitions: board layer-flip (the board turns over to the next layer/scene). Audio: relay clicks, high-frequency zaps, arpeggiated square-wave synth, multimeter beeps. Best for: hardware-adjacent, dev-tools, engineering products.

**S46 · Tilt-Shift Toy Town.** Canvas: miniature-faked daylight; saturated toy colors; shallow DOF on everything. Graphics: **a tiny model village** — buildings, trees, cars, little figures doing the app's story; fast-forward people (time-lapse jerks); model-railroad trees pop up per feature. Type: model-railroad sign lettering + big floating caps that dwarf the town. Signature moves: time-lapse crowd flows, pop-up builds, tilt-shift rack-focus reveals. Transitions: a hand-of-god plucks the scene up; the next diorama slides in on rails. Audio: twee glockenspiel/ukulele, toy-town ambience, cartoonish speed-up whooshes. Best for: community, family, real-estate, playful-everyday apps.

**S47 · Particle Accelerator.** Canvas: physics-lab void; energy colors (white-hot cores, plasma edges). Graphics: **pure simulation** — particle streams accelerate around ring tracks, collide into bursts that crystallize into UI elements; energy-field distortions bend type; containment-field UI frames pulse. Type: HUD physics labels + heavy condensed caps that "contain" the energy. Signature moves: acceleration ramps to the drop, collision-burst morphs, field-containment strain flickers. Transitions: a full-energy discharge whites the frame → new experiment charges up. Audio: rising charge whines, discharge booms, electromagnetic hums, precision ticks. Best for: performance products, AI, games, "power" messaging.

**S48 · Oscilloscope.** Canvas: instrument-cabinet grey/green; glowing trace colors. Graphics: **everything is a waveform** — Lissajous figures morph between shapes, the app's beat literally draws the scenes, XY scope traces build logos and icons; spectrum analyzers bounce under panels; knobs and VU meters animate. Type: oscilloscope-green vector lettering written by the beam. Signature moves: trace-morph reveals (one figure deflects into the next), frequency-split layers, sync-lock snaps. Transitions: beam retraces — a single line whips across drawing the next scene. Audio: clean sine sub, theremin-like glides, calibration beeps, scope hum. Best for: audio/music tools, engineering, measurement products.

**S49 · Flip Grid.** Canvas: matte dark panel; module cells flipping between two faces (binary white/dark or two brand colors). Graphics: **a mechanical flip-field** — thousands of square modules clack over to form images, letters, charts; cascading wave-flips sweep across; partial flip-states create texture. Type: formed BY the grid — letters resolve out of noise one flip-wave at a time. Signature moves: cascading reveal waves on the beat, noise-shuffle suspense, edge-to-center convergences. Transitions: full-field scramble → resolve into the next image. Audio: hundreds of tiny clacks as percussion, relay-chatter rhythms, resonant mechanical bed. Best for: information/dashboard products, departures, playful-data.

**S50 · Mission Control.** Canvas: console-room dark; phosphor green + mission-red + crew-badge colors. Graphics: **a mission in progress** — big board telemetry (trajectory arcs, countdown clocks, comm loops), rows of consoles, each scene a "flight phase" (LAUNCH → ASCENT → ORBIT → DEPLOY = product features); CAPCOM captions; go/no-go polls lighting green. Type: NASA-style condensed caps + seven-segment timers. Signature moves: countdown-tick sync to beat, telemetry trace-draws, all-green GO sequence hits. Transitions: "switch to camera 2" — hard CCTV cut to next phase. Audio: radio squelch, CAPCOM voice-blips (filtered, wordless), room hum, rising orchestral bed under systems-go calls. Best for: productivity, launch/startup products, team tools.

#### Type-led & editorial — S51–S60

**S51 · Sticker Pack.** Canvas: bright flat color or craft table; thick white die-cut borders. Graphics: **die-cut stickers** — screens and phrases arrive as stickers that slap down, get peeled and re-stuck, overlap in a collage; holographic-foil sticker shines sweep; sticker-sheet frames. Type: chunky sticker caps with white outline + drop shadow. Signature moves: slap-sticks on beat, peel-and-flick reveals, sticker-bomb builds that cover the frame. Transitions: a hand peels the whole scene off like a sticker sheet. Audio: slap hits, peel rips, sticky squeaks, fun pop percussion. Best for: social, messaging, creator tools, Gen-Z products.

**S52 · Letterpress.** Canvas: thick cotton paper; ink bite into toothy stock; debossed shadows. Graphics: **impressed ink** — type and plates physically stamp into paper leaving deboss shadows; ink rollers pass; plate registration marks; deckle edges; misprints corrected by over-printing. Type: huge serif/sans caps pressed hard — you can feel the bite. Signature moves: press-stamps on every hit, roller reveals, deboss→ink double-hits. Transitions: the sheet is pulled from the press; a new plate rolls in. Audio: press thumps, roller ink-hiss, paper handling, quiet refined room. Best for: luxury, editorial, wedding/invitation, craftsmanship brands.

**S53 · Times Square.** Canvas: canyon of stacked LED billboards at night. Graphics: **the whole scene is stacked screens** — dozens of ad panels flipping and re-skinning, synchronized wall-moments where every screen merges into one image; camera tilts up through the canyon; crowd lights below. Type: giant LED-display caps flickering like a billboard refresh. Signature moves: multi-panel sync reveals on the drop, panel-flip cascades, vertical canyon dives. Transitions: the hero billboard's image spills across every screen. Audio: city rumble bed, crowd murmur, electronic ad-jingle fragments, big-screen hum. Best for: entertainment, media, "big launch" energy.

**S54 · Karaoke Bounce.** Canvas: warm stage-lights or TV-karaoke blue. Graphics: **sing-along mechanics** — a bouncing ball/marker lands on each syllable exactly on the lyric rhythm, words illuminate as hit; lyric lines scroll; applause meter for the big beats. Type: bold lyric caps, lit-word highlighting, bouncing marker. Signature moves: word-light sweeps synced per-syllable, bounce percussion on hits, crowd-meter reactions. Transitions: verse cards flip — "NEXT TRACK" karaoke screen. Audio: karaoke-room room tone, clap-along percussion, big warm hooks. Best for: music/social, party, sing/read apps.

**S55 · Swiss Assault.** Canvas: flat white or flat black; aggressive Swiss grid, one spot color (red/international orange). Graphics: **typography as weapon** — enormous grid-locked caps slam in per beat with registration crosshairs; bars and rules slice the frame; gridlines snap on/off revealing construction; negative space used violently. Type: Helvetica/Akzidenz-style neo-grotesque at maximum weight — type IS the image. Signature moves: slam-lock words, grid-reveal flickers, baseline-shift bounces, index-tab wipes. Transitions: hard grid wipes; a rule line drags the new scene across. Audio: brutal drums, single stabbing synth, metronomic precision, silence used as a weapon between hits. Best for: design tools, fashion, architecture, confident-minimal products.

**S56 · Brush Stroke.** Canvas: rice-paper warm or ink-black; sumi ink + one vermilion seal. Graphics: **calligraphic energy** — brush strokes paint the frame's shapes; dry-brush texture, ink pooling, splatter on fast strokes; painted enso rings; seal-stamp chops signing scenes. Type: calligraphy as display — strokes assemble characters/letters stroke-by-stroke in correct order. Signature moves: stroke-draw builds per beat, splatter accents on impacts, chop-stamp hits. Transitions: a giant stroke swipes the frame; ink bleeds through to the next paper. Audio: brush scratches, ink-well dips, plucked strings (guqin/koto), meditative percussion. Best for: language/culture, mindfulness, art, heritage.

**S57 · Split-Flap.** Canvas: departure-hall dark; rows of flip modules. Graphics: **the Solari board** — letter tiles flap-flap-flap to spell headlines; rows cascade updates; schedule lines shuffle; a departure-flip storm marks the drop; each screen change is a physical rattle of tiles. Type: split-flap cap grid, tile-by-tile resolution. Signature moves: flapping cascades on beat, line-shuffles (one row scrolls), full-board noise bursts. Transitions: the whole board flutters at once into the next message. Audio: mechanical clatter as percussion (it's the rhythm section), station ambience, PA-ding announcements. Best for: travel, finance tickers, scheduling, retro-mech lovers.

**S58 · Crossword Grid.** Canvas: puzzle-print cream; ink black + pencil grey + one accent for correct answers. Graphics: **letters lock into a grid** — answers fill in from cursor taps, wrong letters get erased, clue numbers sit in cell corners; highlighted answer rows glow when complete; grid zooms and pans like a survey. Type: cell-locked caps + clue-list mono. Signature moves: fill-in streaks on beat, erase-and-retry flips, whole-grid completion flash. Transitions: the solved grid rotates and the next puzzle slides behind it. Audio: pencil scribbles, tap-taps, eraser rubs, soft library ambience, satisfying ding per solve. Best for: puzzle/word apps, education, thinky products.

**S59 · Broadway Marquee.** Canvas: theater-district night; bulb-chase gold, velvet red curtain. Graphics: **chasing bulb arrays** — marquee letters framed by bulbs that chase around borders; curtains part for reveals; footlight rows glow; poster frames with "NOW SHOWING" cards swapped live. Type: show-card caps (mix of slab serif + script) lit by bulb rings. Signature moves: bulb-chase accents on every beat, curtain-part reveals, marquee-message flips. Transitions: curtain close/open; a bulb-chase wipe across the frame. Audio: pit-orchestra hits, bulb-buzz sizzle, applause swells, showtime brass. Best for: entertainment, events, ticketing, theatrical products.

**S60 · Receipt Thermal.** Canvas: till-white receipt paper on dark counter. Graphics: **a printer scrolling the story** — thermal paper feeds upward, printing features as line items with prices (`FEATURE .......... FREE`), barcodes, totals, tear-off perforation; the receipt becomes impossibly long, curling and pooling. Type: thermal-printer caps, barcode motifs, dotted separators. Signature moves: line-by-line print reveals on beat, totals-calculation bursts, tear-off transitions. Transitions: the receipt tears; a fresh one feeds. Audio: printer chatter, register dings, tear perforation rips, supermarket ambience under a clean beat. Best for: finance/shopping, value messaging, playful-commerce.

#### Space & illusion — S61–S70

**S61 · Fractal Dive.** Canvas: mandelbrot/julia gradients (deep blues → fiery edges) or clean recursive geometry. Graphics: **the zoom never stops** — every scene boundary is inside the previous shape (a chart's bar becomes the next landscape, a letter's counter contains the next scene); self-similar motifs recur at every scale. Type: floating caps that the dive passes through like gates. Signature moves: continuous smooth exponential zoom, detail blooms at each scale, kaleidoscopic side-tunnels. Transitions: by definition — you never leave the dive. Audio: hypnotic accelerating pulse, scale-shimmer arps, deep zoom whooshes, drone bed. Best for: AI/infinity/scale messaging, math-adjacent, mind-bending products.

**S62 · Escherworks.** Canvas: architectural ivory/grey with impossible shadows; isometric-ish but broken. Graphics: **impossible architecture** — staircases loop (Penrose), waterfalls feed themselves, gravity flips at walls; the app's elements sit on impossible ledges; figures walk upside down across the frame. Type: carved inscription caps that obey each surface's gravity. Signature moves: gravity-flip camera rolls, endless-loop walks on beat, impossible-structure assembles block by block. Transitions: the camera rolls 90° and a wall becomes the next floor. Audio: echoing footsteps, stone drips, Escher-ish choral mystery, clockwork undertones. Best for: puzzle/strategy, architecture, "think different" products.

**S63 · Kaleidoscope.** Canvas: radial symmetry — real images multiplied into mandalas. Graphics: **the product mirrors into mandalas** — screenshots fold into 6/8/12-segment kaleidoscope patterns that rotate and bloom; sectors swap between mirrored and free on the beat. Type: ring-set type curving around mandala centers. Signature moves: segment rotations on beat, bloom unfolds on drops, symmetry-break shocks. Transitions: the mandala spins faster, blurs, locks into the next pattern. Audio: music-box spins, glassy reflections, slowly rotating stereo field, crystalline bells. Best for: photo/creative tools, wellness, pattern/beauty products.

**S64 · Shadowplay.** Canvas: backlit warm screen (paper lantern); clean silhouette black. Graphics: **pure silhouette theater** — hands/props/screens as crisp shadows on a lit scrim; exaggerated shadow-puppet morphs (a profile becomes a bird becomes a chart); ink-wash spill effects at edges. Type: silhouette caps cut from the light — letters as negative space. Signature moves: morph-magic shape shifts, size-play (small prop throws giant shadow), scrim-splash ink reveals. Transitions: a shadow hand sweeps the light; next scene emerges as darkness reshapes. Audio: soft theatrical percussion, paper rustles, warm room tone, playful plucks. Best for: storytelling, kids, warm/analog, heritage.

**S65 · Glass Parallax.** Canvas: soft focus gradients behind frosted panels. Graphics: **layered frosted-glass panes** — 4–6 translucent panes slide at different depths with real parallax; content prints on each layer (ghost reflections show through); pane edges catch light-lines; depth-of-field racks between layers. Type: etched-glass caps, refraction doubles at edges. Signature moves: rack-focus reveals, pane-slide wipe layers, dewdrop lens accents on hits. Transitions: camera pushes through each pane; the last pane IS the next scene. Audio: glass taps, airy filtered pads, soft high-frequency shimmer SFX. Best for: design/fintech/premium-clean, anything "glass-morphism".

**S66 · Anamorph.** Canvas: industrial loft floor/walls; paint that only resolves from one angle. Graphics: **anamorphic projection tricks** — graphics smeared across floor and wall snap into coherent images only at the camera's sweet spot; the camera orbits through wrong-geometry until the resolve hit; UI painted across 3D-surfaces. Type: distorted caps that snap straight at the solve. Signature moves: drift-to-resolve on each beat, split-geometry assembles (two wall-halves meet), walk-through reveals. Transitions: orbit past the sweet spot — distortion re-scrambles into the next image. Audio: architectural echoes, reveal sweeps, deep tonal drones, resolve-chimes. Best for: architecture, AR/spatial, clever-brand products.

**S67 · Hyperlapse.** Canvas: city blur — long-exposure light smears on dusk scenes. Graphics: **time-compressed world** — traffic streams as light-ribbons, crowds ghost-flow, clouds streak; the product's elements stay tack-sharp floating inside the blur; day-night cycles sweep. Type: clean caps that float stable while the world streaks behind. Signature moves: whip-pan moves between scenes at light-speed, time-slice freezes (blur halts, element rotates), streak-pull typography trails. Transitions: hard whip-pan smears to the next location. Audio: speeding ambient whoosh bed, muffled city pulse, sharp beat cutting through the blur. Best for: travel, delivery/logistics, hustle/productivity.

**S68 · Zero-G Cabin.** Canvas: spacecraft cabin interior; soft key light + Earth-glow bounce. Graphics: **weightless drift** — every element floats, tumbles slowly, drifts past camera; items tethered by straps; droplets sphere up; velcro panels hold UI cards; the Earth rolls slowly past a window. Type: mission-patch caps + labels floating loose. Signature moves: inertia-push reveals (elements drift in, never stop fully), tether-yank recalls, tumble-to-frame compositions. Transitions: the camera pushes off — a slow float into the next module. Audio: air-system hum, suit-thump contacts, muffled cabin sounds, spacious ambient score. Best for: space/science, calm-premium, any "weightless/simple" message.

**S69 · Hyperspace Tunnel.** Canvas: warp-tunnel — streaking star lines, chromatic tunnel walls. Graphics: **sustained warp travel** — scenes arrive by decelerating out of warp; UI panels dock onto tunnel walls; warp-flash gates mark section changes; star-lines bend around passing elements. Type: big caps that warp-stretch into frame and stabilize. Signature moves: punch-in/out warp bursts on every transition, speed-line stutters, tunnel-wall panel docks. Transitions: literally jump to warp; brake into the next scene. Audio: engine-swell risers, warp-hit booms, deceleration whines, sci-fi sub pulses. Best for: sci-fi products, games, fast/performance messaging.

**S70 · Foglift.** Canvas: dense volumetric fog; shapes as darkness-in-mist. Graphics: **reveal by subtraction** — scenes hide in fog and emerge: a fan/lights sweep fog aside in bands; elements silhouettes sharpen as fog thins; god-beams cut channels through the murk; only the fog carries light. Type: caps that coalesce from mist or read as fog-free channels carved through. Signature moves: fog-channel sweeps on beat, silhouette-resolve reveals, beam-slice wipes. Transitions: fog floods back in and parts somewhere new. Audio: low foghorn pulses, moist air ambience, haunting minimal score, breath swells. Best for: mystery/launch teasers, atmospheric products, privacy/security.

#### Craft & culture — S71–S80

**S71 · Embroidery Hoop.** Canvas: stretched fabric in a hoop; linen weave texture. Graphics: **satin-stitch everything** — threads sew the design stitch by stitch (each beat = a stitch row); hoop-frame composition; thread-tail details, needle dips through fabric; stitch-count counters. Type: cross-stitch and script-embroidered lettering. Signature moves: stitch-row builds per bar, thread-color swaps mid-scene, needle-through punctures as hits. Transitions: the hoop loosens, fabric is swapped for the next piece. Audio: needle pokes, thread pulls, sewing-machine runs for fast passages, gentle folk melodies. Best for: craft/fashion, handmade brands, wholesome products.

**S72 · Ukiyo-e.** Canvas: woodblock flat color fields; indigo/vermilion/beige palette, visible registration. Graphics: **woodblock printing** — each color plate stamps down in registration order building the image (like S6 but Japanese flat-color grammar: waves, clouds, speed-rain); wave and wind motifs carry the layout; cartouche boxes hold labels. Type: carved-look caps in cartouches; vertical columns allowed. Signature moves: plate-by-plate builds on beat, wave-curl reveals, wind-line sweeps. Transitions: the next plate prints over; a wave curls across the frame. Audio: woodblock taps, brush-water sounds, shakuhachi/shamisen accents, measured taiko. Best for: culture/travel, food, art, Japanese-aesthetic products.

**S73 · Mosaic Tesserae.** Canvas: grout-dark backing; stone/glass tile palette + gold leaf. Graphics: **tiles click into place** — individual tesserae set one per rhythmic cell building portraits/icons/UI; gold tiles shimmer as light sweeps; occasional "missing tile" reveals; opus patterns (swirling rows) direct the eye. Type: mosaic caps set in tile rows with grout channels. Signature moves: tile-cascade fills on beat, light-sweep gold flashes, zoom-out reveals of the full mural. Transitions: camera pulls back — the finished section turns out to be a small tile in a bigger mosaic (the next scene). Audio: ceramic/stone clinks as percussion, trowel scrapes, Byzantine-echo chant pads. Best for: heritage, luxury, permanence messaging.

**S74 · Spraywall.** Canvas: concrete wall texture; overspray mist; drips. Graphics: **aerosol grammar** — stencils slap on and spray through; drips run off bold fills; throw-up outlines then fat-cap fills; buff-paint covers get re-tagged; masking-tape edges pull clean. Type: fat-cap caps, stencil plates, tag signatures as accents. Signature moves: stencil-slam + spray-fills per beat, drip-timing accents, buff/restore battles. Transitions: a paint flood coats the wall → new wall. Audio: can rattles, spray hiss as snare-adjacent, city ambience, boom-bap or phonk bed. Best for: streetwear/music, youth brands, bold-messaging.

**S75 · Zen Garden.** Canvas: raked sand field; stones, moss island, single maple accent. Graphics: **rake-line geometry** — patterns are raked into sand around each stone (each stone = a feature set); concentric circles, straight rows; a leaf drifts as the only motion accent; light shifts like passing hours. Type: restrained caps on wooden posts or brushed onto sand. Signature moves: rake-pass draws that reveal patterns, stone placements with dust, leaf-drift continuity across scenes. Transitions: the garden "refreshes" — sand smooths, new stones arrive. Audio: bamboo knocks, rake drags, water drop (shishi-odoshi) as metronome, temple ambience. Best for: mindfulness, minimal products, slow-living.

**S76 · Felt Board.** Canvas: flannel board texture; saturated felt cutout colors. Graphics: **pressed felt shapes** — fuzzy die-cut figures press onto the board and peel off; layered felt scenes (trees, houses, characters); yarn-line connectors; thumbtack pins. Type: soft felt caps pressed down letter by letter. Signature moves: press-and-stick placements on beat, peel-off exits, yarn-line draws connecting story beats. Transitions: a hand clears the board; new felt pieces slap on. Audio: fabric presses, gentle finger-tap bumps, warm kids'-room acoustics, xylophone/toy piano. Best for: kids/family, education, warm-handmade products.

**S77 · Ikat Drift.** Canvas: woven textile field; blurred-edge dye patterns. Graphics: **feathered pattern drift** — ikat's signature blurred weaves slide and realign; pattern bands scroll at different speeds; dye-blur bleeds edges; textile texture extreme close-ups mix with wide pattern fields. Type: woven caps whose edges are deliberately dye-blurred. Signature moves: pattern-alignment snaps on beat, weave-band scrolls, dye-bleed reveals. Transitions: the textile feeds through — a new pattern section arrives like fabric off a roll. Audio: loom rhythm, dye-water drips, soft ethnic-instrument motifs, textile-factory ambience. Best for: fashion/textile, craft, cultural products.

**S78 · Knot & Loop.** Canvas: carpet-macro — wool fibers huge, knots visible. Graphics: **knot-level macro world** — the camera lives inside a rug being knotted; each knot ties on a beat (thousands of knots = persistence metaphor); shearing passes flatten surfaces; pattern emerges knot by knot. Type: pile-lettering — text visible only in the carpet's pattern. Signature moves: knot-tying cascades, shear-pass reveals, pattern zoom-out shocks. Transitions: the woven section flips over to its patterned face → next scene. Audio: knot-tugs, shear-buzzes, loom rhythm, warm workshop atmosphere. Best for: persistence/craft messaging, heritage, patient-product stories.

**S79 · Manga Strike.** Canvas: ink white with bold blacks + screen-tone greys; violent accent color. Graphics: **comic-panel grammar** — speed lines converge on impact points, halftone-tone shading, action-burst panels, effect-lettering (ゴゴゴ / BAM-style) integrated into layout; panels slide and rotate like a page being read fast. Type: explosive effect-lettering + manga dialogue caps. Signature moves: speed-line convergence on every hit, panel-slam inserts, impact-star bursts, dramatic pause frames with shaking lines. Transitions: page-turn swipes; a panel punches through the frame into the next panel. Audio: taiko/dramatic hits, whoosh-slashes, shamisen stabs, anime-impact drums. Best for: games, comic/anime audiences, high-energy products.

**S80 · Bauhaus Revue.** Canvas: cream stage; primary geometry (red/yellow/blue circles, triangles, bars) + black. Graphics: **geometric ballet** — primary shapes perform choreography: circles roll, triangles pivot, bars seesaw; shapes form and reform the app's screens like a Bauhaus theater piece; spotlight follows the dancer-shapes. Type: geometric sans caps on baseline stages. Signature moves: shape-dance entrances per beat, balance-act compositions, geometric cascades (shape trains). Transitions: shapes exit stage left, enter stage right re-costumed. Audio: jazzy percussion, muted trumpet, piano riffs — theatrical and witty. Best for: design/education, playful-intellectual, artsy products.

#### Light & optics — S81–S90

**S81 · Laser Dome.** Canvas: black venue haze; saturated laser primaries. Graphics: **coherent beams as architecture** — laser planes sweep forming walls/floors, beam-fans sweep on beats, beam-splitters create copies, beam-written outlines trace the UI; haze makes beams volumetric. Type: caps traced by laser raster sweeps. Signature moves: beam-fan pulses per beat, laser-scan reveals (a sheet of light draws the scene), mirror-bounce redirections. Transitions: laser blackout + reposition — beams re-fire in the next arrangement. Audio: synthwave/techno pulse, beam-hum risers, vaporized zaps, dome-echo percussion. Best for: music/events, gaming, high-tech products.

**S82 · Prism.** Canvas: pure white or pure black; the spectrum does the work. Graphics: **dispersion physics** — white light enters prism solids and fans into rainbow bands that paint the UI; elements refract and split; every edge throws spectral fringes; band sweeps reveal features one hue at a time. Type: caps split into RGB fringes that align on the beat. Signature moves: spectrum-fan wipes, refraction-through-glass passes, RGB-split aligns on hits. Transitions: the whole image refracts — spectrum fans out and recombines as the next scene. Audio: glassy bell tones per band, shimmer sweeps, prism-hum resonance, chromatic arps. Best for: photo/color/creative tools, premium-clean, science.

**S83 · Observatory.** Canvas: deep-sky black; instrument-panel amber; star white. Graphics: **telescope reticle framing** — crosshair reticles, declination circles, star charts with lines connecting UI-features-as-constellations; tracking slow-drift; spectral-class labels; dome-slit light bands. Type: star-atlas serif + coordinate mono. Signature moves: reticle-slew reveals, constellation-line draws on beat, exposure-brightness blooms. Transitions: the telescope slews — stars streak — locks onto the next field. Audio: servo-slew whirs, stellar ambient drones, radio-telescope noise bursts, cool glass tones. Best for: science/education, aspiration messaging, astronomy fans.

**S84 · Blacklight.** Canvas: UV-dark; fluorescent reactive colors (pink/green/orange/blue) on black. Graphics: **invisible-until-lit** — scenes painted in UV-reactive ink: normal light shows nothing, blacklight sweeps reveal glowing art; reactive outlines trace UI; invisible-ink secrets appear under the sweep. Type: fluorescent-tube caps that fluoresce on sweep. Signature moves: sweep-reveal scanning, reactive-paint pours, double-exposure normal-vs-UV toggles. Transitions: lights-out → UV sweep paints the next scene. Audio: UV hum buzz, fluorescent flickers, dark electro pulse, reveal shimmers. Best for: nightlife, secrets/security framing, edgy-fun products.

**S85 · Chiaroscuro.** Canvas: Caravaggio darkness; single candle-level key light. Graphics: **dramatic tenebrism** — elements emerge from black as light finds them: faces of objects lit by a moving candle, deep shadow mass around every edge; light physically travels (flickers, gutters, flares). Type: caps lit edge-only, mostly implied letterforms. Signature moves: candle-sweep reveals, flicker-modulated holds, light-passed-hand-to-hand between elements. Transitions: the light goes out — reignites on the next scene's subject. Audio: intimate room tone, candle hiss, sparse deep piano/strings, breath-paced rhythm. Best for: luxury/dramatic, film-noir, serious craft.

**S86 · Long Exposure.** Canvas: dusk city; traffic becomes red/white light rivers. Graphics: **time-smeared light** — all motion is light trails: vehicles draw ribbons, people ghost, UI cards arrive as light-paint strokes; star-trail arcs for slow scenes; trails etch the layout. Type: light-calligraphy caps drawn in the air. Signature moves: trail-draw builds on beat, time-slice freezes inside the blur, ribbon weaves through elements. Transitions: camera chases a light-ribbon into the next scene. Audio: highway whoosh pulses, neon-ambient synth, photo-shutter snaps. Best for: travel/night, speed messaging, photography apps.

**S87 · Golden Hour.** Canvas: low sun warmth — amber/backlit haze, long shadows. Graphics: **lens-first warmth** — everything is backlit: dust and pollen sparkle in beams, lens flares streak across on pans, silhouettes rim-lit gold; elements hang suspended in the warm air column. Type: serif caps with sun-kissed rim light and shadow sides. Signature moves: flare-swipe reveals, backlight bloom-outs, suspended-particle dances. Transitions: the camera pans INTO the sun — flare whites out — next scene backlit. Audio: warm acoustic/folk bed, cicada/heat ambience, gentle percussion, breath-of-summer pads. Best for: lifestyle, travel, warm-emotional, outdoor.

**S88 · Sparkler Script.** Canvas: night-exposure black; sparkler orange-white + colored variants. Graphics: **light-writing persistence** — sparkler trails write words and draw UI frames in the air (long-exposure look), trails fade after seconds forcing constant redrawing — the scene is always being re-scribed; spark showers. Type: cursive light-written script + block caps drawn in fire. Signature moves: live light-writing on beat, spark-shower accents, fade-erase suspense. Transitions: a line is drawn that becomes the next scene's architecture. Audio: sparkler crackle-hiss, magnesium sizzle pops, night ambience, warm minimal score. Best for: celebration, messaging, night/warm-emotion.

**S89 · Phosphor Rain.** Canvas: terminal-night dark; falling glowing drips/pixels (matrix-adjacent but softer). Graphics: **falling code-rain grown up** — columns of glyph-streaks fall at different speeds; impacts splash into pools that ARE the UI; character colliders make glyphs bounce; rain density builds to the drop. Type: formed where rain columns pause — letters as stacked streak-heads. Signature moves: column cascades per beat, splash-pool formations, rain-freeze mid-air moments. Transitions: a downpour floods the frame; drains to the next scene. Audio: synthesized rain-pat percussion, digital drips, cyber-ambient pad, low rumble. Best for: dev/data/security, cyberpunk products.

**S90 · Followspot.** Canvas: black stage; theatrical followspot cones. Graphics: **spotlight choreography** — multiple followspots hunt, cross, and land on elements; beam-edge transitions; gobos (pattern-cut spots) texture scenes; performers' objects only exist inside the beams. Type: showbill caps caught in the followspot. Signature moves: spot-hunt-and-land on each beat, cross-beam clashes, blackout hit-frames. Transitions: all spots converge to one point → blow out → refind the next scene. Audio: theater-hall acoustics, spotlight relay clunks, orchestral hits, stage-whisper textures. Best for: events, launches, stagey-dramatic products.

#### Extreme & experimental — S91–S100

**S91 · Cymatics.** Canvas: lab-black plate; fine sand in one light color. Graphics: **vibration made visible** — sand jumps into standing-wave figures with each frequency change; the beat literally sculpts the geometry; frequency readouts; figures grow more complex through the video. Type: caps formed by sand figures aligning momentarily. Signature moves: frequency-jump re-patterns on every bar, figure-bloom on the drop, scatter-shock hits. Transitions: a new frequency wipes the pattern into the next figure. Audio: the audio IS the driver — pure-tone sweeps + drum hits visibly sculpting; low drones between figures. Best for: audio/science, meditation, physics-cool products.

**S92 · Rube Goldberg.** Canvas: machine-shop whimsy — brass, wood, string, marbles. Graphics: **absurd causal chains** — a marble tripwires a lever that flips a page that releases a balloon that lights a match... every mechanism maps to a feature (label each gadget `FEATURE_02`); camera tracks the chain's progress. Type: hand-lettered machine-part tags + blueprint callouts. Signature moves: continuous chain progress on beats, suspense near-misses, chain-reaction payoffs at drops. Transitions: the chain literally delivers you to the next machine. Audio: rolling marble clicks, spring sproings, mousetrap snaps, witty percussion orchestra. Best for: onboarding "it just works" stories, playful engineering, complex-simplified products.

**S93 · Slime Pit.** Canvas: matte-pastel or grimy lab; viscous gloss highlights. Graphics: **matte slime physics** — strings of goo stretch and snap, drips land with wobble, surfaces bulge under pressure; UI panels sit in slime molds; suction-cup pops detach elements. Type: gooey caps that stretch, drip, and blob into place. Signature moves: drip-lands on beats with jiggle settle, stretch-snap reveals, blob pressure-bulges. Transitions: the slime swallows the frame; the next scene squeezes out of it. Audio: wet suction pops, drippy plops, cartoon-funk bass, squelch percussion. Best for: playful/gross-fun, kids, anti-polish brands.

**S94 · Holo Booth.** Canvas: showroom dark; volumetric hologram glow (cyan/magenta/white) with scan-flicker. Graphics: **a rotating holo stage** — the product is presented as a volume-lit hologram: elements raster-flicker, ghost afterimages trail motion, interference bands pass through, figures occasionally drop pixels; annotation rings orbit. Type: glitch-flicker caps that stabilize on hits. Signature moves: hologram materializes (raster-build) on beats, interference sweeps, volumetric rotation reveals. Transitions: the holo powers down to scanlines → next subject boots up. Audio: projector hum, raster-sizzle, power-up whines, glitch-pop accents. Best for: AI/tech launches, futuristic products, keynote energy.

**S95 · Weathermap.** Canvas: broadcast-studio green screen + map graphics; sun/storm iconography. Graphics: **meteorology graphics** — pressure fronts sweep as curved lines with triangle/semicircle barbs, animated radar sweeps ping features, temperature gradients fill regions, seven-day panels flip like forecast columns; hurricane-spiral transitions. Type: broadcast caps + H/L pressure badges. Signature moves: front-line sweeps on beat, radar-ping reveals, icon-set flips (sun→storm→sun). Transitions: a front pushes across the map wiping the weather (and scene) behind it. Audio: broadcast-beds (uptempo news-groove), radar sweeps, thunder-crack hits, chimey forecast jingles. Best for: playful-utility, data-driven, everyday apps.

**S96 · Ant Colony.** Canvas: soil-cutaway view or leaf-top macro; amber colony glow. Graphics: **swarm logistics** — ant-trail lines carry payload crumbs (each payload = a feature) along branching paths; pheromone trails draw behind scouts; the colony constructs a structure grain by grain; traffic-jam moments resolve live. Type: trail-side engraved caps + tiny flag markers. Signature moves: trail-branch splits on beats, mass-mobilization swells, payload-handoff transitions. Transitions: the camera follows the trail into the next chamber of the nest. Audio: thousands of tiny footsteps as texture-rhythm, soil rumbles, busy warm percussion, documentary-calm pads. Best for: teamwork/logistics, community, quiet-industrious products.

**S97 · Pinball Playfield.** Canvas: playfield-art saturated neons under glass. Graphics: **the table IS the UI** — the ball riccochets between feature bumpers (each bumper = a feature that flashes and scores), flippers smack the story forward, score reels roll, tilt warnings at chaos peaks, multiball for the drop. Type: score-reel numerals + backglass-display caps. Signature moves: bumper-flash hits on beat, orbit-lane loops, plunger-launch transitions. Transitions: the ball drains and is relaunched into the next table layout. Audio: electromechanical chimes, bumper thwacks, score-reel rolls, knocker on replay. Best for: games, playful-retro, addictive-loop products.

**S98 · Docking.** Canvas: orbital black + earth-limb glow; engineering-white panels. Graphics: **zero-g assembly** — modules float in on thruster puffs, align on docking guides, lock with mechanical clunks; umbilicals connect; each docked module powers up the station (the app); solar arrays unfold for the finale. Type: mission-label caps + alignment-reticle HUD. Signature moves: drift-align-dock sequences on beats, thruster-puff micro-moves, power-up ignition sequences. Transitions: undock and float to the next berthing port. Audio: thruster puffs, docking clunks, radio squelch, station hum, majestic slow-build score. Best for: platform/ecosystem, modular products, space-tech.

**S99 · Magma Lamp.** Canvas: dim lounge; warm wax colors (orange/pink/blue) rising through liquid. Graphics: **wax-blob rhythms** — blobs bud off the floor, rise, morph through shapes (each blob phase = a feature visual), cool and sink; wax conducts the rhythm — blobs pulse with bass; occasional silver glitter-globes swirl. Type: caps formed by blob silhouettes momentarily, or retro lava-label lettering. Signature moves: blob-rise-then-pop on beats, merge-and-split dances, slow psychedelic morphs between scenes. Transitions: the lamp's contents churn — blobs recombine into the next composition. Audio: vintage soul/psychedelic bed, liquid bubble percussion, warm tape-wobble. Best for: music, wellness/chill, retro-fun products.

**S100 · Pyro Finale.** Canvas: night-sky black; firework bursts in brand colors. Graphics: **pyrotechnic choreography** — rockets streak up leaving letter-trails, shells burst into shapes (each burst = a feature icon), trailing glitter falls and forms the next lines, finale barrage fills the sky for the drop; smoke drifts and catches colored light. Type: written by rocket trails + burst-formed caps. Signature moves: launch-streak builds, burst-form reveals on hits, crackle-rainfall accents, finale saturation. Transitions: a shell's flash lights the next scene's sky. Audio: launch whistles, burst booms, crackle-fall percussion, triumphant brass/strings under it all. Best for: celebrations, launches, finales, big-moment products.

### 4.6 Style auto-selection — when STYLE_DIRECTION is empty / "auto"

If the user named a product or gave a URL but did **not** pick a style, you must choose one yourself. Do not default to a generic dark-tech look. Run this procedure and record the result in `direction.md`:

**Step 1 — Fingerprint the product.** From the Phase-1 research, write five one-line signals:

- **Category** — what it is (game, finance tool, meditation app, dev tool…).
- **Audience & voice** — who uses it and how the brand talks (playful, clinical, warm, rebellious, premium).
- **Palette & texture** — the real brand colors and the feel of its UI (flat/glassy/pixel/paper).
- **Core action** — the one verb the product exists for (tap, streak, translate, trade, organize). The hook scene must dramatize this verb.
- **Promise & emotion** — what the viewer should feel (relief, power, calm, fun, awe).

**Step 2 — Match against the library.** Shortlist 3 styles using the mapping below as a starting point (not a straitjacket). Each candidate must satisfy all gates:

- **Hook gate** — the style's signature moves can physically dramatize the core action (e.g. streak app → flip/topple/growth moves work; liquid styles struggle to show a daily checkmark).
- **Readability gate** — the style still obeys §2 rule 12 for this product's copy density (heavy-glitch styles for dense B2B copy = fail).
- **Palette gate** — the style can carry the real brand colors (re-map the spec's palette to brand tokens; the style supplies grammar and texture, not mandatory colors).
- **Casting gate** — screenshots must have a natural home in the style (device frame, plate, panel, sticker — pick whichever the style provides).

| Product signal | Strong candidates |
|---|---|
| Language / education | S56 Brush Stroke, S12 Origami, S58 Crossword, S72 Ukiyo-e, S8 Pop-Up Diorama |
| Habit / health / mindfulness | S4 Data Garden, S31 Ink in Water, S75 Zen Garden, S71 Embroidery, S14 Kinetic Sand |
| Finance / premium / luxury | S20 Clockwork, S52 Letterpress, S7 Liquid Chrome, S73 Mosaic, S85 Chiaroscuro |
| Dev tool / AI / security | S41 Phosphor Terminal, S42 Neural Mesh, S47 Particle Accelerator, S45 PCB Etch, S94 Holo Booth, S89 Phosphor Rain, S27 Noir Venetian |
| Game / playful | S21 Arcade CRT, S97 Pinball, S19 Domino Rally, S13 Clay Lab, S79 Manga Strike, S18 Parade Balloon |
| Kids / family / warm | S76 Felt Board, S64 Shadowplay, S46 Tilt-Shift Toy Town, S39 Terrarium Macro |
| Travel / geo / logistics | S9 Survey Map, S57 Split-Flap, S86 Long Exposure, S67 Hyperlapse, S50 Mission Control |
| Photo / design / creative | S24 Darkroom, S82 Prism, S6 Riso Press, S63 Kaleidoscope, S66 Anamorph, S65 Glass Parallax |
| Music / audio | S29 Vinyl RPM, S23 Cassette Rewind, S48 Oscilloscope, S91 Cymatics, S81 Laser Dome, S3 Neon Nocturne |
| Social / messaging / dating | S51 Sticker Pack, S54 Karaoke Bounce, S28 Mirrorball Disco, S33 Hive Mind, S88 Sparkler Script |
| Commerce / everyday utility | S60 Receipt Thermal, S95 Weathermap, S49 Flip Grid, S30 Office 1994, S53 Times Square |
| Story / content / heritage | S11 Stained Glass, S36 Herbarium, S78 Knot & Loop, S68 Zero-G Cabin (calm), S40 Ember Night |
| Sport / score / competition | S55 Swiss Assault, S19 Domino Rally, S90 Followspot, S100 Pyro Finale, S7 Liquid Chrome |
| Minimal / productivity / B2B | S1 Exploded Blueprint, S55 Swiss Assault, S5 Retro Broadcast, S61 Fractal Dive, S70 Foglift (teasers) |
| Launch / keynote / epic | S10 Monument Type, S94 Holo Booth, S98 Docking, S69 Hyperspace, S83 Observatory |

**Signal modifiers** (nudge within the family): dark-mode UI → prefer dark-native styles; handcrafted/artisan brand → S71–S78 family; ironic/meme voice → S22/S30/S93/S97; "serious engineering" → S1/S20/S50; "calm" → S32/S34/S38/S75; experimental/musician audience → S44/S61/S91.

**Step 3 — Decide and document.** In `direction.md` write: the chosen style + one-line justification tied to the fingerprint, 2 runners-up, how the spec's palette maps to real brand colors, and at most 1–2 borrowed moves from a runner-up if they help the concept.

**Uniqueness rule for batches.** When generating videos for a *set* of products, keep a `USED_STYLES` list and never assign the same style twice — if the best fit is taken, take the runner-up and note the substitution. Across a product line, prefer deliberately contrasting families (e.g. a chrome piece, a paper piece, a broadcast piece) rather than five dark-tech variants.

**Escape hatch.** If no style fits, declare a custom style in `direction.md` using the same spec fields (Canvas / Graphics / Type / Signature moves / Transitions / Audio) and proceed — do not stall.

---

## 5. PHASE 3 — SCRIPT & BEAT SHEET (write it yourself)

### 5.1 Script rules
- On-screen copy only (unless VOICEOVER ≠ none). Short, punchy, spoken-rhythm lines. Use contrast pairs ("Share the shot. / Not the secrets."), triplets ("Draw. Dare. Laugh."), and numbers.
- Every line must be product-true. No generic filler ("Revolutionize your workflow").
- Structure for 15s (scale proportionally for longer):

| Time | Act | Content |
|---|---|---|
| 0.0–4.0s | HOOK | Signature scene dramatizing the core action + 2–3 word slams building to the drop |
| 4.0s | DROP | Flash/shockwave on the downbeat, music opens up |
| 4.0–6.5s | PROOF | Big number counting up (stat) + kicker + support line + badge pill |
| 6.5–11.0s | FEATURES | Device with real screens, 3 features × ~1.5s, screen transitions synced to beats, callout chips |
| 11.0–13.0s | PROMISE | 3 slam lines + animated icon that "locks in" on a hit |
| 13.0–15.0s | LOCKUP | Icon spring-in, name letter-by-letter reveal with light sweep, tagline, CTA pill (platforms + URL), final chord ring-out |

For 30s: two hook beats, proof with 2–3 stats, 5–6 features (alternate device shots with abstract feature visualizations), add a "problem montage" before the drop. For 60s: add a narrative middle (a day-in-the-life sequence built from UI fragments) and a second drop.

### 5.2 Word-sync mode (when the audio has lyrics or speech)
If `MUSIC`/`VOICEOVER` is a track with words (like a song or VO), this is a **lyric/kinetic-type video**:
1. Get word-level timestamps (transcribe with whisper.cpp / Whisper API / read the LRC/SRT if provided).
2. Every word appears on screen within ±1 frame of being heard — slam, type, or morph. One accent word per phrase.
3. Between word hits, the background system keeps evolving (contours morph, radar sweeps, HUD values tick) so the frame never waits on the text.
4. Phrases leave via designed exits before the next phrase needs the space; never let more than ~2 phrases coexist unless deliberately stacking.

### 5.3 Beat sheet (mandatory file: `beats.md` + machine-readable `cues.json`)
- Choose BPM. Frames per beat = `FPS × 60 / BPM` (120 BPM @30fps → 15 frames/beat, 1 bar = 60 frames).
- List **every** event with its exact frame: text slams, element landings, screen switches, transitions, impacts, counters, SFX, music section changes.
- `cues.json` is the **single source of truth** read by BOTH the animation code and the audio generator, so sound and picture can never drift apart. Example:

```json
{
  "fps": 30, "total": 450, "bpm": 120,
  "timeline": { "drop": 120, "phoneIn": 195, "switches": [240, 285], "callouts": [211, 252, 297],
                "trio": 330, "trioLines": [333, 348, 363], "trioHit": 370, "outro": 390, "outroPill": 418 },
  "hook": { "landings": [4, 12, 19, 27, 34, 42, 49, 57], "slams": [60, 75, 90] }
}
```

---

## 6. PHASE 4 — ANIMATION TECHNIQUE LIBRARY (use MANY of these)

Use at least **15 different techniques** across a 15s video, 25+ for 30s+. Tick them off in your final report.

### 6.1 Kinetic typography
- **Slam**: scale 1.6→1.0 + blur 14px→0 + opacity 0→1 in 7 frames (expo-out), with screen shake on land.
- **Mask line reveal**: each line slides up from behind an overflow-hidden mask (110% → 0) in 10 frames, staggered 2 frames per line; exits by sliding up out of the mask.
- **Per-letter cascade**: letters rise from masks with 2-frame stagger; add a moving gradient "light sweep" across the finished word.
- **Scramble / decode**: characters cycle through random glyphs, each settling left-to-right (settle frame = i × 0.35 + 2).
- **Typewriter** with blinking cursor and key-click SFX per character.
- **Counter**: numbers count up with expo-out easing over 30–40 frames, tabular numerals, tick SFX on each change.
- **Word swap**: one word in a sentence flips/rolls vertically through alternatives (odometer effect).
- **Stroke draw**: outline text or SVG strokes drawn via `strokeDashoffset` then filled.
- **Variable emphasis**: accent-colored words, italic swaps, highlight bars that wipe behind a word.
- **Type as shape**: giant cropped letters used as masks or layout blocks moving across frame.

### 6.2 Shape & graphic animation
- SVG path draw-on (icons, underlines, checkmarks, locks, charts).
- Shockwave rings expanding from impacts (3 rings, 4-frame stagger, border thins as they grow).
- Particle bursts (40–80 particles, seeded random angles/speeds, expo-out travel, fade, glow).
- Orbiting / swirling elements that spiral into a center point (vortex collapse).
- **Implode-to-dot → burst**: the whole scene scales down + blurs into a glowing dot, which explodes into a full-screen flash on the drop.
- Morphing blobs / gradient mesh backgrounds drifting slowly.
- Grid / dot-matrix backgrounds scrolling slowly (parallax).
- Confetti with gravity and rotation, coin/star bursts, sparkles (4-point star SVG) twinkling.
- Charts building (bars grow with stagger, lines draw, heatmap cells fill in sequence).
- Tiles flipping in 3D (rotateX from −95° to 0°, transform-origin top).

### 6.2b Technical / HUD graphics (the "lab instrument" set)
- Rotating polar/radar plot: concentric rings + radial axes + degree ticks + a glowing sweep arm; axes can carry labels.
- Topographic contour field: concentric morphing rings (offset a noise field over time) as a living background.
- Blueprint schematic: draw a product-relevant object (device, mascot, icon) as thin glowing strokes with joint nodes and measurement annotations; animate it drawing itself on (path-draw per segment, then nodes blink on).
- Live data panels (monospace): tables whose numbers tick/flicker, bar rows that grow/shrink, an oscilloscope waveform trace, corner metadata readouts. Wire them to real product stats so the "lab" is measuring the product.
- Terminal typewriter: `>` prompt + per-character typing + block cursor + key clicks; the typed line then graduates into big display type.
- Word-level sync: when there is speech/lyrics/voiceover, animate text **per word or syllable exactly on the audio** — words slam in one or two at a time, accumulate, then the line swaps. Transcribe the audio to get word timestamps; never guess.
- Accent word system: per line, one word is solid accent color, one is outlined or glitch-struck; keep it consistent.
- Giant cropped type: a single word filling 60–90% of frame, partially off-canvas; mirrored or upside-down twin drifting behind.
- Chromatic aberration: split text/lines into RGB channels offset 1–3px permanently; pulse to 6–10px on impacts. Cheap version: two offset copies in pure red and blue at low opacity behind white.
- Viewfinder frame: thin corner brackets + tick marks around the frame edge; brackets subtly re-frame (scale/translate a few px) on section changes.
- Recursive corridor / infinite room: repeat a cell outline in 3-point perspective toward a vanishing point; slow dolly makes it feel endless; a "billboard" plane at the end carries the headline.

### 6.3 UI & device work
- Real screenshots inside a hand-built device frame (gradient bezel, rounded screen, colored ambient glow, animated glare sweep across the glass driven by rotation).
- Device enters with a heavy spring from below while rotating out of 3D perspective (rotateX 35°→8°, rotateY −30°→−18°), then floats (sinusoidal drift) and **swings** on every screen switch.
- Screen switches: push transition (old screen slides up + scales 0.92 + dims 50%, new screen slides in from below) synced to a beat + whoosh SFX.
- Callout chips pop out of the device with spring overshoot, pointing at the relevant UI.
- Recreate key UI moments as vector graphics (buttons being tapped with ripple, toggles flipping, toast notifications sliding in, cursor/finger taps).
- Zoom-into-UI: camera pushes into a UI element until it fills the frame and becomes the next scene.

### 6.4 Camera & space
- 2.5D perspective container (`perspective: 1600–2400px`), layers at different Z / parallax speeds.
- Continuous micro camera: `scale(1 + 0.03 × progress)`, `translate` drift, ±2–4° rotation wobble with slow sines.
- Hard moves: whip-pan (fast translate + motion blur 20–40px) , zoom-through (scale 1 → 8 through a shape into the next scene), dolly-back reveal, rack-focus (blur background/foreground alternately).
- **Screen shake** on impacts: decaying sinusoidal offset, amplitude 6–26 px depending on importance, decay τ ≈ 3.5 frames. Keep a list of `[frame, strength]` impacts in cues.

### 6.5 Transitions (pick per scene, don't repeat the same one twice in a row)
- Match cut (shape in scene A becomes shape in scene B at the same position/size).
- Morph (a card becomes a device screen; a dot becomes a ring becomes a logo).
- Flash cut on downbeat (1–2 frame white/brand-tinted flash, 8–10 frame decay).
- Mask wipe with a brand shape (circle iris, diagonal slab, pill, letterform).
- Zoom-through / portal.
- Whip-pan with directional blur.
- Scatter-reassemble (elements explode into particles, particles rebuild into next headline).
- Glitch slice (only for tech styles; 3–6 horizontal slices offset + RGB split for 4–6 frames).

### 6.6 Finishing effects
- Animated film grain (SVG `feTurbulence`, re-seeded per frame via offset), vignette, glow (`drop-shadow` / `text-shadow` in accent color), light leaks/lens streaks on big moments, subtle chromatic aberration on impacts only, background blob lighting that shifts mood per act (e.g. red "panic" glow in the problem act, brand-colored calm glow after the drop).

---

## 7. EASING & TIMING SPEC

Use these exact curves (cubic-bezier) unless the style demands otherwise:

| Name | Curve | Use |
|---|---|---|
| EXPO_OUT | (0.16, 1, 0.3, 1) | default for entrances, reveals, counters |
| IN_OUT | (0.65, 0, 0.35, 1) | transitions, screen pushes, exits |
| BACK_OUT | (0.34, 1.56, 0.64, 1) | playful pops, chips, icons |
| EASE_IN_CUBIC | t³ | things being sucked away / falling |
| Spring | damping 10–16, stiffness 90–180 | device entrance, icon lockup, bouncy UI |

Duration guide @30fps: micro (chips, ticks) 4–6f · text slam 7f · mask line 10f · element entrance 10–16f · screen push 12f · big transition 12–20f · counter 30–40f · slow drift = continuous.
Stagger guide: letters 1–2f · list rows 2–3f · tiles 4–5f · scene-level groups 6–8f.
Anticipation: before any big move, 3–5 frames of counter-motion (slight scale-down or pull-back).

---

## 8. PHASE 5 — AUDIO (music + SFX are mandatory)

### 8.1 Music
- Default: **generate it procedurally** in Python/numpy (no licensing risk), or use the provided file.
- Match genre to style: synthwave/EDM supersaws (tech, energy), funky plucks (party), chiptune squares (games), future-bass bells (AI/creative), piano + pads (inspirational), marimba (clean utility), music box/lullaby (family, calm).
- Arrangement locked to the beat sheet: **filtered intro** (low-pass sweep opening up) with hat build + snare roll into the **drop** at the hook's end; full groove (kick, clap, hats, bass, arp, pads with sidechain pump) during proof/features; brief 0.1s silence gap before the drop and before the final hit; **final chord ring-out** under the lockup; 0.5s fade at the end.
- Use a 4-chord progression that fits the mood (minor for tension/tech, major for joy, maj7 for dreamy, lullaby I–vi–IV–V for gentle).

### 8.2 Sound design — every visual event gets a sound
Build a SFX palette (synthesized or from a licensed library) and map by event type:

| Visual event | SFX |
|---|---|
| Text slam / hard landing | sub thud (pitch-dropping sine 180→42Hz) + noise transient |
| Element pop / chip | short pitched pop or blip (pentatonic pitches ascending for sequences) |
| Drop / big reveal | deep impact (sub + crash noise + snap) + high bell |
| Riser into drop | pitch-rising sine/saw with tremolo, 0.8–1.5s |
| Transitions / device moves | filtered noise whoosh (shape the envelope to the motion) |
| Counter / wheel / ticker | crisp ticks per value change |
| Lock / confirm / check | mechanical click + soft bell |
| Typewriter | per-key clicks with randomized pitch |
| Product-specific actions | design custom ones: LED zap/hum, laser scan sweep, card flick, morse beeps, coin ping, buzzer, pill-drop "tock", soft baby pop, sparkle chimes |
| Outro | whoosh → impact → sparkle bell arpeggio → UI blip on CTA |

### 8.3 Mix
- Stereo; pan repeating SFX left/right alternately for width. Light reverb on SFX, more on music for calm styles.
- Music ≈ −4 dB under SFX peaks; sidechain/duck music under voiceover if present.
- Master: soft clip / limiter, target **−14 LUFS integrated, true peak ≤ −1 dBTP**.
- Calm styles: reduce impact and thud gains ~30%, no screen shake.
- If using a voiceover with ffmpeg `sidechaincompress`, ALWAYS `asplit` the voice stream before feeding both the sidechain and the mix, otherwise the voice silently disappears. Verify speech presence with a transcription pass.

---

## 9. PHASE 6 — TECHNICAL IMPLEMENTATION

### 9.1 Stack (recommended)
- **Remotion** (React, frame-deterministic) + `@remotion/google-fonts` + `@remotion/media` for audio. Alternatives only if unavailable: Motion Canvas, or HTML canvas + Puppeteer + ffmpeg.
- **All animation is a pure function of `useCurrentFrame()`** — use `interpolate`, `spring`, `Easing`. **Never** use CSS transitions/animations, `setTimeout`, or `Math.random()` (use seeded `random("seed")`) — renders must be deterministic.
- `extrapolateLeft/Right: "clamp"` on every interpolate.

### 9.2 Architecture
```
src/<project>/
  cues.json          # single source of truth for timing (shared with audio script)
  kit.tsx            # tokens, easings, useLayout(), primitives: Slam, MaskLine, Pop, Rings, Flash,
                     # Shake, Background (blobs + pattern + grain + vignette), Phone/Device, GradText, Pill
  scenes/*.tsx       # one file per scene; each scene handles its own enter/exit
  Main.tsx           # scene list [Component, fromFrame, toFrame] with 2–6 frame overlaps for transitions
  Root.tsx           # one <Composition> per aspect ratio, all sharing Main
tools/
  gen_audio.py       # reads cues.json, writes music.wav + sfx.wav + mix.wav
  preview.sh         # renders a contact sheet of stills
  render.sh          # renders all aspect ratios sequentially
```
- **Responsive, not cropped**: one component, multiple compositions. `const v = height > width; const u = Math.min(width, height) / 1080;` Multiply every size by `u`. Re-layout for vertical (stack instead of side-by-side, text on top / device below, narrower line lengths). Check text never overflows its container in any ratio — compute font size from available width for long words.
- Scene switching: render a scene only while `from ≤ frame < to` to keep renders fast.
- Keep heavy effects (blur, big shadows) off huge layers when possible; prefer transforms and opacity.
- Load only the font weights you use.

### 9.3 Render
- Render sequentially (parallel renders can crash smaller machines): `npx remotion render <comp> out/<name>.mp4 --codec=h264 --crf=18`.
- Output naming: `{{PRODUCT_NAME}}-motion-{{DURATION}}s-16x9.mp4`, `...-9x16.mp4`.

---

## 10. PHASE 7 — QA LOOP (repeat until everything passes)

1. **Contact sheet**: render stills at ~13 key frames per aspect ratio (one inside every scene, plus mid-transition frames) at 30% scale, tile into a grid, and *look at it*. Fix overflow, clipping, collisions, empty areas, off-center compositions, illegible text, wrong crops.
2. **Motion density audit**: sample 20 random frames; for each, list what is moving. Any frame with < 3 moving things → add motion.
3. **Hold audit**: search for any hero element static > 8 frames → add drift/push.
4. **Sync audit**: every entry in cues.json has both a visual and an audio event; check waveform peaks line up with visual hits.
5. **Read audit**: every text line meets the minimum on-screen time in §2.12.
6. **Transition audit**: count transitions; ≥ 70% motivated; no identical transition twice in a row.
7. **Audio check**: loudness (`ffmpeg -af ebur128`), peak ≤ −1 dB, no clipping, final 0.5s fade, music present for the whole duration.
8. **File check** with ffprobe: exact duration, dimensions, h264 + aac, fps.
9. Iterate. The best results come from multiple rounds of tweaking — do at least **2 full review-and-fix passes** before delivering.

---

## 11. BANNED (anti-patterns)

- Static slides with text fading in and out ("PowerPoint look").
- Default crossfades between every scene; generic "slide from left" for everything.
- Linear easing on entrances/exits.
- Centered-everything with no compositional variety across scenes.
- Stock photos, stock video, AI video clips, clip-art, emoji.
- Fake UI when real screenshots exist; a phone mockup inside another phone mockup.
- Invented statistics or claims not found in research.
- Walls of text, more than 3 lines on screen, lines longer than ~7 words.
- Rainbow palettes with no hierarchy; more than 2 typefaces.
- Silence or music-only with no SFX; SFX that don't match an on-screen event.
- Text clipped by frame edges or overflowing containers in any aspect ratio.
- Elements vanishing on a hard cut with no exit animation.
- Ending without a clear brand lockup + CTA.

---

## 12. DELIVERABLES & FINAL REPORT

Deliver:
1. Rendered videos for every requested aspect ratio in `{{OUTPUT_DIR}}`.
2. `research.md`, `direction.md`, `beats.md`, `cues.json`.
3. Source code + audio generator + render/preview scripts, runnable with one command.
4. A final report containing:
   - The script (every on-screen line with its time range).
   - Scene-by-scene breakdown: techniques used, transition into the next scene, SFX used.
   - Checklist of techniques from §6 that were used (target ≥ 15 for 15s).
   - QA results: ffprobe output, LUFS/peak, motion-density audit summary, list of fixes made in each review pass.
   - Known limitations / anything that could not be verified.

---

## 13. EXAMPLE — 15s BEAT SHEET @30fps, 120 BPM (15 frames per beat)

| Frame | Beat | Visual | Audio |
|---|---|---|---|
| 0–4 | – | Background fades from black, grain + blobs drifting, camera slowly pushing | filtered pad starts |
| 4–57 | 1–4 | **Hook**: 8 product-related objects fly in from off-screen and land around the frame (one every ~7f, each with squash/overshoot and a counter ticking up in the center) | pitched pops on each landing, hats building |
| 60 / 75 / 90 | 5 / 6 / 7 | 3 word slams build a question/claim; objects start spiraling toward center | sub thuds + swirling whoosh + riser |
| 98–118 | – | Vortex collapse: all objects spiral into a glowing dot; headline implodes | riser peaks, snare roll accelerates, 0.1s silence |
| 120 | 9 (DROP) | Dot bursts to full-screen flash → shockwave rings + 40 particles → **stat** counts up with overshoot | big impact + bell, groove kicks in, ticks on count |
| 160 | – | Badge pill springs in under the stat | blip |
| 189–207 | – | Stat flies up & blurs away while device springs in from below in 3D | whoosh + soft thud on landing |
| 203–240 | – | Feature 1: kicker + 2-line headline mask-reveal left, device floats right; callout chip pops | blip |
| 240 | 17 | Screen push to screen 2, device swings | whoosh |
| 285 | 20 | Screen push to screen 3, device swings | whoosh |
| 322–334 | – | Device swings away 80° + shrinks; headline exits up | whoosh |
| 330–370 | – | **Promise**: icon draws itself stroke-by-stroke; 3 slam lines at 333/348/363 | thuds on each line |
| 370 | 25 | Icon "locks" (fills, glows, rings) | click + bell |
| 384–390 | – | Promise scales up and fades | whoosh |
| 390 | 27 | Flash → app icon springs in with rotation; name reveals letter-by-letter with light sweep | impact + sparkle arpeggio |
| 406–418 | – | Tagline rises in; CTA pill pops ("Free on iOS & Android · url") | blip |
| 418–450 | – | Slow push-in on lockup, rings fading, particles drifting | final chord ring-out, 0.5s fade |

Now execute all phases in order. Start with research. Do not skip the QA loop.
