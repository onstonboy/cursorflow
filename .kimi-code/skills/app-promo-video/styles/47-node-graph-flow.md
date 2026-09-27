# Style 47 — Node Graph Flow

Systems thinking made visible. Features as labeled nodes on a canvas connected by animated bezier pipes; data packets travel along edges and activate what they hit.

Best for: automation, integration platforms, no-code tools, AI pipelines, API orchestration.

## Tokens

```ts
canvas "#0C0F16" + dot grid (24px dots at 8%)
node: "#161C28" fill, 1.5px border; glows brand color when active
edges: 2px strokes, flow dashes animating
accent cycle: mint→cyan→purple→pink per node
Font: mono labels inside nodes + sans titles.
FPS 30.
```

Motion grammar: flow — SVG edges drawn via `strokeDasharray` offset animation (dashes travel continuously); packets = small dots traveling along paths (parametrize bezier point-at-length via precomputed samples); node activation = border glow + scale 1→1.06→1 + ripple ring.

## Core mechanism

```tsx
// Edge: cubic bezier path between node anchors; flow dashes:
<path strokeDasharray="8 8" strokeDashoffset={-f*2} .../> // dashes travel
// Packet: sample the path — precompute ~50 point positions along the bezier
//   (lerp the 4 control points), index = (f*speed + offset) % 50 → dot div.
// On packet arrival: node fires — glow pulse + emits its own packets onward.
// Node types: trigger (play glyph), action (gear), output (check). Screenshots
//   appear as expanded node "inspectors" — node grows into a card showing the
//   screen, then collapses back leaving a thumbnail node.
// Canvas camera: slow pan + occasional zoom-to-cluster (scale 1→1.3 toward a
//   node's position). Mini-map in corner (optional flourish).
// Build sequence: nodes+edges draw themselves in order — graph assembles
//   during the video as features connect.
```

## Scene grammar (7–9 scenes, 100–130s)

S01: empty canvas → trigger node drops + first edge draws · S02: problem = disconnected island node, dimmed, "no path" · S03–S07: each feature adds a node to the graph; packets flow through the growing pipeline (packet lights a path through all previously added nodes — compound value); inspector pops show screenshots · S08: full graph executes — packets light the whole graph at once → converge to logo node → CTA.

## Audio

- Music: plucky electronic/minimal-techno 105 BPM — numpy: sequenced pluck arp, warm sub, precise hats; add a harmony layer as the graph grows (build complexity = story).
- SFX: node-drop thunk, packet zip traveling, activation chime on each arrival.
- VO: systems-narrator — explains the graph as it builds ("when X, then Y, automatically").

## Signature details

Traveling dash-flow on edges · packets with bezier-true paths · inspector pop-and-collapse · the graph literally assembling across the video · all-nodes-fire finale.

Anti-patterns: straight-line edges (bezier or bust), packets that jump instead of travel, static graph (it must grow), node labels that aren't mono.
