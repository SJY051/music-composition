# Jazz Harmony

Jazz harmony is functional harmony with extensions as default, substitutions as basic literacy, and voicings as a defining language. The tonal logic is mostly the same as classical functional harmony, but the surface is denser and the substitution toolkit is wider. This file covers what makes jazz harmony jazz, not the broader system.

## When to consult this file

- The user asks about ii-V-I, jazz changes, "comping"
- Tritone substitution, backdoor ii-V, Coltrane changes
- Upper-structure triads, rootless voicings, drop-2/drop-3
- Chord-scale relationships ("what scale do I play over G7♭9")
- Bebop chromaticism, bop language
- Modal jazz harmonic approach (also see `modal-harmony.md`)
- Reharmonization in a jazz context (also see `reharmonization.md`)

For chord spelling and quality, see `chord-construction.md`. For functional logic, see `functional-harmony.md`. For voicings as visual shapes, see `assets/jazz-voicings.md`. For modal jazz specifically, see `modal-harmony.md`.

## What makes jazz harmony jazz

Three axes:

1. **Extensions are the default, not the exception.** A jazz `Cmaj7` is rarely just C-E-G-B; it usually has 9, sometimes 13. A `G7` is rarely just G-B-D-F; it has 9 (or ♭9), and often 13 (or ♭13). The 7th is the *minimum*.
2. **Functional motion is dense.** Every diatonic chord can be approached by its own ii-V. A 32-bar standard might have 30 chord changes, where a comparable pop song might have 8.
3. **Substitution is part of the literacy.** Tritone subs, backdoor ii-Vs, secondary dominants — these aren't "advanced" in jazz; they're starting vocabulary.

A jazz musician who reads `Cmaj7 – Am7 – Dm7 – G7` understands that as a default starting point. The actual played version will have substitutions, alterations, and voicings that the chart doesn't specify.

## Extensions and alterations — jazz defaults

Every chord type has a default extension treatment in jazz. Use these as the starting assumption; deviate for effect.

| Chord type | Default extensions | Common alterations |
|------------|-------------------|---------------------|
| Major 7 | 9, ♯11, 13 (Lydian flavor) | Sometimes natural 11 implied via sus, but ♯11 is more common |
| Dominant 7 (resolving) | 9, 13 | ♭9, ♯9, ♭13 (or ♯5) for tension; commonly all four "altered" tensions |
| Dominant 7 (non-resolving / static) | 9, ♯11, 13 (Lydian dominant) | Less alteration; the chord doesn't need to resolve |
| Minor 7 | 9, 11, occasionally 13 | (rarely altered) |
| Minor 7♭5 (half-diminished) | 11, ♭13; sometimes natural 9 (Locrian ♮2) | (extensions stay where they are) |
| Diminished 7 | 9, 11, ♭13 (each tone of the chord can serve as a "root") | Symmetric — many tensions work |
| Minor-major 7 | 9, 11, 13 | (melodic minor flavor) |

The key idea: when a player sees `G7` resolving to `Cmaj7`, they may add ♭9 or ♭13 (or both) to enrich the dominant pull. When they see `G7♯11` or a dom7 chord that's *not* resolving, they leave the natural extensions or use Lydian dominant flavor.

## ii-V-I — the central jazz cadence

The ii-V-I (or ii-V-i in minor) is the cellular unit of jazz harmonic motion. Every standard contains them; most progressions can be analyzed as chains of ii-Vs.

### Major key ii-V-I

In C major: `Dm7 – G7 – Cmaj7`.

Voice-led smoothly:
- 3rd of `Dm7` (F) is the 7th of `G7`, then resolves down to E (the 3rd of `Cmaj7`)
- 7th of `Dm7` (C) is the 11th-or-implied of `G7`, then can hold or move to B (the 7th of `Cmaj7`)
- The two "guide tones" (3rd and 7th of each chord) are F & C in Dm7, F & B in G7, E & B in Cmaj7. Half-step motion drives the resolution.

### Minor key ii-V-i

In C minor: `Dm7♭5 – G7♭9 – Cm(maj7)` (or Cm6, or Cm7 — the choice depends on style).

Voice-led smoothly:
- The `iiø7` (Dm7♭5) has the same 3rd and 7th as Dm7 in major (F and C), but the ♭5 (A♭) confirms minor key.
- The `V7♭9` borrows the ♭9 from harmonic minor (A♭ becomes the ♭9 of G).
- Resolution to a tonic that's typically `m6`, `m(maj7)`, or `m7`.

### ii-V-I chains

Chains of ii-Vs that target multiple keys are the bread and butter of jazz changes.

`Dm7 – G7 – Cmaj7 | Cm7 – F7 – B♭maj7 | B♭m7 – E♭7 – A♭maj7`

This is a sequence of ii-V-Is descending by whole step. "All the Things You Are" famously uses ii-V-I chains, modulating constantly through the form.

ii-Vs can also be used without the resolution — a "ii-V to nowhere" sets up a key, then redirects.

## The blues form (briefly — see `../genres/jazz-styles.md` for genre depth)

12-bar blues is a foundational form in jazz. Standard form:

| Bars | Chords |
|------|--------|
| 1 | I7 |
| 2 | IV7 (quick change) or I7 |
| 3 | I7 |
| 4 | I7 |
| 5 | IV7 |
| 6 | IV7 (or ♯iv°7 to V) |
| 7 | I7 |
| 8 | VI7 (V/ii) or I7 |
| 9 | ii7 (or V7) |
| 10 | V7 |
| 11 | I7 (or ii-V turnaround) |
| 12 | V7 (or turnaround) |

The "jazz blues" extends this with more substitutions:

| Bars | Chords |
|------|--------|
| 1 | I7 |
| 2 | IV7 |
| 3 | I7 |
| 4 | I7 (or v7-I7) |
| 5 | IV7 |
| 6 | ♯iv°7 |
| 7 | I7 |
| 8 | III7 (V/vi) |
| 9 | VI7 (V/ii) |
| 10 | ii7 |
| 11 | V7 |
| 12 | I7 (turnaround: I-VI-ii-V or I-♭III-II-♭II) |

Bird blues and minor blues add more substitution layers. The blues form is where many jazz substitution tricks are first learned.

## Substitutions

Substitution is replacing a chord with a different chord that performs the same function (or a related function). The five most important:

### 1. Tritone substitution

Replace any dominant 7 chord with the dominant 7 a tritone away. The two share the same tritone (the chord's most defining interval), so they have the same essential function.

`G7` (G B D F) and `D♭7` (D♭ F A♭ C♭) share the tritone B-F (= C♭-F). So `D♭7` can substitute for `G7` in any context, including resolving to `Cmaj7`.

`Dm7 – D♭7 – Cmaj7` is a tritone-sub ii-V-I. The bass moves chromatically (D – D♭ – C), which is exactly why tritone subs feel so smooth.

The notation: `D♭7` can be written as `subV7/I` (substitute V of I) when functioning as a tritone sub.

Tritone subs work on secondary dominants too: `V7/V` (D7 in C major) substituted by `A♭7`. In a long chain, tritone-substituting some V7s and not others creates chromatic descending bass lines.

### 2. Backdoor ii-V

A `iv–♭VII7–I` motion (from the parallel minor's ii-V). In C major: `Fm7 – B♭7 – Cmaj7`.

The `B♭7` looks like it should resolve to E♭ (its conventional target), but it resolves *up* a whole step to C, with smooth voice leading. The 3rd of B♭7 (D) and the 7th of B♭7 (A♭) resolve to the 9th of Cmaj7 (D) and the 3rd of Cmaj7 (E) respectively.

Backdoor ii-Vs are common in standards. They give a momentary minor flavor (the iv chord) before resolving to major.

### 3. Diminished substitution

Any dominant 7♭9 chord shares three notes with a diminished 7 chord built on its 3rd, 5th, or ♭7. So `°7` chords can substitute for dominant chords (and vice versa).

`G7♭9 = G B D F A♭`. The °7 chord built on B (B D F A♭) is the same except for the missing root.

Practical use: replace `V7` with a `°7` for a smoother voice-leading effect, often with a chromatic bass approach.

### 4. ii-V insertion

Insert a ii-V before any chord. Don't have a `Dm7 – G7` before `Cmaj7`? Add one. Don't have a `Em7 – A7` before `Dm7`? Add one. Every chord can be approached by its own ii-V.

A 32-bar tune with 16 chord changes can become one with 32 chord changes by inserting ii-Vs in front of every chord.

This is how players add density and forward motion to simple progressions, and how reharmonization commonly works.

### 5. Coltrane substitution (Coltrane changes)

Replace a single ii-V-I with a sequence of three key centers a major third apart, each with its own ii-V-I.

A compact C-centered Coltrane-cycle illustration: `Cmaj7 – E♭7 – A♭maj7 – B7 – Emaj7 – G7 – Cmaj7`. The Maj7 chords are a M3 apart (C, A♭, E), each connected by a dominant 7. Treat this as a transposed/simplified pattern, not a literal full lead-sheet excerpt from "Giant Steps".

Practical use: replace a long static major-key passage with a Coltrane sequence to add motion. Famously hard to improvise over but conceptually elegant.

## Modal interchange in jazz

Jazz uses modal interchange (borrowing from parallel minor) more aggressively than classical or pop. Examples:

- The minor IV (`iv`) appears constantly in major-key tunes.
- The `♭III` and `♭VII` show up as borrowed chords or modal flavor.
- Minor-key tunes borrow the major-key V (with leading tone) for cadences.

The line between "modal interchange" and "constant chromatic harmony" gets blurry in jazz. Most tunes are happy to borrow whatever's needed.

## Voicing approaches

Jazz harmony lives or dies by voicing. The same chord symbol can be voiced dozens of ways, each with a different feel.

### Shell voicings

Just root + 3 + 7 (omitting the 5). Common in jazz piano left hand. Three-note voicings are clear and don't fight the bass.

`Cmaj7` shell: C (root), E (3), B (7).

### Rootless voicings

Omit the root entirely (the bass player handles it). Replace the root slot with the 9th. Frees the chord for tensions.

`Cmaj7` rootless: E G B D (3 5 7 9). `G7` rootless: F A B D (♭7 9 3 5) — common left-hand voicing.

### Drop voicings

Take a close-position 4-note voicing and drop the 2nd or 3rd voice from the top down an octave.

Starting from `Cmaj7` close position (low → high): `C – E – G – B` (root, 3, 5, 7).

- **Drop 2**: drop the 2nd-from-top voice (`G`) an octave down → `G – C – E – B`. The 5th sits in the bass; the rest stays compact above.
- **Drop 3**: drop the 3rd-from-top voice (`E`) an octave down → `E – C – G – B`. Wider gap between the bass note and the upper triad-shape; useful when you want a clear "bass + chord" separation.

Drop voicings open up the chord for stepwise voice leading on guitar and piano. Drop 2 in particular is the standard jazz guitar voicing because it lays well on the top four strings (or middle four strings). For full inversion tables, see `assets/jazz-voicings.md`.

### Quartal voicings

Stacked 4ths. Modal, McCoy Tyner / "So What" / Herbie Hancock. Common for Dorian and other modal contexts.

`So What` voicing for D Dorian: D G C F A (D, G, C, F, A — a stack of 4ths up to a 3rd at the top).

### Spread voicings

Wide intervals across multiple octaves. Common in piano left-hand-low / right-hand-high arrangements.

### Upper structure triads (UST)

Already covered in `chord-construction.md`. A jazz favorite for getting tensions on top: play a shell or rootless voicing in the left hand and a triad in the right hand whose notes are upper extensions of the chord.

## Chord-scale theory — a brief

For each chord, there's a "default" scale that contains its chord tones plus the available extensions. Improvisers and composers use these as starting points (not as rigid rules — bebop chromaticism violates them constantly).

| Chord | Default scale |
|-------|---------------|
| Imaj7 | Ionian (or Lydian for color) |
| Imaj7♯11 | Lydian |
| ii7 | Dorian |
| iiø7 | Locrian (or Locrian ♮2 if the natural 9 is in the chord) |
| iii7 | Phrygian (or Aeolian if borrowed) |
| IV7 (V/♭VII or blues IV) | Mixolydian or Lydian dominant |
| V7 (resolving) | Mixolydian, with alterations available: altered scale, half-whole diminished, Phrygian dominant |
| V7sus4 | Mixolydian with no 3rd; or "Phrygian over V" for darker color |
| vi7 | Aeolian (or Dorian) |
| vii°7 | Half-whole diminished, or harmonic minor of the next chord |
| Im(maj7) | Melodic minor |
| Im7 (modal context) | Dorian |

This isn't a substitute for ear and taste — it's a starting framework. Many great soloists violate chord-scale defaults constantly.

## Common reharm patterns (brief)

For full treatment see `reharmonization.md`. Quick patterns specific to jazz:

- **Replace V7 with subV7**: tritone sub.
- **Use tritone subs for dominant-function chords, not literally any chord**: `G7 → D♭7` works because both chords contain the same guide-tone tritone. For a non-dominant chord like `Cmaj7`, first reinterpret its function or use another reharm device (chromatic mediant, approach ii–V, pedal, or dominantization); don't call the result a tritone substitution unless it behaves like a dominant substitute.
- **Replace a single chord with a ii-V**: turn `Cmaj7` (lasting 4 bars) into `Cmaj7 – Dm7 – G7 – Cmaj7` or `Cmaj7 – Em7 – A7 – Dm7 – G7 – Cmaj7`.
- **Pedal the V**: replace several beats of various chords with a static V7 (often with extensions changing).
- **Add a turnaround**: the standard `Cmaj7 – Am7 – Dm7 – G7` or its variants (`Cmaj7 – A7 – D7 – G7`; `Cmaj7 – Bm7♭5 – E7 – Am7 – D7 – G7`).

## Genre notes within jazz

- **Swing**: simpler harmony, often diatonic with secondary dominants. Standard ii-V-I motion.
- **Bebop**: dense ii-V chains, tritone subs, fast-moving changes. "Anthropology", "Cherokee".
- **Cool jazz**: smoother, modal-flavored, less dense. "Kind of Blue".
- **Hard bop**: gospel-flavored, bluesy, with rich extended chords. Horace Silver, Art Blakey.
- **Modal jazz**: see `modal-harmony.md`.
- **Free jazz**: harmony is largely abandoned; pitch organization happens in other ways. See `techniques/20th-century-techniques.md`.
- **Fusion**: jazz harmony with rock/funk rhythm; often more modal, often with electric voicings.
- **Contemporary jazz / post-bop**: extended harmonic vocabulary, slash chords, polychords, chromatic mediants. Wayne Shorter, Brad Mehldau.

## Common pitfalls when advising

- **Don't suggest extensions without considering the bass.** A `Cmaj9♯11` sounds great with C in the bass; the same notes with E in the bass become an `Em7 add ♯5` (dissonant nightmare).
- **Don't pile alterations on a non-resolving dominant.** `7♯11` flavor is for static or modal dominants; `7♭9♯9` and `7alt` are for resolving dominants.
- **Don't tritone-sub everything.** Indiscriminate tritone subs lose the resolution feel. Use them where chromatic descent is wanted.
- **Don't ignore the chord-scale default for context.** A `D7` in the middle of a C major context (V/V) wants Mixolydian or altered. The same `D7` in a D blues wants D Mixolydian with blue notes.
- **Don't chase substitution without ear.** Substitutions are tools; the goal is sound, not complexity.

## Quick decision matrix

| Want | Use |
|------|-----|
| Smooth, textbook jazz cadence | ii-V-I with extensions |
| Chromatic bass descent into tonic | Tritone-sub the V (D♭7 → C) |
| Momentary minor flavor before major tonic | Backdoor ii-V (iv-♭VII7-I) |
| Add motion to static harmony | Insert ii-V before each chord |
| Modal vamp instead of changes | Static modal chord with quartal voicings |
| Maximum tension on dominant | V7♭9♯9♭13 (altered) |
| Bright dominant that doesn't resolve | V7♯11 (Lydian dominant) |
| Suspended sound | sus4 voicings, often with 9 |
| Full vertical color | Upper structure triads |
| Lyrical, vocal-friendly extensions | 9 and 13, mostly natural; avoid stacked alterations |

## Cross-references

- Chord spelling and qualities → `chord-construction.md`
- Functional logic underlying ii-V-I → `functional-harmony.md`
- Voice leading guide tones → `voice-leading.md`
- Voicing shapes (drop 2/3, rootless, quartal) → `assets/jazz-voicings.md`
- Modal jazz specifically → `modal-harmony.md`
- Reharmonization techniques in depth → `reharmonization.md`
- Modulation in jazz → `modulation.md`
- Jazz styles by sub-genre → `../genres/jazz-styles.md`
- Bebop melodic language → `../melody/melodic-construction.md`, `../genres/jazz-styles.md`
