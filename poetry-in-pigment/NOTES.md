# Poetry in Pigment — Build Notes

Field generation and review built around pigment histories. Includes the contact
sheets used to cull runs, and the field-generation guide the prompts are written
against.

---

## Verifying an export instead of trusting it

The layout fills letterforms with a pigment field or an uploaded pattern, masked
so the pattern shows through the glyphs only. Masks are exactly the kind of thing
that looks right in the browser and flattens on export.

So the acceptance test reads the exported file rather than the preview: scan the
word band in the 2000×2666 PNG and count pattern-coloured pixels *inside* the
glyph shapes. Finding 72,003 yellow and 10,104 red pixels there proves the mask
survived rasterisation and neither flattened nor dropped.

Checked in the same pass: zero italics (by computed style, not by eye), zero
hairline rules, subscripts intact. The field fill uses the identical clipped
`<image>` path, so it is covered by the same guarantee.

**A screenshot of the preview would have passed a broken export.**

---

## Licensed faces make a file stop being self-contained

Two of the display faces are licensed and referenced by their installed system
family name. They are deliberately **not** embedded and carry no `@font-face`
rule, per licence.

The consequence is stated rather than hidden: on any machine without those faces
installed — including any machine this file is opened on elsewhere — they fall
back to substitutes. PNG export fidelity for those two faces depends on running
the export where they are installed.

The open-licence monospace is web-loaded and inlined as base64 on export, so it
behaves correctly everywhere.

This is the tradeoff the single-file convention makes when it meets type
licensing, and it is worth naming: **the file is portable, the typography is
not.**

---

## Chemistry as typography

Pigment formulas render as real type rather than as an image: `parseFormula()`
tokenises symbol and stoichiometry into a reusable structure, and the stack sizes
adaptively across three to five units, clamped between 40 and 116px and
baseline-snapped.

Subscripts are actual subscripts. They survive export, which is what the pixel
scan above confirms.

---

## Batch pipelines drop things quietly

Where fields are generated in batches, the pipeline submits sequentially and
polls per run rather than firing a parallel fan-out. Parallel returns arrive in
completion order rather than submit order, which makes direction labels
unassignable after the fact — you get the images and lose the record of what
produced them.

The sequential pipeline held at batch scale: 48 runs submitted, 48 returned, zero
dropped.

One correction worth recording: the brief specified a text-to-image endpoint,
which takes no image input and therefore cannot be reference-conditioned. The
image-to-image variant of the same model does, passing the reference through an
undocumented but accepted parameter. Verified on a single test run before
committing the rest of the batch.
