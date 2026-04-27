# Pitch, Intervals, and Scales

The foundational vocabulary for everything else in this skill. This file covers the default pitch grid used by most modern Western notation and instruments (12-tone equal temperament), how intervals are named and measured, and the scales — major, minor, modal, pentatonic, blues, symmetric, folk-derived, and non-diatonic — that organize pitch into usable material.

## When to consult this file

- The user asks about specific scales, intervals, or pitch material
- Questions like "what scale fits over Cm7", "what's an augmented 4th", "what's the difference between harmonic and melodic minor"
- Building a chord, melody, or progression and needing to verify pitch content
- Cross-checking enharmonic spelling

For chord construction from these intervals, see `harmony/chord-construction.md`. For the modes as harmonic frameworks, see `harmony/modal-harmony.md` and the cheatsheet `assets/modes-cheatsheet.md`. For scale formulas in compact reference form, see `assets/intervals-and-scale-formulas.md`.

## The pitch system

### 12-tone equal temperament (12-TET)

Most modern Western notation, DAWs, fixed-pitch instruments, and pop/jazz/classical teaching default to 12 equal divisions of the octave. Each division is a *semitone* (half-step). Twelve semitones = one octave; an octave = a frequency ratio of 2:1.

In 12-TET, every semitone is the same size: 2^(1/12) ≈ 1.0595 frequency ratio. This is a compromise — it makes every key equally available at the cost of slightly tempering pure intervals. Just intonation, meantone, well temperaments, and other historical/alternative systems can make some intervals or keys sound smoother and more characterful; modulation may change color, require retuning, or become limited depending on the system.

For composition purposes: the agent should treat 12-TET as the default and assume all intervals are equal-tempered unless the user specifies otherwise. Microtonal music, just intonation, and historical temperaments are out of scope for most situations but worth flagging if relevant.

### Octave equivalence

Notes one or more octaves apart are functionally the same pitch *class*. C4 (middle C) and C5 (an octave higher) are both "C". When discussing pitch material abstractly (scales, chords), we use pitch class names (C, D♭, F♯, etc.); when register matters, we use scientific pitch notation (C4, C5).

### The chromatic alphabet

12 pitch classes, written with 7 letters (A through G) plus accidentals (♯ for sharp, ♭ for flat). Most pitch classes have two enharmonic spellings:

| Pitch class | Common spellings |
|-------------|------------------|
| 0 | C, B♯, D𝄫 |
| 1 | C♯, D♭ |
| 2 | D, C𝄪, E𝄫 |
| 3 | D♯, E♭ |
| 4 | E, F♭, D𝄪 |
| 5 | F, E♯ |
| 6 | F♯, G♭ |
| 7 | G, F𝄪, A𝄫 |
| 8 | G♯, A♭ |
| 9 | A, G𝄪, B𝄫 |
| 10 | A♯, B♭ |
| 11 | B, C♭, A𝄪 |

(The 0–11 numbering is pitch-class numbering used in set theory and post-tonal analysis. Outside that context, just use letter names.)

### Enharmonic spelling — when it matters

A C♯ and a D♭ sound the same in 12-TET, but they imply different things. Spelling matters for:

- **Key context**: in D major, F♯ is correct; in C minor, G♭ would be wrong even though F♯ and G♭ are the same pitch.
- **Interval identity**: C–E♭ is a minor third; C–D♯ is an augmented second. They sound the same but function differently.
- **Voice leading**: a chromatic scale ascending should spell ♯ (C, C♯, D, D♯, E...) and descending should spell ♭ (C, B, B♭, A, A♭, G...).
- **Chord construction**: stack thirds for chords. So Cmaj7 is C–E–G–B, not C–E–G–C♭. The notes must be on every other letter.

When advising, use the spelling that matches the harmonic context. If the user is in E♭ major, write A♭ not G♯. If in B major, write D♯ not E♭.

## Intervals

An interval is the distance between two pitches. Measured by:

- **Size** (number): the number of letter names spanned. C–E is a third (C-D-E = 3 letters). C–F♯ is a fourth (C-D-E-F = 4 letters), even though it has a sharp.
- **Quality**: the precise distance in semitones, which determines whether the interval is major, minor, perfect, augmented, or diminished.

### Interval qualities — the table

For each size, there are possible qualities. The "perfect" qualities (P1, P4, P5, P8) are historically treated as a special consonance class in Western theory. Major/minor distinctions exist for the other sizes.

| Interval | Semitones | Examples (from C) | Notes |
|----------|-----------|-------------------|-------|
| P1 (perfect unison) | 0 | C–C | Same pitch |
| m2 (minor 2nd) | 1 | C–D♭ (or descending C–B) | Half-step |
| M2 (major 2nd) | 2 | C–D | Whole-step |
| m3 (minor 3rd) | 3 | C–E♭ | Defines minor chord |
| M3 (major 3rd) | 4 | C–E | Defines major chord |
| P4 (perfect 4th) | 5 | C–F | Open consonance |
| A4/d5 (augmented 4th / diminished 5th) | 6 | C–F♯ / C–G♭ | The tritone |
| P5 (perfect 5th) | 7 | C–G | Strongest consonance after octave |
| m6 (minor 6th) | 8 | C–A♭ | Inverts to M3 |
| M6 (major 6th) | 9 | C–A | Inverts to m3 |
| m7 (minor 7th) | 10 | C–B♭ | Inverts to M2 |
| M7 (major 7th) | 11 | C–B | Inverts to m2 |
| P8 (perfect octave) | 12 | C–C (next octave) | Octave equivalence |

Beyond an octave: compound intervals (9th = octave + 2nd, 11th = octave + 4th, 13th = octave + 6th). These are used in extended chord names.

### Augmented and diminished intervals

Any interval can be augmented (one semitone larger than its perfect or major form) or diminished (one semitone smaller than its perfect or minor form).

| Base interval | Augmented | Diminished |
|---------------|-----------|------------|
| P5 | A5 (8 semitones) — same sound as m6 | d5 (6 semitones) — the tritone |
| P4 | A4 (6 semitones) — the tritone | d4 (4 semitones) — same sound as M3 |
| M3 | A3 (5 semitones) — same sound as P4 | d3 (2 semitones) — same sound as M2 |
| m3 | (becomes M3) | d3 (same as above, from the minor side) |

The same pitch distance can have multiple names depending on the spelling. Six semitones can be A4 (e.g., C–F♯) or d5 (C–G♭) — the tritone. The two spellings imply different resolutions.

### Inversion of intervals

Invert an interval by flipping which note is on top. C–E (M3) inverts to E–C (m6). The rules:

- The two interval sizes always sum to 9 (the inverted M3 is a 6th, not a 5th — because we're now spanning E to the next C).
- Major inverts to minor (M3 → m6), minor to major (m6 → M3).
- Perfect inverts to perfect (P5 → P4).
- Augmented inverts to diminished (A4 → d5), diminished to augmented.

Useful for: voicing decisions (close vs. open), counterpoint, chord inversions.

### The tritone — the special interval

The augmented 4th / diminished 5th is exactly six semitones — the half-octave, the only interval that is its own inversion in 12-TET. It is often nicknamed *diabolus in musica* in later teaching lore, but avoid overstating this as a simple medieval ban; the practical point is its strong instability in tonal contexts.

Two tritones make an octave. The tritone is the most dissonant interval in the diatonic system and the engine of dominant-7th chord function — `V7` contains a tritone between the 3rd and ♭7th, which resolves inward (or outward) by half-step to the 3rd and root of `I`.

### Consonance / dissonance taxonomy

Western tradition broadly classifies intervals by stability:

| Class | Intervals | Use |
|-------|-----------|-----|
| Perfect consonances | P1, P5, P8; P4 by context | Stable goal intervals, but the 4th above the bass is treated as a dissonance in strict common-practice harmony |
| Imperfect consonances | M3, m3, M6, m6 | Stable in tonal context, expressive in melodic |
| Mild dissonances | M2, m7 | Resolution preferred but not always required |
| Sharp dissonances | m2, M7 | Demand resolution; create strong tension |
| Tritone (A4/d5) | The defining dissonance | Resolves outward (d5) or inward (A4) by half-step |

These are stylistic generalizations. In jazz, M7 over a tonic chord (Cmaj7) is consonant, not dissonant. In medieval music, the M3 was treated as imperfect. Context decides.

## Scales

A scale is an ordered set of pitches within an octave, defining the pitch material of a piece or section. Most scales are described by their interval pattern from the tonic.

### The major scale (Ionian mode)

Seven notes, formula `W W H W W W H` (whole-step, whole-step, half, whole, whole, whole, half).

C major: C D E F G A B
Scale degrees: 1 2 3 4 5 6 7

The major scale is the reference for everything else. When describing other scales as "major with X altered", the major scale is the baseline.

### The three minors

| Form | Formula | C example | Use |
|------|---------|-----------|-----|
| Natural minor | `W H W W H W W` (Aeolian mode) | C D E♭ F G A♭ B♭ | Modal/folk minor; no leading tone |
| Harmonic minor | `W H W W H Aug2 H` (raised ^7) | C D E♭ F G A♭ B | Functional minor; gives V chord a leading tone |
| Melodic minor | Ascending: `W H W W W W H` (raised ^6 and ^7); Descending: same as natural minor | Asc: C D E♭ F G A B; Desc: C B♭ A♭ G F E♭ D C | Smoother voice leading in lines |

In modern jazz, "melodic minor" usually refers to the ascending form used in both directions (called "jazz minor"). The classical convention (different ascending and descending) has fallen out of favor in jazz pedagogy.

### The seven diatonic modes

All built from the same 7-note set as the major scale, but starting on different degrees. Detailed discussion in `harmony/modal-harmony.md`; here's the formula reference:

| Mode | Formula from tonic | C version |
|------|--------------------|-----------|
| Ionian | `W W H W W W H` | C D E F G A B |
| Dorian | `W H W W W H W` | C D E♭ F G A B♭ |
| Phrygian | `H W W W H W W` | C D♭ E♭ F G A♭ B♭ |
| Lydian | `W W W H W W H` | C D E F♯ G A B |
| Mixolydian | `W W H W W H W` | C D E F G A B♭ |
| Aeolian | `W H W W H W W` | C D E♭ F G A♭ B♭ |
| Locrian | `H W W H W W W` | C D♭ E♭ F G♭ A♭ B♭ |

### Pentatonic scales

Five-note scales. The two most common are derived from the major and minor scales by removing semitones (^4 and ^7 in major; ^2 and ^6 in minor).

| Scale | Notes (C tonic) | Use |
|-------|-----------------|-----|
| Major pentatonic | C D E G A | Folk, country, gospel; safe over major chords |
| Minor pentatonic | C E♭ F G B♭ | Blues, rock; safe over minor chords |

Pentatonics are foundational because they avoid the half-step intervals that often create sharp clashes. In many pop, folk, rock, blues, and improvisational contexts, a pentatonic collection can sit over several related chords, but it still needs checking against the bass, chord quality, and melody target notes.

### The blues scale

Minor pentatonic + the ♭5 (the "blue note"). C blues scale: C E♭ F G♭ G B♭.

The ♭5 is a passing tone, not a stable pitch. The blues scale doesn't follow Western functional logic — it's a melodic palette superimposed on chords that may or may not contain its notes. Over a `C7` blues, the C blues scale clashes "correctly".

There are also major-blues variants (major pentatonic + ♭3 as a passing tone): C D E♭ E G A. Used in rockabilly, country, and major-mode blues.

### Modes of melodic minor (jazz minor)

A separate set of seven modes built from the ascending melodic minor scale. Each has a distinct character and is used over specific jazz chord types.

| Mode | Built on | Formula | Use over |
|------|----------|---------|----------|
| Melodic minor | ^1 | `W H W W W W H` | Cm(maj7) chords; Im(Δ) tonic in jazz minor |
| Dorian ♭2 | ^2 | `H W W W W H W` | iim7♭5 in some contexts |
| Lydian augmented | ^3 | `W W W W H W H` | Maj7♯5 chords; ambiguous, bright-tension color |
| Lydian dominant | ^4 | `W W W H W H W` | 7♯11 chords (non-resolving dominants) |
| Mixolydian ♭6 | ^5 | `W W H W H W W` | dom7 chords with ♭13 |
| Locrian ♮2 | ^6 | `W H W H W W W` | iiø7 chords |
| Altered (super Locrian) | ^7 | `H W H W W W W` | 7alt chords (resolving dominants with all alterations) |

The altered scale is the most-used by far in modern jazz — over `V7alt` resolving to `i`.

### Modes of harmonic minor

Less commonly used as full mode systems, but two are common as melodic palettes:

| Mode | Built on | Use |
|------|----------|-----|
| Harmonic minor (the parent) | ^1 | Tonic minor in classical and some jazz |
| **Phrygian dominant** | ^5 | Over V7♭9 chords resolving to minor; flamenco, Klezmer, metal |

The Phrygian dominant scale (C version: C D♭ E F G A♭ B♭) has a strongly marked augmented 2nd between ♭2 and 3 (D♭ to E here). It can suggest flamenco-adjacent, klezmer-adjacent, metal, or maqam-adjacent colors in Western equal temperament, but it is not a substitute for those traditions' full melodic, rhythmic, and intonational practices.

### Symmetric scales

Scales whose interval pattern repeats within the octave. They have no clear tonic — every note can be heard as the root.

| Scale | Formula | Notes (C version) | Use |
|-------|---------|-------------------|-----|
| Whole-tone | `W W W W W W` (6 notes) | C D E F♯ G♯ B♭ | Over 7♯5 / whole-tone dominant colors; B♭ is the dominant spelling of the enharmonic A♯ |
| Diminished (whole-half) | `W H W H W H W H` (8 notes) | C D E♭ F G♭ A♭ A B | Over diminished chords |
| Diminished (half-whole) | `H W H W H W H W` (8 notes) | C D♭ D♯ E F♯ G A B♭ | Over dominant ♭9 chords; D♯ is ♯9 over C7 |
| Chromatic | All 12 semitones | C C♯ D D♯ E F F♯ G G♯ A A♯ B | Passing material; serialism |
| Augmented | `A2 H A2 H A2 H` (6 notes) | C D♯ E G A♭ B | Coltrane changes; symmetric augmented sound (A2 = augmented 2nd, enharmonic to m3) |

### Non-diatonic and folk-derived scales (selected)

| Scale | Formula | Notes (C version) | Origin/use |
|-------|---------|-------------------|------------|
| Hungarian minor | `W H Aug2 H H Aug2 H` | C D E♭ F♯ G A♭ B | Hungarian folk, Romani |
| Byzantine / double harmonic | `H Aug2 H W H Aug2 H` | C D♭ E F G A♭ B | Greek, Middle Eastern |
| Bebop major | Major + ♯5 (or ♭6) added as passing | C D E F G A♭ A B | Bebop solo language |
| Bebop dominant | Mixolydian + natural 7 added | C D E F G A B♭ B | Bebop over dom7 |
| Bebop Dorian | Dorian + natural 3 added | C D E♭ E F G A B♭ | Bebop over m7 |
| Japanese (Hirajōshi) | `W H M3 H M3` | C D E♭ G A♭ | Pentatonic, Japanese traditional-adjacent color |

### Non-Western traditions — brief pointer

Many non-12-TET or tradition-specific pitch systems do not fit the default Western equal-tempered grid cleanly:

- **Indian classical** uses ragas — melodic frameworks that can include ascent/descent behavior, important tones, characteristic phrases, ornamentation rules, and intonational nuance.
- **Arabic / Turkish music** uses *maqam* / *makam* systems with characteristic pitch intonation, melodic pathways, ornaments, and modulations. Some tones fall between 12-TET semitones, but these traditions should not be reduced to a simple equal-quarter-tone grid.
- **Indonesian gamelan** uses 5-tone (slendro) and 7-tone (pelog) scales unrelated to 12-TET.
- **Sub-Saharan African** music uses scales that vary by tradition; some are pentatonic or hexatonic with regional inflections.

This skill is Western-music-focused. For non-Western collaboration, flag the limitation and recommend the user consult specialist resources or work with practitioners.

## Chord-scale defaults — a short reference

When improvising or composing a melodic line over a chord, these are the default scales to start from. (Full treatment in `harmony/jazz-harmony.md`.)

| Chord | Default scale |
|-------|---------------|
| Imaj7 (tonic in major) | Ionian or Lydian |
| Imaj7♯11 | Lydian |
| ii7 | Dorian |
| iiø7 (half-dim) | Locrian or Locrian ♮2 |
| iii7 | Phrygian or Aeolian |
| IV (major) | Lydian |
| IV7 (blues IV) | Mixolydian or Lydian dominant |
| V7 (resolving) | Mixolydian; for tension: altered, half-whole diminished, Phrygian dominant |
| V7♯11 (non-resolving) | Lydian dominant |
| vi7 | Aeolian or Dorian |
| vii°7 | half-whole diminished |
| Im(maj7) | Melodic minor |
| Im7 (modal) | Dorian |
| Imadd2 | Dorian or Aeolian |

## Common pitfalls when advising

- **Don't conflate enharmonic equivalents.** C♯ and D♭ sound the same but aren't always interchangeable; the spelling tells the player and reader what function the note plays.
- **Don't frame scales or traditions as novelty colors.** Whole-tone, octatonic, and various non-Western systems aren't oddities; they're legitimate organizing systems with their own logic.
- **Don't over-prescribe a scale per chord.** Improvisation often spans chord-scale relationships, and great solos violate "the right scale" constantly. Use chord-scale theory as a starting reference, not a cage.
- **Don't ignore ear training.** Telling a user "the second mode of melodic minor" is useless if they don't recognize the sound. Pair theory with audible examples ("it sounds like X piece").

## Cross-references

- Chord construction from interval stacking → `../harmony/chord-construction.md`
- The modes as harmonic systems (not just scales) → `../harmony/modal-harmony.md`
- Quick scale formula reference → `../assets/intervals-and-scale-formulas.md`
- Modes cheatsheet (formulas + characteristic chords) → `../assets/modes-cheatsheet.md`
- Chord-scale theory in jazz → `../harmony/jazz-harmony.md`
- Scales used in 20th-century non-tonal music → `../techniques/20th-century-techniques.md`
- Microtonal pitch systems beyond 12-TET (just intonation, EDOs, *maqam*, *raga*) → `../techniques/microtonal.md`
- Notation of accidentals, key signatures → `notation-and-conventions.md`
