# Musical Brainstorming

This file is for generating musical ideas with the user before the piece is fully defined. It is not generic project brainstorming. It treats musical ideas as playable materials: motives, grooves, progressions, textures, lyrical images, form arcs, instrumentation, constraints, and reference relationships.

Use this file when the user says things like:

- "I want to start a song but I don't know where to begin."
- "Let's brainstorm ideas."
- "Give me several directions for this chorus / cue / theme."
- "I have a mood but no musical material yet."
- "I'm stuck and need sparks."
- "Can we explore options before committing?"

For quick prompt cards, use `../../assets/musical-brainstorming-cards.md`. For session state and decision tracking, use `user-agent-collaboration.md` and `../../assets/session-brief-and-decision-log.md`.

## Core principle

Brainstorming is not the same as giving an answer. In brainstorming mode, the agent should create **possibility space** first, then help the user select and develop one path.

A useful loop:

```text
intent → seed → divergent options → quick audition → selection → focused development → next decision
```

Do not over-explain theory during the divergent phase. Give compact, playable options. Explanation comes after a candidate feels promising.

## The two modes: divergent and convergent

### Divergent mode

Goal: generate many distinct musical directions.

Good outputs:

- 6–12 short options
- contrasting directions, not tiny variants
- at least one safe option, one bold option, one strange option
- concrete musical material: chords, rhythm, scale degrees, texture, form move, lyric image

Bad outputs:

- one polished answer too early
- long theory lecture
- ten options that all mean the same thing
- options that cannot be played or tested quickly

### Convergent mode

Goal: choose, combine, simplify, or develop.

Good outputs:

- compare options by effect
- name trade-offs
- preserve the user's preference
- turn one sketch into 4–16 bars
- define the next small decision

Bad outputs:

- keep adding ideas forever
- erase the user's chosen direction
- solve everything at once

## First response pattern

When the user asks for brainstorming and gives little context, do not ask five questions. Ask **one useful question** or make a reasonable assumption and provide a starter board.

Good:

```text
Let's start broad. I'll assume contemporary pop unless you say otherwise. Here are eight starting points: two chord-first, two groove-first, two melody-first, one lyric-image first, and one weird texture-first idea.
```

Also good:

```text
Give me one anchor: genre, emotional target, or reference track. If you don't have one, I can start from mood alone.
```

Avoid:

```text
What key, tempo, instrumentation, genre, lyrical subject, target platform, vocal range, and reference tracks do you want?
```

## The minimum creative brief

A complete brief is nice, but brainstorming can start from only one of these:

| Seed type | Example | What the agent can generate |
|---|---|---|
| Emotion | lonely but not sad | mode, register, tempo, density, lyric images |
| Genre | J-pop chorus | form, tempo, rhythm, harmonic lift, topline shapes |
| Reference | "like the energy of X, not the melody" | craft-variable profile, safe transformations |
| Instrument | acoustic guitar | idiomatic voicings, strum/pick patterns, song shape |
| Lyric image | rain on a city street | motif, harmony color, texture, rhyme field |
| Rhythm | 6/8 but modern | groove options, phrase lengths, chorus lift |
| Constraint | only three chords | progression variants, bass motion, texture development |
| Function | boss battle loop | intensity states, loopable cells, transition stingers |

If none is given, start with 3 mood choices and 3 workflow choices.

## Brainstorming lenses

Use these lenses to make options genuinely different.

### 1. Harmony-first

Generate the emotional engine through chords.

Example output:

```md
1. Soft ache: | Cmaj9 | Em7 | Am9 | Fmaj7(#11) |
2. Darker lift: | Am | F | C/E | Gsus4 G |
3. Cinematic ambiguity: | C | Abmaj7 | Fm6 | Gsus4 |
```

Use when the user asks about mood, color, or a section transition.

Cross-references: `../harmony/functional-harmony.md`, `../harmony/modal-harmony.md`, `../harmony/chromatic-harmony.md`, `../harmony/reharmonization.md`.

### 2. Melody-first

Generate a memorable cell before chords.

Example output:

```md
Motif cell in C minor:
^5 - ^6 - ^5 - ^3 | ^4 - ^3 - ^2

Development options:
- repeat it one step higher
- answer it with longer notes
- compress it into a hook chant
```

Use when the user wants a theme, hook, topline, riff, or motif.

Cross-references: `../melody/melodic-construction.md`, `../melody/motivic-development.md`, `../songwriting/topline-craft.md`.

### 3. Rhythm/groove-first

Generate motion before pitch.

Example output:

```text
Kick: 1 . . a | 2 . & . | 3 . . a | 4 . & .
Snare/clap: 2 and 4
Hook rhythm: long-short-short, then a held note over barline
```

Use when the track feels stiff, the genre is groove-defined, or the user does not know the harmony yet.

Cross-references: `../rhythm-groove/groove-and-feel.md`, `../rhythm-groove/rhythmic-devices.md`.

### 4. Texture-first

Generate the sonic world through density, register, and timbre.

Example output:

```md
- Verse: one dry vocal + muted guitar pulses + sub on downbeats only
- Pre: add high ostinato + harmony pad widening every two bars
- Chorus: octave vocal doubles + open-hat pattern + bass becomes melodic
```

Use when the user describes atmosphere, cinematic feeling, or arrangement problems.

Cross-references: `../orchestration/arrangement-density.md`, `../orchestration/voicing-and-texture.md`, `../production-aware/energy-and-dynamics.md`.

### 5. Form/narrative-first

Generate the dramatic arc before details.

Example output:

```text
A. Slow reveal: intro → small verse → half chorus → larger verse → full chorus
B. Immediate hook: chorus tag intro → verse → pre → chorus → post-chorus
C. Spiral: 4-bar loop, each repeat adds one destabilizing element
```

Use when the user wants a whole piece, cue, game loop, musical theatre song, or section plan.

Cross-references: `../form/popular-song-forms.md`, `../form/narrative-and-transitions.md`, `../genres/game-music.md`, `../genres/musical-theatre.md`.

### 6. Constraint-first

Generate ideas by limiting choices.

Example constraints:

- only three chords
- melody must use five notes
- no downbeat chord changes
- bass moves stepwise only
- chorus hook must start before bar 1
- every section uses the same motive in a new rhythm
- no cymbals until the chorus
- only register changes, no new instruments

Use when the user is blocked, overwhelmed, or making generic choices.

Cross-references: `../techniques/constraint-based-composition.md`, `../techniques/theme-and-variation.md`.

### 7. Reference-triangulation

Use multiple references to avoid copying one track.

```text
Reference A = energy
Reference B = harmony density
Reference C = vocal phrasing
Your song = new melody, new lyrics, new form choices
```

Use when the user has taste but not a concrete composition direction.

Cross-references: `../research/reference-track-digging.md`, `../research/style-reference-and-copyright.md`, `../research/user-listening-context-and-streaming-services.md`.

## Brainstorming output formats

### Option board

Use for early-stage ideation.

```md
| Option | Core move | Effect | Try this now |
|---|---|---|---|
| 1. Warm ache | vi-IV-I-V with upper extensions | emotional but familiar | play in A minor at 78 BPM |
| 2. Floating | I-II-IV-I Lydian color | hopeful, less resolved | keep bass on tonic for two bars |
| 3. Tense cinematic | i-♭VI-iv-Vsus | darker pull | put ^5 on top of the first chord |
```

### Three-lane sketch

Use when the user wants contrasting directions.

```md
**Safe lane**: genre-native, immediately usable.
**Fresh lane**: one unusual move, still practical.
**Wild lane**: high-risk but inspiring.
```

### Seed pack

Use when the user just needs sparks.

```md
- Chord seed:
- Motif seed:
- Groove seed:
- Texture seed:
- Lyric/image seed:
- Form twist:
```

### Prototype card

Use after choosing an idea.

```md
Key:
Tempo:
Feel:
4-bar core:
Hook rhythm:
Arrangement entrance:
Main risk:
Next experiment:
```

## How to brainstorm without cloning references

When a reference track is involved, extract variables rather than surface signatures.

Allowed variables:

- tempo range
- energy arc
- groove family
- harmonic density
- topline contour type
- arrangement density
- broad production role, e.g., dry vocal vs. stacked vocal
- emotional function

Avoid copying:

- melody
- lyric phrases
- distinctive riff or bassline
- unique sample
- signature vocal identity
- producer tag
- exact arrangement sequence

If the user asks too directly for a living artist's style, route through `../research/style-reference-and-copyright.md`.

## Common brainstorming traps

| Trap | Symptom | Fix |
|---|---|---|
| Too many questions | user loses momentum | ask one anchor or start with assumptions |
| Too much theory | ideas feel academic | give playable material first |
| Too many options | user cannot choose | group into 3 lanes |
| Too safe | everything sounds generic | add one constraint or one contradiction |
| Too weird | nothing feels usable | keep form/groove stable while changing one variable |
| Premature polishing | energy dies before sketch exists | prototype first, refine later |
| Reference cloning | idea is too close to a track | triangulate 2–3 references, replace protected elements |
| Agent domination | user becomes passive | ask which option sparks and why |

## Working with different user types

### Beginner

Use plain language, fewer options, more concrete examples.

```text
Try this four-chord loop first. It works because the bass falls step by step, which usually feels natural and emotional.
```

### Advanced composer

Use denser variables and let them choose the axis.

```text
We can mutate the cell by inversion, metric displacement, or harmonic reinterpretation. Which axis do you want to stress?
```

### Producer / DAW-based writer

Use loop, section, density, and topline language. Avoid notation-heavy answers unless requested.

### Score-based composer

Use motive, register, orchestration, counterpoint, and form language.

### Lyric-first songwriter

Start with title, image field, vowel shape, and phrase length. Then attach melody/harmony.

## A default 20-minute brainstorming session

The agent can run this as a conversational pattern.

### Minute 0–2: brief

Ask one of:

- What emotion should the listener feel?
- What reference lane are we near?
- What section are we writing?

### Minute 2–6: option board

Generate 6–8 options across different lenses.

### Minute 6–8: user selection

Ask:

```text
Which two feel alive, even if they're not perfect?
```

### Minute 8–12: combine or contrast

Make two hybrids:

```text
A + C = stable groove, darker harmony
B + F = hook-first structure, stranger texture
```

### Minute 12–16: prototype

Create 4–8 bars of concrete material.

### Minute 16–20: next decision

Ask for one choice:

- develop chorus
- write verse contrast
- change key/tempo
- make it more idiomatic for instrument/voice
- generate lyrics/topline

## The "yes, and / no, but" revision rule

When the user reacts, translate their reaction into a musical direction.

| User reaction | Agent interpretation |
|---|---|
| "Too pretty" | add tension, reduce consonant extensions, roughen rhythm/timbre |
| "Too dark" | raise register, add major color, thin low density |
| "Too generic" | change bass, rhythm, phrase length, or one borrowed chord |
| "Too complicated" | reduce harmonic rhythm, fewer syncopations, simpler hook contour |
| "Not emotional enough" | stronger melodic appoggiatura, register peak, harmonic arrival |
| "Too close to reference" | preserve only one variable, replace melody/groove/form |

## Micro-prompts the agent can use

- "Give me three safe ideas and three reckless ideas."
- "What if the chorus starts with the hook before the downbeat?"
- "What if the bass tells the story instead of the chords?"
- "Make the verse smaller without making it boring."
- "Keep the same chords but change the emotional reading."
- "Write the wrong version first, then fix it."
- "Give me one idea that would work live and one that only works in production."
- "Turn this mood into a rhythm, not a chord."

## Cross-references

- Fast brainstorming cards → `../../assets/musical-brainstorming-cards.md`
- Session state and decision tracking → `user-agent-collaboration.md`, `../../assets/session-brief-and-decision-log.md`
- General agent workflow → `../workflow.md`
- Critique after a sketch exists → `../critique-and-feedback.md`
- Teaching mode → `../teaching-composition.md`
- Reference digging → `../research/reference-track-digging.md`
- Current web research → `../research/web-music-trend-research.md`
- Web search cheat sheet → `../../assets/web-search-cheatsheet.md`
