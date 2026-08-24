# The Breathing Room — Build Notes

Motion out of geometry. Load an SVG; every `<path>` becomes a group and every
subpath inside it becomes a part. The parts breathe — opening outward, holding,
settling — over an adjustable envelope.

Built after a long session animating a stencil mark by hand, where the same
three mistakes kept being made and corrected. The tool exists so they don't have
to be made again.

---

## The three findings it encodes

**Move the pieces, not the mark.** Scaling a whole lockup opens the gaps but
thickens the strokes with them, which is fatal for a stencil, where the cuts
*are* the identity. Splitting each path into subpaths and translating them
rigidly leaves stroke weight untouched. This is why intake splits rather than
simply importing.

**Dilate about the group centre; never step by a fixed distance.** The first
version pushed every part a fixed amount along a unit vector from its group
centre. That breaks for any part sitting near that centre: one arch measured
0.15 units off centre, so normalising the offset produced an essentially
arbitrary direction — the arch slid sideways while its cuts opened at half the
rate of neighbouring letterforms. Under dilation, displacement is proportional to
distance, so a central part holds still and outer parts travel far enough to open
every cut equally. Correct, and simpler.

**Calibrate amplitude to the median part distance.** Otherwise `0.3` means
something different for every mark loaded. `K = amp / median` keeps the number
stable across marks, so a setting tuned on one mark stays meaningful on the next.

---

## Carried over deliberately from a sibling tool

`captureStream(0)` with an explicit `track.requestFrame()` per rendered frame,
because a held breath is static between frames and auto-capture only emits on
pixel change — the same defect that produced 14KB export shells elsewhere.

And the visibility guard written the *fixed* way (`else if (hiddenAt)`), so only
measured hidden time is credited to the clock. The naive version adds the whole
page uptime whenever an export begins on an already-backgrounded tab.

Both of these are the residue of debugging done once, in another instrument, and
not repeated.

---

## Verification

Intake of the demo mark resolves to 7 groups, 21 parts, median 5.34 units,
independently reproducing figures derived offline during the source session.
Dilation displacements on the middle letterform read `-0.551 / 0.008 / 0.556` —
centre held, outer two travelling, both cuts opening to match the neighbouring
`o` at 0.55.

Export is written to the pattern that works in the sibling tool but wants one
hand-run confirmation; realtime capture needs a fronted, visible tab.

---

## Known limits

- **Intake handles `<path>` only.** Text, `<rect>`, `<circle>` and stroked
  artwork are ignored — outline them first. The status line says so when it finds
  no paths.
- **Grouping is one group per source path.** A mark drawn as a single compound
  path arrives as one group; dilation still works, spread has nothing to act on.
- **Elliptical arcs pass through unflattened.** Fine for rendering, but their
  bounding boxes come from the measurement SVG, so a part that is only an arc may
  centre slightly off.
- **`spread` moves groups horizontally only** — right for a wordmark, wrong for a
  mark stacked vertically. Radial group spread is the obvious next knob.
- Export duration carries the usual realtime drift against the nominal cycle.
