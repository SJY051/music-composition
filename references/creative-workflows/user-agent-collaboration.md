# User-Agent Collaboration Patterns

This file describes how the agent should collaborate with the user across an iterative composition session. It is about conversation design: keeping momentum, preserving decisions, making revisions legible, and turning the user's taste into musical choices.

Use this file when:

- the user wants to build a piece over multiple turns
- the user asks for brainstorming, then revision, then critique
- the user wants the agent to remember the current sketch inside the conversation
- the user is comparing options and needs a decision process
- the user asks for "workflow", "process", "let's develop this", or "help me finish it"

For idea generation specifically, use `musical-brainstorming.md`. For quick state templates, use `../../assets/session-brief-and-decision-log.md`.

## Collaboration stance

The agent should behave like a composition partner, not a replacement composer.

Good collaboration:

- keeps the user's aesthetic intent visible
- offers options before locking decisions
- explains trade-offs briefly
- preserves rejected ideas when they might be useful later
- tracks the current version of the sketch
- turns vague reactions into musical variables

Bad collaboration:

- repeatedly asks for the same information
- rewrites the entire piece when the user asked for a small change
- makes hidden assumptions about genre, vocal range, or instrumentation
- treats the first generated idea as final
- loses track of key, tempo, form, or the user's chosen option

## Session modes

Identify the current mode and answer accordingly.

| Mode | User signal | Agent behavior |
|---|---|---|
| Discovery | "I don't know what I want yet" | offer lanes, ask one anchor, avoid finality |
| Ideation | "Give me ideas" | generate option board, no long critique |
| Drafting | "Write a verse / chorus / cue" | provide concrete material and rationale |
| Revision | "Make it more X" | change one or two variables and show before/after |
| Diagnosis | "This doesn't work" | identify likely causes, prioritize fixes |
| Selection | "Which is better?" | compare against the user's stated goal |
| Polish | "Make it tighter" | small edits, idiom, prosody, playability, clarity |
| Learning | "Explain why" | teach the principle after the example |

If the mode changes, name it briefly:

```text
Cool — we're moving from ideation into revision. I'll keep the chorus concept and only change the harmonic rhythm.
```

## The project card

For multi-turn work, maintain a compact project card inside the conversation when useful.

```md
**Project card**
- Working title:
- Goal / mood:
- Genre frame:
- References:
- Key / tempo / meter:
- Current form:
- Chosen seed:
- Do-not-change:
- Open decisions:
```

Do not force the user to fill every field. Use it only when it helps the session stay coherent.

## The decision log

When the user chooses a direction, record it in plain language.

```md
**Decisions so far**
1. Keep the chorus in D minor, not F major.
2. Use the syncopated hook rhythm from Option B.
3. Avoid copying the reference's bassline; keep only its halftime energy.
```

This prevents the agent from undoing user choices later.

## Revision granularity

Before editing, decide the scale of change.

| Scale | When to use | Example |
|---|---|---|
| Micro | one chord, one note, one lyric stress | change bar 4 from G to G7sus4 |
| Phrase | 2–4 bars | rewrite the second half of the melody |
| Section | verse/chorus/bridge | create a contrasting chorus |
| Arrangement | instrumentation/density | keep chords, change energy arc |
| Concept | mood/genre/reference | reframe the whole song |

If the user asks for a small change, do not perform a concept rewrite.

## Before/after revision format

Use this for concrete edits.

```md
**Original**
| Am | F | C | G |

**Revision: more lift into chorus**
| Am | F | C/E | Gsus4 G |

**What changed**
- `C/E` makes the bass climb instead of reset.
- `Gsus4 G` creates a clearer pre-chorus release.
```

## A/B/C comparison format

Use this when the user is deciding.

```md
| Version | Strength | Risk | Best if you want... |
|---|---|---|---|
| A | immediate, familiar | predictable | radio-pop clarity |
| B | darker, more distinctive | less singalong | emotional tension |
| C | bold texture | may distract from lyric | a signature moment |
```

End by asking which trade-off matters most, not which is "correct".

## Taste extraction

When the user reacts emotionally, translate the reaction into variables.

| User phrase | Possible variable |
|---|---|
| "More expensive" | wider voicings, cleaner voice leading, fewer busy fills |
| "More intimate" | lower register, fewer layers, closer vocal rhythm |
| "More anthemic" | higher tessitura, longer notes, group-vocal-friendly hook |
| "More modern" | shorter intro, earlier hook, leaner loop, current groove/reference check |
| "More classic" | longer setup, live-band idiom, stable form, less abrupt editing |
| "More weird" | asymmetry, modal color, unexpected timbre, phrase displacement |
| "More emotional" | appoggiaturas, registral peak, stronger cadence or withheld cadence |

Always confirm the interpretation when ambiguity matters.

## Handling conflict between user goals

Users often want mutually tense things:

- familiar but not generic
- complex but catchy
- modern but timeless
- sad but uplifting
- genre-authentic but fresh
- reference-like but original

Turn the conflict into a design rule.

```text
Let's make the groove familiar and the harmony fresh.
```

```text
Let's keep the chorus catchy, but make the bridge harmonically stranger.
```

```text
Let's use the reference for energy only, not melody or bassline.
```

## Branching without chaos

When exploring multiple directions, label branches.

```md
**Branch A: intimate ballad**
- 72 BPM, piano, close vocal, vi-IV-I-V

**Branch B: glossy midtempo**
- 96 BPM, syncopated bass, brighter chorus lift

**Branch C: darker cinematic**
- 68 BPM, i-♭VI-iv-V, strings/pad texture
```

When the user chooses, retire or archive the others:

```text
We'll continue Branch B. I'll keep A and C as fallback ideas if the chorus needs contrast later.
```

## The "do-not-change" list

Before revising heavily, protect what the user likes.

```md
**Keep**
- the title phrase
- the descending bass in the verse
- the halftime chorus feel

**Change**
- pre-chorus length
- second line of melody
- final cadence
```

This is especially important when the user says, "I like this, but..."

## How to ask useful follow-up questions

Ask questions that unlock composition decisions.

Weak:

```text
What exactly do you want?
```

Better:

```text
Should the chorus feel bigger because the melody rises, because the chords brighten, or because the arrangement opens up?
```

Weak:

```text
What genre?
```

Better:

```text
Should the listener hear this as pop first, R&B first, or cinematic first?
```

Weak:

```text
Any references?
```

Better:

```text
Give me one reference for energy and one for vocal phrasing. They don't need to be the same genre.
```

## When not to ask a question

Do not ask a clarifying question if the user clearly wants momentum and the missing detail can be assumed safely.

Instead:

```text
I'll assume 4/4, midtempo, contemporary pop for this sketch. If you want jazz/EDM/film later, we can reframe it.
```

Good assumptions are reversible. Bad assumptions silently determine the whole piece.

## Keeping outputs playable

For every generated idea, provide at least one of:

- chord symbols
- Roman numerals
- scale degrees
- rhythm grid
- instrumentation/density instruction
- lyric line with stress marks
- form map
- register/tessitura note

Avoid abstract labels without material.

## User momentum protocols

### When the user is excited

Move forward. Do not slow down with a lecture.

```text
Great, let's develop that. I'll turn Option 3 into an 8-bar chorus and keep the pre-chorus unresolved.
```

### When the user is unsure

Reduce choices.

```text
Pick between these two: A is more singable, B is more distinctive.
```

### When the user is blocked

Use constraints.

```text
Let's write a bad version in 4 bars, then fix one thing at a time.
```

### When the user dislikes everything

Change the axis, not just the notes.

```text
The harmonic lane may be wrong. Let's try rhythm-first and texture-first ideas instead.
```

## Cross-references

- Musical brainstorming → `musical-brainstorming.md`
- Revision and feedback loops → `revision-and-feedback-loops.md`
- Session templates → `../../assets/session-brief-and-decision-log.md`
- Response formats → `../../assets/response-templates.md`
- Diagnostic tables → `../../assets/diagnostic-checklists.md`
- General workflow → `../workflow.md`
- Critique mode → `../critique-and-feedback.md`
- Reference digging → `../research/reference-track-digging.md`
- Style/copyright guardrails → `../research/style-reference-and-copyright.md`
