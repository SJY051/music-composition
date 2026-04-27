# Constraint-Based Composition

Sometimes the most generative compositional approach is to *limit* yourself. Constraint-based composition deliberately restricts choices — to a few pitches, to a fixed pattern, to a procedural rule — and forces creativity to operate within the limits. This file covers the common constraint techniques: limited pitch sets, ostinato, ground bass, isorhythm, process-based composition, and other systematic approaches.

For sonata form's structural constraints, see `form/classical-forms.md`. For 12-tone and serial constraints (a specific kind of constraint), see `20th-century-techniques.md`. For variations as a constraint approach, see `theme-and-variation.md`.

## When to consult this file

- The user is stuck creatively and wants a structural prompt
- Composing with a limited pitch palette
- Working with ostinato, ground bass, riffs, or pedal points
- Process-based or procedural composition
- Algorithmic or generative approaches
- Pedagogical exercises in composition
- Why constraints often produce better music than complete freedom

## Why constraints help

Total freedom is often paralyzing. A blank page can produce decision fatigue: too many options, no anchor, nothing forcing the next move. Constraints force choices and provide structure.

Constraints also:

- **Generate unity**: limited materials force repetition and variation, creating coherence.
- **Drive invention**: when an obvious move is forbidden, the composer has to find a less obvious one.
- **Create style**: most musical "styles" are sets of constraints. Common-practice tonality forbids parallel 5ths; 12-tone forbids tonal-sounding intervals; pop typically forbids 11-bar choruses.
- **Reduce decision space**: fewer options means less time spent deciding, more time spent composing.

The discipline of constraint is a fundamental compositional tool, used by composers from Bach to Reich.

## Limited pitch palette

The simplest constraint: use only certain pitches.

### Single mode or scale

Compose within a specific mode (Dorian, Lydian, etc.) for an entire piece. The lack of "borrowed" chromaticism creates a unified modal flavor.

### Pentatonic

Use only the 5 pitches of a major or minor pentatonic. Many folk traditions use pentatonic or pentatonic-adjacent scales; name the specific tradition instead of treating Celtic, Asian, or African practices as interchangeable. Avoids the half-step intervals that create dissonance.

### A specific 4–6 note set

Choose a small set of pitches and use only them. Useful for atmospheric pieces; the limited palette creates a specific color.

### Pitch class set as basis

Choose a 4–7 note set and let it govern the piece's pitch content. Set theory provides the analytical framework.

Example: a piece based on the set {0, 1, 4, 6} (e.g., C, C♯, E, F♯) — every melodic and harmonic event uses pitches from this set or its transpositions/inversions.

## Ostinato (repeated figure)

A short pattern that repeats throughout a section or piece. The pattern is the constraint; the music happens "over" or "around" it.

### Types of ostinato

| Type | Description | Examples |
|------|-------------|----------|
| **Bass ostinato** | A repeating bass line | Pachelbel's Canon, Holst's "Mars" |
| **Rhythmic ostinato** | A repeating rhythmic pattern | Bolero (snare), Drumming (Reich) |
| **Melodic ostinato** | A repeating melodic figure | Many Phil Glass works |
| **Harmonic ostinato** | A repeating chord progression | Pop loops, jazz vamps |

### Ostinato as compositional constraint

The constraint of an ostinato forces the composer to:

- Vary other elements (melody, orchestration, texture) while the ostinato continues.
- Create interest through change *around* the constant.
- Choose carefully which moments break the ostinato (the break becomes structurally significant).

### Famous ostinato pieces

- Pachelbel's Canon — bass ostinato (D-A-Bm-F♯m-G-D-G-A) repeats throughout
- Ravel's Boléro — single rhythmic ostinato through entire piece
- Holst's "Mars, Bringer of War" — driving 5/4 ostinato
- Reich's "Drumming" — extended ostinato variations
- Most pop songs have an ostinato (the bass line; the chord loop)

## Ground bass and chaconne / passacaglia

A ground bass is a specific type of ostinato — a bass line that repeats while the upper voices vary.

The forms:

- **Passacaglia**: variations over a ground bass. The bass repeats; everything above varies.
- **Chaconne**: similar; sometimes distinguished from passacaglia by tempo or character (chaconne in 3/4, often slower; passacaglia variable). The distinction is loose; often used interchangeably.

### Compositional approach

1. Compose a ground bass — usually 4–8 bars, in a clear key, with strong harmonic implications.
2. Repeat it many times.
3. Compose variations over it, increasing in complexity, intensity, or contrapuntal interest.
4. Build to a climax in the late variations.
5. Conclude with a final variation that resolves.

### Famous examples

- Bach, Passacaglia and Fugue in C minor — masterpiece of the form
- Brahms, Symphony No. 4, finale (passacaglia on a Bach theme)
- Pärt, *Passacaglia* for violin
- Britten, *The Young Person's Guide to the Orchestra* (passacaglia at the end)

### In jazz and pop

Jazz "vamps" are essentially ground basses. A song over a 4-bar repeating chord progression is using the principle. Modal jazz pieces ("So What", "Maiden Voyage") have extended sections over a single chord — a kind of single-chord ground.

## Isorhythm

A medieval and modern technique. A pre-set rhythmic pattern (the *talea*) is repeated, and a pre-set melodic pattern (the *color*) is also repeated, but they have different lengths so they don't realign immediately.

The two cycles intersect over time. Each repetition of the talea matches different pitches from the color.

### Example

Talea: 8 rhythmic units (e.g., 8 measures of a pattern)
Color: 12 pitches

Each repetition of the talea has different pitches. They realign every 24 measures (lcm(8,12)).

### Modern uses

Some 20th-century composers (Messiaen, Carter, Boulez) used isorhythmic principles to organize complex rhythmic structures. The technique provides a way to generate variety from a small amount of pre-composed material.

## Process composition

A piece governed by a process — a procedural rule that determines how the material evolves.

Steve Reich's *Music for 18 Musicians* and earlier process pieces. Philip Glass's early operas. La Monte Young's drone work.

### Examples of processes

- **Phasing**: two voices play the same pattern; one slowly drifts faster (or slower) than the other, creating an evolving rhythmic relationship that returns to alignment after some duration.
- **Additive**: notes are added (or subtracted) one at a time over many bars.
- **Subtractive**: the inverse — start with all notes, gradually remove.
- **Permutation**: a fixed set of pitches reordered systematically.
- **Note-by-note transformation**: each note is replaced by a procedural rule (raise by 1 semitone, e.g.).

### Compositional approach

1. **Choose a starting state**: a pattern, a chord, a single note.
2. **Choose a process**: an explicit rule for how the state changes.
3. **Apply the process**: repeatedly, until the music has unfolded.
4. **Decide when to stop**: typically when the process completes (returns to starting state, fully transforms, exhausts options).

The discipline: don't cheat. The process is the composer; the composer's job is to set it up well.

### Famous process pieces

- Reich, *Piano Phase* (1967) — two pianos play the same pattern; one accelerates slightly until they're back in phase.
- Reich, *Drumming* (1971) — additive process; notes added one at a time.
- Reich, *Pendulum Music* (1968) — microphones swung over speakers, creating evolving feedback.
- Glass, *Music in Twelve Parts* — additive and modular processes.

## Aleatoric / chance constraints

Constraints that force chance to determine outcomes. See `20th-century-techniques.md` for full treatment. Briefly:

- **I Ching divination** (Cage): hexagrams determine pitch, duration, dynamic.
- **Limited choice**: performer chooses among options provided by composer.
- **Graphic notation**: visual scores that performers interpret freely.

These approaches use constraints (the score's structure, the rules of choice) to channel randomness toward specific aesthetic ends.

## Algorithmic composition

A modern extension. Music is generated (or partly generated) by computer algorithms. Constraints are expressed as code.

### Approaches

- **Stochastic**: random within constraints (Xenakis used this — *Pithoprakta* is built from probability distributions).
- **L-systems / fractal**: mathematical structures generating melodic/rhythmic patterns.
- **Markov chains**: each event determined by the previous N events.
- **Genetic algorithms**: musical "fitness" functions evolve material over generations.
- **Neural networks** (modern): trained on existing music, generate new material in similar style.

### Modern uses

Algorithmic composition is increasingly common in:

- Generative ambient music
- Game audio (procedural music)
- Modular synthesis
- Some contemporary classical (David Cope, Brian Eno's generative work)

## Other constraint techniques

### Pedal point

Holding a single pitch (often the tonic or dominant) while harmony changes above. The pedal acts as constraint — all subsequent harmony must work over the held pitch.

Common in:

- Classical (Bach's organ music)
- Jazz (vamps over a static bass)
- Rock (Hendrix-style sustained drone)
- Film scoring (atmospheric pads)

### Cantus firmus

A pre-existing melody (often a chant) that's used as the structural backbone of a new piece. The cantus is given; new material is composed against it.

Renaissance and Baroque practice. Modern composers occasionally borrow.

### Quotation and collage

Using existing music as raw material. Constraints come from the source — its harmony, rhythm, character. Modern composers (Ives, Schnittke, Adams) use quotation for specific aesthetic ends.

In pop and hip-hop, sampling is a quotation/collage technique with its own constraints.

### Forbidden intervals or motions

Common-practice counterpoint forbids parallel 5ths and 8ves; 12-tone composition forbids tonal-sounding intervals; some pop production forbids changing chord on weak beats. Each style has implicit constraints.

Composers can invent their own: "this piece will never use a perfect 5th"; "every phrase must end with a stepwise descent"; "no two consecutive notes can be the same".

The constraints themselves become part of the piece's character.

### Time/duration constraints

- **Fixed total duration**: write a piece exactly 4 minutes long.
- **Fixed section lengths**: every section must be 16 bars.
- **Equal duration**: all sections of equal length.

Useful for forcing density decisions.

### Single-instrument or limited-ensemble constraints

Composing for solo violin, or for a specific small ensemble (e.g., piano trio, woodwind quintet). The instrumentation forces idiomatic writing.

## When constraints help most

Constraints are most useful when:

- **The composer is stuck**. A new constraint can break a creative impasse.
- **The piece needs unity**. Limited materials produce coherence.
- **The piece needs character**. Specific constraints (modal, ostinato, etc.) create immediate recognizable identity.
- **Working in unfamiliar territory**. Constraints provide rules to follow when the composer doesn't yet have intuition for the style.
- **Pedagogically**. Composition exercises with constraints are excellent teaching tools.

## When constraints become limiting

Constraints can hurt when:

- **They override musical instinct**. If the constraint forces music that sounds wrong, abandon the constraint or modify it.
- **They become the point**. Sometimes a piece is "about" the constraint; if the constraint is interesting only to analysts and not to listeners, the piece may fail.
- **They prevent revision**. If you can't change the constraint, you can't fix problems that arise from it.

The skilled composer uses constraints as tools, not as commandments.

## Common pitfalls when advising

- **Don't impose constraints on music that doesn't want them.** Free, intuitive composition is also valid. Match approach to user's intent.
- **Don't make constraints arbitrary.** A constraint should produce a desired aesthetic result. "Use only pitches A, C♯, F" is a constraint; what does it accomplish?
- **Don't conflate constraint with structure.** Sonata form has constraints (key relationships, sectional functions) but is also a flexible structure. Constraint and structure interact but aren't identical.
- **Don't ignore the result.** A constraint that produces beautiful music is a good constraint. One that produces only academic exercises is less so.
- **Don't underestimate simple constraints.** "Two-chord vamp" or "single-pitch drone" sounds limiting but has produced extraordinary music (modal jazz, drone rock, much ambient).
- **Don't be precious about strict adherence.** Sometimes the best music comes from following a constraint mostly and breaking it at one strategic moment.

## A workflow for constraint-based composition

If the user is starting a piece using a constraint:

1. **Choose the constraint deliberately.** What aesthetic effect should it produce? What kind of music does it suggest?
2. **Test it briefly.** Write a few bars or a phrase. Does it produce sound that's interesting or that's awkward?
3. **Commit to it for a while.** The piece develops by exploring what's possible within the constraint.
4. **Notice what the constraint forces.** When the obvious move is unavailable, what alternatives appear? These are the discoveries.
5. **Decide whether to break it.** If the constraint is producing deadlocks, modify it. If a strategic break would create dramatic moment, plan it.
6. **Use the constraint structurally.** Often a piece can have multiple sections, each with its own constraint, creating contrast through constraint-shifts.

## Quick decision matrix

| Want | Try (constraint) |
|------|------------------|
| Unified modal feel | Single mode for entire piece |
| Folk/world feel | Pentatonic-only |
| Atmospheric, contemplative | 4–6 note set; pedal point |
| Driving, hypnotic | Ostinato over which other elements vary |
| Structural variations | Ground bass / passacaglia |
| Process unfolding | Phasing or additive process |
| Algorithmic generation | Markov chains, L-systems, generative grammar |
| Atonal coherence | Pitch-class set as governing material |
| Strict serial discipline | 12-tone row with limited transformations |
| Stuck creatively | Add an arbitrary constraint to break the deadlock |
| Pedagogical exercise | Forbid a common move (parallel 5ths, leap larger than 5th) |

## Cross-references

- 12-tone and serial constraints → `20th-century-techniques.md`
- Algorithmic / AI-assisted composition (algorithmic systems are constraint sets) → `algorithmic-and-AI-assisted.md`
- Microtonal pitch systems as compositional constraint → `microtonal.md`
- Theme-and-variation as a kind of constraint → `theme-and-variation.md`
- Ostinato in jazz (vamps) and pop (loops) → `../harmony/jazz-harmony.md`, `../genres/pop-rock.md`
- Modal composition → `../harmony/modal-harmony.md`
- Counterpoint as constraint-based composition → `../counterpoint.md`
- Form as constraint → `../form/classical-forms.md`, `../form/popular-song-forms.md`
- Process music in 20th-century context → `../genres/classical-periods.md`
- Production-side constraints (DAW, instrumentation) → `../production-aware/arrangement-for-mix.md`
