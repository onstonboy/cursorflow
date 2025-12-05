---
agent: agent
---

# UI/UX Design System Generator Guide

This document provides a structured approach for AI to analyze user requirements and generate comprehensive UI/UX design specifications from basic descriptions to complete design systems.

## CRITICAL: Mandatory Execution

**⚠️ AI MUST COMPLETE ALL STEPS SEQUENTIALLY**

When you receive a UI/UX design request, you MUST:
1. Execute ALL 6 steps in order
2. Generate ALL deliverables for each step
3. Create complete design specifications
4. Do NOT skip any step
5. Do NOT ask for permission to proceed - execute automatically
6. Complete the entire workflow before returning results

---

## UI/UX Design Generation Workflow

### Step 0: Research Top-Tier Similar Products (MANDATORY)

**Objective:** Research and analyze top-tier similar products on the internet to inform design decisions

**⚠️ AI MUST COMPLETE THIS STEP BEFORE PROCEEDING TO STEP 1**

#### 0.0 Check UI Styles Reference & Match Project Requirements (MANDATORY)

**⚠️ CRITICAL: AI MUST CHECK THE UI STYLES REFERENCE FIRST**

**Action Required:**
1. **Read and analyze** `.cursor/commands/common/ui_styles_reference.md`
2. **Extract project/feature requirements** from the user's request
3. **Match project type** with suitable UI styles from the reference
4. **Research on Internet** (if possible) to validate and find additional inspiration
5. **Select best-fit UI styles** that match the project requirements

**Process:**
```markdown
### UI Styles Reference Analysis

**Project/Feature Requirements:**
- Project Type: [SaaS, E-commerce, Portfolio, Gaming, etc.]
- Target Audience: [Description]
- Brand Personality: [Modern, Luxury, Playful, Professional, etc.]
- Key Features: [List main features]
- Performance Requirements: [Mobile, Desktop, Both]
- Complexity Constraints: [Low, Medium, High]

**UI Styles Reference Check:**
1. Reviewed `.cursor/commands/common/ui_styles_reference.md`
2. Identified relevant styles based on "Suitable Project Types" attribute
3. Cross-referenced with project requirements

**Matching UI Styles Found:**
- [Style Name 1] - WOW Factor: X/10, Complexity: [Low/Medium/High], Performance: [Excellent/Good/Fair]
  - Match Score: [High/Medium/Low]
  - Why it fits: [Explanation]
  - Suitable Project Types: [List from reference]
  - Visual Description: [From reference]
  - Technical Specifications: [From reference]
  
- [Style Name 2] - WOW Factor: X/10, Complexity: [Low/Medium/High], Performance: [Excellent/Good/Fair]
  - Match Score: [High/Medium/Low]
  - Why it fits: [Explanation]
  - Suitable Project Types: [List from reference]
  - Visual Description: [From reference]
  - Technical Specifications: [From reference]

**Internet Research (if applicable):**
- [Additional research findings from web search]
- [Current trends in similar products]
- [Validation of style choices]
- [Real-world implementation examples]

**Selected Best-Fit UI Styles:**
1. **Primary Style:** [Style Name] - [Brief justification]
   - WOW Factor: [X/10]
   - Complexity: [Low/Medium/High]
   - Performance: [Excellent/Good/Fair]
   - Mobile Support: [Yes/Partial/No]
   
2. **Secondary Style (optional):** [Style Name] - [Brief justification]
   - WOW Factor: [X/10]
   - Complexity: [Low/Medium/High]
   - Performance: [Excellent/Good/Fair]
   - Mobile Support: [Yes/Partial/No]

3. **Combination Approach:** [If combining multiple styles]
   - How styles complement each other
   - Implementation strategy

**Style Implementation Plan:**
- Background Effects: [Selected from reference with technical specs]
- Animation Patterns: [Selected from reference with timing]
- Visual Effects: [Selected from reference with parameters]
- Color Palette: [From style reference or custom]
- Typography: [From style reference or custom]
- Component Styles: [How style affects components]
```

**Deliverable:** UI Styles Reference Analysis document with matched styles, technical specifications, and implementation plan

---

#### 0.1 Identify Similar Products

**Research Sources:**
- Industry-leading products in the same category
- Award-winning design examples (Awwwards, CSS Design Awards, etc.)
- Popular apps/websites with similar functionality
- Design inspiration platforms (Dribbble, Behance, Mobbin, etc.)
- Case studies and design system documentation
- App Store/Play Store top-rated apps in the category

**Research Criteria:**
- Products with similar functionality/domain
- Products recognized for excellent UX/UI
- Products with high user ratings and engagement
- Products that represent current design trends
- Analyze at least 3-5 top-tier products

#### 0.2 Analyze Design Patterns & Trends (WITH FOCUS ON ANIMATIONS, BACKGROUNDS & EFFECTS)

**⚠️ CRITICAL FOCUS: Animations, Backgrounds, and Visual Effects - MAKE THEM WOW**

**What to Analyze (Prioritize WOW Factor):**
```markdown
### Competitive Analysis Summary

**Products Analyzed:**
1. [Product Name] - [URL/Reference]
   - Category: [E-commerce, SaaS, Social, etc.]
   - Key Strengths: [List design strengths]
   - Design Patterns: [Notable patterns]
   - Color Palette: [Primary colors, accent colors]
   - Typography: [Font choices, sizes, weights]
   - Layout Structure: [Grid systems, spacing]
   - Interaction Patterns: [Notable interactions]
   - Component Design: [Button styles, card designs, etc.]
   
   **🎨 ANIMATIONS & EFFECTS (WOW FACTOR - PRIMARY FOCUS):**
   - Background Effects: [Animated gradients, particle systems, video backgrounds, parallax layers, geometric patterns, glass morphism, mesh gradients, noise textures]
   - Page Transitions: [Smooth transitions, fade effects, slide animations, reveal effects]
   - Micro-interactions: [Button hover effects, card animations, loading states, icon animations]
   - Scroll Animations: [Parallax scrolling, reveal animations, sticky effects, scroll-triggered animations]
   - Hover Effects: [Transform effects, shadow changes, color transitions, glow effects]
   - Loading Animations: [Skeleton screens, progress indicators, creative loaders, animated spinners]
   - Special Effects: [Glass morphism, blur effects, glow effects, 3D transforms, particle systems]
   - Animation Timing: [Duration, easing functions, choreography, performance]
   - Visual Impact: [What makes it WOW? What immediately catches attention? How does it create visual attraction?]

2. [Product Name] - [URL/Reference]
   - [Same structure as above, especially ANIMATIONS & EFFECTS section]

3. [Product Name] - [URL/Reference]
   - [Same structure as above, especially ANIMATIONS & EFFECTS section]

**Common Patterns Identified:**
- [Pattern 1]: [Description, frequency, and why it works]
- [Pattern 2]: [Description, frequency, and why it works]
- [Pattern 3]: [Description, frequency, and why it works]

**🎬 WOW Animation Patterns Identified:**
- [Animation Pattern 1]: [Description, visual impact, how it creates WOW, implementation approach]
- [Animation Pattern 2]: [Description, visual impact, how it creates WOW, implementation approach]
- [Animation Pattern 3]: [Description, visual impact, how it creates WOW, implementation approach]

**🎨 WOW Background Effects Identified:**
- [Background Effect 1]: [Description, visual impact, how it creates WOW, implementation approach]
- [Background Effect 2]: [Description, visual impact, how it creates WOW, implementation approach]
- [Background Effect 3]: [Description, visual impact, how it creates WOW, implementation approach]

**✨ Special Effects That Create WOW:**
- [Effect 1]: [Description, implementation approach, visual impact, performance considerations]
- [Effect 2]: [Description, implementation approach, visual impact, performance considerations]
- [Effect 3]: [Description, implementation approach, visual impact, performance considerations]

**Modern Design Trends Observed:**
- [Trend 1]: [Description and implementation examples]
- [Trend 2]: [Description and implementation examples]
- [Trend 3]: [Description and implementation examples]

**Best Practices Extracted:**
- [Practice 1]: [How it improves UX/UI]
- [Practice 2]: [How it improves UX/UI]
- [Practice 3]: [How it improves UX/UI]

**Design Insights:**
- [Insight 1]: [Key takeaway for our design]
- [Insight 2]: [Key takeaway for our design]
- [Insight 3]: [Key takeaway for our design]

**💡 WOW Factor Insights:**
- [Insight 1]: [What creates visual attraction and engagement, how to make it memorable]
- [Insight 2]: [How animations/backgrounds match the product theme and user requirements]
- [Insight 3]: [Techniques for creating memorable first impressions and user attraction]
- [Insight 4]: [Balance between WOW factor and performance]
```

#### 0.3 Design Style Determination & WOW Factor Planning

**Style Decision Logic:**
1. **If user specifies a style:** Use the specified style (e.g., glass morphism, neumorphism, material design, brutalist)
2. **If user does NOT specify a style:** Default to **MODERN** design style

**Modern Design Characteristics (Default):**
- Clean, minimalist aesthetics with purposeful use of space
- Generous white space for breathing room
- Subtle shadows and depth (elevation system)
- Smooth, purposeful animations and transitions (200-300ms)
- Contemporary color palettes (often with vibrant accent colors)
- Modern typography (sans-serif families, clean lines, proper hierarchy)
- Rounded corners (moderate radius, typically 8-16px for cards, 4-8px for buttons)
- Card-based layouts with clear separation
- Micro-interactions for feedback
- Responsive and adaptive design (mobile-first approach)
- Accessibility-first approach (WCAG AA compliance)
- Consistent spacing system (typically 4px or 8px base unit)
- Modern iconography (outline or filled, consistent style)

**🎨 WOW Background & Animation Strategy (MANDATORY):**

**Based on user requirements, create corresponding WOW backgrounds and animations that attract users:**

**Background Design Approach:**
- **Match Theme:** Background must align with user's product/theme requirements
  - Tech/SaaS: Futuristic gradients, particle systems, geometric patterns
  - E-commerce: Product-focused backgrounds, subtle animations, elegant textures
  - Creative/Portfolio: Bold gradients, artistic patterns, dynamic effects
  - Luxury: Elegant textures, subtle animations, sophisticated color schemes
  - Nature/Wellness: Organic patterns, flowing gradients, natural textures
  - Gaming/Entertainment: Dynamic effects, vibrant colors, energetic animations
- **Visual Impact:** Create backgrounds that immediately grab attention and create WOW
- **Animation Integration:** Backgrounds should have subtle or dynamic animations based on theme
- **Background Types:**
  - Animated gradients (smooth color transitions, flowing gradients)
  - Particle systems (floating particles, stars, dots, interactive particles)
  - Video backgrounds (subtle, looping videos that match theme)
  - Parallax layers (multiple depth layers creating depth illusion)
  - Geometric patterns (animated shapes, lines, grids)
  - Glass morphism effects (blurred, translucent layers with depth)
  - Mesh gradients (complex, flowing color meshes)
  - Noise textures (animated grain effects, texture overlays)
  - Custom illustrations (animated illustrations matching theme)

**Animation Design Approach:**
- **Entrance Animations:** Create WOW first impression
  - Fade-in with scale (elements appear with gentle scale)
  - Slide-in with bounce (elements slide in with playful bounce)
  - Reveal effects (elements reveal progressively)
  - Stagger animations (elements animate in sequence)
- **Interactive Animations:** Respond to user actions with impressive feedback
  - Button hover: Scale, glow, shadow increase, color shift
  - Card hover: Lift effect, shadow increase, slight scale
  - Input focus: Glow effect, border animation, label animation
- **Scroll Animations:** Elements animate as user scrolls
  - Parallax effects (different scroll speeds)
  - Reveal animations (fade-in on scroll)
  - Sticky effects (elements stick and transform)
  - Progress indicators (show scroll progress)
- **Loading States:** Creative, engaging loading animations
  - Skeleton screens with shimmer effect
  - Creative spinners matching theme
  - Progress bars with animations
  - Custom loaders with brand personality
- **Page Transitions:** Smooth, impressive transitions
  - Fade transitions
  - Slide transitions
  - Scale transitions
  - Custom transitions matching theme
- **Micro-interactions:** Delightful small animations
  - Button press feedback
  - Card flip effects
  - Icon animations
  - Badge animations
  - Notification animations

**WOW Factor Requirements:**
- **Visual Attraction:** Design must immediately catch user's eye and create memorable first impression
- **Memorable:** Create unique, memorable visual experiences that users remember
- **Performance:** Smooth 60fps animations (optimize for performance, use GPU acceleration)
- **Purposeful:** Every animation should have a purpose (guide attention, provide feedback, create delight)
- **Thematic Match:** Animations/backgrounds must match user's product theme and requirements exactly
- **Balance:** Balance WOW factor with usability (don't sacrifice usability for effects)

**Deliverable:** Complete competitive analysis document with design insights, patterns, style determination, and detailed WOW background/animation strategy matching user requirements

---

### Step 1: Analyze User Requirements (MANDATORY)

**Objective:** Extract design intent and style preferences from user input, informed by competitive research

**Example Input:** "I want to do a shoes shop web/app with glass morphism style"

#### 1.1 Core Requirements Extraction
- **Primary Purpose:** [e.g., Shoe shopping e-commerce]
- **Platform:** [Web/Mobile App/Desktop/Cross-platform]
- **Target Audience:** [Who will use this?]
- **Key Actions:** [Browse, Purchase, Filter, etc.]

#### 1.2 Design Style Analysis
- **Visual Style:** [Glass morphism, Material, Minimal, Modern (default), etc.]
  - **Note:** If no style specified, default to MODERN design
- **Mood/Tone:** [Modern (default), Elegant, Playful, Professional]
- **Color Scheme:** [Inferred from competitive research or requested]
- **Animation Preferences:** [Subtle (default for modern), Dynamic, None]
- **Influences from Research:** [Key patterns/trends from Step 0 that will be incorporated]

#### 1.3 Implicit Requirements
- Industry standards (e.g., e-commerce needs cart, wishlist)
- Platform conventions (iOS/Android/Web patterns)
- Accessibility needs

**Deliverable:**
```markdown
## Requirement Analysis

**Project:** [Name]
**Platform:** [Platform]
**Style:** [Style keywords]
**Target Users:** [User description]

**Core Features:**
- [Feature 1]
- [Feature 2]

**Design Direction:**
- Visual Style: [Style - Modern if not specified]
- Color Palette: [Colors - informed by competitive research]
- Typography: [Font characteristics - modern sans-serif if not specified]
- Design Influences: [Key patterns from top-tier products analyzed]
```

---

### Step 2: Define Design Atomic Components (MANDATORY)

**Objective:** Specify all foundational UI elements following atomic design principles

#### 2.1 Typography System
```markdown
### Typography

**Font Families:**
- Primary: [Font name] - Body text, general content
- Secondary: [Font name] - Headings, emphasis
- Monospace: [Font name] - Code, technical content

**Type Scale:**
- Display: [Size]px / [Line height] - Hero sections
- H1: [Size]px / [Line height] - Page titles
- H2: [Size]px / [Line height] - Section headers
- H3: [Size]px / [Line height] - Subsection headers
- H4: [Size]px / [Line height] - Card titles
- Body Large: [Size]px / [Line height] - Prominent text
- Body: [Size]px / [Line height] - Standard text
- Body Small: [Size]px / [Line height] - Secondary text
- Caption: [Size]px / [Line height] - Labels, hints

**Font Weights:**
- Light: 300
- Regular: 400
- Medium: 500
- Semibold: 600
- Bold: 700

**Style Applications:**
[How typography applies to the design style, e.g., glass morphism typography with subtle shadows]
```

#### 2.2 Color System
```markdown
### Color Palette

**Primary Colors:**
- Primary: [Hex] - Main actions, CTAs
- Primary Light: [Hex] - Hover states
- Primary Dark: [Hex] - Active states

**Secondary Colors:**
- Secondary: [Hex] - Supporting elements
- Secondary Light: [Hex]
- Secondary Dark: [Hex]

**Neutral Colors:**
- Background: [Hex] - Main background
- Surface: [Hex] - Card backgrounds
- Surface Elevated: [Hex] - Elevated cards
- Border: [Hex] - Dividers, outlines
- Text Primary: [Hex] - Main text
- Text Secondary: [Hex] - Supporting text
- Text Disabled: [Hex] - Disabled state

**Semantic Colors:**
- Success: [Hex] - Success messages
- Warning: [Hex] - Warning messages
- Error: [Hex] - Error messages
- Info: [Hex] - Info messages

**Style-Specific Colors:**
[For glass morphism: transparency values, backdrop blur amounts]
- Glass Surface: rgba([R], [G], [B], 0.1-0.3)
- Glass Border: rgba([R], [G], [B], 0.2)
- Backdrop Blur: [Value]px
```

#### 2.3 Spacing System
```markdown
### Spacing Scale

**Base Unit:** [Value]px (typically 4px or 8px)

**Scale:**
- xs: [Value]px - Tight spacing
- sm: [Value]px - Close spacing
- md: [Value]px - Standard spacing
- lg: [Value]px - Comfortable spacing
- xl: [Value]px - Loose spacing
- 2xl: [Value]px - Section spacing
- 3xl: [Value]px - Large section spacing

**Component Padding:**
- Button: [Vertical] x [Horizontal]
- Input: [Vertical] x [Horizontal]
- Card: [All sides]
```

#### 2.4 Border & Radius System
```markdown
### Borders & Radius

**Border Radius:**
- None: 0px
- xs: [Value]px - Subtle rounding
- sm: [Value]px - Standard rounding
- md: [Value]px - Moderate rounding
- lg: [Value]px - Large rounding
- xl: [Value]px - Extra large rounding
- full: 9999px - Pill shape

**Border Width:**
- thin: 1px
- medium: 2px
- thick: 4px

**Style Application:**
[e.g., Glass morphism uses medium radius (16-24px) with thin borders]
```

#### 2.5 Shadow & Elevation System
```markdown
### Shadows & Elevation

**Shadow Levels:**
- Level 1 (Subtle): [Box-shadow values]
- Level 2 (Low): [Box-shadow values]
- Level 3 (Medium): [Box-shadow values]
- Level 4 (High): [Box-shadow values]
- Level 5 (Highest): [Box-shadow values]

**Style-Specific Shadows:**
[For glass morphism: inner shadows, glow effects]
- Glass Shadow: [Values]
- Inner Glow: [Values]
```

**Deliverable:** Complete atomic design system specification

---

### Step 3: Define Molecular Components (MANDATORY)

**Objective:** Design composite UI elements built from atomic components

#### 3.1 Button System
```markdown
### Buttons

**Button Variants:**

1. **Primary Button**
   - Purpose: Main CTAs (Add to Cart, Purchase)
   - States: Default, Hover, Active, Disabled
   - Specifications:
     * Background: [Color]
     * Text: [Color]
     * Border: [Style]
     * Padding: [Values]
     * Border Radius: [Value]
     * Shadow: [Level]
   - Glass Style: [Specific glass morphism properties]

2. **Secondary Button**
   - Purpose: Secondary actions (View Details, Filter)
   - States: Default, Hover, Active, Disabled
   - Specifications: [Similar structure]

3. **Text Button**
   - Purpose: Tertiary actions (Cancel, Skip)
   - Specifications: [Details]

4. **Icon Button**
   - Purpose: Compact actions (Like, Share, Close)
   - Specifications: [Details]

5. **Floating Action Button (FAB)**
   - Purpose: Primary page action
   - Specifications: [Details]

**Button Sizes:**
- Small: [Height]px
- Medium: [Height]px
- Large: [Height]px

**Icons in Buttons:**
- Position: [Left/Right/Only]
- Size: [Value]px
- Spacing: [Value]px
```

#### 3.2 Input Fields
```markdown
### Input Fields

**Text Input**
- States: Default, Focus, Filled, Error, Disabled
- Specifications:
  * Height: [Value]px
  * Border: [Style]
  * Background: [Color/Glass effect]
  * Label: [Floating/Fixed]
  * Helper text: [Position and style]
  * Error message: [Position and style]

**Search Input**
- Icon: [Position]
- Clear button: [When to show]
- Autocomplete: [Style]

**Textarea**
- Min/Max height: [Values]
- Resize: [Allowed/Not allowed]

**Select/Dropdown**
- Style: [Native/Custom]
- Dropdown appearance: [Glass effect details]

**Checkbox/Radio**
- Size: [Value]px
- Checked state: [Style]
- Label spacing: [Value]

**Toggle/Switch**
- Specifications: [Details]
```

#### 3.3 Cards
```markdown
### Card Components

**Product Card** (for shoe shop example)
- Layout: [Image + Title + Price + CTA]
- Dimensions: [Width x Height]
- Glass effect: [Specific properties]
- Hover state: [Transformation/elevation change]
- Image aspect ratio: [Ratio]
- Content padding: [Values]

**Info Card**
- Purpose: [Display information]
- Specifications: [Details]

**Interactive Card**
- Purpose: [Clickable cards]
- Specifications: [Details]
```

#### 3.4 Chips & Tags
```markdown
### Chips & Tags

**Filter Chip**
- Purpose: Filtering options (Size, Color, Brand)
- States: Unselected, Selected
- Specifications: [Details]

**Tag**
- Purpose: Labels, categories
- Specifications: [Details]
```

**Deliverable:** Complete molecular component library

---

### Step 4: Define Organism Components (MANDATORY)

**Objective:** Design complex UI sections combining molecules and atoms

#### 4.1 Navigation Components
```markdown
### Navigation

**App Bar / Header**
- Height: [Value]px
- Glass effect: [Backdrop blur, transparency]
- Content:
  * Logo: [Position, size]
  * Navigation links: [Style]
  * Search: [Position, style]
  * Icons: [Cart, Profile, etc.]
  * Mobile menu trigger: [Position]
- Sticky behavior: [Yes/No, transition]

**Bottom Navigation Bar** (Mobile)
- Height: [Value]px
- Items: [3-5 main items]
- Active indicator: [Style]
- Labels: [Always shown/On selection]
- Glass effect: [Details]

**Sidebar / Navigation Drawer**
- Width: [Value]px
- Overlay: [Color, opacity]
- Animation: [Slide/Fade]
- Content structure: [Layout]

**Breadcrumb**
- Style: [Separator, hover states]
- Max items shown: [Number]
```

#### 4.2 Dialog & Modal System
```markdown
### Dialogs & Modals

**Alert Dialog**
- Purpose: Confirmations, warnings
- Structure: [Title + Message + Actions]
- Backdrop: [Color, opacity, blur]
- Glass container: [Properties]
- Max width: [Value]px
- Animations: [Entry/Exit]

**Full-Screen Modal**
- Use case: [Detailed views, forms]
- Close button: [Position]
- Specifications: [Details]

**Bottom Sheet** (Mobile)
- Heights: [Half/Full/Auto]
- Drag handle: [Style]
- Backdrop: [Details]
- Specifications: [Details]
```

#### 4.3 List & Grid Components
```markdown
### Lists & Grids

**Product Grid** (for shoe shop)
- Columns: Desktop [4], Tablet [3], Mobile [2]
- Gap: [Value]px
- Responsive breakpoints: [Values]
- Loading skeleton: [Style]

**List View**
- Item height: [Value]px
- Dividers: [Style]
- Hover state: [Background change]

**Infinite Scroll**
- Loading indicator: [Position, style]
- Specifications: [Details]
```

#### 4.4 Feedback Components
```markdown
### Feedback Elements

**Toast / Snackbar**
- Position: [Top/Bottom, Left/Right/Center]
- Duration: [Seconds]
- Style: [Glass effect details]
- Action button: [Optional]
- Close button: [Optional]
- Icon: [Position, size]

**Loading Indicators**
- Spinner: [Style, size, color]
- Progress bar: [Style]
- Skeleton screens: [Style matching glass theme]

**Empty States**
- Illustration: [Style]
- Message: [Typography]
- CTA: [Button to encourage action]
```

#### 4.5 Feature-Specific Organisms
```markdown
### Feature Components

**Shopping Cart** (for shoe shop)
- Layout: [Side panel/Full page]
- Item card: [Image + Details + Quantity + Remove]
- Summary section: [Subtotal, Shipping, Total]
- Checkout CTA: [Style]
- Empty state: [Design]

**Product Detail View**
- Image gallery: [Carousel/Grid]
- Size selector: [Button group/Dropdown]
- Color selector: [Swatches]
- Add to cart: [Button prominence]
- Description: [Expandable/Always visible]
```

**Deliverable:** Complete organism component library

---

### Step 5: Define Templates & Layouts (MANDATORY)

**Objective:** Create page-level structures and responsive layouts

#### 5.1 Layout System
```markdown
### Grid & Layout

**Container Widths:**
- Mobile: 100% - [padding]
- Tablet: [max-width]px
- Desktop: [max-width]px
- Wide: [max-width]px

**Breakpoints:**
- xs: 0px - 599px
- sm: 600px - 959px
- md: 960px - 1279px
- lg: 1280px - 1919px
- xl: 1920px+

**Grid System:**
- Columns: 12-column grid
- Gutter: [Value]px
- Margin: [Value]px
```

#### 5.2 Page Templates
```markdown
### Page Templates

**Homepage Template** (for shoe shop)
- Header: [App bar with navigation]
- Hero Section: [Featured products, banner]
- Category Grid: [Browse by category]
- Featured Products: [Product grid]
- Footer: [Links, social, newsletter]

**Product Listing Page**
- Header: [App bar]
- Filters: [Sidebar/Drawer on mobile]
- Product Grid: [Responsive grid]
- Pagination/Infinite scroll
- Footer

**Product Detail Page**
- Header: [App bar with back button]
- Product Gallery: [Images]
- Product Info: [Title, price, description]
- Options: [Size, color selectors]
- Actions: [Add to cart, wishlist]
- Recommendations: [Related products]
- Footer

**Cart Page**
- Header: [App bar]
- Cart items: [List of products]
- Summary: [Price breakdown]
- Checkout: [CTA]
- Recommendations: [You might also like]

**Checkout Page**
- Progress indicator: [Steps]
- Forms: [Shipping, payment]
- Summary: [Order summary]
- Submit: [Place order button]
```

#### 5.3 Responsive Behavior
```markdown
### Responsive Design Rules

**Mobile (< 600px):**
- Single column layout
- Bottom navigation
- Hamburger menu
- Full-width cards
- Stacked forms

**Tablet (600px - 960px):**
- 2-column grid for products
- Collapsible sidebar for filters
- Hybrid navigation

**Desktop (> 960px):**
- 3-4 column grid
- Persistent sidebar
- Top navigation
- Hover states active
- Larger glass effect areas
```

**Deliverable:** Complete page template specifications

---

### Step 6: Generate Animation & Interaction Patterns (MANDATORY - WOW FACTOR FOCUS)

**Objective:** Define motion design and interaction behaviors that create WOW and attract users

**⚠️ CRITICAL: Focus on creating impressive animations, backgrounds, and effects that match user requirements**

#### 6.1 Animation System (WOW FACTOR)

```markdown
### Animation Principles (Creating WOW)

**Timing Functions:**
- Ease-out: [cubic-bezier values] - Elements entering (creates smooth, natural feel)
- Ease-in: [cubic-bezier values] - Elements exiting
- Ease-in-out: [cubic-bezier values] - Elements moving
- Bounce: [cubic-bezier values] - Playful, attention-grabbing animations
- Elastic: [cubic-bezier values] - Dynamic, energetic animations
- Linear: - Progress indicators

**Duration Scale:**
- Instant: 0ms - State changes
- Fast: 100ms - Micro-interactions
- Medium: 200ms - Component transitions
- Slow: 300ms - Page transitions
- Slower: 500ms - Complex animations
- WOW Entrance: 400-600ms - First impression animations (longer for impact)

**Animation Types (WOW Factor Focus):**

1. **🎨 Background Animations (WOW Factor)**
   - Animated Gradients: [Flowing color transitions, duration, easing, visual impact]
   - Particle Systems: [Floating particles, interactive particles, density, movement speed]
   - Parallax Layers: [Multiple layers, scroll speeds, depth illusion]
   - Video Backgrounds: [Looping videos, overlay effects, performance optimization]
   - Geometric Patterns: [Animated shapes, rotation, scale, movement]
   - Mesh Gradients: [Flowing color meshes, transformation, visual impact]
   - Noise Textures: [Animated grain, texture overlay, subtle movement]

2. **🎬 Entrance Animations (WOW First Impression)**
   - Fade-in with Scale: [Duration, easing, scale amount, creates depth]
   - Slide-in with Bounce: [Direction, bounce intensity, duration, playful impact]
   - Reveal Effects: [Progressive reveal, direction, duration, creates anticipation]
   - Stagger Animations: [Sequence timing, delay between elements, creates flow]
   - 3D Transforms: [Rotate, perspective, depth, creates dimensional impact]
   - Morphing Shapes: [Shape transformation, duration, creates visual interest]

3. **✨ Glass Effect Animations**
   - Blur intensity transition: [Duration, easing, blur amount]
   - Opacity fade: [Duration, easing, transparency levels]
   - Border glow: [Duration, easing, glow intensity, color]
   - Depth animation: [Shadow changes, elevation, creates 3D feel]

4. **🎯 Button Interactions (Impressive Feedback)**
   - Hover: [Scale/Color change, shadow increase, glow effect, duration, creates anticipation]
   - Active: [Scale/Shadow change, press feedback, duration]
   - Ripple effect: [Duration, size, color, expansion speed, creates tactile feel]
   - Loading state: [Spinner, progress, creative loader matching theme]

5. **🃏 Card Animations (Engaging Interactions)**
   - Hover: [Elevation change, scale, shadow increase, duration, creates depth]
   - Click: [Scale feedback, bounce, duration, creates tactile response]
   - Loading: [Skeleton shimmer, pulse effect, creates anticipation]
   - Flip effect: [3D rotation, perspective, creates interactive feel]

6. **📄 Page Transitions (Smooth, Impressive)**
   - Enter: [Fade + slide, scale, duration, easing, creates smooth flow]
   - Exit: [Fade, slide out, duration, easing]
   - Custom transitions: [Theme-specific transitions matching requirements]

7. **🎭 Modal Animations (Attention-Grabbing)**
   - Backdrop: [Fade in, blur effect, duration, creates focus]
   - Content: [Scale + fade, slide in, bounce, duration, creates presence]
   - Exit: [Scale down + fade, slide out, duration]

8. **🎪 Scroll Animations (Dynamic Engagement)**
   - Parallax: [Scroll speed ratio, depth layers, creates immersive feel]
   - Reveal on scroll: [Fade in, slide up, scale, creates progressive disclosure]
   - Sticky effects: [Stick and transform, creates interactive feel]
   - Progress indicators: [Show scroll progress, animated, creates feedback]
```

#### 6.2 Interaction Patterns
```markdown
### Interaction Behaviors

**Hover States:**
- Buttons: [Color shift + shadow increase]
- Cards: [Elevation + scale]
- Links: [Underline + color]

**Focus States:**
- Outline: [Color, width, offset]
- Glass glow: [Inner shadow]

**Active States:**
- Buttons: [Slight scale down + shadow decrease]
- Toggles: [Smooth transition]

**Loading States:**
- Buttons: [Spinner + disabled style]
- Content: [Skeleton + blur]

**Error States:**
- Input: [Red border + shake animation]
- Form: [Error message fade-in]

**Success States:**
- Checkmark animation: [Duration, easing]
- Toast appearance: [Slide + fade]
```

#### 6.3 Micro-interactions
```markdown
### Micro-interactions

**Add to Cart:**
1. Button press animation
2. Item flies to cart icon
3. Cart badge increments
4. Success toast appears

**Like/Wishlist:**
1. Heart icon fills with color
2. Scale up + down animation
3. Particle effect (optional)

**Filter Selection:**
1. Chip state changes
2. Grid updates with fade
3. Count badge updates

**Image Gallery:**
1. Smooth carousel transitions
2. Zoom on click
3. Thumbnail highlights
```

**Deliverable:** Complete animation and interaction guide

---

## Final Deliverable: Complete Design System Specification

After completing all 6 steps, generate:

```markdown
# [Project Name] Design System Specification

**Version:** 1.0
**Date:** [Date]
**Style:** [Design style]
**Platforms:** [Target platforms]

---

## 1. Design Tokens

### Colors
[Complete color palette from Step 2.2]

### Typography
[Complete typography system from Step 2.1]

### Spacing
[Complete spacing system from Step 2.3]

### Borders & Radius
[Complete border system from Step 2.4]

### Shadows
[Complete shadow system from Step 2.5]

---

## 2. Components Library

### Atomic Components
[Reference to Step 2]

### Molecular Components
[Complete specifications from Step 3]

### Organism Components
[Complete specifications from Step 4]

---

## 3. Page Templates
[Complete templates from Step 5]

---

## 4. Motion Design
[Complete animation guide from Step 6]

---

## 5. Design Guidelines

### Accessibility
- WCAG compliance level: [A/AA/AAA]
- Color contrast ratios: [Values]
- Focus indicators: [Specifications]
- Screen reader support: [Guidelines]

### Responsive Design
- Breakpoints: [Values]
- Mobile-first approach: [Yes/No]
- Touch targets: [Minimum size]

### Glass Morphism Guidelines
[Style-specific best practices]
- When to use glass effects: [Guidelines]
- Blur intensity rules: [Values]
- Transparency ranges: [Values]
- Layering principles: [Guidelines]

---

## 6. Implementation Notes

### CSS Framework
- Recommended: [Framework name]
- Custom properties setup: [Code examples]

### Component Library
- Recommended: [Library name]
- Customization approach: [Guidelines]

### Assets
- Icon set: [Name/Source]
- Image formats: [Formats]
- Optimization: [Guidelines]

---

## 7. Examples & Use Cases

### Example Screens
[Screenshots or wireframes for key pages]

### Component Combinations
[Examples of how components work together]

### Do's and Don'ts
[Visual examples of correct and incorrect usage]

---

## 8. Maintenance & Evolution

### Version Control
[How to track design system changes]

### Contribution Guidelines
[How to propose new components]

### Update Schedule
[Review and update cadence]
```

---

## Best Practices

### Do:
✅ Start with user requirements and platform
✅ Define atomic elements first
✅ Build components progressively (atoms → molecules → organisms)
✅ Consider accessibility from the beginning
✅ Provide specific values (don't use placeholders)
✅ Adapt guidelines to the stated design style
✅ Include responsive specifications
✅ Define all interaction states
✅ Create consistent naming conventions

### Don't:
❌ Skip atomic definitions
❌ Ignore platform-specific patterns
❌ Forget about edge cases (loading, error, empty states)
❌ Use generic descriptions without specific values
❌ Ignore accessibility requirements
❌ Forget about responsive behavior
❌ Skip animation and interaction details

---

## Usage Instructions

**To use this guide:**

1. **Receive user input** (e.g., "I want a shoe shop app with glass style")
2. **Execute Step 1:** Analyze and extract requirements
3. **Execute Step 2:** Define all atomic components with specific values
4. **Execute Step 3:** Define molecular components
5. **Execute Step 4:** Define organism components
6. **Execute Step 5:** Create page templates
7. **Execute Step 6:** Define animations and interactions
8. **Generate final deliverable:** Complete design system document

**Output Format:**
Single comprehensive markdown document with all specifications, ready to be used by designers and developers.

---

## FINAL REMINDER

**When you receive a UI/UX design request, you MUST:**

✅ **Step 0:** Research and analyze 3-5 top-tier similar products on the internet FIRST
✅ **Step 0:** Extract modern design patterns and best practices from research
✅ **Step 0:** Determine design style (use specified style OR default to MODERN if not specified)
✅ Analyze user requirements completely (informed by research)
✅ Define EVERY component from atoms to organisms
✅ Provide SPECIFIC values (not placeholders)
✅ Include ALL states (default, hover, active, disabled, error, loading)
✅ Specify responsive behavior
✅ Define animation and interactions
✅ Create a complete, actionable design system
✅ Incorporate insights from competitive research

**DO NOT:**
❌ Skip the competitive research step (Step 0)
❌ Skip any component category
❌ Provide vague descriptions
❌ Forget edge cases
❌ Ignore accessibility
❌ Leave placeholders without values
❌ Use outdated design patterns (always default to modern if style not specified)

**Design Style Rules:**
- **If user specifies a style:** Use that exact style (e.g., glass morphism, neumorphism, material design, brutalist)
- **If user does NOT specify a style:** Default to **MODERN** design with contemporary patterns, clean aesthetics, and current best practices

**🎨 WOW Factor Requirements (MANDATORY):**
- **Focus on Animations:** Create impressive, smooth animations that attract users and create memorable experiences
- **Focus on Backgrounds:** Design WOW backgrounds that match user requirements and create immediate visual impact
- **Focus on Effects:** Implement special effects (glass morphism, particles, parallax, gradients, etc.) that create WOW
- **Match Requirements:** Backgrounds and animations must correspond exactly to user's product/theme requirements
- **Visual Attraction:** Every design must have elements that immediately catch attention and create memorable first impression
- **Performance:** Ensure smooth 60fps animations (optimize for performance, use GPU acceleration)
- **Balance:** Balance WOW factor with usability (don't sacrifice usability for effects)

**Remember:** The goal is to create a complete, specific, and actionable design system that developers can implement immediately without guessing any details. Always research top-tier products first to ensure the design is competitive and modern. **MOST IMPORTANTLY: Focus on creating WOW animations, backgrounds, and effects that attract users and match their requirements. Make them say "WOW!"**

---

## CRITICAL: Comprehensive Detail Requirements

**⚠️ ALL UI/UX DESIGN SPECIFICATIONS MUST BE DETAILED AND COMPREHENSIVE - NO SIMPLIFICATIONS**

When creating UI/UX design systems, you MUST:

1. **Expand Every Component:** Every component (atomic, molecular, organism) must have comprehensive specifications with specific values, not placeholders
2. **Document All States:** All component states (default, hover, active, disabled, error, loading, empty) must be fully specified
3. **Specify All Interactions:** All user interactions must be documented with detailed animation specifications
4. **Complete Responsive Design:** All breakpoints and responsive behaviors must be fully specified
5. **Comprehensive Animation Specs:** All animations must have timing, easing, duration, and performance considerations
6. **Detailed WOW Elements:** All WOW backgrounds, animations, and effects must be fully specified with technical details
7. **Complete Accessibility:** All accessibility features must be documented (ARIA labels, keyboard navigation, screen reader support)
8. **Additional Design Elements:** Always consider and document additional design elements/sections/parts/UI that could match project requirements

**DO NOT:**
- ❌ Simplify or summarize design specifications
- ❌ Use placeholders without specific values
- ❌ Skip component states or variations
- ❌ Ignore responsive design details
- ❌ Overlook additional design elements that could enhance the UI/UX
- ❌ Provide vague descriptions

**DO:**
- ✅ Provide comprehensive, detailed design specifications
- ✅ Expand every component with full details
- ✅ Include all states, variations, and edge cases
- ✅ Document additional design elements/sections/parts/UI that match requirements
- ✅ Provide specific values for all properties (colors, sizes, spacing, timing, etc.)
- ✅ Create thorough, enterprise-grade design systems

**The design system should be so comprehensive that a developer can implement it without asking additional questions.**
