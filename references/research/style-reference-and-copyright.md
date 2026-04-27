# Style Reference and Copyright Guardrails

> **Snapshot note:** Last content review snapshot: 2026-04-26. Copyright rules, AI policies, platform rules, lawsuits, and licensing norms change quickly. Use this file for durable creative guardrails, and verify current legal/platform facts through active web research before giving high-stakes advice.

This file helps the agent respond when the user asks for music "in the style of" an artist, song, producer, label, era, or scene. It is not legal advice. It is a composition workflow for staying original while still learning from references.

## Core principle

A style request should become a **craft-variable request**, not a clone request.

Instead of:

```text
Write a chorus exactly like [living artist / current hit].
```

Transform into:

```text
Let's extract transferable variables: tempo range, groove, harmonic rhythm, section contrast, vocal register, hook timing, arrangement density, and emotional arc — then write a new idea that avoids the reference's melody, lyrics, riff, sample, and signature vocal identity.
```

## What is usually safer to extract

These are broad musical ideas. They can still become risky if combined too closely with one specific reference, but they are the right starting point.

| Extractable variable | Example |
|---|---|
| Tempo / meter | 96 BPM, 4/4, half-time chorus |
| Groove family | dembow-like, boom-bap, shuffle, four-on-floor, 6/8 ballad |
| Harmonic palette | minor add9 loop, backdoor cadence, modal vamp, gospel-adjacent plagal movement |
| Harmonic rhythm | one chord per bar, two-bar vamp, pre-chorus acceleration |
| Form role | hook before 0:40, post-chorus chant, bridge breakdown |
| Arrangement density | sparse verse → dense chorus; low verse → octave-wide chorus |
| Topline strategy | narrow verse, higher chorus peak, repeated 3-note hook |
| Lyric craft | conversational verse, slogan-like chorus, internal rhyme density |
| Performance energy | whispered, belted, chant-like, call-response — without copying a specific voice |

## What to avoid copying

| Avoid | Why |
|---|---|
| Exact or near-exact melody | Melody is one of the most recognizable protected elements in songs |
| Copyrighted lyrics or close paraphrases | Lyrics are protected expression, not just style |
| Signature riff / hook / motif | Often the identity of the recording/composition |
| Samples from recordings | Sound recordings require separate clearance in many workflows |
| Distinctive vocal identity of a living artist | Ethically risky and often platform/policy-sensitive |
| Producer tags / exact sound-design signatures | Can imply unauthorized imitation or confuse attribution |
| One-reference cloning | Even if each element is small, the combination can become recognizably derivative |

## Living artist and current-hit requests

When the user names a living artist or very recent hit:

1. Acknowledge the target energy.
2. Refuse to clone exact expressive elements.
3. Translate into neutral craft variables.
4. Offer an original sketch.
5. Recommend using multiple references.

Template:

```md
I can help capture the broad craft traits — [tempo/groove/density/hook strategy] — but I won't copy [artist]'s melody, lyrics, vocal identity, or signature riff.

Original direction:
- Tempo: ...
- Groove: ...
- Harmony: ...
- Topline: ...

Playable sketch:
...
```

## Historical, public-domain, and genre requests

Requests like "baroque sequence", "bebop head", "Motown-inspired bassline", "early rock and roll", or "1960s girl-group energy" are usually easier to handle because they target a broader idiom or historical convention. Still avoid copying a specific protected song.

Safer phrasing:

- "Use a baroque-style circle sequence."
- "Use bebop-like enclosure and chromatic approach tones."
- "Use a 1960s soul/pop backbeat, call-response backing vocals, and I-vi-IV-V harmonic language."
- "Use a classic funk clavinet-style syncopation without copying a particular riff."

## Reference-stack method

For any style request, build a reference stack:

| Layer | Purpose |
|---|---|
| Anchor references | The desired energy and market frame |
| Boundary references | What the user does *not* want |
| Root references | Older idiom sources that explain the groove/harmony/vocal language |

A three-track anchor set is safer and more useful than one target track. The agent should identify shared variables across references, not imitate the most famous one.

See `reference-track-digging.md` for the full workflow.

## Anti-copy transformation moves

If a generated idea feels too close to the reference, transform at least two independent dimensions:

| Dimension | Transformation |
|---|---|
| Melody | Change contour, interval skeleton, phrase length, and climax placement |
| Rhythm | Change pickup, syncopation, note density, or bar placement |
| Harmony | Keep mood but change chord order, bass motion, or cadence |
| Form | Move hook earlier/later, change pre-chorus length, add/remove post-chorus |
| Arrangement | Change register, instrumentation, or density arc |
| Lyric | Change image field, rhyme scheme, syntax, and hook wording |
| Groove | Keep broad family but change kick/bass relationship or subdivision |

A single cosmetic change is not enough when the reference remains recognizable.

## Copyright concepts the agent should keep straight

Use this as plain-language guidance, not legal advice.

| Concept | Composition relevance |
|---|---|
| Idea vs. expression | Broad ideas, methods, and style traits are different from specific melodies, lyrics, riffs, and recordings |
| Composition vs. sound recording | A song's melody/lyrics/harmony chart and a particular recording can be separate rights |
| Sample vs. interpolation | Sampling uses an actual recording; interpolation re-records/recreates musical material and still may require composition rights |
| Public domain | A composition may be public-domain while a modern recording of it is not |
| Fair use | Context-specific legal analysis; do not promise that a use is fair use |
| AI-assisted output | Human authorship and creative control may matter for registration/ownership in some jurisdictions |

## AI-assisted composition guardrails

For AI-assisted workflows, the agent should encourage human creative control:

- document human decisions: prompt intent, selection, editing, arrangement, performance, lyrics, melody revisions
- avoid using AI to mimic a living artist's voice or exact style
- treat generated outputs as drafts requiring human curation
- verify platform, distributor, and copyright rules when the user plans release
- avoid claiming copyrightability or clearance certainty without current legal review

## When to web-check

Use active web research when the user asks about:

- current lawsuits, licensing standards, AI music policies, or copyright office guidance
- current artist/reference comparisons
- platform/distributor rules for AI-generated or AI-assisted music
- whether a particular work is public domain in a jurisdiction
- sample/interpolation clearance norms for a current release workflow

See `web-music-trend-research.md` for source hierarchy and search patterns.

## External source anchors to verify current facts

Check current versions of:

- U.S. Copyright Office — copyright basics, AI reports, registration guidance
- WIPO — general copyright concepts across jurisdictions
- official distributor/platform policies when releasing music
- current court filings or reputable legal reporting for active lawsuits
- rights-holder or publisher information for specific works

## Good response examples

### User: "Make it sound like [current artist]."

```md
I can aim for a similar broad lane — dark mid-tempo pop with a sparse verse, early hook, and wide chorus — but I'll keep the melody, lyric, vocal identity, and signature production elements original.

Try this original sketch:
Key: F minor, 92 BPM
Verse: | Fm(add9) | D♭maj7 | A♭/C | E♭sus |
Pre:   | B♭m7 | C7♭9 | Fm | E♭ |
Chorus:| D♭ | A♭ | E♭ | Fm |
Topline: narrow verse around ^3-^5, chorus peak on ^6, repeated three-note hook.
```

### User: "Use the exact chorus melody but change the chords."

```md
I can't provide a close derivative of a recognizable copyrighted chorus melody. I can analyze the contour in abstract terms — for example, 'short repeated pickup, leap to peak, stepwise fall' — and write a new melody with a different contour and rhythm.
```

### User: "Can I release this if it uses AI?"

```md
That depends on jurisdiction, platform rules, the amount of human authorship, and whether any protected material or voice likeness was used. For composition work, document your human creative decisions and check current copyright/platform rules before release.
```

## Cross-references

- Reference digging → `reference-track-digging.md`
- User listening context → `user-listening-context-and-streaming-services.md`
- Regional trend evolution → `regional-trend-evolution-analysis.md`
- Minor and hybrid genres → `../genres/minor-and-hybrid-genres.md`
- Current web research → `web-music-trend-research.md`
- AI-assisted composition → `../techniques/algorithmic-and-AI-assisted.md`
- Pre-production reference decisions → `../production-aware/pre-production-decisions.md`
- Diagnostic anti-copy checklist → `../../assets/diagnostic-checklists.md`
- Response templates → `../../assets/response-templates.md`
