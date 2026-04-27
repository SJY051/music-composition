# Response Templates

Use these templates to keep music-composition answers concrete, playable, and easy to revise. They are templates, not scripts: shorten, expand, or combine them based on the user's level and the task.

## General answer shape

For most creative help:

```md
Assumption: [genre / key / tempo / instrumentation if not stated]
Goal: [what the user wants musically]

Option 1 — [name]
[playable material]
Why it works: [1–2 sentences]
Trade-off: [what it may weaken]

Option 2 — [name]
[playable material]
Why it works: ...
Trade-off: ...

Try first: [one concrete next action]
```

Keep the *playable material* first. Put theory after the user can hear or play something.

## Chord progression request

```md
Key: [C minor]
Tempo / feel: [72 BPM, slow 6/8 ballad]

Progression:
| Cm(add9) | A♭maj7 | E♭/G | G7sus4 G7 |

Roman numerals:
| i(add9) | ♭VImaj7 | ♭III6 | V7sus4 V7 |

Why it works:
- [A♭maj7 softens the minor color.]
- [E♭/G keeps the bass stepwise.]
- [G7 creates a real dominant pull into the next phrase.]

Variation:
| Cm(add9) | Fm9 | A♭maj7 | G7♭9 |
```

For beginners, skip Roman numerals unless useful. For advanced users, include voicing or voice-leading notes.

## Melody / topline request

```md
Key / scale: [A minor, with raised ^7 over E7]
Range target: [A3–E5]
Phrase length: [4 bars]

Scale-degree sketch:
Bar 1: ^5 ^5 ^6 ^5 ^3
Bar 2: ^4 ^3 ^2 —
Bar 3: ^5 ^6 ^7 ^1̂
Bar 4: ^2 ^7 ^1 —

Contour idea:
- Start narrow and speech-like.
- Peak once on [E5] in bar 3.
- Resolve by step, not by another leap.

Lyric placement:
[Put the hook word on the highest note / longest note.]
```

If the user gave lyrics, preserve their words and adjust rhythm/prosody first.

## Reharmonization request

```md
Original:
| C | Am | F | G |

Reharm option A — smoother bass:
| C | G/B | Am | Fmaj7 G |
Why: bass descends C-B-A, making the simple loop feel intentional.

Reharm option B — jazzier:
| Cmaj9 | E7♭9 | Am9 | Dm9 G13 |
Why: E7 tonicizes Am; Dm9-G13 creates a ii-V back to C.

Keep unchanged:
- [melody notes that define the hook]
- [strong lyric downbeats]
```

Always state what should **not** change so the song identity survives.

## Critique / feedback request

```md
My read:
[One-sentence diagnosis: the chorus has good energy, but the melody and arrangement peak too early.]

What is working:
1. ...
2. ...

Highest-impact fix:
[One fix that changes the most with the least damage.]

Detailed notes:
| Area | Observation | Fix |
|---|---|---|
| Melody | ... | ... |
| Harmony | ... | ... |
| Form | ... | ... |
| Arrangement | ... | ... |

Revision path:
1. [small experiment]
2. [A/B compare]
3. [commit or revert]
```

Be honest but useful. Diagnose before prescribing.

## "The chorus doesn't hit" response

```md
The chorus may not be failing harmonically; it may be failing by contrast. Check these in order:

1. Melody: does the chorus hit a higher or longer focal note than the verse?
2. Rhythm: does the chorus simplify or intensify the groove?
3. Harmony: does the pre-chorus create enough dominant / rising / suspended energy?
4. Arrangement: does a new register or layer enter exactly at the chorus?

Two concrete fixes:
A. Harmonic lift:
Verse loop: | vi | IV | I | V |
Pre:        | IV | V/vi | vi | V |
Chorus:     | I | V | vi | IV |

B. Melodic lift:
Move the chorus hook peak from ^3 to ^5 or ^6, and hold it for at least a dotted quarter / half note.
```

Pair with `diagnostic-checklists.md` when deeper diagnosis is needed.

## Song plan request

```md
Working title / concept: [optional]
Genre frame: [alt-pop / K-pop ballad / neo-soul]
Tempo: [96 BPM]
Key center: [D minor]
Core hook idea: [3-note chant: ^5-^6-^5]

Form:
Intro: 4 bars — [hook fragment]
Verse 1: 8 bars — [low register, sparse]
Pre: 8 bars — [rising sequence]
Chorus: 8 bars — [full hook]
Verse 2: 8 bars — [variation]
Bridge: 8 bars — [relative major / breakdown]
Final chorus: 16 bars — [ad-libs / countermelody]

Core progression:
Verse:  | Dm | B♭ | F | C |
Pre:    | Gm | A7 | Dm | C |
Chorus: | F | C | Dm | B♭ |

Next writing step:
[Write only the chorus hook first; do not arrange yet.]
```

## Genre / trend answer

```md
Static genre frame:
[durable conventions from the relevant genre file]

Current check needed:
[charts/platforms/local scene/source types]

Composition takeaway:
1. [hook timing]
2. [groove/bass/drum pattern]
3. [form/density]
4. [lyric/prosody]

Caveat:
[platform-specific, region-specific, or trend too noisy]
```

Use `../references/research/web-music-trend-research.md` for current facts.

## Reference-track-driven request

```md
I won't copy the reference directly. I'll extract transferable craft variables.

Reference variables:
- Tempo / feel:
- Groove:
- Harmony:
- Topline:
- Form:
- Arrangement density:
- Signature element to avoid copying:

Original direction:
[New idea that shares energy but not melody/lyrics/riff/sample]

Playable sketch:
[Chord loop / melody contour / rhythm cell]
```

Use `../references/research/reference-track-digging.md` and `../references/research/style-reference-and-copyright.md`.

## Music analysis request

```md
Surface facts:
- Key center:
- Meter / tempo feel:
- Form:
- Main progression:

Functional read:
[Roman numerals and cadence points]

What creates the effect:
1. Harmony: ...
2. Melody: ...
3. Rhythm/groove: ...
4. Texture/arrangement: ...

Composer takeaway:
[One transferable technique]
```

Do not overclaim exact transcription if the user only provided a rough chart or audio description.

## Orchestration / arrangement request

```md
Goal: [make chorus wider without clutter]

Register plan:
Low: [bass / low cello / sub]
Mid: [piano/guitar comp]
High: [strings/synth pad/counterline]
Vocal space: [leave 1–3 kHz range uncluttered]

Move:
- Double the melody at the octave only on the hook word.
- Put sustained harmony above the vocal, not in the same register.
- Use rhythmic instruments in verse, sustained instruments in chorus for contrast.

Risk:
[too much density; check lyric intelligibility]
```

## Game / interactive music request

```md
State map:
Exploration → Tension → Combat → Victory / Failure

Shared material:
- Motif: [^1-^3-^2]
- Tempo grid: [120 BPM]
- Key center: [D Dorian]

Layer plan:
Layer 1: ambient bed, loopable 16 bars
Layer 2: percussion, enters on tension
Layer 3: bass ostinato, enters on combat
Layer 4: brass/stinger, one-shot transitions

Transition rule:
[quantize transitions to 1 bar / 4 bars / next cadence]
```

## Teaching request

```md
Level assumption: [beginner/intermediate/advanced]
Goal: [learn secondary dominants]

Core idea:
[one plain-language explanation]

Tiny exercise:
1. Play | C | G | C |
2. Insert V/V: | C | D7 G | C |
3. Hear how D7 makes G feel inevitable.

Check-yourself question:
[What chord is V/vi in C major?]

Next step:
[try it in another key]
```

## User listening-context request

```md
I can use your listening context as evidence, not as something to copy.

Safe inputs:
- public playlist link / 5-10 track names / Replay-Wrapped summary / Last.fm top tracks
- no login details or private credentials

Listening-context signal:
- Personal anchors:
- Boundary tracks:
- Platform or market check:

Composition variables:
1. Tempo/groove:
2. Harmony:
3. Topline/prosody:
4. Form/hook timing:
5. Arrangement density:

Concrete next move:
[4-8 bar sketch, reference matrix, or playlist-fit plan]
```

## Regional trend-evolution request

```md
Scope:
- Region/market:
- Time window:
- Platform signal:
- Reference cluster:

What seems to be changing:
1. Platform/function:
2. Groove:
3. Topline/prosody:
4. Form/arrangement:
5. Collaboration or industry pattern:

Composition advice:
- Keep:
- Modernize:
- Avoid:
- Concrete 4-8 bar move:

Caveat:
[platform/region/time-window specificity]
```

## Microgenre / hybrid genre request

```md
I will treat this as a scene/tag question, not a fixed universal genre rule.

Genre ingredients:
- Main anchor:
- Supporting ingredient:
- Platform/scene context:

Craft variables:
| Variable | Choice | Confidence |
|---|---|---|
| Tempo/groove | | |
| Harmony | | |
| Topline/vocal | | |
| Texture | | |
| Form | | |

Sketch:
[playable progression/rhythm/topline contour]

Avoid copying:
[reference melody, lyrics, sample, meme phrase, producer tag, vocal identity]
```

## Cross-references

- Answer calibration / controlled variation → `../references/creative-workflows/answer-calibration.md`
- Vague problem triage → `diagnostic-checklists.md`
- Progression lookup → `progressions-catalog.md`
- Form templates → `form-templates.md`
- Chord symbols → `chord-symbol-conventions.md`
- Reference-track workflows → `../references/research/reference-track-digging.md`
- User listening context → `../references/research/user-listening-context-and-streaming-services.md`
- Regional trend evolution → `../references/research/regional-trend-evolution-analysis.md`
- Minor/hybrid genres → `../references/genres/minor-and-hybrid-genres.md`
- Trend/reference matrices → `trend-and-reference-matrices.md`
- Style/copyright guardrails → `../references/research/style-reference-and-copyright.md`


## Musical brainstorming option board

Use when the user asks for ideas, sparks, or multiple directions.

```md
I'll give you three lanes so we don't commit too early.

| Lane | Core idea | Playable seed | Why it might work | Risk |
|---|---|---|---|---|
| Safe | | | | |
| Fresh | | | | |
| Wild | | | | |

Which one feels alive enough to prototype?
```

## Multi-turn session state

Use when the conversation becomes iterative.

```md
**Project card**
- Goal:
- Genre frame:
- Key/tempo/meter:
- Current best seed:
- Keep:
- Change:
- Open decision:

**Next move**
I'll revise only [variable] and preserve [do-not-change item].
```

## Web research quick summary

Use after active web/reference research.

```md
**What I checked**
- Region/platform:
- Time window:
- Source types:

**Signals**
- High-confidence:
- Medium-confidence:
- Leads only:

**Composition translation**
- Groove:
- Harmony:
- Topline:
- Arrangement/form:
```
