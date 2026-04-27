# Analysis

This file is about how to analyze music — to understand a piece's structure, harmony, melody, rhythm, form, and stylistic character. Analysis is a skill in itself, and good analysis requires a methodical approach: knowing what to look for, how to look for it, and what conclusions to draw.

This file complements the rest of the skill by focusing on the *receptive* side. The other files cover composition (creating); this file covers analysis (understanding). Many skills overlap, but the questions are different: instead of "what should I write", it's "what is happening in this music?"

## When to consult this file

- The user wants to analyze a specific piece
- "Why does this song work?" / "What's happening in this passage?"
- Reverse-engineering a piece to understand its techniques
- Comparative analysis of multiple pieces
- Pedagogical analysis (learning from existing music)
- "What style is this?" / "What period?"
- Form and key analysis

## Why analyze

Analysis serves several purposes:

1. **Learning**: understanding how master composers achieved their effects, then applying those techniques.
2. **Performance**: knowing what's structurally important in a piece informs how to play it.
3. **Composition**: analyzing pieces in your target style trains your ear and informs your own choices.
4. **Criticism**: explaining why a piece works or doesn't work requires analytical vocabulary.
5. **Theory**: building larger patterns from many analyzed pieces (genre conventions, period style).

The skilled analyst doesn't just describe what's there — they identify what *causes* the music's effect on the listener.

## A general analytical workflow

For any piece, work through (in roughly this order):

### 1. Listen first

Before reading the score or analyzing on paper:

- Listen multiple times.
- Identify what catches your ear: a melodic moment, a chord change, a rhythmic shift, a textural surprise.
- Form an emotional impression: what is this piece doing to the listener?
- Try to predict what comes next as the piece unfolds; notice when your predictions are confirmed or surprised.

Listening before analyzing prevents you from imposing theoretical frameworks that don't match the piece's actual effect.

### 2. Identify the genre / style / period

What kind of music is this?

- Period (Baroque, Classical, Romantic, modern, etc. — see `genres/classical-periods.md`)
- Genre (pop, jazz, hip-hop, etc. — see relevant `genres/*.md`)
- Sub-style within the genre

Style identification informs everything that follows. A "wrong note" in a Bach fugue is bad voice leading; a "wrong note" in a Coltrane solo might be deliberate altered tension.

### 3. Identify the form

Map the piece's sections.

For classical: sonata form, rondo, theme-and-variations, fugue, etc. (see `form/classical-forms.md`).

For popular: verse-chorus, AABA, blues, EDM build-and-drop, etc. (see `form/popular-song-forms.md`).

For each section, note:

- Length (in bars or seconds)
- Key area
- Rough character (loud/soft, dense/sparse, melodic/harmonic)
- Role in the larger structure (statement, contrast, development, return, etc.)

### 4. Identify the key(s)

What's the home key? Where does the music modulate? When?

For tonal music: trace the key plan. A sonata-form exposition typically goes I → V (or i → III); a development modulates broadly; the recapitulation returns to I throughout.

For modal music: identify the mode (Dorian, Phrygian, etc.).

For atonal music: there's no key, but there may be pitch-class set organization.

### 5. Identify the harmonic language

What kinds of chords are being used?

- Diatonic only?
- With secondary dominants?
- With modal mixture / borrowed chords?
- With chromatic mediants?
- With augmented sixths or Neapolitan?
- With jazz extensions and substitutions?

Harmonic vocabulary is a big indicator of period and style. Common-practice tonality has a specific vocabulary; jazz extends it; modal music avoids functional progressions; atonality abandons tonality.

### 6. Trace the melody

Identify the main melodic material:

- Themes and motifs
- Phrase structure (period, sentence, hybrid)
- Range and contour
- Climax position
- Use of chord tones vs. NCTs

For a piece that gets developed (sonata, fugue), trace how the melodic material is transformed across the piece.

### 7. Identify the rhythmic profile

- Time signature(s)
- Tempo
- Groove (swing, straight, syncopated)
- Rhythmic motifs
- Polyrhythm or hemiola
- Asymmetric phrases

### 8. Identify orchestration / instrumentation

What instruments are involved? How are they used? Which carries the melody, which the bass, which the chord, which color?

In recorded music: production choices count. Compression, reverb, EQ, sidechaining, etc.

### 9. Trace energy / dynamics

How does the piece's energy build and release? Where are the peaks? Where are the breaks?

Map the dynamic profile across the form. See `form/narrative-and-transitions.md`.

### 10. Identify what's distinctive

What makes this piece this piece? What's the "fingerprint"? Often this is:

- A recurring motif used in unusual ways
- A specific harmonic move (a key chord change, an unexpected modulation)
- A textural innovation
- A formal twist

The distinctive features are what make the piece memorable. Identifying them is the analytical payoff.

## Roman numeral analysis (RN)

The standard analytical notation for tonal music. See `fundamentals/notation-and-conventions.md` for full notation.

Quick reminders:

- Capital roman numerals = major chords (I, IV, V)
- Lowercase = minor (i, iv, v)
- ° = diminished
- + = augmented
- 7, 9, 11, 13 = chord extensions
- Inversions: 6 (first), 6/4 (second), 4/3 (third for 7th chord)
- Slashes: V/V = "V of V" (secondary dominant)

In analysis, write the roman numeral analysis below each chord on the score. This makes harmonic patterns visible.

### Common patterns to recognize

- **Cadences**: PAC (V-I), HC (ending on V), deceptive (V-vi), plagal (IV-I). See `assets/cadence-reference.md`.
- **Tonicization** (a brief move toward another key, then return): V/V → V → I.
- **Modulation** (a longer establishment of a new key): see `harmony/modulation.md`.
- **Sequence** (repeated harmonic pattern at different pitch levels).

## Schenkerian analysis (briefly)

Heinrich Schenker's system reduces a piece to its underlying voice-leading "skeleton". Useful for understanding how surface ornament relates to deep structure.

Key concepts:

- **Background**: the piece's most fundamental structure (e.g., I → V → I).
- **Middleground**: intermediate level showing the main harmonic events.
- **Foreground**: the actual notes of the piece.

Schenker analysis is sophisticated and specialized. For most analytical purposes, RN analysis is sufficient.

## Phrase analysis

Identify phrase boundaries (where one phrase ends and the next begins). Look for:

- Cadences (the most reliable indicator)
- Rests or sustained notes
- Tessitura changes
- Rhythmic resets

Then categorize the phrase structure (period, sentence, hybrid). See `melody/phrase-structure.md`.

## Motivic analysis

Identify motifs (recurring melodic-rhythmic units). For each motif:

- Where does it first appear?
- How is it varied / developed across the piece?
- Are different motifs combined?
- Is one motif the "main" motif, or are several equally important?

Trace motivic transformations: repetition, sequence, inversion, retrograde, augmentation, diminution, fragmentation. See `melody/motivic-development.md`.

## Genre-specific analytical priorities

Different genres reward different analytical focuses:

### Classical (Common Practice)

Focus on:

- Form (sonata, rondo, etc.)
- Key plan and modulation
- Roman numeral harmony
- Phrase structure (period, sentence)
- Motivic development
- Counterpoint (especially in fugue)
- Historical / stylistic context

### Jazz

Focus on:

- Form (32-bar AABA, blues, modal)
- Chord changes (often dense; extensions and substitutions)
- Soloist's lines (chord-scale relationships, motivic development across choruses)
- Harmonic substitutions (tritone subs, ii-V chains, reharmonizations)
- Rhythm (swing feel, time, microtiming)
- Comping and rhythm section interaction

### Pop / Rock

Focus on:

- Section structure (verse, chorus, pre-chorus, bridge)
- Hook identification (where, what, how often)
- Chord progressions (often simple; what makes them effective)
- Melodic identity (range, contour, climax)
- Production choices (what's the kick like? the vocal? the stereo image?)
- Lyric analysis

### Hip-hop

Focus on:

- Beat structure (drum pattern, sample, 808)
- Flow analysis (rapper's rhythm against the beat)
- Rhyme scheme
- Sample sources (where samples come from; how transformed)
- Production techniques

### EDM / Electronic

Focus on:

- Build-and-drop structure
- Bass design
- Sound design (synth choices, processing)
- Energy contour
- Repetition and variation in patterns

### Film score

Focus on:

- Themes (leitmotifs)
- Theme transformations across cues (how leitmotif varies with character/scene)
- Atmospheric vs. melodic cues
- Scene-music integration

## Comparative analysis

Comparing two or more pieces:

- What do they share? (Genre, key, structure, instrumentation)
- What's different? (Specific harmonic moves, melodic shapes, rhythmic feels)
- What does the comparison reveal? (E.g., comparing two Bach fugues reveals what's specifically Bach vs. specific to one fugue)

Comparative analysis is especially useful for understanding genre conventions: analyze 5–10 pieces in a genre to identify what they have in common.

## Common analytical mistakes

- **Imposing theoretical frameworks that don't fit the music.** Don't analyze a Coltrane solo with strict common-practice voice-leading rules. Match analytical method to musical style.
- **Confusing what's there with what's effective.** A piece may have technically correct counterpoint and still be boring. Analysis identifies what's there; aesthetic judgment is separate.
- **Ignoring context.** A piece by Mozart (Classical period) and a piece by Schoenberg (Modernist) cannot be compared as if their stylistic frameworks were identical.
- **Over-relying on Roman numerals.** RN analysis works for tonal music; it's awkward for modal, atonal, jazz, and pop.
- **Missing the forest for the trees.** Detailed harmonic analysis doesn't help if you've missed that the piece is in ABA form.
- **Conflating analysis with appreciation.** Knowing how a piece works doesn't mean liking it (or vice versa). Analysis serves understanding, not validation.
- **Forgetting the listener.** The point of analysis is usually to explain why the music *affects* the listener. If your analysis doesn't connect to listening experience, you've missed something.

## Quick analytical workflow checklist

For any piece, ask:

- [ ] What's the genre / period / style?
- [ ] What's the form? (Map the sections)
- [ ] What's the key plan?
- [ ] What's the harmonic language? (Diatonic? Chromatic? Modal? Jazz-extended?)
- [ ] What are the main melodic / motivic ideas? (Identify themes; trace development)
- [ ] What's the phrase structure? (Period? Sentence? Hybrid? Asymmetric?)
- [ ] What's the rhythmic profile? (Meter, tempo, groove, syncopation)
- [ ] What's the orchestration / texture? (Instruments; voicing; density)
- [ ] What's the dynamic / energy profile? (Builds, peaks, breaks)
- [ ] What's distinctive? What makes this piece this piece?

## Sample analysis: a Beatles song ("Yesterday")

To demonstrate the workflow:

- **Genre / period**: 1960s British pop; folk-influenced ballad
- **Form**: AABA with extra sections at the start and end. Roughly: A (verse) - A - B (bridge) - A - B - A
- **Key**: F major (with brief excursion to D minor in the bridge)
- **Harmonic language**: diatonic with secondary dominants and modal mixture (the iv chord — B♭m — borrowed from F minor)
- **Melodic ideas**: the iconic descending melodic motif (F-E-F over the line "Yesterday, all my troubles seemed so far away")
- **Phrase structure**: 7-bar phrases (asymmetric — most pop is 8-bar; the 7-bar phrase is part of the song's distinctive feel)
- **Rhythm**: simple 4/4, slow ballad tempo, swung subtly
- **Orchestration**: voice + acoustic guitar + string quartet (added in studio)
- **Energy**: gentle throughout; no big dynamic peaks
- **Distinctive**: 7-bar phrase length; the borrowed iv chord (B♭m) at "love was such an easy game to play" — this minor chord brings momentary darkness to a major-key song

This kind of analysis takes 10–20 minutes and reveals what makes the song special.

## Cross-references

- Cadences and harmonic vocabulary → `../assets/cadence-reference.md`, `harmony/functional-harmony.md`
- Roman numeral notation → `fundamentals/notation-and-conventions.md`
- Form templates (classical and popular) → `form/classical-forms.md`, `form/popular-song-forms.md`
- Phrase structure → `melody/phrase-structure.md`
- Motivic development → `melody/motivic-development.md`
- Genre / period identification → `genres/classical-periods.md`, other `genres/*.md`
- Jazz harmony for jazz analysis → `harmony/jazz-harmony.md`
- Modal harmony for modal analysis → `harmony/modal-harmony.md`
- 20th-century analytical techniques (set theory, etc.) → `techniques/20th-century-techniques.md`
- Workflow for the agent's own composition tasks → `workflow.md`
- Critique mode (analysis put to evaluative use) → `critique-and-feedback.md`
- Teaching mode (analysis as a pedagogical tool) → `teaching-composition.md`
