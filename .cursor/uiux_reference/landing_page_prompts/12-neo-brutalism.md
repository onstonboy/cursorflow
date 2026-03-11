# Design Style: Neo-Brutalism

## Design Philosophy

A raw, high-contrast aesthetic that mimics print design and DIY punk culture. Characterized by cream backgrounds, thick black borders (4px), hard offset shadows with zero blur, clashing vibrant colors (Hot Red, Vivid Yellow, Soft Violet), and Space Grotesk typography at heavy weights. Embraces asymmetry, rotation, sticker-like layering, and organized visual chaos.

**Vibe**: Raw, Punk, Print-inspired, High-contrast, Bold, Unapologetic, DIY, Sticker-aesthetic

## Layout Ideas

### Hero
Asymmetric split with massive rotated headline text blocks. Left side has border-boxed text with different colors and rotations. Right side features a "visual chaos" container with overlapping shapes and badges. CTAs use brutalist shadows that translate on hover. Fully responsive with stacked layout on mobile.

### Stats
4-column brutalist grid (2 columns on tablet, 1 on mobile) with thick white borders on black background. Hover inverts to accent color.

### Features
Three-column grid with lifted cards featuring corner decorations (circle/triangle/square). Each card has geometric icon in bordered container. Hover lift effect.

### How It Works
Horizontal timeline with thick connecting line (desktop only). Steps use alternating geometric shapes.

### Pricing
Three-tier cards with thick black borders and hard offset shadows. Selected plan has inverted (black) background.

### Testimonials
Bordered quote blocks with rotated avatar frames. Raw, poster-like treatment.

## Design Token System

### Colors
- **Background**: Cream (#F5F5DC or similar off-white)
- **Foreground**: Black (#000000)
- **Accent**: Hot Red (#E63946), Vivid Yellow (#FACC15), Soft Violet (#8B5CF6)—use in clashing combinations
- **Border**: 4px solid black throughout

### Typography
- **Font**: Space Grotesk, heavy weights (600–700)
- **Style**: Uppercase for headlines, bold everywhere. No delicate type.

### Shadows
- **Brutalist shadow**: `box-shadow: 6px 6px 0px 0px #000` (or 8px 8px). Zero blur. Hard offset. Hover can translate so shadow "follows" or disappears.

### Border Radius
- Minimal (0px–4px). Sharp corners preferred.

### Borders
- **Standard**: 4px solid black. Use on cards, buttons, and key containers.

## Component Patterns

### Buttons
- Solid fill or outline with 4px black border. Hard offset shadow. Hover: translate (2px 2px) so shadow reduces or inverts colors.

### Cards
- White or cream background, 4px black border, hard offset shadow. Optional small geometric shape (circle, square, triangle) in corner. Rotation (-2deg to 2deg) for sticker feel.

### Layout
- Asymmetry is key. Break the grid. Overlap elements. Use rotation. Sticker-like layering.

## Anti-Patterns
- No soft shadows or blur
- No minimal or “clean” spacing without purpose
- No muted or corporate color palette
- Avoid perfect symmetry

---

*Design prompt reference from [Design Prompts](https://www.designprompts.dev/) — AI-Powered Design Style Explorer. © Design Prompts.*
