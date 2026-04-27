# Piano and Keyboards

Use this file when the user asks for piano voicings, keyboard accompaniment, left-hand patterns, gospel/jazz comping, synth/keys arrangement roles, or piano playability.

## Core idea

Piano can cover melody, harmony, rhythm, and bass at once, but idiomatic writing still needs hand spacing, register control, and pedal/decay awareness.

```text
Piano part = register + hand shape + rhythm + sustain plan
```

## Playability basics

- Standard piano range: A0-C8.
- Comfortable hand span varies; write octaves as normal, tenths as optional unless the player is advanced.
- Fast repeated wide leaps are harder than they look in MIDI.
- Low closed chords get muddy; use open fifths, octaves, or tenths in the bass.
- Pedal can connect harmony, but too much pedal blurs rhythm and chromatic motion.

## Register guide

| Register | Best use | Caution |
|---|---|---|
| A0-C2 | power, sub-like bass, dramatic hits | dense chords become mud |
| C2-C4 | left-hand bass, stride, arpeggios, comp foundation | avoid constant conflict with bass guitar |
| C4-C6 | melody, chord voicing, accompaniment | crowded vocal range if too busy |
| C6-C8 | sparkle, filigree, doubled melody | can become brittle or piercing |

## Common accompaniment patterns

### Block-chord comp

```text
RH: 3- or 4-note chord stabs
LH: bass note or octave
Use: pop, gospel, theatre, rock ballad
```

### Broken-chord arpeggio

```text
LH: root-5th-10th shape
RH: chord tones or melody support
Use: ballad, cinematic, singer-songwriter
```

### Alberti-like pattern

```text
low-high-middle-high
Use: classical/light pop reference, gentle motion
```

### Stride / country-gospel left hand

```text
LH: bass note on beat 1/3, chord or octave answer on 2/4
Use: old-time, gospel, ragtime-adjacent, roots color
```

### Gospel / R&B comp

```text
LH: bass walk or rootless support
RH: 3rds/7ths + extensions, rhythmic fills between vocals
Use: gospel, R&B, neo-soul
```

### Synth/key pad

```text
Sustained voicing, slow filter/dynamic motion, minimal rhythm
Use: pop, worship, ambient, film/game underscore
```

## Voicing rules of thumb

- Put 3rd and 7th in the middle register for harmonic clarity.
- Put melody/top note in a singable register if the piano is carrying the hook.
- Spread low voicings; close high voicings can sparkle.
- For solo piano, include bass, inner rhythm, and melody; for ensemble piano, leave space.
- In dense band arrangements, two- or three-note voicings often beat full chords.

## Genre-specific moves

| Style | Useful piano/keys move |
|---|---|
| Pop ballad | broken octaves, soft RH triads/add9, pedal-controlled sustain |
| Gospel | passing diminished chords, octave melody, response fills |
| Jazz | shell voicings, rootless 3-7-9-13 shapes, comp syncopation |
| Country | simple triads, walkups, honky-tonk octaves, piano/organ support |
| Rock | octave riffs, repeated chord stabs, organ pads |
| EDM/pop | sidechain-friendly pads, plucks, simple voicings, hook ostinato |
| Film/game | ostinato, register layering, pedal point, sparse motif |

## Quick examples

### Pop ballad in C

```text
LH: C2-G2-E3-G2 | A1-E2-C3-E2 | F1-C2-A2-C2 | G1-D2-B2-D2
RH: melody or soft triads above C4
Effect: emotional but playable.
```

### Gospel tag in C

```text
| C/E | F | F#°7 | Gsus G |
RH: voice-lead E-A-C → F-A-C → F#-A-C-E♭ → G-C-D-F / G-B-D-F
```

### Sparse pop comp

```text
LH: root only on bar 1
RH: 3rd + 7th + 9th on offbeats
Leave space for vocal.
```

## Common pitfalls

- **Do not stack full triads below C3.** Spread them.
- **Do not write nonstop RH fills under a vocal.** Fill between phrases.
- **Do not assume two hands can cover every MIDI layer.** Divide into piano + pad if needed.
- **Do not use sustain pedal to hide unclear harmony.** Pedal is color, not glue for bad writing.
- **Do not make left hand and bass guitar fight.** In a band, piano LH can thin out.

## Cross-references

- Chord voicings → `../harmony/voice-leading.md`, `../harmony/jazz-harmony.md`
- Gospel and CCM → `../genres/gospel-and-ccm.md`
- Country and Americana → `../genres/country-americana.md`
- Arrangement density → `../orchestration/arrangement-density.md`
- Production-aware frequency spacing → `../production-aware/arrangement-for-mix.md`
