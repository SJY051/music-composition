# Scale-Degree Spelling Cheatsheet

Use this asset when the agent needs to spell chords, Roman numerals, modes, altered tensions, or borrowed chords clearly. The goal is not only to name the pitch class, but to spell the musical function.

## Core rule

Spell notes by **scale degree function** first, enharmonic convenience second. C♯ and D♭ may be the same piano key, but they usually mean different things.

## Major key Roman-numeral spelling from C

| Roman numeral | Chord | Notes | Why |
|---|---|---|---|
| `I` | C | C E G | tonic triad |
| `ii` | Dm | D F A | diatonic supertonic minor |
| `iii` | Em | E G B | diatonic mediant minor |
| `IV` | F | F A C | diatonic subdominant major |
| `V` | G | G B D | diatonic dominant major |
| `vi` | Am | A C E | diatonic submediant minor |
| `vii°` | Bdim | B D F | leading-tone diminished triad |
| `♭II` | D♭ | D♭ F A♭ | lowered supertonic, not C♯ major |
| `♭III` | E♭ | E♭ G B♭ | borrowed lowered mediant |
| `♯iv°` | F♯dim | F♯ A C | raised subdominant leading to V or as common-tone color |
| `♭VI` | A♭ | A♭ C E♭ | borrowed lowered submediant |
| `♭VII` | B♭ | B♭ D F | borrowed lowered leading-tone/subtonic chord |

## Minor key Roman-numeral spelling from A minor

| Roman numeral | Chord | Notes | Why |
|---|---|---|---|
| `i` | Am | A C E | tonic minor |
| `ii°` | Bdim | B D F | diatonic supertonic diminished in natural minor |
| `III` | C | C E G | diatonic lowered mediant |
| `iv` | Dm | D F A | subdominant minor |
| `v` | Em | E G B | natural-minor dominant minor |
| `V` | E | E G♯ B | harmonic-minor raised leading tone |
| `VI` | F | F A C | diatonic lowered submediant |
| `VII` | G | G B D | subtonic major |
| `vii°` | G♯dim | G♯ B D | leading-tone chord to i |

## Secondary dominants in C major

| Function | Chord | Notes | Resolution target |
|---|---|---|---|
| `V/V` | D | D F♯ A | G |
| `V7/V` | D7 | D F♯ A C | G |
| `V/ii` | A | A C♯ E | Dm |
| `V7/ii` | A7 | A C♯ E G | Dm |
| `V/vi` | E | E G♯ B | Am |
| `V7/vi` | E7 | E G♯ B D | Am |
| `V/IV` | C7 | C E G B♭ | F |

Raised notes usually create leading tones to the target chord. Spell them as sharps when they resolve upward by half step: F♯→G, C♯→D, G♯→A.

## Borrowed chords in C major

| Borrowed chord | Notes | Source color |
|---|---|---|
| `iv` = Fm | F A♭ C | parallel minor |
| `♭VI` = A♭ | A♭ C E♭ | parallel minor |
| `♭VII` = B♭ | B♭ D F | Mixolydian / parallel minor rock-pop color |
| `♭III` = E♭ | E♭ G B♭ | parallel minor / modal mixture |
| `iiø7` = Dm7♭5 | D F A♭ C | parallel minor pre-dominant |
| `Ger⁶` | A♭ C E♭ F♯ | augmented-sixth predominant to G |

The German augmented sixth in C uses A♭ and F♯ because the voice-leading expands outward to G, not because the chord is simply an A♭7 in all contexts.

## Modal spelling from C tonic

| Mode | Characteristic degree | Notes |
|---|---|---|
| C Dorian | ♮6 against minor third | C D E♭ F G A B♭ |
| C Phrygian | ♭2 | C D♭ E♭ F G A♭ B♭ |
| C Lydian | ♯4 | C D E F♯ G A B |
| C Mixolydian | ♭7 | C D E F G A B♭ |
| C Aeolian | ♭6 and ♭7 | C D E♭ F G A♭ B♭ |
| C Locrian | ♭2 and ♭5 | C D♭ E♭ F G♭ A♭ B♭ |

Spell C Lydian with F♯, not G♭, because the note functions as raised ^4.

## Altered dominant tensions from E

| Tension over E7 | Pitch | Why |
|---|---|---|
| ♭9 | F | lowered ninth above E |
| ♯9 | G | raised ninth above E; enharmonic to minor third, but not labeled ♭3 in dominant context |
| ♯11 / ♭5 | A♯ / B♭ | use A♯ for ♯11, B♭ for ♭5 |
| ♭13 / ♯5 | C / B♯ | use C for ♭13, B♯ only when the raised-fifth spelling matters |

The common E7alt pitch set often includes E, G♯, D, plus some of F, G, A♯/B♭, and C. Do not label A♯ as ♯9 over E.

## Spelling decision table

| Situation | Prefer | Example |
|---|---|---|
| leading tone to a chord tone | sharp spelling | F♯ resolves to G in `V/V` |
| lowered borrowed scale degree | flat spelling | A♭ in `iv` or `♭VI` in C major |
| raised modal degree | sharp spelling | F♯ in C Lydian |
| lowered modal degree | flat spelling | B♭ in C Mixolydian |
| altered dominant ♯9 | raised ninth label | E7♯9 uses G natural |
| augmented sixth voice-leading | outward-resolving spelling | A♭ and F♯ resolve to G |
| slash-bass inversion | actual bass pitch | C/E, G/B |

## Common mistakes to avoid

- Do not spell `♭II` in C as C♯ major.
- Do not spell C Lydian as C D E G♭ G A B.
- Do not label E–A♯ as a ♯9; it is ♯11 / ♭5 territory.
- Do not flatten or sharpen letters mechanically without checking scale-degree function.
- Do not treat Roman numerals as fixed chord names; they depend on the key.

## Cross-references

- Intervals and scale formulas → `intervals-and-scale-formulas.md`
- Modes cheatsheet → `modes-cheatsheet.md`
- Chord symbol ambiguity → `chord-symbol-ambiguity-and-parsing.md`
- Functional harmony → `references/harmony/functional-harmony.md`
- Chromatic harmony → `references/harmony/chromatic-harmony.md`
- Modulation → `references/harmony/modulation.md`
