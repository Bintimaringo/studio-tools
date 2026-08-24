# Studio Tools

Instruments built at [Binti Maringo](https://bintimaringo.studio) for the studio's
own work. Each one exists because a thing needed doing repeatedly and by hand,
and doing it by hand kept producing the same three mistakes.

They are single-file HTML. No build step, no dependencies, no install. Open one
in a browser and it runs.

---

## The instruments

**[The Cutting Room](the-cutting-room/)** — Momentum out of cuts. A locked text
block over imagery jump-cutting at strobe pace, exported as video. Takes stills
and short clips, rations the palette, and writes out mp4 at the aspect you ask
for.

**[The Breathing Room](the-breathing-room/)** — Motion out of geometry. Built
after a long session animating a stencil mark by hand, so that the corrections
made there would not have to be made again.

**[The Hand Presenting the Work](hand-presenting-the-work/)** — A compositor for
placing work into a photographic plate: real paper texture, thumb shadows,
sheen, and crease, with the content window masked to the plate's measured
geometry. The bar was that the seam should not be findable at 100%.

**[Collage Compositor](collage-compositor/)** — Composition from cut fragments,
with a slicer prototype and a cull sheet for reviewing generated pools before
anything reaches a composition.

**[Poetry in Pigment](poetry-in-pigment/)** — Field generation and review, built
around pigment histories. Includes the contact sheets used to cull runs and the
field-generation guide the prompts are written against.

**[Broadside Studio](broadside-studio/)** — Type and layout for broadsides.

**[recipes/](recipes/)** — Saved parameter sets, portable between tools.

---

## Running them

Most tools open straight from the filesystem. A few fetch their presets, which
browsers block on `file://`, so serve the folder instead:

```
python3 serve.py
```

Then open <http://localhost:4602>. Standard library only, nothing to install.

---

## The notes

Every tool carries a `NOTES.md`: what the hard problem was, what failed, and the
diagnosis that fixed it. The green boundary seam in the plate compositor. The
contact shadow that kept being mistaken for translucent fabric, because the
maths genuinely could not tell them apart. The corner vignette invisible at
review size and fatal at full scale. The export clock that would have run for
seventy-eight minutes.

They are the most useful thing in this repository. The tools are the residue of
the thinking; the notes are the thinking.

---

## What is not here

**Generated output.** These tools make images and video. Those live elsewhere —
the instrument is the artifact worth keeping, not its exhaust.

**Fonts.** The house faces are licensed per seat and are not redistributed. The
tools reach for them, shrug when they are absent, and fall back — typography
changes, nothing breaks. Everything else comes from Google Fonts over CDN and
resolves on its own.

**Plates and source imagery.** The plate variant of the Hand compositor needs a
photographic plate, illumination maps, an occluder, and two licensed typefaces.
None of that is ours to hand out, so that variant is not included here.

**Ground plates for The Breathing Room.** The demo mark is bundled; the two
ground images are not. Use the file pickers to supply your own, or leave the
ground on `solid`.

## Known edges

Saving a recipe to disk posts to a `/save` endpoint that the bundled server does
not implement — it was written against the studio's own node server. Recipes in
`recipes/` still load. Everything else runs on the static server above.

---

*Built to hold.*
