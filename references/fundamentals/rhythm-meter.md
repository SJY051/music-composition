# Rhythm and Meter

This file covers the time-domain fundamentals: note durations, time signatures, beat hierarchies, and tempo. It's the rhythmic counterpart to `pitch-intervals-scales.md`.

For rhythmic devices that *manipulate* the meter (syncopation, polyrhythm, hemiola, displacement), see `rhythm-groove/rhythmic-devices.md`. For groove and feel (microtiming, swing, pocket), see `rhythm-groove/groove-and-feel.md`. For odd meters and polymetric writing, see `rhythm-groove/odd-meters-polyrhythm.md`. For notation conventions specifically, see `notation-and-conventions.md`.

## When to consult this file

- The user asks about time signatures, note durations, tuplets
- "What's compound time", "what's 6/8 vs. 3/4"
- Tempo terminology, BPM ranges by genre
- Beat hierarchy, strong/weak beats
- Anacrusis (pickup notes), beaming, basic notation of rhythm

## Note durations

The standard durations and their fractions of a whole note:

| Name (US) | Name (UK) | Symbol | Fraction of whole note |
|-----------|-----------|--------|------------------------|
| Whole note | Semibreve | 𝅝 | 1 |
| Half note | Minim | 𝅗𝅥 | 1/2 |
| Quarter note | Crotchet | ♩ | 1/4 |
| Eighth note | Quaver | ♪ | 1/8 |
| Sixteenth note | Semiquaver | 𝅘𝅥𝅯 | 1/16 |
| 32nd note | Demisemiquaver | 𝅘𝅥𝅰 | 1/32 |
| 64th note | Hemidemisemiquaver | 𝅘𝅥𝅱 | 1/64 |

Each rest has the same duration as its corresponding note value.

### Dotted notes

A single dot adds half the value of the note:
- ♩. (dotted quarter) = ♩ + ♪ = 3 eighth notes
- 𝅗𝅥. (dotted half) = 𝅗𝅥 + ♩ = 3 quarter notes

A double dot adds half + a quarter (75% of the original):
- ♩.. = ♩ + ♪ + 𝅘𝅥𝅯 = 7 sixteenth notes

Dotted notes are essential for compound time signatures.

### Ties

Two notes of the same pitch connected by a curved line (the tie) sound as one continuous note with their durations summed. Use ties to:

- Cross a barline (the only way to write a duration that spans a barline)
- Express a duration that doesn't fit a single note value (e.g., 5 eighth notes = ♩ tied to ♩.)
- Visualize beats clearly even when a single longer note value would work

### Tuplets

A tuplet is a group of notes that fits into the time of a different number of notes. The most common:

| Tuplet | Notes | Plays in time of |
|--------|-------|------------------|
| Triplet | 3 | 2 of the same value (e.g., 3 eighth-note triplets in the time of 2 eighth notes = 1 quarter note) |
| Duplet | 2 | 3 of the same value (in compound time) |
| Quintuplet | 5 | 4 (sometimes 6) |
| Septuplet | 7 | 4, 6, or 8 |
| Sextuplet | 6 | 4 |

Triplets are by far the most common. Quintuplets and septuplets are common in modern classical, prog rock, and contemporary jazz.

## Time signatures

Two stacked numbers. The top number is the number of beats per measure; the bottom number is the note value that gets one beat (4 = quarter, 8 = eighth, 2 = half, 16 = sixteenth).

### Simple meters

The beat divides into 2. The top number indicates how many beats; the bottom indicates the beat value.

| Time sig | Beats per bar | Beat value | Notes |
|----------|---------------|------------|-------|
| 2/4 | 2 | quarter | March |
| 3/4 | 3 | quarter | Waltz, minuet |
| 4/4 | 4 | quarter | "Common time" — written `c`; the most common |
| 2/2 | 2 | half | "Cut time" — written `¢`; fast 2 feel |
| 3/8 | 3 | eighth | Fast 3-beat |

In simple meter, beat 1 is the strongest; subsequent beats are progressively weaker. In 4/4 the standard hierarchy is 1 (strongest) > 3 (medium-strong) > 2 = 4 (weak), with offbeats (the "and" of each beat) weakest.

### Compound meters

The beat divides into 3. The top number indicates the *total* number of subdivisions per bar; divide by 3 to get the actual beat count.

| Time sig | Subdivisions | Actual beats | Beat value | Notes |
|----------|--------------|--------------|------------|-------|
| 6/8 | 6 eighth notes | 2 dotted-quarter beats | dotted quarter | Lilting two-feel; jigs, ballads |
| 9/8 | 9 eighth notes | 3 dotted-quarter beats | dotted quarter | Three-feel with triplet division |
| 12/8 | 12 eighth notes | 4 dotted-quarter beats | dotted quarter | Slow blues, ballads, doo-wop |
| 6/4 | 6 quarter notes | 2 dotted-half beats | dotted half | Slower compound 2 |

In compound meter, count the actual beats (e.g., 6/8 is "ONE-and-a, TWO-and-a", not "1-2-3-4-5-6").

### How to tell simple vs. compound

A common point of confusion: 6/8 vs. 3/4. Both have 6 eighth notes per bar. The difference is grouping:

- 3/4: groups of two — 1-2 1-2 1-2 (three beats of two divisions each)
- 6/8: groups of three — 1-2-3 1-2-3 (two beats of three divisions each)

The stress pattern differs. 3/4 stresses every other eighth (♩|♪♪|♪♪|♪♪|); 6/8 stresses every third (♪|♪♪♪|♪♪♪|).

When converting between time signatures, the underlying *feel* matters more than the math.

### Asymmetric (irregular) meters

The top number is not divisible into clean groups of 2 or 3 — usually 5, 7, 11.

| Time sig | Common groupings | Examples |
|----------|------------------|----------|
| 5/4 | 3+2 or 2+3 | "Take Five" (Brubeck), "Mission: Impossible" |
| 5/8 | 3+2 or 2+3 | Some Eastern European folk |
| 7/4 | 4+3 or 3+4, sometimes 2+2+3 | Pink Floyd "Money", much progressive rock |
| 7/8 | 2+2+3 or 3+2+2 or 2+3+2 | Balkan music, prog rock, certain math rock |
| 11/8 | various — 3+2+3+3, etc. | Frank Zappa, Stravinsky, modern jazz |

The grouping isn't a fixed property of the time signature — it's a compositional choice that the composer indicates by beaming and accents. A 7/8 measure beamed as `2+2+3` feels different from `3+2+2`.

### Additive meters

Some pieces use a meter where each measure's grouping is explicitly written: `3+2+3/8`, `2+3+2/8`, etc. These come from Eastern European, Middle Eastern, and Indian traditions and from contemporary classical music. They make explicit what a 7/8 or 8/8 meter would only imply.

### Mixed meter

The time signature changes from bar to bar. Common in 20th-century classical (Stravinsky's "Rite of Spring" famously) and in progressive rock. The pattern can be:

- **Regular alternation**: 5/8 + 7/8 + 5/8 + 7/8 (a 12-beat composite cycle).
- **Through-composed**: each bar's meter is determined by the music, with no repeating pattern. Stravinsky, Carter, much of Schoenberg.
- **Cyclical patterns**: 5+5+5+5+7 (a 27-beat cycle, common in Middle Eastern dance forms).

### Irrational meters

A time signature whose lower number isn't a power of 2: 4/12, 3/10, etc. The denominator implies tuplet relationships at the bar level. Used in modern classical (Ferneyhough, Adès) and rarely elsewhere.

## Beat hierarchy

Within a measure, beats have varying strength. The hierarchy:

1. **Downbeat** (beat 1): strongest. Marks the start of a measure.
2. **Strong beats**: in 4/4, beats 1 and 3. In 3/4, beat 1.
3. **Weak beats**: in 4/4, beats 2 and 4. In 3/4, beats 2 and 3.
4. **Off-beats** (subdivisions between beats): weaker still. The "and" of a beat is weaker than the beat itself.
5. **Off-off-beats** (further subdivisions): even weaker.

This hierarchy creates expectation. Music plays with it by:

- **Confirming the hierarchy**: putting strong content on strong beats. Default, most music.
- **Crossing it (syncopation)**: putting accents or emphasis on weak beats and off-beats. Most pop, R&B, jazz, hip-hop.
- **Suspending it (rubato)**: stretching/compressing time so the beat hierarchy becomes flexible. Romantic music, ballads.
- **Violating it dramatically**: hemiola (3 against 2), polyrhythm. See `rhythm-groove/rhythmic-devices.md`.

## Tempo

Tempo is the rate at which beats pass. Measured in BPM (beats per minute). Italian terms historically described tempo with associated character; modern scores often combine the two.

### Italian tempo terms

Roughly slow to fast. Approximate BPM ranges (for ♩ — quarter note in simple meter):

| Term | BPM | Character |
|------|-----|-----------|
| Larghissimo | < 24 | Extremely slow |
| Grave | 25–45 | Very slow, solemn |
| Largo | 40–60 | Broad, slow |
| Lento | 45–60 | Slow |
| Adagio | 55–75 | Slow, leisurely |
| Adagietto | 65–80 | A little faster than adagio |
| Andante | 75–110 | Walking pace |
| Andantino | 80–110 | Slightly faster than andante (sometimes slower; ambiguous) |
| Moderato | 108–120 | Moderate |
| Allegretto | 110–125 | Fairly fast |
| Allegro | 120–168 | Fast, lively |
| Vivace | 168–176 | Very fast, vivacious |
| Presto | 168–200 | Very fast |
| Prestissimo | > 200 | Extremely fast |

These are guidelines; actual BPM varies by style and editor. A "slow allegro" might be 115; a "fast allegro" might be 145.

### Tempo modifiers

| Term | Meaning |
|------|---------|
| poco | a little |
| molto | very |
| meno | less |
| più | more |
| ma non troppo | but not too much |
| assai | quite, rather |

So "allegro ma non troppo" = "fast but not too much"; "molto adagio" = "very slow".

### Tempo changes

| Term | Meaning |
|------|---------|
| accelerando (accel.) | gradually faster |
| ritardando (rit. / ritard.) | gradually slower |
| rallentando (rall.) | gradually slower (more abrupt than ritardando) |
| stringendo | hurrying, urgently faster |
| allargando | broadening (slower with widening dynamics) |
| a tempo | return to the original tempo |
| tempo primo (tempo I) | return to the first tempo of the piece |
| rubato | flexible tempo, "stolen time" |

Tempo changes can be written as ranges (`accel. al ♩=140`) or left to performer discretion (`accel. poco a poco`).

### Tempo by genre — rough table

Use these as starting points; significant variation exists within each genre.

| Genre | BPM range | Typical |
|-------|-----------|---------|
| Slow ballad / chillout | 60–80 | 70 |
| Hip-hop (modern) | 80–95 | 85 |
| Hip-hop (boom-bap, classic) | 85–95 | 90 |
| Trap / drill | 130–160 (counted in halftime as 65–80) | 140/70 |
| Lo-fi hip-hop | 70–85 | 75 |
| Reggae | 60–90 | 75 |
| Bossa nova | 120–140 | 130 |
| Jazz ballad | 60–85 | 70 |
| Jazz medium swing | 120–160 | 140 |
| Jazz uptempo | 200–300+ | 240 |
| Pop ballad | 60–80 | 70 |
| Modern pop | 100–130 | 115 |
| Disco | 110–135 | 120 |
| Funk | 95–130 | 105 |
| Rock (mid-tempo) | 110–130 | 120 |
| Rock (uptempo) | 130–160 | 145 |
| Punk / hardcore | 160–250 | 180 |
| Country | 80–130 | 110 |
| House | 118–135 | 124 |
| Techno | 120–140 | 130 |
| Trance | 130–150 | 138 |
| Drum and bass / jungle | 160–180 | 174 |
| Dubstep | 138–142 (often counted in halftime) | 140 |
| Hardcore / gabber | 160–250+ | 200 |
| K-pop | 90–135 | 115–120 (varies wildly) |
| J-pop | 100–145 | 120 |
| Anime opening | 130–180 | 150 |
| Film score (action) | 120–180 | 140 |
| Film score (drama) | 60–100 | 75 |
| Trailer music | 70–90 (often half-time) | 80 |
| Musical theatre | 60–160 | varies by song type |
| Ambient | 50–80 (or no clear pulse) | 65 |

The same genre can be written at different tempos for different effects. K-pop ballads often live at 70–90 BPM; K-pop dance tracks at 120–135.

## Anacrusis (pickup notes)

A note (or notes) before the first downbeat of a piece or phrase. The first full measure starts on the next downbeat; the anacrusis "borrows" time that's compensated by the final measure being short.

In notation: the pickup measure and the final measure together equal one full bar. So a piece in 4/4 with a one-beat pickup would have a final measure of 3 beats.

Anacrusis is essential to many vocal styles — phrases that begin on weak beats and resolve to downbeats feel more conversational and forward-leaning than phrases that always start on downbeats.

## Beaming conventions

Beaming groups together notes shorter than a quarter note (eighth, sixteenth, etc.) to clarify beat structure. Default beaming groups together notes within a beat:

- 4/4: beam eighth notes in pairs (one beat at a time), or all four together if it makes sense as a group
- 6/8: beam eighth notes in groups of three (one compound beat at a time)
- 7/8 (2+2+3): beam in groups of 2+2+3
- 7/8 (3+2+2): beam in groups of 3+2+2

Beaming explicitly tells the player how to count the bar. Misleading beaming is one of the most common notation errors. When in doubt, beam by beat.

For vocal music, beaming traditionally followed the syllable (one note per syllable was beamed alone; melismas were beamed together). Modern vocal scores often use instrumental beaming for readability.

## Common pitfalls when advising

- **Don't confuse 3/4 and 6/8.** They look similar, sound different. The grouping is the issue, not the count.
- **Don't assume one tempo for a genre.** Ranges are wide; the same genre at different tempos has different character.
- **Don't ignore the relationship between tempo and density.** A passage that works at 120 BPM with sixteenth notes will be unreadable at 200 BPM. Match note values to tempo.
- **Don't write asymmetric meters without indicating grouping.** A 7/8 piece needs to communicate whether it's 2+2+3, 3+2+2, or 3+4. The reader can't guess.
- **Don't use rubato as a default.** Rubato is a specific expressive device. Most music wants a steady tempo.
- **Don't rely on Italian terms alone.** Modern scores typically include a BPM marking (`♩=120`) alongside or instead of "Allegro" because the term is too vague.

## Cross-references

- Notation specifics (clefs, key signatures, dynamics, articulations) → `notation-and-conventions.md`
- Rhythmic devices (syncopation, hemiola, displacement) → `rhythm-groove/rhythmic-devices.md`
- Groove and feel (swing, microtiming, pocket) → `rhythm-groove/groove-and-feel.md`
- Odd meters and polyrhythm → `rhythm-groove/odd-meters-polyrhythm.md`
- Phrase structure and how rhythm interacts with phrase boundaries → `melody/phrase-structure.md`
- Tempo conventions in genre context → various `genres/*.md` files
