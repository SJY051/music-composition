# Reference Track Digging

> **Snapshot note:** Last content review snapshot: 2026-04-26. This is a method for turning reference tracks into compositional decisions without copying protected expression or flattening genre differences.

A reference track is not a command to imitate. It is evidence: a compact example of tempo, form, groove, harmony, melody, arrangement, production density, vocal delivery, and cultural context.

## When to use this file

Use this file when the user says:

- "Make it feel like [song/artist/genre]."
- "What should I reference for this style?"
- "I want current K-pop/J-pop/EDM/hip-hop/ballad energy."
- "Find me the sound of [scene/region/year]."
- "How do I study references without just copying?"

For current references, pair this with `web-music-trend-research.md`. If the user has a streaming service, public playlist, Replay/Wrapped summary, or Last.fm/scrobbling history, pair with `user-listening-context-and-streaming-services.md`. For living-artist, copyright, AI-assisted, sample, interpolation, or too-close imitation issues, pair with `style-reference-and-copyright.md`.

## Ethical and creative guardrails

- Extract **craft variables**, not melodies, lyrics, signature riffs, or distinctive recordings.
- Avoid imitating a living artist's exact style or vocal identity.
- If a reference is highly recognizable, use multiple references so the result is a blend, not a clone.
- For traditional or regional music, do not treat one track as the whole tradition. Study several examples and, when possible, work with practitioners.
- When the user asks for copyrighted lyrics, melody, or a too-close rewrite, redirect toward analysis and original alternatives.

## The three-layer reference stack

A strong reference set usually has three layers:

| Layer | Purpose | Example use |
|---|---|---|
| Anchor references | The closest sonic/emotional target | "This is the energy and form center." |
| Boundary references | Show what *not* to drift into | "This is too clubby / too rock / too sentimental." |
| Root references | Older or deeper idiom sources | "This explains where the groove or harmonic language comes from." |

For a hybrid style, build one stack per ingredient. Example: "K-pop with K-trad percussion and neo-soul harmony" needs K-pop anchors, K-trad rhythm/instrument roots, and neo-soul harmony references.

## Personal-library first pass

When the user's own taste matters, ask for lightweight streaming evidence before digging generic references:

- 5 anchor tracks they already love
- 2 boundary tracks that are close but wrong
- a public playlist link, if available
- a Replay/Wrapped/Last.fm summary, if they choose to share it

Then compare those with current platform or chart signals. User taste is the target; charts are context.

## Minimum viable reference set

For a fast composition answer:

1. **3 anchor tracks**
2. **2 contrast tracks**
3. **1–2 root/context tracks**

For a deeper style study:

1. 5–8 current tracks
2. 3 historical/idiom roots
3. 2 adjacent-market examples
4. 1 "wrong direction" example

## Listening pass template

For each reference, fill this out:

| Category | What to capture |
|---|---|
| Tempo / meter | BPM, swing/straight, half-time/double-time feel |
| Form | intro length, verse/pre/chorus/bridge layout, hook timing |
| Groove | kick/snare placement, hi-hat density, percussion pattern, bass rhythm |
| Harmony | key center, loop length, harmonic rhythm, modal/functional language |
| Melody / topline | range, contour, repeated cells, leaps, climax placement |
| Lyrics / prosody | syllable density, rhyme pattern, language-tone constraints, hook words |
| Arrangement | layer entry/exit, density arc, register spread, contrast between sections |
| Signature element | one element that makes it memorable |
| Transferable move | what can be borrowed abstractly |
| Do-not-copy element | exact melody, lyric phrase, riff, sample, vocal identity, or signature production tag |

## Reference matrix

Use a matrix to prevent shallow imitation:

```md
| Track | Role | Tempo | Form clue | Groove clue | Harmony clue | Topline clue | Arrangement clue | Transferable idea |
|---|---|---:|---|---|---|---|---|---|
| Track A | Anchor | 100 | hook by bar 9 | dembow-like | 4-chord loop | chant hook | sparse verse → dense chorus | early group-vocal hook |
| Track B | Boundary | 128 | drop-centered | four-on-floor | static | short phrases | club build | avoid this much EDM pressure |
| Track C | Root | 92 | call-response | traditional cycle | drone/modal | ornamented | live percussion | adapt call-response, not surface sample |
```

## How to dig by style

### Pop / K-pop / J-pop / C-pop

Look for:

- hook placement and section contrast
- pre-chorus lift strategy
- chorus density and group-vocal treatment
- dance-break or post-chorus role
- language-specific prosody and syllable density
- current chart/platform context

Pair with:
- `../genres/kpop-jpop.md`
- `../genres/cpop-and-southeast-asian-pop.md`
- `../fundamentals/prosody-and-language.md`
- `web-music-trend-research.md`

### Hip-hop / R&B / neo-soul

Look for:

- drum pocket and swing/microtiming feel
- bass/sub relationship
- sample/chop logic or interpolation risk
- harmonic color: minor 9, maj9, sus, planing, gospel moves
- vocal/rap flow density and rhyme placement

Pair with:
- `../genres/hip-hop-rnb.md`
- `../rhythm-groove/groove-and-feel.md`
- `../harmony/jazz-harmony.md`

### EDM / electronic

Look for:

- loop length and phrase grid
- build/drop/breakdown timing
- kick/bass relation as composition, not just mixing
- hook type: vocal chop, lead motif, bass riff, texture
- subgenre tempo and drum pattern

Pair with:
- `../genres/electronic-edm.md`
- `../production-aware/energy-and-dynamics.md`
- `../form/popular-song-forms.md`

### Film / game / media

Look for:

- dramatic function, not just genre
- theme transformability
- loopability / editability
- density under dialogue or gameplay
- stinger and transition language

Pair with:
- `../genres/film-tv-scoring.md`
- `../genres/game-music.md`
- `../genres/media-and-commercial-music.md`

### Traditional / regional fusion

Look for:

- the actual tradition being referenced
- rhythmic cycle, mode, ornament, language, and instrument idiom
- whether the source is concert, ritual, pop-fusion, film-score, or sample-pack mediated
- what requires a practitioner rather than a text description

Pair with:
- `../genres/korean-traditional.md`
- `../genres/folk-roots-and-traditions.md`
- `../techniques/microtonal.md`
- `../fundamentals/prosody-and-language.md`

## Turning references into original composition prompts

Bad prompt:

```text
Write a song like Track X.
```

Better prompt:

```text
Use Track X only as a craft reference:
- 96 BPM, minor-key dance-pop
- hook enters before 0:40
- verse is sparse and low-register
- pre-chorus rises by sequence
- chorus uses chantable 3-note hook
- avoid copying melody, lyric, or signature synth riff
Create a new 8-bar chorus progression and topline contour with similar energy.
```

## Quick anti-copy checklist

Before giving the user a generated musical idea, check:

- Is the melody a new contour, not the reference melody with small changes?
- Are lyrics original and not a paraphrase of a recognizable hook?
- Is the chord loop generic enough or transformed enough?
- Are signature riffs/samples/production tags avoided?
- Are references blended rather than copied one-to-one?
- Did you explain the transferable craft principle?
- If the request names a living artist/current hit, did you apply `style-reference-and-copyright.md`?

## Final advice

A reference track is most useful after it has been decomposed. The agent should answer with playable, concrete moves — chords, rhythm cells, contour, form plan — not vague adjectives like "make it more modern."

## Quick asset

- Fast web-search cheatsheet → `../../assets/web-search-cheatsheet.md`
