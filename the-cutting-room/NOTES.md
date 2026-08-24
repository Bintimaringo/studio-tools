# The Cutting Room — Build Notes

Momentum out of cuts. A locked text block over imagery jump-cutting at strobe
pace, exported as video.

The engine is **scale contrast, not motion**. Full looks alternate with extreme
detail crops — several apparently different frames are the same image at
different crop scales — with occasional slow horizontal glides between hard
cuts. The text never moves. It is the constant; the imagery is the variable.

---

## The bug that mattered: static canvases record nothing

Canvas `captureStream` only emits a frame when pixels change. A jump-cut loop is
static between cuts. The first exports were 14KB shells reporting durations of
0.03 seconds.

Fixed with `captureStream(0)` and an explicit `track.requestFrame()` per
rendered frame, taking the clock away from the browser.

A sibling tool built earlier never hit this, because video content changes every
frame and auto-capture had nothing to notice. The failure only exists for work
that holds still — which is precisely what this instrument makes.

---

## The export clock could run for 78 minutes

A visibility guard credited hidden time back to the export clock:

```js
start += now - hiddenAt;   // on becoming visible
```

`hiddenAt` is only set by a preceding *hidden* event. A visible event without
one adds the entire page uptime to the clock. The recorder went to **−4666
seconds** against a 31.2 second target and would have run for 78 minutes.

Reachable in ordinary use any time an export begins while the tab is already
backgrounded. Fixed with `else if (hiddenAt)` and a reset, so only measured
hidden time is ever credited.

---

## Serving video without Range support breaks seeking silently

The development server answered every request with a full `200`, so browsers
could not seek any video it served. A 31 second file reported `duration = 2.29s`
and every seek landed in the first two seconds.

This is the kind of defect that looks like a tool bug for a long time. Fixed by
answering `206 Partial Content` with `Content-Range` and `Accept-Ranges`,
streamed rather than buffered whole.

---

## Compositions persist, in two different kinds

The question that prompted this was simply *"if I wanted to work on this later,
how do I prevent it from disappearing?"* Nothing did. Exports were on disk, but
the arrangement that produced them lived only in the tab.

**Autosave, in IndexedDB.** Every mutation schedules a debounced write of the
whole composition, restored on boot ahead of the demo, so a reload or a crash
costs nothing. Assets fetched from the project folder are stored by path and
refetched; files dropped from elsewhere carry their actual bytes. The boot demo
is explicitly excluded — restoring a demo as though it were work would be worse
than useless.

**Recipe files, as JSON.** Portable and human-readable: a 31 second, 61 cut
composition is 13KB. Records ratio, tempo, each slide's asset, crop scale, hold,
glide and pan, and the whole text block. Assets with a project path reload
automatically; assets from outside it are asked for by name through a relink
panel.

The format was proved by round-trip rather than by inspection. A recipe authored
by hand loaded to 61 cuts at 31.2 seconds, and saving from the tool afterwards
produced a file identical to the hand-authored one, field for field. **That
equality is the proof.**

---

## Known limits

- **Export is realtime capture**, so duration carries roughly 10–20% wall-clock
  drift against the nominal loop length, and the tab must stay visible while
  recording. Hidden time is now paused rather than corrupted. A frame-exact,
  faster-than-realtime path is the known next step, with the dependency it
  implies.
- **Bitrate is fixed at 14 Mbps**, so a 31 second export runs about 68MB. Fine
  for review, heavy for a site embed. A quality control is the obvious next knob.
- **Snippet in-points** seek within the captured five-second window; precision is
  blob-seeking, adequate for flash cuts.
- **No true GIF export**, deliberately. Platforms treat short muted mp4s as gifs
  at a fraction of the size.
