# Instrument Idiom Overview

This folder gives composition-facing guidance for writing parts that feel natural on real instruments. It complements `../orchestration/instruments-ranges-character.md`, which gives range and character summaries. Use these files when the user asks for a part, riff, accompaniment, section writing, or playability check.

## What "idiomatic" means

An idiomatic part respects the way an instrument naturally produces sound:

- physical layout: strings, keys, valves, sticks, breath, hand span
- natural resonances: open strings, registers, pedal tones, vowels
- gesture: strum, bow, tongue, roll, bend, comp, walk, breathe
- fatigue: brass endurance, vocal tessitura, repeated leaps, hand stretches
- ensemble role: bass foundation, drum timekeeping, guitar comping, string pad, vocal lead

Idiomatic does **not** mean predictable. It means the part gives the performer a believable path to the sound.

## When to consult instrument-idiom files

| User asks | Start here |
|---|---|
| Piano voicing, left-hand pattern, keyboard accompaniment | `piano-keyboards.md` |
| Guitar chords, riffs, strumming, capo, tuning, playable voicing | `guitar.md` |
| Bassline, walking bass, synth/electric bass role | `bass.md` |
| Drum groove, fill, kit writing, percussion layer | `drums-percussion.md` |
| String quartet/section writing, bowing, divisi, double stops | `strings.md` |
| Flute/clarinet/oboe/bassoon/sax line or section | `winds.md` |
| Brass fanfare, horn line, trumpet/trombone/tuba section | `brass.md` |
| Solo vocal, backing vocals, choir-adjacent pop writing | `vocals.md` |

## Fast idiom diagnostic

When a part sounds fake or awkward, check these in order:

1. **Range** — is it possible?
2. **Tessitura** — is it comfortable for more than a moment?
3. **Gesture** — does the pattern match how the instrument moves?
4. **Breath / decay** — does the phrase allow sound to be renewed?
5. **Register color** — is the chosen register giving the intended timbre?
6. **Density** — is the part competing with too many other parts?
7. **Notation / communication** — could a player understand the intent quickly?

## Idiom vs. orchestration

- **Orchestration** asks: which instruments should play this musical idea?
- **Instrument idiom** asks: once chosen, how should the idea be shaped so the instrument speaks naturally?

Example:

```text
Idea: fast repeated notes
Orchestration answer: strings, flute, marimba, guitar tremolo, repeated synth, snare roll
Idiom answer: each instrument repeats differently; do not copy-paste the same MIDI pattern.
```

## Real performers vs. sample libraries

A sample library can make impossible writing sound plausible for a few seconds, but that does not make it performer-friendly. Conversely, real performers can solve awkward writing if the musical goal is clear.

Use this rule:

```text
If the user is writing for a real session, prioritize playability and notation.
If the user is producing in a DAW, prioritize believable gesture and sonic clarity.
If unknown, give both versions.
```

## Common part-writing modes

| Mode | What matters most |
|---|---|
| Lead line | range, breath/bow/picking, phrase shape, register color |
| Accompaniment | rhythmic pocket, voicing, density, non-conflict with vocal |
| Riff | physical repeatability, accent pattern, timbre, memorability |
| Pad / sustain | register spacing, re-articulation, blend, dynamic contour |
| Counterline | independence, register separation, answer timing |
| Section writing | voicing, balance, fatigue, blend, orchestration role |

## Common pitfalls

- **Do not write only from piano-roll logic.** Instruments have bodies.
- **Do not equate possible with good.** A note may exist but sound weak or strained.
- **Do not forget recovery.** Brass, winds, singers, and drummers need endurance planning.
- **Do not use the same voicing across instruments.** A piano chord, guitar chord, string voicing, and horn voicing behave differently.
- **Do not over-specify technique when a musical description is enough.** "Warm, connected, not too loud" can be more useful than too many markings.

## Cross-references

- Instrument ranges and characters → `../orchestration/instruments-ranges-character.md`
- Voicing and texture → `../orchestration/voicing-and-texture.md`
- Arrangement density → `../orchestration/arrangement-density.md`
- Notation and conventions → `../fundamentals/notation-and-conventions.md`
- Rhythm and groove → `../rhythm-groove/groove-and-feel.md`
- Production-aware arrangement → `../production-aware/arrangement-for-mix.md`
