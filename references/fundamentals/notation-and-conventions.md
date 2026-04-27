# Notation and Conventions

This file covers the visual and notational conventions of Western music — clefs, key signatures, accidentals, dynamics, articulations, ornaments, score layout, and the specific conventions of pop/lead-sheet/jazz writing. It's a reference for what's on the page (or what should be).

For tempo and meter, see `rhythm-meter.md`. For pitch-system theory (intervals, scales), see `pitch-intervals-scales.md`. For chord symbols specifically, see `harmony/chord-construction.md`.

## When to consult this file

- Questions about clefs, key signatures, dynamics, articulations
- Reading or writing a score
- Lead-sheet conventions (Real Book, pop charts)
- Nashville Number System
- Roman numeral analysis notation
- Standard expressive markings

## Clefs

A clef indicates which lines and spaces of the staff correspond to which pitches.

| Clef | Notes the line/space | Used for |
|------|----------------------|----------|
| Treble (G clef) | The G clef curls around G4 (second line up) | Most instruments above middle C; right hand of piano; soprano and alto voice |
| Bass (F clef) | The two dots flank F3 (fourth line up) | Most instruments below middle C; left hand of piano; bass and baritone voice |
| Alto (C clef on middle line) | Middle line = C4 (middle C) | Viola; some choral alto parts (mostly historical) |
| Tenor (C clef on fourth line) | Fourth line up = C4 | Cello, trombone, bassoon (in their high register); some choral tenor parts |
| Soprano clef | First line = C4 | Historical only |
| Mezzo-soprano clef | Second line = C4 | Historical only |
| Baritone clef | Various positions | Historical only |
| Octave-displaced treble | Treble clef with `8` above (sounding up) or below (sounding down) | Tenor voice (8va below); piccolo/celeste sometimes (8va above) |

Treble and bass clefs are the modern defaults. C clefs (alto, tenor) are still used for specific instruments to keep ledger lines manageable.

The treble clef with `8` below (often written `treble 8va bassa`) is standard for tenor voice in modern scores — it sounds an octave below the written pitch, putting the tenor's range conveniently on the staff.

## Key signatures

A key signature appears at the start of each staff line, after the clef, indicating which pitches are sharpened or flattened throughout the piece (or until the next key signature).

### The cycle of fifths and key signatures

| Sharps | Major key | Relative minor | Sharps in order |
|--------|-----------|----------------|-----------------|
| 0 | C major | A minor | — |
| 1 | G major | E minor | F♯ |
| 2 | D major | B minor | F♯ C♯ |
| 3 | A major | F♯ minor | F♯ C♯ G♯ |
| 4 | E major | C♯ minor | F♯ C♯ G♯ D♯ |
| 5 | B major | G♯ minor | F♯ C♯ G♯ D♯ A♯ |
| 6 | F♯ major | D♯ minor | F♯ C♯ G♯ D♯ A♯ E♯ |
| 7 | C♯ major | A♯ minor | F♯ C♯ G♯ D♯ A♯ E♯ B♯ |

| Flats | Major key | Relative minor | Flats in order |
|-------|-----------|----------------|----------------|
| 0 | C major | A minor | — |
| 1 | F major | D minor | B♭ |
| 2 | B♭ major | G minor | B♭ E♭ |
| 3 | E♭ major | C minor | B♭ E♭ A♭ |
| 4 | A♭ major | F minor | B♭ E♭ A♭ D♭ |
| 5 | D♭ major | B♭ minor | B♭ E♭ A♭ D♭ G♭ |
| 6 | G♭ major | E♭ minor | B♭ E♭ A♭ D♭ G♭ C♭ |
| 7 | C♭ major | A♭ minor | B♭ E♭ A♭ D♭ G♭ C♭ F♭ |

### Order of sharps and flats

Sharps are added in this order: F♯ C♯ G♯ D♯ A♯ E♯ B♯
Flats: B♭ E♭ A♭ D♭ G♭ C♭ F♭

Each is a perfect fifth above the previous (for sharps) or below (for flats). Memorizing the order makes reading and writing key signatures fluent.

### Finding the tonic from the key signature

For sharp keys: the last sharp is one half-step below the tonic (last sharp F♯ → key of G; last sharp C♯ → key of D).

For flat keys: the second-to-last flat names the tonic (flats B♭ E♭ A♭ → key is E♭). Exception: F major has only one flat (B♭), no second-to-last; just memorize.

For minor keys: the relative minor is a m3 below (or M6 above) the relative major. So 1 sharp = G major OR E minor; the actual key is determined by listening for the tonic, not by the signature alone.

## Accidentals

Accidentals override the key signature for individual notes within a measure.

| Symbol | Name | Effect |
|--------|------|--------|
| ♯ | Sharp | Raise by a semitone |
| ♭ | Flat | Lower by a semitone |
| ♮ | Natural | Cancel any prior sharp/flat |
| 𝄪 (or ♯♯) | Double sharp | Raise by two semitones |
| 𝄫 | Double flat | Lower by two semitones |

An accidental applies for the rest of the measure on that pitch (same octave, same letter name) unless cancelled by another accidental. After the barline, the key signature reasserts.

For modern atonal/serial music or in passages where every note is accidental, scores sometimes write each accidental explicitly (no carry-through). The composer should specify if they're using non-standard practice.

### Microtonal accidentals (briefly)

For quarter-tone and other microtonal music, additional accidentals exist (varying by composer/system). Most common:

- ½♯ (half-sharp) — raise by quarter-tone
- ½♭ (half-flat) — lower by quarter-tone
- 1½♯ (sharp + half-sharp) — three-quarter-tone

Used in contemporary classical, some jazz (rarely), and adaptations of non-Western music.

## Dynamics

| Marking | Italian | Volume |
|---------|---------|--------|
| pppp | piano-pianissimo or pianissississimo | Extremely soft |
| ppp | pianississimo | Very, very soft |
| pp | pianissimo | Very soft |
| p | piano | Soft |
| mp | mezzo piano | Moderately soft |
| mf | mezzo forte | Moderately loud |
| f | forte | Loud |
| ff | fortissimo | Very loud |
| fff | fortississimo | Very, very loud |
| ffff | fortissississimo | Extremely loud |

### Dynamic accents and modifiers

| Marking | Meaning |
|---------|---------|
| sf, sfz | sforzando — sudden strong accent on a single note |
| fp | forte-piano — start loud, immediately drop to soft |
| sfp | sforzando-piano — sudden accent that immediately drops to soft |
| rfz | rinforzando — reinforced (similar to sfz, less abrupt) |
| > | accent (louder than surrounding notes; not as sharp as sfz) |
| ^ | marcato (strong, marked accent) |
| ten. | tenuto (full duration, slight emphasis) |

### Dynamic transitions

| Marking | Meaning |
|---------|---------|
| crescendo (cresc.) or `<` | Gradually louder |
| decrescendo (decresc.) or `>` (with terminal mark) | Gradually softer |
| diminuendo (dim.) | Gradually softer (synonym for decrescendo) |
| poco a poco | little by little (modifies cresc. or dim.) |

The hairpin notation (`<` `>`) is a graphical alternative to "cresc." / "dim." Both are common.

## Articulations

Articulation markings affect how each note is played — its length, attack, and emphasis.

### Strings and winds

| Marking | Name | Effect |
|---------|------|--------|
| `.` (dot above/below note) | staccato | Short, detached; about half the written duration |
| `'` (wedge or stroke) | staccatissimo | Very short |
| `_` (line) | tenuto | Hold full value, slight emphasis |
| `_.` (line + dot) | portato | Slightly separated but full-bodied |
| `>` | accent | Stronger attack on this note |
| `^` | marcato | Strong, sharp attack |
| slur (curved line over notes) | legato | Smooth connection between notes; in winds and strings, played in one bow/breath |

### Bowed strings

| Marking | Name | Effect |
|---------|------|--------|
| `↑` | up-bow | Bow moves toward the player |
| `n` (square shape) | down-bow | Bow moves away from the player |
| arco | "with the bow" | Cancel pizzicato |
| pizz. | pizzicato | Plucked |
| col legno | "with the wood" | Strike with the bow's wooden side |
| sul ponticello | "on the bridge" | Glassy, scratchy timbre |
| sul tasto | "on the fingerboard" | Soft, flute-like timbre |
| spiccato | (technique) | Bouncing, light short notes |
| tremolo (z or // through stem) | rapid bow strokes | Sustained shimmer |

### Brass and winds (selected)

| Marking | Name | Effect |
|---------|------|--------|
| flutter | flutter-tonguing (rolled R while playing) | Buzzy, growly |
| tongued / slur | normal tonguing or smooth | Default vs. legato |
| mute (with `+` or `o`) | hand-stopped or muted | Brass: changes timbre |
| open / mute | for trumpet, trombone | Specific mute states |
| double tongue, triple tongue | (technique) | Rapid articulation |

### Percussion

Percussion notation varies by instrument. Common conventions:

- Drum kit: notated on a 5-line staff with specific positions for each drum (kick on the bottom space, snare on the middle, hi-hats above the staff).
- Mallet percussion (xylophone, marimba, vibraphone): pitched, written on standard staff.
- Auxiliary percussion: often a single-line staff with x-noteheads.

For drum charts in pop/jazz, see "Pop and lead-sheet conventions" below.

### Voice

| Marking | Effect |
|---------|--------|
| slur | One syllable across multiple notes (melisma) |
| no slur | One syllable per note |
| portamento | Slide between pitches (slow glissando in vocal context) |
| spoken | Spoken rhythm, no pitch |
| Sprechstimme (or `x`-noteheads) | Speech-singing, approximate pitch |

## Ornaments

Decorative figures, often improvised in earlier eras and now often written out fully.

| Symbol | Name | Effect |
|--------|------|--------|
| tr | trill | Rapid alternation between the written note and the note above (usually a M2; sometimes m2 depending on style/key) |
| 𝆔 | mordent | A quick alternation: principal note → upper neighbor → principal |
| 𝆕 | inverted mordent | Principal → lower neighbor → principal |
| 𝆖 | turn | Four-note figure: upper neighbor → principal → lower neighbor → principal |
| 𝆗 | inverted turn | Lower neighbor → principal → upper neighbor → principal |
| (small grace note before main note) | acciaccatura | Crushed grace note; takes essentially no time from the main note |
| (small grace note before main note, slurred) | appoggiatura | Lyrical grace note; takes time from the main note (typically half its value) |
| ~/| / | glissando | Slide between two notes |
| (wavy line) | vibrato | Pitch wavers slightly |

The interpretation of ornaments is style-dependent. A Baroque trill starts on the upper note; a Classical or modern trill usually starts on the principal note. Mark or describe explicitly when style might be ambiguous.

## Score layout

### Order of instruments (full orchestral score)

From top to bottom:

1. **Woodwinds** (piccolo, flutes, oboes, English horn, clarinets, bass clarinet, bassoons, contrabassoon)
2. **Brass** (horns, trumpets, trombones, tuba)
3. **Percussion** (timpani, then auxiliary, then mallet)
4. **Keyboards / harp** (if present)
5. **Voices / chorus** (if present)
6. **Strings** (violin I, violin II, viola, cello, double bass)

Within each section, instruments are ordered from highest to lowest. Horns are an exception — they appear above trumpets in the brass section by tradition, even though they're lower-pitched.

### Bracketing

Instruments of the same family are grouped with a bracket on the left. Subgroups (e.g., flute 1+2) get a sub-bracket. The string section uses a thicker bracket.

### Measure numbers

Modern practice: number every measure (or every 5 or 10) at the top of the system. The first measure of a piece is bar 1 unless there's an anacrusis, in which case the first full bar is 1.

### Rehearsal marks

Letters or numbers placed in boxes at structural points to facilitate rehearsal: `A`, `B`, `C` (or `1`, `2`, `3`). Often placed at the start of new sections, key changes, or thematic returns.

### Cues and divisi

| Marking | Meaning |
|---------|---------|
| div. | divisi (a section splits into multiple parts) |
| unis. | unison (cancel divisi) |
| solo | One player (rather than the full section) |
| tutti | Everyone plays |
| a 2 | Both players (when two share a stand or part) |

## Expression markings

Italian is the standard language; some scores use German, French, or English. The agent should recognize common expressions.

### Italian (standard)

| Term | Meaning |
|------|---------|
| dolce | sweetly |
| espressivo | expressively |
| cantabile | singing, lyrical |
| con brio | with spirit |
| con fuoco | with fire |
| con moto | with motion |
| grazioso | gracefully |
| leggiero | lightly |
| maestoso | majestically |
| appassionato | passionately |
| tranquillo | calmly |
| risoluto | resolutely |
| pesante | heavy |
| scherzando | playfully |
| morendo | dying away |
| calando | decreasing (dynamic and tempo) |

### German (Romantic and 20th C.)

Mahler, Schoenberg, and others wrote markings in German.

| German | Meaning |
|--------|---------|
| ruhig | calm |
| heftig | violent |
| zart | tender |
| schnell | fast |
| langsam | slow |
| mit | with |
| ohne | without |

### French (Impressionist mostly)

| French | Meaning |
|--------|---------|
| doux | sweet |
| très | very |
| en dehors | bring out (used for emphasis) |
| comme un soupir | like a sigh |

## Pop and lead-sheet conventions

Lead sheets (especially the Real Book and similar collections) use a stripped-down notation: melody on a treble staff, chord symbols above. The arranger fills in the rest.

### Chord symbols

See `harmony/chord-construction.md` for the full table. Quick reminders:

- Major: `C`, `Cmaj`, `CM` (rarely just the bare letter without specification)
- Minor: `Cm`, `Cmin`, `C-`
- Major 7: `Cmaj7`, `CΔ`, `CM7`
- Minor 7: `Cm7`, `C-7`
- Dominant 7: `C7`
- Half-diminished: `Cø7`, `Cm7♭5`
- Diminished 7: `C°7`, `Cdim7`
- Augmented: `C+`, `Caug`, `C(♯5)`

### Slash chords

`X/Y` = chord X over bass Y. `C/E` is C major in first inversion (E in bass); `F/G` is F major over G bass (effectively a G dominant suspension).

### Drum chart notation

Drum charts often use simplified notation:

- `x` noteheads for cymbals and hi-hat
- Standard noteheads for snare and toms
- Single-line or full 5-line staff
- "Slash" notation (`/`) for "play time" — keep going with the same groove
- `Fill` markings for fills

A typical drum chart for a verse might be: `|1: Time | 2: Time | 3: Time | 4: Fill |`

### Tab (guitar tablature)

Six lines representing the six strings. Numbers indicate which fret to play. Common modifications:

- `h` = hammer-on
- `p` = pull-off
- `b` = bend
- `r` = release bend
- `/` or `\` = slide
- `~` = vibrato
- `x` = muted note

Tab is widely used by guitarists in lieu of standard notation, especially for rock and folk. It conveys what to play but not pitch directly.

### Nashville Number System

A shorthand for chord progressions using scale degrees (numbers) instead of letters. Used heavily in Nashville session work because it's instantly transposable to any key.

| Notation | Meaning |
|----------|---------|
| `1` | I (tonic) |
| `2m` | ii (minor) |
| `3m` | iii (minor) |
| `4` | IV |
| `5` | V |
| `6m` | vi (minor) |
| `7°` | vii° |
| `1/3` | I in first inversion (3 in bass) |
| `5/7` | V with leading tone in bass |
| `1Δ` | Imaj7 |
| `5 7` | V7 |
| `b7` | ♭VII (borrowed) |

A Nashville chart for "Country Roads": `1 6m | 4 1 | 1 6m | 4 1 |` etc.

For minor keys, lowercase or specifically marked numbers indicate minor mode. Conventions vary somewhat by sheet writer.

### Roman numeral analysis

Used in classical analysis and academic settings:

| Symbol | Meaning |
|--------|---------|
| `I`, `IV`, `V` | Major triad on that scale degree |
| `i`, `iv`, `v` | Minor triad |
| `vii°` | Diminished triad on ^7 |
| `III+` | Augmented triad |
| `V7`, `ii⁶/⁵` | 7th chord with figured-bass inversion |
| `V/V` | "V of V" — secondary dominant |
| `♭III` | Lowered (borrowed) III |
| `N⁶` | Neapolitan in first inversion (♭II⁶) |
| `It⁶`, `Fr⁶`, `Ger⁶` | Augmented 6th chords |

Always specify the key context. "ii" in C major is Dm; "ii" in A♭ major is B♭m.

## Common pitfalls when advising

- **Don't mix conventions.** Pick lead-sheet symbols OR Roman numerals OR Nashville for any one piece of analysis or chart. Mixing is confusing.
- **Don't use double-flats and double-sharps decoratively.** They have specific theoretical purposes (e.g., the diminished 7 of B°7 is A♭ becoming A𝄫 in spelling). Using them where ♮ or simpler accidentals work is bad spelling.
- **Don't write enharmonic equivalents at random.** F♯ and G♭ are not interchangeable in context — pick the spelling that fits the key signature and the harmonic function.
- **Don't forget the cadence-confirming dynamic.** A score with no dynamics is hard to interpret. Even simple lead sheets benefit from a few markings.
- **Don't over-articulate.** A staccato on every note becomes meaningless. Articulations should mark moments of change or emphasis.

## Cross-references

- Pitch system, intervals, scales → `pitch-intervals-scales.md`
- Tempo, meter, beat hierarchy → `rhythm-meter.md`
- Chord symbols and analysis (Real Book, pop, RN, Nashville) → `harmony/chord-construction.md`, `assets/chord-symbol-conventions.md`
- Notation in genre-specific contexts → various `genres/*.md`
- Score layout for orchestration → `orchestration/instruments-ranges-character.md`
- Roman numeral analysis applied to actual progressions → `analysis.md`
