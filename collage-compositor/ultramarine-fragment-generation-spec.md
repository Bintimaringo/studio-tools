# COLLAGE COMPOSITOR — Ultramarine Fragment Generation Spec

Companion to Poetry in Pigment's Field Generation Guide, for the **B-side subject family**. The A-side generates *fields* (romantic, full-bleed, colour-led). The B-side generates *subjects* — photographic, monochrome, tonally structured — for the slicer and the compositor. The tools supply the composition; the generated source supplies the tone.

Written per the studio's standing rule: complete spec before any image is sourced. Nothing generates until this document says how.

---

## The one difference that changes every prompt

**Generate in black and white.** The tools' duotone chain maps grayscale onto the locked Ultramarine palette (`#141633` shadows → `#ECEEF6`/`#22379B` highlights). Colour in the source is discarded at `saturate(0)` before mapping, so generating in colour wastes the model's attention and risks muddy tonal structure. Every prompt below asks for monochrome photographic imagery with **full tonal range — true blacks AND paper whites.**

The slicer test (2026-07-07, logged) proved why the highlight half matters: on **Ultramarine Deep** (`#0A0C1C` ground) shadows melt into the sheet by design — an image without genuine highlights simply vanishes. *Every asset in this family must survive a near-black ground.* That is the first cull criterion, not a nice-to-have.

---

## Two asset classes

### Class S — slice subjects (for the slicer)
Full-frame compositions the slicer cuts into windows. Requirements:

- **Portrait 3:4**, subject occupying 50–80% of frame with clear figure-ground
- Full tonal range; highlight areas that read on a dark ground
- The subject must survive fragmentation: strong silhouette or internal structure that stays legible at a ninth-width strip (the strip test, below)
- Atmosphere allowed; text, watermarks, borders never

### Class C — cutout subjects (for the compositor)
Single subjects the white-key ingest lifts to alpha. The key algorithm floods edge-connected near-white pixels (tolerance ~28 RGB), so the ground must *be* the key:

- **Flat, even, seamless near-white studio ground** — no gradient falloff, no vignette, no environment
- **One subject**, fully in frame, ≥8% white margin on all sides
- **Soft contact shadow only** — a cast shadow streaking to the frame edge will key raggedly
- Subject edges must contrast the ground (a white-lit rim on a white ground will erode at key time)
- Aspect free; portrait or square preferred

### Both classes
- **Format:** PNG, no compression artefacts, no banding in the falloff (regenerate if the darks posterise)
- **Dimensions:** minimum 1024px on the long edge; request the largest portrait size the model offers
- **File size:** ≤ 8MB
- **Never:** text, watermarks, UI, frames, colour cast as a *subject* (incidental cast is survivable — `saturate(0)` runs first — but don't invite it)
- **Keeper record:** every culled-in asset gets one line in the build log — filename + a one-line plain description (this is the alt-text provision; it also becomes the caption pool later)

---

## Guardrails — inherited from the A-side, non-negotiable

1. **Evocative, never literal/documentary.** The cost is felt, not captioned. The drape holds an absence; it is not a ghost costume. The hands bear the pigment; they are never injured for effect.
2. **Bearing, not spectacle.** Same test as the field guide: relationship with the colour, never gore or distress played for edge.
3. **Body-family discipline.** The HANDS family is body-family: specific, intentional diasporic hands, never generic editorial stock. Tightest cull in this spec, and an **studio review before any hands asset reaches published work.**

---

## The subject families

Six families from the Creative Director's direction. Naming: `ultramarine_{class}_{family}_v{n}.png` where class is `cut` or `slice` — e.g. `ultramarine_cut_stone_v03.png`, `ultramarine_slice_ridge_v01.png`. Store in `fragments/ultramarine/{family}/`.

### STONE — Class C (primary), Class S (secondary) · 6–8 variants
The lapis itself. The compositor's anchor object; also the substitution head.
> A single fist-sized chunk of raw lapis lazuli, photographed in black and white, deep shadowed facets with bright pyrite glints, strong raking light from the upper left, resting on a flat seamless white studio ground, soft contact shadow only, the full stone in frame with generous white margin on all sides, monochrome documentary object photography, no text, no hands, high resolution, rich tonal range from true black to paper white.

### HANDS — Class C · 8–10 variants, cull hardest · body family
Three directions, one prompt skeleton — *holding the stone* / *cupping ground pigment* / *at the balance*:
> A pair of hands [cupping a small mound of ground pigment powder / holding a rough chunk of lapis lazuli / resting beside a small balance pan], photographed in black and white, strong single side light, skin texture rendered in full tonal range, specific and intentional diasporic hands, not generic stock, isolated on a flat seamless white studio ground, arms cropped cleanly at the wrist by the frame edge, soft contact shadow only, no text, high resolution, true blacks and a paper-white ground.

### SCALE — Class C · 6 variants
The transaction as object. Ounce against ounce.
> A small antique balance scale with one pan sunk lower than the other, photographed in black and white, single dramatic raking light, the full object isolated on a flat seamless white studio ground with generous margin, soft contact shadow only, documentary object photography, no text, no hands, high resolution, full tonal range.

### COIN — Class C · 6 variants
The counterweight. Reads with SCALE or alone as a compositor satellite.
> A single worn coin with heavy relief, edge-lit so the face is half in shadow, photographed in black and white, isolated on a flat seamless white studio ground with generous margin, soft contact shadow only, macro documentary photography, no text, no hands, high resolution, true black shadow and paper-white ground.

### RIDGE / SEA — Class S · 6–8 variants each direction
The crossing. Badakhshan and the water between. These feed the slicer — especially the Deep register, so the highlight requirement is strictest here.
> *(ridge)* A high mountain ridge under hard light, photographed in black and white — bare rock faces in deep shadow against a bright washed-white sky, the ridgeline cutting the frame diagonally, documentary landscape photography with visible grain, portrait 3:4, full tonal range from true black rock to white sky, no text, high resolution.
> *(sea)* Open sea swell photographed in black and white, hard sun breaking on the water so the wave crests burn to paper white against near-black troughs, high contrast documentary marine photography with visible grain, portrait 3:4, horizon high in the frame, no text, high resolution.

### DRAPE — Class S (primary), Class C (secondary) · 8 variants
The robe without the figure — the strongest substitution image this series can own. Guardrail applies hardest here: the cloth holds the *shape of an absence*, evocative, never a costume.
> A heavy fall of drapery in the manner of a Renaissance robe with no figure inside it, the cloth holding the shape of an absence, photographed in black and white, deep folds falling to true black, highlights burning bright along the ridges of the cloth, [suspended against a plain dark ground, portrait 3:4 → Class S / isolated on a flat seamless white studio ground with generous margin → Class C], no text, no figure, high resolution, full tonal range.

---

## The cull — four gates, in order

1. **Tonal gate:** histogram has real highlights. Drop it on Ultramarine Deep in the slicer; if it vanishes, it fails — however beautiful.
2. **Key gate (Class C only):** ingest into the compositor; must key clean at tolerance 24–36 with no more than minor edge erosion. Interior highlights surviving the flood is the design; a subject that keys away with its ground fails.
3. **Strip gate (Class S only):** run through the Weave at 9 cuts; the subject must stay legible sliced.
4. **Guardrail gate:** literal/documentary → out; spectacle → out; generic-stock hands → out. For HANDS, studio review before publication.

## Workflow notes

- Generate in batches per family, cull hard. Parallel runs return out of order — classify by eye, then name.
- Keepers logged in the build log with the one-line description (the alt-text rule).
- Disclosure unchanged from the A-side: studio format is "Concept AI realised" — no tool credit in published versions.
- The ledger-ephemera swap (trade lines replacing the neutral lexicon) is **not** part of this spec — it is authored content and waits on the creative direction pass's line-by-line pass.
