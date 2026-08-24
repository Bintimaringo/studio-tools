# Collage Compositor — Build Notes

Composition from cut fragments. A slicer prototype for banded, misregistered
arrangements, and a cull sheet for reviewing generated pools before anything
reaches a composition.

---

## The defect that is invisible at thumbnail size

A fragment carried a faint grey vignette in one corner: raw RGB around 180
against roughly 245 flat white everywhere else. Invisible on the contact sheet.
Glaring at full scale, and fatal to the key — the flood fill cannot route past a
corner that reads as content.

Sweeping key tolerance from 28 to 90 found no setting that both cleared the
corner and kept the subject, because petal edges and corner grey sit at similar
luminance. There was no tolerance to tune toward; the asset was simply bad.

Resolution was to sample all four corners by raw pixel value and pick a sibling
that was flat:

```
v01   244–245 luma, flat      → clean cutout at standard tolerance
v02   230–240                 → near-clean, negligible
v03   179 worst               → fails
v04   183 worst               → fails
```

**The lesson is a check, not a fix.** A four-corner luma sample at ingest catches
this entire class of defect before it reaches composition. Two of eight assets in
one batch were unusable at standard tolerance, and neither was visible at
review size.

The second check matters as much as the first: a low-luma corner is not
automatically fatal if the flood can route around it via clean neighbouring
border pixels. So the real gate is the leftover-pixel count after an actual
key attempt, not the luma reading alone.

---

## A layout bug latent since the first poster

The metadata block's date line and the caption's first line shared a
y-coordinate in both tools. Any caption long enough to reach 46% of the frame
width collided with the right-aligned date.

It had been there since the first composition and never fired, because short
captions never reached far enough right. Fixed by moving the date to its own
baseline above the caption block, matching how the title sits above everything
else.

Existing recipes are unaffected — the fix changes vertical position, not content.

---

## Machine verdicts are advisory

The cull sheet renders every fragment in a pool with its measured gate chips —
highlight percentage, shadow percentage, key removal percentage, and the working
tolerance that produced them — plus per-family notes, click-to-keep with
`localStorage` persistence, and full-size zoom.

The measurements narrow the field. They do not make the decision. A fragment can
pass every gate comfortably and still be wrong for the work, and the sheet is
built to make that judgment fast rather than to replace it.

In one series, 64 fragments were generated and 7 were kept.

---

## Generation lessons worth keeping

Where a generated pool feeds the tool, three prompt corrections came out of
measurement rather than taste:

1. "Soft contact shadow only" is too weak. It needs to be "no cast shadow beyond
   the object's base."
2. A flat-ground clause needs "perfectly even, no vignette, no gradient" — see
   the corner defect above.
3. Dark-ground prompts need their highlight clause moved earlier and
   strengthened. The model weights dark clauses harder, and highlights starve.
