# The Hand Presenting the Work — Build Notes

A compositor for placing work into a photographic plate: a pair of hands holding
a frame, photographed once, with the frame's contents replaced.

The bar the build was held to: **the seam should not be findable at 100%.**

---

## The architecture inverted once, and that was the whole build

The first version composited procedurally — synthetic grain, synthetic shadows,
a drawn frame — and set the result next to a photographed hand. That will always
show the seam, no matter how good the grain is. Procedural texture beside real
texture reads as procedural.

The second version inverts it. **The raw photograph is the base layer, and only
the plaque's pixels change.** Everything else in the frame stays exactly as it
was shot: paper tooth, thumb shadows, sheen, the crease down the spine.

Fixed geometry is the cost. The first version stretched to any ratio; this one
is welded to the photograph it was built from.

---

## Three defects, found before the tool existed

Each was caught in a static mock and fixed there, which is cheaper than finding
them in a running instrument.

**A green line along the boundary.** The base-luminance field switched red↔green
on a segmentation mask misregistered by a few pixels from the real reflectance
edge, minting a bright seam. Fixed with a soft chroma-weighted base field,
`w = g/(r+g)` normalised between the two grounds. Boundary continuity went to
0.980 from 0.969. The residual step is the sheet's real inset relief, kept.

**Magenta thumbs.** Decontaminating every occluder pixel against the red base
over-subtracted red from skin midtones. Fixed by leaving interior pixels
(α≈1) exactly photographic and running decontamination only in the
semi-transparent transition band. The nail's red spill neutralises to a
plausible backlight on non-red content.

**A teal seam through the thumb.** Occluder alpha was being multiplied by the
*feathered* content mask, carving a one-pixel translucent column at the quad
edge. Fixed by clipping the occluder to a hard-edged face polygon outset 4px —
outside the face it redraws plate over plate, which is invisible. Residual
after the fix: mean difference 1.19/255 in the seam band.

---

## The trap: contact shadow reads as translucent fabric

The sleeve is semi-transparent black organza over a light ground. Separating it
means solving per-pixel alpha by projection onto the line between a sampled
background colour and a sampled dense-fabric colour, with a residual check to
reject pixels that don't fit a two-colour blend.

Applied broadly against a single global background sample, that test produced a
solid dark bar spanning the gap between the two hands, on every iteration, until
the cause surfaced: **the contact shadow under the frame's bottom rail is dark
and desaturated enough to fit the fabric-blend line too.** The maths could not
tell a shadow from a sheer sleeve.

Three fixes together:

- Restrict decontamination to a band close to **both** a real ground sample and
  a real dense-fabric sample — the actual fold edge, not anything that merely
  resembles one.
- Exclude a generous buffer around the frame's own edge from ever triggering it.
- A final geometry-aware pass, using the plate's measured frame bounding box,
  that clears the centre-gap shadow strip specifically.

A remnant survives at each wrist contact point, left deliberately: occlusion
there is baked into the photograph.

**Two safety nets, one of which ate fingers.** A "still looks like ground"
catch-all (bright, neutral hue) was added to mop up a backdrop wrinkle, and it
took notches out of both index fingers — sheer-fabric highlights on fingertips
are bright and fairly neutral too. Fixed by carving out a core-subject zone,
grown from confirmed fabric and skin seeds, that no safety net may touch.

**The structural fix was inverting the default.** Early passes treated every
non-ground, non-frame pixel as "keep as photographed," which is backwards — it
let ambiguous dark pixels survive by default, and most ambiguous dark pixels are
shadow. Final version defaults everything to transparent and only allows opaque
within a dilation of confirmed seeds.

---

## Measure the plate; don't trust the round numbers

Approximate pixel call-outs were available from the direction pass. Measuring the
plate programmatically — colour-threshold edge scans at multiple rows and
columns, away from hand occlusion — disagreed with several:

| | Stated (~) | Measured |
|---|---|---|
| Frame width | 3300px | 3273px |
| Side rail | 557px | 548px |
| Top rail | 356px | **269px** |
| Bottom rail | 356px | **328px** |
| Base strip | 745px | **870px** |
| Window | 2185×1564px | 2177×1566px |

The window matches closely, which is a good sign the method is sound. The
vertical figures don't: top and bottom rail are not equal to each other, and the
base strip is meaningfully larger.

Rather than pick one, both were cross-validated against a separate ratio table.
Computing headroom from the **measured** 870px base strip reproduces the stated
21% and 34% almost exactly. The 745px figure does not reproduce them. The
measured values are what the tool is built on, and the discrepancy was raised
rather than silently overridden.

---

## The bug that only appears on export

The metadata line's `font-family` referenced a CSS custom property. That
resolves fine in the live page and does nothing inside the detached SVG used for
export — there is no cascade from `:root` into an off-DOM image loaded from a
data URI. The preview was correct and the export was wrong.

Caught by running the actual `rasterize()` path in headless Chrome and
inspecting the resulting canvas, rather than screenshotting the preview. Fixed
to an explicit font stack.

**Verifying the preview is not verifying the export.**

---

## Known limits

- **4:5 was dropped.** A 4:5 crop of this plate amputates the hands mid-finger:
  the face spans x 667–3951 of 4608, and 4:5 gives 2970 wide. Square and native
  only. Corrected rather than shipped quietly.
- **Crease displacement is parked.** The illumination pass alone sells the
  relief. Revisit only if content needs to bend over the spine.
- The plate variant depends on a sidecar asset folder — a deliberate deviation
  from the single-file convention, since embedding a 4608px plate as base64
  produces a ~25MB file and native-resolution export mattered more.
