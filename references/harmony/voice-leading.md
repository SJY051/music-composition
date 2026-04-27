# Voice Leading

Voice leading is the discipline of moving each individual voice (line) smoothly from one chord to the next. It's the engine of tonal music. A progression that looks ordinary on paper can sound exquisite or clumsy depending on voice leading; a progression that looks adventurous can sound tame if voice-led predictably.

## When to consult this file

- The user asks how to "connect" chords smoothly
- 4-part writing, chorale style, SATB
- The user has a chord progression that "sounds clunky" or "doesn't flow"
- Questions about parallel 5ths, parallel octaves, "rules" of harmony
- Suspensions, anticipations, passing tones, neighbor tones (NCTs)
- Cadential 6/4 chords
- How jazz/pop voice leading differs from classical

For the function of chords, see `functional-harmony.md`. For chord spelling and qualities, see `chord-construction.md`. For texture/orchestration considerations, see `orchestration/voicing-and-texture.md`.

## The four voices (SATB)

Classical voice leading uses four voices, named by vocal part. Their typical ranges:

| Voice | Range (typical) | Range (extended) |
|-------|-----------------|------------------|
| Soprano | C4 – G5 | A3 – C6 |
| Alto | G3 – D5 | E3 – F5 |
| Tenor | C3 – G4 | B2 – A4 |
| Bass | E2 – C4 | C2 – E4 |

Adjacent voices should not exceed an octave apart, except bass-tenor (which may exceed an octave because the bass is registrally distinct).

These ranges are templates. Pop, jazz, and instrumental writing can be looser, but the underlying principle — keep voices in their comfort zone, avoid extremes — applies everywhere.

## Doubling rules

When writing a 4-voice texture for a 3-note triad, one note must be doubled.

| Chord type | Default double | Avoid doubling |
|------------|----------------|----------------|
| Major triad in root position | Root | Leading tone (creates parallel 8ves on resolution) |
| Major triad in first inversion | Root, soprano note, or 5th | Leading tone |
| Major triad in second inversion | Bass (the 5th) | Other notes |
| Minor triad | Root or 3rd | (no major issue) |
| Diminished triad (rare in root pos) | 3rd (the soft note) | Root or 5th (creates tritone exposure) |

In strict common-practice four-part writing, avoid doubling the leading tone (^7) in a `V` or `vii°` chord because both copies tend to resolve up to ^1, often producing exposed or parallel octaves. In pop, jazz, guitar voicings, and non-resolving textures, this is a style-aware caution rather than a universal ban.

For 7th chords, all four voices can be different, so doubling isn't required. If you do double in strict tonal writing, the root or 5th is usually safer than the 7th; doubling the 7th often creates awkward resolution because both copies tend to resolve downward.

## Motion types

Between any two voices, there are four kinds of motion:

| Motion | Definition | Example (from C-E to D-F) |
|--------|------------|---------------------------|
| **Parallel** | Both voices move in the same direction by the same interval | C-E → D-F (both up a M2; interval stays a M3) |
| **Similar** | Both voices move in the same direction by different intervals | C-E → D-G (both up, but one M2 and one P4) |
| **Contrary** | Voices move in opposite directions | C-E → B-F (one down, one up) |
| **Oblique** | One voice moves, the other stays | C-E → C-F |

Contrary motion is the most "independent" — it's the gold standard for keeping each voice melodically distinct. Similar motion is fine. Parallel motion is fine for most intervals but produces specific problems for two of them.

## The parallel-fifth and parallel-octave prohibition

In common-practice classical (Baroque through late Romantic), two prohibitions:

- **Parallel perfect fifths**: two voices that are a P5 apart moving to another P5 (e.g., C-G → D-A).
- **Parallel perfect octaves**: two voices that are a P8 apart moving to another P8 (e.g., C-C → D-D).

Why? P5 and P8 are the strongest consonances after the unison — so strong that in parallel they collapse the perception of two voices into one. The whole point of polyphony is voice independence; parallel P5s/P8s undermine that.

This is a context-specific aesthetic, not a universal rule. Where it applies and where it doesn't:

| Context | Status |
|---------|--------|
| Classical vocal counterpoint, chorale, fugue | Strictly forbidden |
| Romantic symphonic writing | Mostly avoided in 4-voice texture; tolerated in doublings (e.g., octaves between violin sections) |
| Impressionist (Debussy, Ravel) | Used deliberately for color |
| Jazz piano voicing | Tolerated and ignored |
| Rock guitar (power chords are parallel 5ths) | The whole genre runs on it |
| EDM / synth lead doubling | Routine |
| Hip-hop / lo-fi sample chops | Whatever the sample does |
| Choral pop arrangement | Avoid for SATB realism |

When advising, identify the genre frame first. Tell a metal songwriter to avoid parallel 5ths and they'll laugh.

## Hidden (or "direct") fifths and octaves

Two voices arriving at a P5 or P8 by similar motion (rather than parallel). Less serious than parallel 5ths/8ves, but in strict counterpoint they're avoided when the outer voices are involved and the soprano leaps. The detection is:

- Both voices move in the same direction
- They arrive at a P5 or P8
- The soprano didn't approach by step

Beginners don't need to memorize this — it's a refinement layer for chorale-style writing. For pop, jazz, and most film, ignore.

## Tendency tones

Some scale degrees have strong directional pull. Voice leading respects these tendencies by default and breaks them deliberately for effect.

| Tendency tone | Wants to go to | Why |
|---------------|----------------|-----|
| Leading tone (^7) in V or vii° | ^1 (up by m2) | Half-step gravity to tonic |
| 7th of dom7 (♭^7 of V7, which is ^4 of the key) | ^3 (down by m2 in major; half-step) | Tritone resolution inward |
| 7th of any 7th chord | down by step (preferably half-step, the 7th wants to "fall") | Continues the falling-7th sequence |
| ♭^6 (in minor or borrowed) | ^5 (down by m2) | Half-step gravity below |
| Chromatic neighbors (e.g., a passing ♯^4) | back to whichever scale degree they came from / are heading to | Local chromatic resolution |

In `V7 → I` (C major):
- B (^7) → C (^1) — leading tone up
- F (^4, the 7th of G7) → E (^3) — 7th down
- G (^5, common tone) — stays
- D (^2, the 9 of G7 if present) → C (^1) or E (^3) — usually steps

If the user writes a `V7 → I` and it sounds wrong, check that ^7 went up and the 7th went down. 95% of "this cadence sounds bad" problems are tendency-tone mismanagement.

## A practical 5-step workflow for voice-leading a progression

Given a chord progression, here's a systematic way to voice it.

1. **Decide the soprano line first.** What's the melody (or the top of the chordal accompaniment) doing? This is the most exposed voice and the one the listener tracks.
2. **Decide the bass line.** Often dictated by the chord progression itself (root motion). Adjust by using inversions when stepwise bass is wanted.
3. **Fill in the inner voices** (alto, tenor) by minimum motion — keep common tones, move other voices by step when possible.
4. **Resolve tendency tones.** Leading tones up, 7ths down, ♭6 down. Override only if you need a specific effect.
5. **Check for parallel 5ths/8ves and bad doublings.** Fix by re-voicing — usually by inverting one chord, or by reassigning a voice to a different chord tone.

### Worked example: G7 → C in C major, four voices

Starting voicing for `G7` (low → high): `G – F – B – D` (bass root, tenor ♭7, alto 3rd, soprano 5th — using one common arrangement). Resolving each voice:

| Voice | G7 | C | Motion |
|-------|----|----|--------|
| Soprano | D (5 of G7) | E (3 of C) | step up |
| Alto | B (3, leading tone) | C (root) | step up — leading tone resolves |
| Tenor | F (♭7) | E (3) | step down — 7th resolves down |
| Bass | G (root) | C (root) | leap up P4 |

Result on `C`: bass `C`, tenor `E`, alto `C`, soprano `E`. The 5th is omitted (a normal outcome when the leading tone and 7th both resolve correctly without doubling). All tendency tones resolved correctly. No parallel 5ths or 8ves.

If you'd prefer a `C` chord with all three triad members present, use a `G7` voicing that doubles the root and omits the 5th: `G – F – B – G` (bass root, tenor ♭7, alto 3rd, soprano root doubled). Then the resolution is:

| Voice | G7 | C |
|-------|----|----|
| Soprano | G | G (common tone, the 5th of C) |
| Alto | B | C |
| Tenor | F | E |
| Bass | G | C |

Result: complete `C` triad with doubled root. This is the textbook resolution shown in most harmony classes — tendency tones resolved, no parallels, every triad member present.

## Cadential, passing, and neighboring 6/4 chords

Second-inversion triads (6/4 chords) are unstable in classical practice. They're used in three specific contexts:

- **Cadential 6/4**: a `I⁶/₄` over a dominant bass, immediately resolving to `V` (or `V7`). Functionally, the chord is *not* tonic; it's a dominant decorated by suspensions. Notation: sometimes shown as `V⁶/⁴–⁵/³` to clarify the 6/4 is a delay of the V.
- **Passing 6/4**: connects two chords via stepwise bass motion. E.g., `I` → `V⁶/₄` → `I⁶`. The bass walks up or down stepwise, and the 6/4 is just a passing harmony.
- **Neighboring 6/4** (sometimes "pedal 6/4"): bass stays, upper voices oscillate. E.g., `I` → `IV⁶/₄` → `I` over a held tonic bass. Embellishment, not real motion.

In pop and rock, slash chords with the 5th in bass are routine and don't need this categorization — the listener doesn't expect classical voice-leading expectations.

## Suspensions, anticipations, and other non-chord tones

Non-chord tones (NCTs) are notes that don't belong to the chord at the moment they sound. They create melodic interest and small dissonances that resolve to consonance.

### Suspensions

A note is held over from the previous chord into the new one, becomes dissonant, then resolves down by step.

Three steps: **preparation** (consonance in the previous chord) — **suspension** (dissonance with the new chord) — **resolution** (down by step to consonance).

Common suspension types (named by the interval above the bass at the suspension and the resolution):

| Type | Example | Notes |
|------|---------|-------|
| 4–3 | Bass C, voice held on F resolves to E | Most common; "suspended 4" |
| 7–6 | Bass C, voice held on B resolves to A | Common in renaissance |
| 9–8 | Bass C, voice held on D resolves to C | Less stable; 9-8 over a root is sometimes weak |
| 2–3 | Suspension in the bass (rare) | Bass D held into chord wanting C; resolves up to E (if upper voices are spelled to make the dissonance an interval of 2 above bass) |

Pop/rock: the `sus4` chord (`Csus4` → `C`) is functionally a 4-3 suspension, and resolving it is the same operation. Pop often *doesn't* resolve `sus4`, treating it as its own color — that's a stylistic choice, not a voice-leading mistake.

### Anticipation

The next chord's note arrives early. Common in pop and gospel:

`G7 → C` where the soprano sings B → (C arrives on the "and" of beat 4 before the actual chord change on beat 1) → C continues.

Anticipations release tension early and create a forward-leaning feel. Almost always at cadences.

### Passing and neighbor tones

- **Passing tone** — fills in stepwise between two chord tones. C → D → E (D is passing).
- **Neighbor tone** — steps to a non-chord tone and returns. C → D → C (D is upper neighbor) or C → B → C (lower neighbor).

These are weak NCTs (barely felt as dissonance). They're the connective tissue of melodic lines.

### Appoggiatura

A leap to a non-chord tone that resolves by step (usually down). The dissonance is *emphasized* — landed on, lingered on, then released. Appoggiaturas are emotional. The opening of "Yesterday" is appoggiatura-heavy.

### Escape tone (échappée)

A stepwise motion away from a chord tone, then a leap in the opposite direction to the next chord tone. C → D → A. The D is the escape tone. Less common than the others; classical filler.

## A 9-item voice-leading checklist for problem progressions

When a user's progression sounds clumsy, walk through:

1. Are tendency tones resolving? (Leading tones up, 7ths down.)
2. Any parallel 5ths or 8ves? (In styles that care.)
3. Any doubled leading tones?
4. Inner voices moving by leap when they could be moving by step?
5. Voice crossing (alto going below tenor, etc.)? Avoid in chorale style; OK in some textures.
6. Voice overlap (one voice moving past where the next-higher voice was)? Same — avoid in chorale, fine in some textures.
7. Bass line leaps too much? Stepwise bass usually feels smoother; consider inversions to walk the bass.
8. Soprano line directionless? Even chordal accompaniments benefit from a top voice that has shape.
9. Common tones not held? Holding common tones between chords reduces unnecessary motion and clarifies the harmony.

## Jazz voice leading

Jazz uses voice leading as the glue between extended chords, but with different priorities:

- **Guide tones** are the most important voices: the 3rd and the 7th of each chord. They define the chord's quality. In a ii–V–I progression, the guide tones move chromatically: in C major, Dm7 has F and C, G7 has F and B, Cmaj7 has E and B. So one guide tone holds (B in G7 → B in Cmaj7), the other moves by half-step (F in Dm7 → F in G7 → E in Cmaj7).
- **Rootless voicings** put guide tones on the bottom and tensions on top. The bass player handles roots.
- **Drop voicings** (drop 2, drop 3) are derived by taking a close-position chord and dropping a voice an octave to add air.
- **Parallel motion is fine.** Parallel 9th chords moving in parallel are a McCoy Tyner specialty.

See `jazz-harmony.md` and `assets/jazz-voicings.md`.

## Pop and rock voice leading

Even more relaxed:

- Power chords are parallel P5s by design.
- Chord shapes (e.g., open chords on guitar) determine voicing more than abstract voice-leading concerns.
- The vocal melody is the soprano and is composed independently of the chord voicings.
- Pad and synth layers often move in parallel for thickening, not voice independence.

Pop voice-leading wisdom is largely about: keep the bass musical; avoid muddy low intervals; keep one or two common tones between chords if possible to reduce "jumpy" feel.

## Modal and contemporary voice leading

In modal music, the leading-tone resolution is gone (no leading tone in most modes), so voice-leading focuses on the characteristic notes of the mode. Parallel motion is more accepted because the music isn't governed by tendency tones.

In post-tonal music (12-tone, atonal), voice leading is about register, contour, and pitch-class proximity, not tonal function. Composers often think in terms of voice-leading distance (how many semitones each voice moves) — a "smooth" voice leading minimizes total motion.

## Cross-references

- Functional context (why tendency tones tend) → `functional-harmony.md`
- Specific chord shapes and their voicings → `chord-construction.md`, `assets/jazz-voicings.md`
- Voicing across instruments → `orchestration/voicing-and-texture.md`
- Chromatic voice-leading patterns (line clichés, descending chromatic basses) → `chromatic-harmony.md`
- Jazz-specific voice leading → `jazz-harmony.md`
- 20th-century voice leading (parsimonious, neo-Riemannian) → `techniques/20th-century-techniques.md`
