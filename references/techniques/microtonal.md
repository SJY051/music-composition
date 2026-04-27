# Microtonal and Xenharmonic Music

This file covers composing with pitch systems outside of 12-tone equal temperament (12-TET) — the assumed default of Western music since roughly the 19th century. Microtonal music uses intervals smaller than the semitone; xenharmonic music more broadly is anything that doesn't fit the 12-TET grid, including just intonation, equal divisions of the octave other than 12, non-octave-repeating systems, and historical temperaments.

These traditions are not new — most of the world's music is microtonal in some sense, and Western art music used unequal temperaments for most of its history. The "xenharmonic" framing is a modern composer's perspective that treats 12-TET as one option among many, not as a default.

This file complements `../fundamentals/pitch-intervals-scales.md` (basic pitch and scale theory) and `../harmony/modal-harmony.md` (modal systems, some of which require microtonal pitch). For Korean traditional ornamentation that includes microtonal inflections, see `../genres/korean-traditional.md`. For non-Western pitch systems generally, see `../genres/folk-roots-and-traditions.md`.

## When to consult this file

- Composing in just intonation, equal divisions other than 12-TET, or other tunings
- Working with traditions that use non-12-TET pitch (Indian classical, Arabic *maqam*, Indonesian *gamelan*, Persian *dastgah*, much non-Western music)
- Writing music with quarter-tone or smaller pitch inflections
- Composing for instruments that can produce microtones (strings, woodwinds, brass, voice, fretless instruments, electronic instruments, retuned digital instruments)
- Historical performance practice (mean-tone, well-tempered, just intonation)
- Spectralism (pitch derived from harmonic spectra)

## Why microtones?

Three broad motivations:

1. **Acoustic / physical**: 12-TET is a compromise. Just-intonation intervals (small whole-number ratios) have a sonic clarity that 12-TET approximations lack. A pure 5:4 major third (about 14 cents flat of 12-TET) sounds noticeably different.

2. **Cultural / traditional**: most non-Western traditions use pitch systems that don't fit 12-TET. To work authentically in Indian classical, Arabic, Persian, Turkish, or many other traditions, microtonal pitch is non-negotiable.

3. **Expressive / new**: some modern composers explore microtonality for the new musical possibilities it opens — pitch combinations and progressions impossible in 12-TET.

The composer's question is rarely "should I use microtones?" in the abstract; it's "is the music I want to make accessible only through pitch outside 12-TET, or is 12-TET sufficient?"

## Cents — the universal currency

Pitch differences across tuning systems are measured in **cents**: 100 cents per 12-TET semitone, 1200 cents per octave. Cents are logarithmic, so equal cent-differences are equal-sounding pitch ratios.

| Cents | Meaning |
|-------|---------|
| 0 | Same pitch |
| 5–10 | Barely audible difference (within tuning tolerance) |
| 14 | Just-intonation major 3rd (5:4) compared to 12-TET (deviation: 14 cents flat) |
| 22 | Pythagorean comma — the gap between 12 perfect fifths and 7 octaves |
| 50 | Quarter-tone (half a semitone) |
| 100 | One semitone |
| 200 | One whole tone |
| 1200 | Octave |

Cents notation is the standard way to specify exact pitch in microtonal contexts. "C +14¢" means C, 14 cents sharp.

## Just intonation

Just intonation (JI) tunes intervals as small whole-number ratios. The simplest:

| Interval | Ratio | Cents | 12-TET equivalent |
|----------|-------|-------|-------------------|
| Unison | 1:1 | 0 | 0 |
| Octave | 2:1 | 1200 | 1200 (exact) |
| Perfect 5th | 3:2 | ~702 | 700 (12-TET ~2¢ flat) |
| Perfect 4th | 4:3 | ~498 | 500 (12-TET ~2¢ sharp) |
| Major 3rd | 5:4 | ~386 | 400 (12-TET 14¢ sharp) |
| Minor 3rd | 6:5 | ~316 | 300 (12-TET 16¢ flat) |
| Major 6th | 5:3 | ~884 | 900 (12-TET 16¢ sharp) |
| Minor 6th | 8:5 | ~814 | 800 (12-TET 14¢ flat) |
| Major 2nd (Pythagorean) | 9:8 | ~204 | 200 (12-TET 4¢ flat) |
| Major 2nd ("just") | 10:9 | ~182 | 200 (12-TET 18¢ sharp) |
| Harmonic 7th | 7:4 | ~969 | 1000 (12-TET 31¢ sharp) |
| Septimal minor 3rd | 7:6 | ~267 | 300 (12-TET 33¢ sharp) |

The deeper ratios (using prime numbers 7, 11, 13) sound increasingly unfamiliar to ears accustomed to 12-TET. The 7:4 "harmonic 7th" — 31¢ flatter than the 12-TET minor 7th — has a particular blues-like or "leaning" quality.

### The comma problem

Just intonation has a structural problem: you can't tune a 12-note keyboard such that every interval is just. Different paths between two pitches yield different exact frequencies (because 5/4 × 5/4 ≠ 25/16 ≠ 8/5).

Three responses to this problem:

1. **Just intonation, restricted**: tune the keyboard for one tonal center; modulation breaks the system. La Monte Young, Harry Partch, Ben Johnston work this way (Partch built a 43-tone scale and his own instruments).
2. **Adaptive just intonation**: an electronic instrument or a vocal ensemble re-tunes on the fly to keep each chord just. Difficult for keyboard instruments; natural for voices and strings.
3. **Temperament**: distribute the comma errors across many intervals, sacrificing pure ratios for usability across all keys. This is what 12-TET does — every interval slightly off, but every key equally usable.

## Equal divisions of the octave (EDOs)

Equal divisions of the octave divide the octave into N equal cents-steps. 12-TET is 12-EDO (12 equal divisions, 100 cents each). Other EDOs:

| EDO | Step size | Notable for |
|-----|-----------|-------------|
| 5-EDO | 240¢ | Indonesian *slendro* gamelan (approximate) |
| 7-EDO | ~171¢ | Thai traditional tuning (approximate); also resembles a "perfectly equalized" diatonic scale |
| 12-EDO | 100¢ | Western standard |
| 17-EDO | ~71¢ | Approximates Pythagorean tuning; popular in xenharmonic experimentation |
| 19-EDO | ~63¢ | Better approximations of just-intonation thirds than 12-TET; meantone-like properties |
| 22-EDO | ~55¢ | Sruti-related (Indian classical theory) |
| 24-EDO | 50¢ | Quarter-tone system; standard in modern Arabic and some Western avant-garde notation |
| 31-EDO | ~39¢ | Excellent JI approximations; popular in microtonal communities |
| 53-EDO | ~23¢ | Almost-perfect Pythagorean and just intervals; approximates Turkish *koma* |
| 72-EDO | ~17¢ | Used by Joe Maneri, some jazz microtonal applications |

Each EDO has its own "modal" possibilities. In 19-EDO, for instance, there are scales that have no analogue in 12-TET but feel internally consistent. In 31-EDO, many just intervals are within a few cents of an EDO step, making 31-EDO a strong "everyday" microtonal option.

## Quarter-tones — the modest microtonal step

The most common microtonal extension of 12-TET is the addition of quarter-tones — pitches halfway between adjacent semitones, at 50¢ intervals. This gives 24-EDO when applied uniformly.

Quarter-tones are central to:
- **Modern Arabic music**: *maqam* scales use quarter-tone-related intervals (though traditional Arabic intervals are not exactly 24-EDO; they're closer to specific just-intonation tunings)
- **Avant-garde Western**: Charles Ives, Alois Hába, Iannis Xenakis, Ligeti, Pierre Boulez
- **Spectral music**: Gérard Grisey, Tristan Murail, Kaija Saariaho
- **Persian / Turkish music**: traditions use scales with quarter-tone-like intervals (though the actual tuning is more nuanced)

### Notation conventions for quarter-tones

| Symbol | Meaning |
|--------|---------|
| ♯ (sharp) | +100¢ |
| ♮ (natural) | natural |
| ♭ (flat) | −100¢ |
| ♯ with vertical line through stem (or "quarter-sharp") | +50¢ |
| ♭ with reversed flag | −50¢ |
| Various Stein-Zimmerman accidentals | +50¢, +25¢, etc. |
| Cent values in superscript: `C +14¢` | Exact specification |

Standardization is incomplete. Different schools use different symbols. When notating microtonal music, include a key clarifying which symbol means which deviation.

## Non-Western traditions that require microtones

### Indian classical music

Built on the *sruti* system, traditionally counted as 22 *sruti* per octave (though they are not equally spaced). The 22-sruti system maps to specific just-intonation ratios.

Key concepts:
- **Raga**: a melodic framework, with characteristic ascending / descending patterns, ornamentation rules, and time-of-day associations
- **Sa, Ri, Ga, Ma, Pa, Dha, Ni** — solfege analogous to Western Do-Re-Mi but with multiple variants of Ri, Ga, Dha, Ni at different sruti
- **Gamaka**: ornamental microtonal slides between fixed pitches; central to Indian melody, comparable in aesthetic role to Korean *sigimsae*

Performance is typically heterophonic (melody + tanpura drone + tabla); chordal harmonic accompaniment is generally non-idiomatic to traditional Indian classical, though contemporary Indian fusion and film music use Western harmony freely.

### Arabic *maqam*

Arabic music uses the *maqam* system: scales with characteristic interval patterns that include quarter-tone-like intervals. Major *maqamat*:

- *Rast*: roughly C D E♭⁺ F G A B♭⁺ (with E♭⁺ and B♭⁺ being neutrals around 50¢ flat of E and B)
- *Bayati*: C D⁻ E♭ F G A♭ B♭ (with D⁻ being a neutral around 50¢ flat)
- *Hijaz*: C D♭ E F G A♭ B (with augmented 2nd between D♭ and E)
- *Saba*: C D⁻ E♭ F♭ G A♭ B♭

The "neutral" intervals (between major and minor) are central to the *maqam* sound. They're not exactly quarter-tones; they vary by region and tradition (Egyptian vs. Syrian vs. Turkish *maqam* are tuned differently).

### Persian *dastgah* and Turkish *makam*

Related to Arabic *maqam* but distinct. Persian *dastgah* uses *koron* (lowered by ~50¢) and *sori* (raised by ~50¢) accidentals. Turkish *makam* uses *koma* — about 1/9 of a tone — as the basic step, giving many subtle interval variations.

### Indonesian gamelan

*Slendro* (5-pitch, near-equal) and *pelog* (7-pitch, unequal) tunings. Each gamelan ensemble is tuned to its own slightly different version — there's no standard pitch reference. Tuning *is* the gamelan's identity.

### Other traditions

Many West African, sub-Saharan African, Polynesian, and Native American traditions use pitch systems that don't fit 12-TET. Generalizations across these are dangerous; specific knowledge of a tradition is essential.

## Spectralism

A modern Western tradition (Grisey, Murail, Saariaho, Hurel) that derives pitch from the harmonic spectrum of natural sounds. Rather than starting from scales, the composer analyzes a sound's spectrum and uses the partials as pitch material — which often produces microtonal pitches because the upper partials don't align with 12-TET.

Practical implication: spectralism uses ensembles that can produce specific microtonal pitches (string and wind ensembles primarily; sometimes specially-tuned percussion or electronics). The sound is often "shimmery" or "non-functional" in the harmonic sense — the music is about timbre and pitch-as-color rather than about chord progression.

## Composing microtonally — practical workflow

### Decide what kind of microtonality you want

The decisions cascade:

- **Which tradition / tuning?** Just intonation? An EDO (which one)? Quarter-tones? *Maqam*-style neutrals? Spectral? Each choice constrains everything downstream.
- **Which instruments?** Voices and strings can produce any pitch with proper rehearsal. Fretted instruments need refretting or specific bend technique. Keyboards need retuning (digital is easy, acoustic is committal). Wind instruments have specific microtonal capabilities and limits.
- **How will you notate?** Cents-precision? Stein-Zimmerman accidentals? Tradition-specific notation (Indian *sargam* ornament marks, Arabic *maqam* notation)?
- **Who's performing?** A chamber ensemble specializing in new music vs. a symphony orchestra vs. a tradition-specific ensemble (Indian classical, Arabic *takht*, gamelan) — each handles different microtonal approaches.

### Notating microtonal music

Some practical conventions:

- **Add a "microtonal accidentals key"** at the start of the score, defining each symbol's exact cent value
- **Use cent annotations** where precision matters (`C +14¢` or `C +14`)
- **For frequent microtones**, define the system once (e.g., "quarter-tones, 24-EDO") and use a consistent symbol set
- **For tradition-specific microtones**, use the tradition's notation (Indian sruti markings; Persian *koron*/*sori*) when working in that tradition

Modern engraving software (Sibelius, Finale, Dorico, MuseScore, Lilypond) supports microtonal notation to varying degrees. Custom symbols may need image insertion or custom-font solutions.

### Rehearsal cost

Microtonal music takes more rehearsal time than 12-TET music, often substantially. Singers and instrumentalists must learn unfamiliar pitches; ensembles must learn to tune unfamiliar intervals together.

If working with a non-specialist ensemble, budget extra rehearsal. For amateur ensembles, microtonality may be impractical at any meaningful complexity.

For specialists (microtonal new music ensembles, Indian classical performers, Arabic *takht* musicians), microtonal pitch is normal and rehearsal cost is no different from any new piece.

## Common pitfalls when advising

- **Don't conflate "microtonal" with "out of tune".** Microtonal music is precise; it just uses different pitches than 12-TET. "Out of tune" is failure to hit intended pitches; microtonality is hitting different intended pitches.
- **Don't apply Western theoretical concepts uncritically.** Indian classical *raga* is not a "scale" in the Western sense; it has rules of motion and ornamentation that go beyond pitch content. Arabic *maqam* is not "Western minor with a quarter-tone".
- **Don't assume EDO is the framework for non-Western music.** Indian classical *sruti* is not 22-EDO; Arabic *maqam* tuning is not 24-EDO; gamelan is not 5-EDO or 7-EDO. EDOs *approximate* these traditions but aren't identical.
- **Don't ignore performer capability.** A microtonal piece for non-specialist performers needs simpler microtonality than the same piece for specialists.
- **Don't romanticize "microtonality" as magic.** The aesthetic value depends on the specific tuning, the music written for it, and the performance — not on microtonality in itself.
- **Don't use microtones for shock value.** Microtonality used as a one-time "weird" effect rarely works; sustained microtonal language used coherently can be transformative.
- **Don't notate carelessly.** Imprecise notation in microtonal music produces garbage in performance. Cent values, accidental keys, and consistent conventions matter.
- **Don't ignore digital options.** A retuned digital instrument (synth, sampler, MIDI keyboard) is the easiest way to compose microtonally. Tools like Scala, the SCALA tuning database, and Pianoteq's micro-tuning support are now standard.

## Quick decision matrix

| Want | Try |
|------|-----|
| Pure intervals, "natural" sound | Just intonation; restrict to one tonal center; use voices, strings, or retuned digital instruments |
| Quarter-tone Western avant-garde | 24-EDO; reference Hába, Ives, Boulez |
| Spectral / shimmering / atmospheric | Spectralism; pitches from harmonic series; reference Grisey, Murail, Saariaho |
| Arabic / Persian / Turkish tradition-adjacent writing | Specific *maqam* / *dastgah* / *makam*; work with tradition specialists; use tradition-appropriate notation |
| Indian classical influence | Specific *raga* with proper *gamaka*; recognize that pitch is only part of the system |
| Indonesian gamelan-adjacent writing | Pelog or slendro tuning (find a specific gamelan's tuning); use specific gamelan instruments |
| Equal-temperament alternative to 12-TET | 19-EDO or 31-EDO for better just approximations; 17-EDO for Pythagorean-like sound |
| Microtonal slides and bends without committing to a system | Continuous pitch on strings, voice, fretless bass, slide instruments; notate with glissando + cent targets |
| Korean traditional-adjacent ornamentation | Stay in 12-TET pitch frame but add *sigimsae*-style microtonal pitch inflections; reference `../genres/korean-traditional.md` |
| Demo / prototype microtonal idea | Retuned digital instrument (any DAW with microtonal support); iterate before committing to a notational and performer plan |

## Cross-references

- Pitch system fundamentals (12-TET, intervals, octave equivalence) → `../fundamentals/pitch-intervals-scales.md`
- Modal harmony (the modal frame applies to many microtonal traditions) → `../harmony/modal-harmony.md`
- Korean traditional music with *sigimsae* microtonal inflections → `../genres/korean-traditional.md`
- Folk, roots, and tradition-specific music (where microtonality is common) → `../genres/folk-roots-and-traditions.md`
- 20th-century compositional techniques (where microtonality intersects with avant-garde) → `20th-century-techniques.md`
- Constraint-based composition (microtonality often is the constraint) → `constraint-based-composition.md`
- Notation generally (microtonal accidentals are an extension) → `../fundamentals/notation-and-conventions.md`
- Orchestration (instrument capabilities for microtones) → `../orchestration/instruments-ranges-character.md`
