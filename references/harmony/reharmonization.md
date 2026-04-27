# Reharmonization

Reharmonization is the act of replacing the chords of an existing piece (or section, or phrase) while keeping its melody, form, or character largely intact. It's a synthesis discipline — every reharm technique pulls from chromatic harmony, jazz substitution, modal interchange, or voice-leading reasoning. This file pulls those techniques together and frames them as decisions about *what role* the new chord plays.

## When to consult this file

- The user has a chord progression they want to rework
- "How do I make this progression more interesting"
- "Reharmonize this melody"
- Replacing chords for variety, mood change, sectional contrast (e.g., reharmonizing the bridge of an AABA tune)
- Setting up a richer arrangement of a simple song
- Jazz-style chart writing

For the underlying tools, see: `chord-construction.md` (extensions, alterations), `functional-harmony.md` (functional substitutes), `chromatic-harmony.md` (secondary dominants, modal mixture, special chords), `jazz-harmony.md` (tritone subs, ii-V chains, Coltrane). This file is the application layer.

## Why reharmonize

Three motivations cover almost every case:

1. **The melody is good but the harmony is plain or generic.** The melody has already proven itself memorable; the chords are doing the bare minimum. Reharm adds depth.
2. **The progression has been heard too many times.** Pop-songbook reharms (e.g., axis progression all the way through) feel familiar; substitution adds personality.
3. **Sectional contrast.** AABA forms benefit from reharmonizing the second A or the bridge; final choruses can feature reharm to elevate the energy or color.

## The melody is sacred

When reharmonizing under a fixed melody, every new chord must contain the melody note (or accommodate it as an extension or non-chord tone). This is the central constraint.

If the melody plays C on beat 1, your reharm chord must:
- Contain C as a chord tone (root, 3, 5, 7, etc.), OR
- Contain C as an extension (9 of B♭maj7, ♯11 of F♯ aren't the same thing — read carefully — 11 of G7sus4, etc.), OR
- Treat C as a non-chord tone that resolves quickly (passing tone, suspension, appoggiatura)

Most reharms keep the melody as a chord tone or a clear extension. NCT-treated reharm is a more sophisticated move and works best when the chord changes faster than the melody.

## Reharm by chord function — substitution within roles

The simplest reharm: replace a chord with another that performs the same function.

### Tonic substitutes

`I` can be substituted by `vi`, `iii`, or `Imaj7` (with extensions for color).

`I – IV – V – I` becomes `vi – IV – V – I` or `iii – IV – V – I`. The function is the same; the color shifts.

### Predominant substitutes

`IV` and `ii` are interchangeable as predominants. `vi` can serve too. So:

`C – F – G – C` (I-IV-V-I) becomes `C – Dm – G – C` (I-ii-V-I) or `C – Am – G – C` (I-vi-V-I, though this is heard differently because vi is also tonic-flavored).

### Dominant substitutes

`V` and `vii°` share function. `V7` for full power; `vii°` for softer dominant. In jazz, `subV7` (tritone sub) is added to the dominant family.

`G – C` becomes `Bm7♭5 – C` (vii°-derived) or `D♭7 – C` (tritone sub).

## Reharm by adding chromaticism

Take a diatonic progression and chromatically extend it.

### 1. Insert secondary dominants

Before any diatonic chord (other than `vii°`), insert its `V` or `V7`.

`C – Dm – G – C` (I-ii-V-I) → `C – A7 – Dm – G – C` (I-V/ii-ii-V-I).

The A7 tonicizes Dm. Adds drive without changing the underlying progression's logic.

Stack secondary dominants for more density: `C – E7 – A7 – Dm – G – C` (the E7 is V/vi → which would resolve to Am, but here it goes to A7 instead, which is V/ii → Dm — so you've made a chain of secondary dominants down the cycle).

### 2. Insert ii-Vs

Even more substantial than secondary dominants: insert a full `ii-V` before each chord.

`C – F – Dm – G – C` (I-IV-ii-V-I) → `C – Gm7 – C7 – F – Em7 – A7 – Dm – G – C` (I, then ii-V to F, F, then ii-V to Dm, Dm, V, I).

Now the progression has 9 chords where it had 5. Used heavily in jazz reharms of pop songs.

### 3. Borrowed chords

Replace a diatonic chord with its parallel-mode equivalent. The most common moves:

- Replace `IV` with `iv` (the "Beatles move"): `C – F – G – C` becomes `C – Fm – G – C`.
- Insert `♭VI` before `V` for cinematic color: `C – F – G` becomes `C – F – A♭ – G`.
- Use `♭VII` instead of `V` for modal flavor: `C – F – G – C` becomes `C – F – B♭ – C`.

Combine with secondary dominants for richer reharm: `C – Fm – B♭ – Cmaj7` (I – iv – ♭VII – I, with smooth voice leading).

### 4. Tritone substitution

Replace any `V7` with the dom7 a tritone away.

`C – Dm – G7 – C` → `C – Dm – D♭7 – C`. The chromatic descent (D – D♭ – C) is the gain.

In a chain: `C – A7 – Dm – G7 – C` → `C – E♭7 – Dm – D♭7 – C` (both dominants tritone-substituted; bass: C – E♭ – D – D♭ – C, mostly chromatic).

## Reharm by changing the bass line

Bass motion drives much of the perceived progression. Reharm by designing a bass line, then choosing chords that fit it.

### Stepwise descending bass

A bass that walks down stepwise from tonic to dominant (or further). Fit chords above:

C major, descending bass: `C – B – A – G – F – E – D – G`.

| Bass | Possible chord |
|------|----------------|
| C | C |
| B | G/B (V in first inversion) or Em/B |
| A | Am |
| G | C/G (I in second inversion) or G |
| F | F or Dm/F |
| E | C/E (I in first inversion) or Em |
| D | Dm or G/D (V in second inversion) |
| G | G |

The progression becomes melodic in the bass while supporting the original melody above. This is the Pachelbel-canon territory and the foundation of many ballads.

### Pedal bass

Hold a single bass note and let chords change above it. The pedal note is usually the tonic or the dominant.

Tonic pedal: `C – F/C – G/C – C – Am/C – Dm/C – G/C – C`. The bass C never moves. Used for tense static-harmony moments.

Dominant pedal: bass on G (or 5 of any tonic), various chords above. Builds tension before the resolution.

### Chromatic descending bass

Each bass note is a half-step below the previous. Find chords that work above it.

`C – G/B – Am – Am7/G – F♯m7♭5 – F – C/E – D7 – G7 – C`. Bass: C–B–A–G–F♯–F–E–D–G–C. Chromatic from C down to D.

This is a classic jazz reharm move and shows up in dozens of standards.

## Reharm by recontextualizing function

Take a chord and reinterpret it as having a different function in a different (briefly tonicized) key.

Example: a `Cmaj7` in the original progression. Reharm by treating the melody's C as the 3rd of `A♭maj7` instead — now you're momentarily in A♭ major, and the melody note serves as the chord's 3rd.

`Cmaj7 – Dm7 – G7 – Cmaj7` reharmed: `A♭maj7 – Dm7 – G7 – Cmaj7`. The first chord is no longer tonic but a chromatic mediant; melody note C is now the 3rd of A♭maj7. Suddenly the progression sounds Schubertian.

This kind of reharm is harder — you have to verify the melody fits the new chord — but yields the most striking results.

## Reharm by sequence

If the original progression repeats a phrase, reharm one of the repetitions to a different key center, then sequence it.

`Cmaj7 – Am7 – Dm7 – G7 || Cmaj7 – Am7 – Dm7 – G7` (repeating phrase) becomes `Cmaj7 – Am7 – Dm7 – G7 || E♭maj7 – Cm7 – Fm7 – B♭7`. The second half is the same progression a m3 up.

Sequential reharm is structurally satisfying — the listener perceives the parallel and feels the lift of the new key.

## Reharm by line — counterpoint reharm

Treat the upper voice (or an inner voice) as a counterpoint line and rebuild the harmony to support it. The most striking version is the **pedal-melody reharm**: a single sustained note in the melody, against shifting chords that each interpret the held note as a different chord tone or extension.

Example: the melody sustains a long `C` for four bars. Pick chords whose chord tones (or available tensions) include `C`, and design a bass line that creates motion underneath:

| Bar | Chord | `C` functions as |
|-----|-------|------------------|
| 1 | `Cmaj7` | root |
| 2 | `A♭maj7` | major 3rd |
| 3 | `Fmaj7` | 5th |
| 4 | `D♭maj7` | major 7th |

The melody `C` never moves; the harmony around it shifts through chromatic-mediant relationships. Each chord recasts the same pitch as a different chord tone, producing a constantly-changing emotional reading of one note.

Other common targets for sustained `C`:
- `Am7` — `C` is the m3 (chord tone)
- `Dm7` — `C` is the ♭7 (chord tone, very lush)
- `F♯ø7` — `C` is the ♭5 (chord tone, dark)
- `B♭maj7` — `C` is the 9 (extension)
- `E♭maj7` — `C` is the 13 (extension)

When designing a reharm under a held note, the test is strict: every chord's pitch content must contain the melody note as a chord tone, or accept it as a clearly available extension (9, 11, 13, or altered tension where idiomatic). Notes that fall on "avoid" extensions — like a natural 11 over a major 7 — produce sour clashes and break the line.

Counterpoint reharm under a *moving* upper line works the same way but with more constraints: every beat the melody changes, every chord must contain (or accept) that beat's note. Bill Evans, Brad Mehldau, and the late-Romantic harmonic tradition (Wolf, Strauss) all reward close study here.

## Reharm by texture — same chords, different feel

Sometimes "reharm" doesn't mean changing chords at all — it means changing the *voicing* and *bass position* of the existing chords.

Original: `C – Am – F – G` (close-position triads).

Reharm by texture: same chords, but voiced as `C9 – Am11 – Fmaj9 – G13sus4 – G13`, with rootless voicings and a busier bass line.

The ear hears this as significantly more interesting, even though the harmonic skeleton is identical.

## Reharm priorities — what to focus on

When reharmonizing a piece, decide what you want to *change* and what you want to *preserve*:

| Preserve | Change | Result |
|----------|--------|--------|
| Melody, function | Surface chord choices | Subtle reharm; same emotional weight, more colors |
| Melody, color | Function | Bold reharm; same notes, but a new emotional reading |
| Melody, texture | Bass line | Walking-bass reharm; jazzy |
| Melody, key | Sectional treatment | Different sections sound like different songs |
| Melody | Everything else | Full reharm; could be Brad Mehldau territory |

Most pop-style reharms preserve function and change surface. Most jazz reharms change both function and surface. Avant-garde reharms can preserve only the melodic shape.

## Less is more

The hardest discipline in reharm is restraint. A heavily reharmonized verse can feel exhausting; the listener loses track of the song. The most affecting reharms often:

- Leave most of the original progression alone
- Change the harmony at one or two key moments (the title hook, the second-A in AABA, the bridge)
- Use just enough new color to make those moments feel special

A reharm that swaps every chord can feel like exhibitionism. A reharm that swaps three chords at the perfect moments feels like genius.

## Common reharm patterns in pop and jazz

### Bridge reharm

The bridge is the most reharmonized section in popular forms. AABA bridges typically modulate to a related key and use richer harmony than the A sections.

Common moves: bridge in the relative minor, bridge in the parallel minor, bridge starting on `IV` and modulating, bridge as a ii-V-I chain.

### Final chorus reharm

The last chorus (or last A) can reharm the original progression with extensions, secondary dominants, or modulation. This signals "we've arrived" musically.

Pop final-chorus reharm: original is `I – V – vi – IV`; final chorus is `I – V/vi – vi – V/V – V – IV – I` (more chord changes, more chromatic motion) — or just modulate up a half-step.

### Outro reharm

The outro can reharm by *simplifying* — strip the extensions, repeat a single chord with variation, or land on an unresolved dominant or modal vamp. Effective when contrasted with a fully harmonized song body.

### Intro reharm

A song in C major might intro on a related key (the relative minor, a chromatic mediant), creating uncertainty before the verse's clear arrival on `C`.

## Genre notes

- **Classical (esp. Romantic)**: reharms operate at the level of variation movements and through-composed development. Late Romantic music constantly reharmonizes its own themes.
- **Jazz**: reharm is the genre. Standards exist as much for reharmonization as for melody. Bill Evans' reharms of standards are landmark.
- **Pop**: reharm is more conservative; usually applied at the bridge or final chorus. Acoustic singer-songwriters often reharm covers as a defining stylistic choice.
- **R&B / neo-soul**: heavy reharm with rich extensions and modal interchange. Stevie Wonder, D'Angelo, Robert Glasper.
- **Film/TV**: reharm of themes is the language of leitmotif. The same theme appears in different keys and harmonic contexts to reflect narrative.
- **K-pop / J-pop**: reharm at the bridge and second chorus. Often modulates and adds extensions. Sometimes reharm becomes a hook unto itself.

## Common pitfalls when advising

- **Don't reharm just to reharm.** "Make it more interesting" without a target feeling produces busy, unmotivated chords.
- **Don't lose the song.** A reharm that obscures the original progression so completely that the song loses its identity has gone too far. (Unless that's the goal.)
- **Don't put dissonant extensions in the bass.** The lowest note is the most defining; reharms that move the bass should keep the bass intervals consonant.
- **Don't ignore tempo.** A reharm that adds chord changes on every beat will work at 60 BPM and not at 140 BPM. Density is tempo-dependent.
- **Don't ignore the melody's strong notes.** Reharms that put a melody's structural note on a chord where it's a weird tension will sound wrong, even if the chord itself is fine.

## Quick decision matrix

| Want | Try |
|------|-----|
| Smoother bass motion | Slash chords / inversions / pedal bass |
| More tension before resolution | Insert secondary dominants or tritone subs |
| Wistful, "Beatles" minor color in major | Borrowed iv |
| Modal flavor | Replace V with ♭VII |
| Cinematic darkness | ♭VI inserted before V; modal mixture chords |
| Jazzy density | Insert ii-Vs before each chord |
| Sectional contrast (e.g., bridge) | Modulate to a chromatic mediant or parallel mode |
| Old Hollywood lush | Augmented 6ths approaching V |
| Schubertian magic | Reinterpret a chord via common-tone modulation |
| Gospel/R&B richness | Replace simple chords with extended (9, 11, 13), use slash chords for stepwise bass |
| Final-chorus lift | Modulate up a step or half-step |

## Cross-references

- The toolkit (functional substitutions) → `functional-harmony.md`
- Chromatic toolkit (secondary dominants, modal mixture, Neapolitan, +6) → `chromatic-harmony.md`
- Jazz substitution toolkit (tritone sub, backdoor ii-V, Coltrane) → `jazz-harmony.md`
- Modulation as reharm at the section level → `modulation.md`
- Voice leading constraints during reharm → `voice-leading.md`
- Voicings that change feel without changing chords → `chord-construction.md`, `assets/jazz-voicings.md`
- Form-level reharm (where to apply, when) → `form/popular-song-forms.md`, `form/classical-forms.md`
- Reharm in genre context → `genres/jazz-styles.md`, `genres/film-tv-scoring.md`, `genres/kpop-jpop.md`
