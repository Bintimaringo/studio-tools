# POETRY IN PIGMENT — Field Generation Guide

Companion to the build brief. This covers **Stage 1**: generating the pigment field images that drop into the compositor. The tool composites; it does not generate. This guide is where the colour actually comes from.

---

## How the pool works

Each pigment has a field pool containing **three families**:

- **BLOOM** (type A) — fluid, atmospheric pigment diffusing in liquid. Romantic. The Lilian register.
- **SPECIMEN** (type B) — the raw pigment as a conservation object on a dark ground, single dramatic light. Forensic. The Maabara register (same grammar as the Fundi vitrine plates: honey, propolis, jacaranda).
- **EDITORIAL / UNCANNY** (type C) — the pigment in an oblique, surreal relationship with an object, a body, a planet, a chemical state. Evocative, not documentary. Carries the colour's *charge* rather than its history. See **EDITORIAL / UNCANNY** below for the full discipline — it runs on different guardrails than BLOOM/SPECIMEN and is the highest-risk family to misgenerate.

Generate **6–8 variants of each family per pigment** (8–10 for EDITORIAL, cull hard) — run the same prompt repeatedly (or vary the seed) and keep the strongest. That variant pool is what the tool's Field reshuffle cycles through.

### Which layouts pull from which family
- **BLOOM →** Monolith, Soft-romance, Disc, Cascade, Vertical (the field is the emotional event)
- **SPECIMEN →** Assay, Anchor, The Edge, Formula-dominant, Centred-severe (the field is evidence beside the text)
- **EDITORIAL / UNCANNY →** tagged per direction at the point of use:
  - *(severe/object)* → The Edge, Centred-severe, Monolith, Assay
  - *(romantic/body)* → Soft-romance, Monolith, Disc
  - *(uncanny/in-your-face)* → editorial layouts, the loud severe layouts
- The tool keeps **one flat pool per pigment** and the Field control cycles all of it — there is no `preferredFamily` enforcement in the code (confirmed: the family map is a discipline you apply by hand when culling/labelling, not something the tool reads). Overriding the map is part of the play. Which *falloff* you generated matters as much as which family: see **Tonal targets** below.

---

## Technical constraints (apply to EVERY prompt)

These make the image *composite well*, not just look good alone. Bake them into every generation:

1. **Portrait, 3:4.** All canvases are portrait (3:4 / A4 / 4:5). Generate 3:4 so the field fills the sheet without awkward crop.
2. **Type-safe tone.** The single most important craft note, and it is not one rule. The tool composites the field three different ways, so the falloff you want depends on the destination layout. Pick the right falloff clause from **Tonal targets** below and slot it into the pigment prompt. Generating every field with near-black margins (the old universal rule) is correct for full-bleed layouts, wasted on clipped ones, and actively wrong under the layouts that lighten the field.
3. **Chemically true.** The bloom or specimen must behave the way the real compound behaves — not a generic colour. The per-pigment notes below encode this. Truth to the substance is the whole receipt thesis; a generic blue blob fails it.
4. **No text, no objects, no hands.** Pure field only. The tool adds all type. No watermarks, no captions, no UI, no vessels unless the specimen prompt calls for one.
5. **High resolution**, even light gradient, no harsh digital banding in the dark falloff (generation sometimes bands — regenerate if the darks posterise).

---

## Tonal targets — match the falloff to where the field lands

The tool composites the field three ways, so "leave dark space for text" is really three instructions. The colour behaviour in each pigment prompt stays the same. What changes is the **falloff clause** you slot in, chosen by destination.

**GROUND** — full-bleed, light type sits directly on the field, and the tool darkens it further (scrims, black overlays).
→ Anchor, Monolith, The Cascade, Formula-dominant.
Clause: *"…concentrated in the upper-centre, falling to deep near-black at all four edges, a quiet dark zone in the lower third for text."*
Caution: the composite darkens again, so keep the colour rich. A field already near-black at the margins can go muddy under a 50–60% black scrim.

**OBJECT** — the field is clipped to a disc or a swatch, so its rectangular margins are cropped away. The dark type-zone comes from the poster, not the field.
→ The Disc, The Edge, Corner, Centred-severe, Assay.
Clause: *"…colour and subject filling the frame, centred, evenly saturated, no forced dark corners."*
Note: on the black-ground layouts (The Disc, The Edge) a soft dark vignette is a bonus, reading as a glowing orb. On the pale-ground layouts (Corner, Centred-severe, Assay) keep the colour out to the crop or it reads as a dark blob on white.

**LIFT** — full-bleed on a pale sheet, and the tool lightens the lower region toward white.
→ Soft-romance, Vertical.
Clause: *"…colour spread broadly and luminous across the frame, soft gentle falloff, no heavy near-black margins."*
Caution: this is the one case where the dark rule inverts. A dark-margined field turns grey and muddy under the white lift. Give it light to work with.

---

## EDITORIAL / UNCANNY — the third field family

BLOOM and SPECIMEN are literal: they show the pigment as itself. EDITORIAL / UNCANNY is oblique — the pigment appears in an unexpected relationship (with an object, a body, a planet, a chemical state) that is evocative rather than documentary. **The image is a poem, not evidence.**

Why this exists: the series runs on Option C (romantic surface, severe cost). BLOOM/SPECIMEN carry the surface and the forensic. This family carries the charge — the strangeness and tension that makes a colour feel loaded. Crucially, **the cost is felt, not captioned.** Ultramarine smoke leaving a body carries violence without being a literal injury. White-as-deathmask carries mortality without being a corpse. The receipt is in the image, oblique.

**Two hard guardrails, non-negotiable, same discipline as the rest of the tool:**

1. **Evocative, never literal/documentary.** The point is the unexpected relationship, not an illustration of the pigment's history. If a prompt starts explaining the cost, it has failed. Smoke = elegiac; a nosebleed = failed. A wound-that-is-a-flower = charged; an actual injury = failed.
2. **Bearing, not spectacle.** Where a body appears, it must read as bearing/wearing the colour, never as damaged for shock. The test: does it read as the body in relationship with the colour, or as gore/distress played for edge? The second is spectacle — exactly the surface-trafficking the studio refuses. Vermilion's romantic/body and White's romantic/body sit closest to this line — tightest cull for both.

**Body-family discipline:** where the diasporic body is the subject, it must be specific and intentional, not generic editorial stock — this is THE BODY movement, most native to the studio, heritage-loaded, same discipline as the kanga and the endonym. **Worth an studio review before any body field goes to published work.**

Technical constraints are the same as every field in this guide (portrait 3:4, type-safe dark negative space, no text/watermarks/UI, high resolution, smooth dark falloff) — generate 8–10 per direction and cull hard to the strongest with the cleanest type-zones.

A single pigment can hold an object-field AND a body-field in its pool; the layout pulls the right temperature (e.g. ultramarine's marble/Earth object-field pairs with Centred-severe).

---

## ULTRAMARINE

True behaviour: deep lapis blue from a sulphur radical trapped in a crystal lattice. The blue is, literally, a flaw. Pools richly; the finest grade approaches violet-blue. Costlier than gold by weight.

**BLOOM prompt** — baseline target: GROUND (Monolith, The Cascade). For The Disc swap in the OBJECT clause; for Soft-romance and Vertical swap in the LIFT clause:
> Deep ultramarine blue ink diffusing slowly in clear water, lapis-lazuli blue concentrated in the upper-centre and blooming outward into tendrils, falling to deep near-black navy at all four edges, soft organic diffusion, a faint violet undertone at the brightest core, photographed against black, abstract fluid pigment study, portrait 3:4, generous dark negative space in the lower third for text, no text, no objects, high resolution, smooth tonal falloff.

**SPECIMEN prompt** — baseline target: GROUND / swatch (Anchor, Formula-dominant, Assay). For The Edge and Centred-severe, centre the subject and use the OBJECT clause:
> A single raw chunk of lapis lazuli and a small mound of ground ultramarine pigment, deep blue with fine gold pyrite flecks in the stone, resting on a matte black surface, single dramatic raking light from upper left, conservation specimen photography, dark ground falling to black, museum plate aesthetic, portrait 3:4, the object in the upper two-thirds leaving dark space below, no text, no hands, high resolution.

**EDITORIAL prompts** — beyond-the-sea, cosmic, gold-costly:

*(severe/object)* → The Edge, Centred-severe, Monolith, Assay:
> A perfect sphere of deep ultramarine blue, reading as a planet — Earth seen from the dark side of space, lit along one edge by a distant unseen sun, suspended alone on pure black. Cosmic, still, vast, the curvature precise and planetary, no stars, no atmosphere haze beyond a thin limb of light, portrait 3:4, the sphere held in the upper two-thirds with deep black falling away below for text, no text, no UI, high resolution, smooth dark falloff.

*(romantic/body)* → Soft-romance, Monolith, Disc:
> A profile of a face, lips just parted, exhaling a slow drift of deep ultramarine smoke into near-black space — the body releasing something too vast for it to hold. Elegiac, abstracted, the smoke catching a single soft light as it dissolves upward, skin barely lit, the rest of the frame falling to black. Smoke only, never liquid or paint. Specific, intentional diasporic features, not generic stock. Portrait 3:4, dark negative space surrounding the figure for text, no text, no UI, high resolution, smooth dark falloff.

*(uncanny)* → editorial layouts, the loud severe layouts:
> A single drop of deep ultramarine ink falling into clear liquid, caught at the exact instant of impact mid-bloom, suspended and frozen like a held heartbeat, saturated violet-blue core radiating into delicate tendrils against a dark surround. High-speed macro photography aesthetic, portrait 3:4, the drop held centre-frame with black falling away at the edges for text, no text, no UI, high resolution, smooth dark falloff.

---

## INDIAN YELLOW

True behaviour: luminous deep yellow to amber, bleeding to crimson and near-black at its densest. Originally euxanthic acid from the urine of cows fed only mango leaves. Glows; the colour of light, made from a starved body.

**BLOOM prompt** — baseline target: GROUND (Monolith, The Cascade). For The Disc swap in the OBJECT clause; for Soft-romance and Vertical swap in the LIFT clause:
> Luminous Indian yellow pigment diffusing in water, glowing amber-gold at the centre bleeding outward through deep orange into crimson and near-black at the edges, warm radiant core like backlit honey, soft organic diffusion against black, abstract fluid pigment study, portrait 3:4, dark crimson-to-black negative space at the margins for text, no text, no objects, high resolution, smooth tonal falloff.

**SPECIMEN prompt** — baseline target: GROUND / swatch (Anchor, Formula-dominant, Assay). For The Edge and Centred-severe, centre the subject and use the OBJECT clause:
> A small mound of deep amber-yellow Indian yellow pigment in raw lumps, glowing warm ochre with darker crimson-brown edges, on a matte black surface, single dramatic raking light from upper left, conservation specimen photography, dark ground falling to black, museum plate aesthetic, portrait 3:4, object in the upper two-thirds leaving dark space below, no text, no hands, high resolution.

**EDITORIAL prompts** — glow, the body-as-factory, the animal cost:

*(severe/object)* → The Edge, Centred-severe, Monolith, Assay:
> A glass or ceramic vessel filled with luminous Indian Yellow, glowing from within like something deliberately kept alive, set alone on pure black — the colour read as captive light rather than paint. Warm amber-gold glow bleeding to crimson at its core, the vessel's silhouette simple and unornamented. Portrait 3:4, the vessel held in the upper two-thirds with black falling away below for text, no text, no UI, high resolution, smooth dark falloff.

*(romantic/body)* → Soft-romance, Monolith, Disc:
> Indian Yellow pigment pooled warm and luminous in the hollow of a collarbone, or cupped in an open palm, as if the body itself is producing the colour — the "made from a body" charge held obliquely, never as illness or wound. Skin specific and intentional, warm-lit, the pigment glowing amber-gold against it, rest of frame falling to near-black. Portrait 3:4, dark negative space surrounding the figure for text, no text, no UI, high resolution, smooth dark falloff.

*(uncanny)* → editorial layouts, the loud severe layouts:
> A burst of Indian Yellow pigment powder caught hanging in mid-air, backlit so each particle glows amber-gold, frozen mid-explosion — glory and violence held in one frame, beautiful and faintly dangerous at once. Dense cloud bleeding to crimson-black at its edges against pure black. Portrait 3:4, the burst centred with black falling away at the margins for text, no text, no UI, high resolution, smooth dark falloff.

---

## INDIGO

True behaviour: dense vegetal blue, deeper and more matte than ultramarine — the second blue, whose cost was paid in skin not gold. Diffuses denser, less crystalline; a drowning, clouding blue rather than a sparkling one. (Never conflate with ultramarine: different blue, different cost.)

**BLOOM prompt** — baseline target: GROUND (Monolith, The Cascade). For The Disc swap in the OBJECT clause; for Soft-romance and Vertical swap in the LIFT clause:
> Dense indigo dye clouding through water, deep matte vegetal blue-black, heavy billowing diffusion sinking and clouding rather than sparkling, concentrated in the centre and dropping to total black at the edges, muted and oceanic, abstract fluid dye study against black, portrait 3:4, deep black negative space at the margins for text, no text, no objects, high resolution, smooth tonal falloff.

**SPECIMEN prompt** — baseline target: GROUND / swatch (Anchor, Formula-dominant, Assay). For The Edge and Centred-severe, centre the subject and use the OBJECT clause:
> A broken cake of dried indigo dye, deep blue-black with a faint coppery sheen on the fracture surfaces, and a scatter of indigo powder, on a matte black surface, single dramatic raking light from upper left, conservation specimen photography, dark ground falling to black, museum plate aesthetic, portrait 3:4, object in the upper two-thirds leaving dark space below, no text, no hands, high resolution.

**EDITORIAL prompts** — the second blue, drowning, cost paid in skin:

*(severe/object)* → The Edge, Centred-severe, Monolith, Assay:
> A monolith or slab of pure indigo, so dark and matte it reads almost as void — a cut of night standing upright on black, its edges barely distinguishable from the ground it sits on, one faint rim of light defining its form. Cold, still, architectural. Portrait 3:4, the slab held in the upper two-thirds with black falling away below for text, no text, no UI, high resolution, smooth dark falloff. Must read denser/matte than ultramarine — if it looks crystalline or sparkling, regenerate.

*(romantic/body)* → Soft-romance, Monolith, Disc:
> A hand or shoulder, skin specific and intentional, half-submerged into dense indigo darkness that reads as both water and disappearance — the body meeting a blue that is swallowing it, gently, without struggle. The drowning felt, not staged as a dye-house document. Matte, oceanic, never sparkling. Portrait 3:4, dark negative space surrounding the figure for text, no text, no UI, high resolution, smooth dark falloff.

*(uncanny)* → editorial layouts, the loud severe layouts:
> Indigo dye clouding through water in a heavy, billowing fall — sinking rather than rising, dense and oceanic, matte and clouded rather than crystalline. Concentrated mass dropping through clear water into total black below. Portrait 3:4, the cloud held centre-frame with black falling away at the margins for text, no text, no UI, high resolution, smooth dark falloff. Discipline: if this reads crystalline or sparkling, it has drifted into ultramarine's register — regenerate. The two blues are never interchangeable.

---

## POTASSIUM PERMANGANATE

True behaviour: a genuine gift for this series — dark purple-black crystals that dissolve into vivid magenta-purple, and as it reacts/dilutes it runs through pink to a startling green-teal. Real chemistry doing the series' work: one substance, many colours, a transformation. (Held for its own future treatment, but generate fields now.)

**BLOOM prompt** — baseline target: GROUND (Monolith, The Cascade). For The Disc swap in the OBJECT clause; for Soft-romance and Vertical swap in the LIFT clause:
> Potassium permanganate crystals dissolving in water, vivid magenta-purple plumes streaming from dark crystalline points, the colour shifting through deep purple to magenta to a startling green-teal at the dissolving edges, dramatic chemical diffusion against black, abstract fluid study, portrait 3:4, dark negative space at the margins for text, no text, no objects, high resolution, smooth tonal falloff.

**SPECIMEN prompt** — baseline target: GROUND / swatch (Anchor, Formula-dominant, Assay). For The Edge and Centred-severe, centre the subject and use the OBJECT clause:
> A small heap of potassium permanganate crystals, dark purple-black with a metallic violet sheen, a few crystals beginning to dissolve into magenta streaks on the surface beneath, on a matte black surface, single dramatic raking light from upper left, conservation specimen photography, dark ground falling to black, museum plate aesthetic, portrait 3:4, object in the upper two-thirds leaving dark space below, no text, no hands, high resolution.

---

## VERMILION — mercury, heat, the maker poisoned

**Not yet wired into the tool's `PIGMENTS` array** (no text/formula authored). EDITORIAL fields can be generated now; BLOOM/SPECIMEN prompts to follow when the pigment is built.

True behaviour: brilliant red-orange from mercury sulphide, ground by hand for centuries by workers who absorbed the mercury through skin and lungs. Heat and alarm in a single saturated red — beauty that poisoned its own maker.

**EDITORIAL prompts:**

*(severe/object)* → The Edge, Centred-severe, Monolith, Assay:
> A struck match-head or single glowing ember in pure vermilion red-orange, suspended against black, heat implied through saturation and a faint corona of light rather than visible flame. Danger held as a still, alarming object. Portrait 3:4, the ember held in the upper two-thirds with black falling away below for text, no text, no UI, high resolution, smooth dark falloff.

*(romantic/body) — TIGHT CULL, studio review required before publication* → Soft-romance, Monolith, Disc:
> A bloom of vermilion red opening across skin like a flower unfurling — petalled, deliberate, the saturated red spreading in a botanical pattern rather than a wound shape. Danger held as beauty, never as injury. Skin specific and intentional, softly lit, rest of frame falling to near-black. Portrait 3:4, dark negative space surrounding the figure for text, no text, no UI, high resolution, smooth dark falloff.
> Must read unmistakably as flower/bloom; if it reads as gore or literal blood, discard and regenerate with a more botanical, less wound-shaped bloom.

*(uncanny)* → editorial layouts, the loud severe layouts:
> Vermilion red rendered as molten metal or liquid mercury, beading and catching hard specular light on a dark surface — too alive, too hot, too mobile to read as a fixed colour. Portrait 3:4, the beaded pool held centre-frame with black falling away at the margins for text, no text, no UI, high resolution, smooth dark falloff.

---

## MAGENTA — synthetic, coal-tar, the lab-born Ghost

**Not yet wired into the tool's `PIGMENTS` array.** EDITORIAL fields can be generated now; BLOOM/SPECIMEN prompts to follow when the pigment is built.

True behaviour: the first synthetic dye, coal-tar derived, impossibly saturated in a way no historical pigment could achieve — an engineered colour, the lab-born ghost of the series.

**EDITORIAL prompts:**

*(severe/object)* → The Edge, Centred-severe, Monolith, Assay:
> A perfect sphere or soap-film bubble in impossibly saturated magenta, its surface announcing its own artificiality through hard, even, synthetic colour with no organic variation — engineered, not grown. Suspended alone on pure black. Portrait 3:4, the sphere held in the upper two-thirds with black falling away below for text, no text, no UI, high resolution, smooth dark falloff.

*(romantic/body — inverted)* → Soft-romance, Monolith, Disc:
> A magenta stain across skin that reads as deliberately engineered — too clean, too even, faintly plastic, a dye that visibly does not belong on a body. The inversion of the series' other body-fields: not ancestral, not bearing, but a synthetic intrusion. Skin specific and intentional, the stain hard-edged rather than diffused. Portrait 3:4, dark negative space surrounding the figure for text, no text, no UI, high resolution, smooth dark falloff.

*(uncanny)* → editorial layouts, the loud severe layouts:
> Magenta rendered as oil-slick iridescence, or a chemical reaction caught mid-bloom in clear liquid — the birth of the lab-made colour visualised, slick, strange, shifting at its edges toward violet and cyan. Portrait 3:4, the bloom held centre-frame with black falling away at the margins for text, no text, no UI, high resolution, smooth dark falloff.

---

## WHITE (lead white) — the killing cosmetic, beauty as poison

**Not yet wired into the tool's `PIGMENTS` array.** EDITORIAL fields can be generated now; BLOOM/SPECIMEN prompts to follow when the pigment is built.

True behaviour: basic lead carbonate, the brilliant cool white that built five centuries of portraiture and slowly poisoned the painters and the women who wore it as cosmetic. Beauty that kills by accumulation, not impact.

**EDITORIAL prompts:**

*(severe/object)* → The Edge, Centred-severe, Monolith, Assay:
> A fragment reading as carved marble or stone, brilliant cool lead white, its surface suggesting a living form that has turned to monument. Cold, still, statuary, a single raking light defining its planes against black. Portrait 3:4, the fragment held in the upper two-thirds with black falling away below for text, no text, no UI, high resolution, smooth dark falloff.

*(romantic/body) — TIGHT CULL, the studio's sleeper image, mandatory studio review before publication* → Soft-romance, Monolith, Disc:
> A face or shoulder dusted in matte lead white to the point of statuary perfection — life arrested into object, too still, too perfect, reading as a beautiful death-mask rather than a corpse. Features specific and intentional beneath the white, softly lit, rest of frame falling to near-black. Portrait 3:4, dark negative space surrounding the figure for text, no text, no UI, high resolution, smooth dark falloff.
> Must read as beautiful and statuary; if it reads as a corpse or literal death, discard and regenerate with a softer, more arrested stillness. Mortality oblique, not literal — handle with the most care of any field in this guide.

*(uncanny)* → editorial layouts, the loud severe layouts:
> Fine white powder settling and falling like ash or quiet snow over a dark surface, beautiful, restrained, faintly funereal — no figure, no violence, just the slow fall. Portrait 3:4, the fall held centre-frame with deep black surrounding it for text, no text, no UI, high resolution, smooth dark falloff.

---

## STIL DE GRAIN — fugitive, fading, the colour that betrays

**Not yet wired into the tool's `PIGMENTS` array.** EDITORIAL fields can be generated now; BLOOM/SPECIMEN prompts to follow when the pigment is built.

True behaviour: a fugitive lake pigment from unripe buckthorn berries, brilliant yellow that fades and yellows further with light exposure — the colour that betrays its own permanence, here today and thinning tomorrow.

**EDITORIAL prompts:**

*(severe/object)* → The Edge, Centred-severe, Monolith, Assay:
> A surface or small object in buckthorn yellow caught mid-disappearance, the colour visibly thinning and evaporating at its edges as if fading in real time, against deep black. Portrait 3:4, the object held in the upper two-thirds with black falling away below for text, no text, no UI, high resolution, smooth dark falloff.

*(romantic/body)* → Soft-romance, Monolith, Disc:
> A stain of buckthorn yellow on skin, half-lifted and dissolving, caught in the act of leaving — a mark abandoning the body rather than arriving on it. Skin specific and intentional, softly lit, the stain's edges visibly thinning. Portrait 3:4, dark negative space surrounding the figure for text, no text, no UI, high resolution, smooth dark falloff.

*(uncanny)* → editorial layouts, the loud severe layouts:
> Buckthorn-yellow light diffusing through dark space and thinning to nothing, a colour caught mid-vanish, fading rather than blooming. Portrait 3:4, the fading light held centre-frame with black surrounding it for text, no text, no UI, high resolution, smooth dark falloff.

---

## Workflow notes

- **Generate in batches, cull hard.** Run each prompt 8–10 times, keep the 6 with the best dark type-zones and truest colour behaviour. The cull is where quality lives — a field that's beautiful but has no dark quiet zone is unusable, however pretty. For EDITORIAL/UNCANNY, the cull is also a guardrail check, not just a quality check: discard anything that reads literal/documentary instead of evocative, or spectacle instead of bearing.
- **Check against the layout it's for.** A bloom destined for Soft-romance needs a clean lower third; a specimen for Assay needs to sit happily in the right two columns; an editorial field is tagged severe/object, romantic/body, or uncanny at the point of use. Generate with the destination layout in mind.
- **Keep the families labelled** in your file names: `{pigment}_{family}_{direction}_v{n}.png` — e.g. `ultramarine_bloom_lift_v2.png`, `indigo_specimen_object_v4.png`, `ultramarine_editorial_marble_v3.png`, `indigo_editorial_submerged_v2.png` — so the tool's pool stays organised and the right field loads for the right layout.
- **Body-family fields are the highest-risk culls.** Where the diasporic body is the subject (every EDITORIAL romantic/body direction), it must be specific and intentional, not generic editorial stock — THE BODY movement, heritage-loaded, same discipline as the kanga and the endonym. Tightest cull of any field in this guide; run an studio review before any body field goes to published work. Vermilion's and White's romantic/body directions sit closest to the spectacle/literal line — handle with the most care.
- **Permanganate fields can be generated now** even though its text stays placeholder — the fields are reusable when its treatment is written.
- **Vermilion, Magenta, White, and Stil de Grain are not yet wired into the tool's `PIGMENTS` array** — only their EDITORIAL directions are written so far. BLOOM/SPECIMEN prompts and pigment text follow when each is built.
- **Disclosure:** studio format is "Concept AI realised" — no tool credit in published versions.
- **Indigo discipline:** its field must read denser and more matte than ultramarine's. If a generation looks crystalline or sparkling, it's reading as ultramarine — regenerate. The two blues are never interchangeable. The same discipline applies to indigo's EDITORIAL directions.
