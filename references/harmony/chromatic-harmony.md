# Chromatic Harmony

Chromatic harmony introduces notes outside the prevailing key without leaving the key. The diatonic system gets enriched with borrowed colors, secondary tonal centers, and chromatic voice-leading chords. This is the layer that turns a workmanlike progression into one that feels searching, lush, or surprising.

## When to consult this file

- The user wants more harmonic color without changing keys
- "What's a secondary dominant", "what's modal mixture", "what's a Neapolitan"
- A specific chromatic chord appears in analysis
- The user asks how to sneak surprise into an otherwise diatonic progression
- Songwriting goals like "wistful", "yearning", "dramatic", "old-Hollywood" — chromatic harmony is the most common toolkit

This file does not cover full key change. For that, see `modulation.md`. For chromatic harmony in jazz idiom (with extensions and substitution), see `jazz-harmony.md`. For "outside" without functional logic, see `modal-harmony.md` and `techniques/20th-century-techniques.md`.

## The four chromatic toolkits

Almost every chromatic chord falls into one of four families. They overlap, but it's a useful map:

1. **Tonicization** — apply functional dominant motion to a chord that isn't tonic. Secondary dominants, secondary leading-tone chords.
2. **Modal mixture (borrowing)** — borrow chords from the parallel mode (most often parallel minor in major keys).
3. **Special chromatic chords** — Neapolitan, augmented 6ths, common-tone diminished, common-tone augmented.
4. **Chromatic mediants** — chords whose roots are a third away and which share a chromatic third relationship.

## Tonicization

A *tonicization* briefly treats a non-tonic diatonic chord as a temporary tonic by approaching it via its own dominant (or leading-tone chord). The "key" of the music doesn't change — the moment passes — but the local sense of arrival on the tonicized chord adds weight.

### Secondary dominants

A secondary dominant is a `V` (or `V7`) of a non-tonic chord. Notation: `V/x` reads "V of x". Built by taking the chord that's a perfect 5th *above* the target.

In C major, the diatonic chords (other than `vii°`, which is itself dissonant) can each be tonicized:

| Target | Secondary dominant | Notes (C major) | Chord |
|--------|--------------------|-----------------| ------|
| ii (Dm) | V/ii | A C♯ E (G) | A or A7 |
| iii (Em) | V/iii | B D♯ F♯ (A) | B or B7 |
| IV (F) | V/IV | C E G B♭ | C7 (the only secondary that doesn't introduce a new note for the triad — the ♭7 makes it dominant) |
| V (G) | V/V | D F♯ A (C) | D or D7 |
| vi (Am) | V/vi | E G♯ B (D) | E or E7 |

`V/vii°` doesn't exist functionally (you don't tonicize an unstable chord).

The diagnostic for a secondary dominant: a major or dominant 7 chord whose root is a P5 above another diatonic chord, immediately followed by that chord.

In progression: `C – A7 – Dm – G7 – C` is `I – V7/ii – ii – V7 – I`. The A7 tonicizes Dm by introducing C♯ (the leading tone to D), creating a momentary ii-becomes-tonic feeling.

### Secondary leading-tone chords

Same idea, but using a `vii°` instead of `V`. Notation: `vii°/x`.

`vii°/V` in C major = F♯° (F♯ A C). It contains the leading tone of G (F♯) and resolves to G with the same dominant function as `V/V`, but with a softer color (no real root motion of a fifth — the bass moves by half-step).

Secondary leading-tone chords are common when you want chromatic voice leading without the strong root motion of `V/x`.

### Where secondary dominants and leading-tone chords go

Almost always to their target. A `V/V` that doesn't go to V is just a chromatic chord — the listener will hear it as a deception or modulation. The functional power of these chords *is* their resolution to the target.

Common patterns in progressions:

- **`I – V/V – V – I`** — the most common chromatic insertion. Adds drive to the cadence.
- **`I – V/vi – vi – IV – V – I`** — tonicizes the relative minor briefly. Common in ballads, film.
- **`I – V/IV – IV – V – I`** — the V/IV (which is a I7 chord; e.g., C7 in C major) is a blues-flavored move.
- **`vi – V/V – V`** — using the V/V as a predominant.

### Tonicizing in the cycle of fifths

A long cycle-of-fifths sequence can be reinterpreted with secondary dominants at every step:
`I – V/vi – vi – V/ii – ii – V – I` becomes a chromatic sequence where every chord is briefly tonicized before passing on. This is a Bach-flavored move; a slowed-down version is also common in jazz ("ii-V chains").

## Modal mixture (borrowing)

Modal mixture borrows chords from the parallel mode. In a major key, that's the parallel minor (C major borrows from C minor). In a minor key, it's borrowing from parallel major (less common, but real — most often the Picardy third).

### Borrowed chords from parallel minor (in major keys)

| Borrowed chord | What it is in C major | Source in C minor | Effect |
|----------------|----------------------|-------------------|--------|
| `iv` | F minor (F A♭ C) | iv of C minor | Wistful, "smiling-through-tears"; the most common borrowed chord |
| `♭III` | E♭ major (E♭ G B♭) | ♭III of C minor | Bittersweet, distant, sometimes heroic |
| `♭VI` | A♭ major (A♭ C E♭) | ♭VI of C minor | Dark, cinematic, "Hollywood" |
| `♭VII` | B♭ major (B♭ D F) | ♭VII of C minor | Modal, rock-flavored, plagal-direction motion |
| `iiø7` | Dm7♭5 (D F A♭ C) | iiø7 of C minor | Approach to V with darker color |
| `vii°7` (with ♭6) | B D F A♭ | vii°7 of harmonic minor | Stronger leading-tone chord |

Borrowed chord progressions:

- **`I – ♭VI – ♭VII – I`** — the "lift" progression. Common in cinematic pop, anthemic rock.
- **`I – iv – I`** — minor plagal cadence. The Beatles, R&B.
- **`I – V – ♭VI – V`** — the deceptive cadence taken further; very dramatic.
- **`I – ♭III – IV – I`** — modal-flavored, hovering between major and minor.

### Borrowed dominants

Sometimes a borrowed `V` from parallel minor is used. `Vsus♭9` or `V7♭9` borrows ♭6 from minor. Adds darkness to the dominant.

### Picardy third (and the reverse)

The Picardy third is a major tonic chord at the end of a minor-key piece. It's a borrowing from parallel major used at the cadence — purely for effect. Common in Baroque and modern adaptations.

The reverse (minor tonic ending a major piece) is rarer but used — a sudden plunge into minor at the end can be devastating.

## Special chromatic chords

### The Neapolitan (♭II)

A major chord built on the lowered second scale degree. In C major: D♭ major (D♭ F A♭). Almost always in first inversion (`♭II⁶`), with F in the bass.

Functions as a *predominant* — substitutes for `ii` or `iv`. Resolves to V (or V7), then to I.

`I – ♭II⁶ – V – I` is the classic Neapolitan progression. The bass typically walks: C → F → G → C, all stepwise except the last fifth.

In minor, the Neapolitan is even more at home — `♭II⁶` is closely related to the iv chord in minor, and the chromatic descent ♭2 → 1 echoes the Phrygian flavor.

Effect: dramatic, slightly archaic, intensifies the predominant before V. Beethoven uses it constantly.

### Augmented 6th chords

Three chords that are essentially predominants with a chromatic kick — they're built specifically to drive into V via a half-step pull from both sides.

The defining interval is the **augmented 6th** between ♭6 (in the bass) and ♯4 (in an upper voice). When this interval expands outward by half-step in each voice, it lands on the octave at scale degree 5 — i.e., the root of `V`. So the chord tightly pulls into `V`.

The three flavors differ in what's between the ♭6 and ♯4:

| Type | Notes (in C major resolving to V=G) | Other notes |
|------|-------------------------------------|-------------|
| **Italian (It⁶)** | A♭ (♭6) – C – F♯ (♯4) | Just the 3rd added |
| **French (Fr⁶)** | A♭ – C – D – F♯ | Add a 4th above the bass (D, the ^2) — has a whole-tone quality |
| **German (Ger⁶)** | A♭ – C – E♭ – F♯ | Add a m3 above the 3rd (E♭, the ♭3) — sounds almost identical to a dominant 7 chord on A♭, hence enharmonic potential for modulation |

All three resolve to `V`, with the ♭6 → ^5 down by half-step and the ♯4 → ^5 up by half-step (so they collide on the octave at ^5). The German 6th creates parallel 5ths going to V, traditionally avoided by routing through a cadential 6/4 (`Ger⁶ → I⁶/₄ → V`).

Effect: highly dramatic, pre-cadential, nineteenth-century operatic. Wagner uses augmented 6ths heavily.

### Common-tone diminished and common-tone augmented

A diminished 7 chord that shares a *common tone* with the chord that follows. Often written `°7` with the implicit understanding that it's a passing/embellishing function.

In C major, `C°7` (C E♭ G♭ B𝄫) — sharing the common tone C — embellishes a Cmaj7 chord. Used as a passing chord to delay or color the resolution.

Similarly, an augmented chord can share a common tone and provide a chromatic step-up to a target chord.

These are decorative chromatic harmonies, not functional — they're voice-leading flourishes.

### Chromatic mediants

Two chords whose roots are a third apart and share a chromatic relationship. Examples in C:

- C major → E major (chromatic third up)
- C major → A♭ major (chromatic third down)
- C major → E♭ major (also chromatic — borrowed ♭III)
- C major → A major (chromatic — V/ii context, or just chromatic mediant)

Chromatic mediants don't have strong functional drive; they're used for *color*. Schubert, Liszt, late Romantic, and film composers love them. The harmony "swerves sideways" rather than going through dominant logic.

`C → A♭ → C` (I – ♭VI – I) is bittersweet.
`C → E → C` (I – III – I) is uncanny, magical.

These are also the root motions used in neo-Riemannian theory (P, L, R, and chained transformations) — see `techniques/20th-century-techniques.md`.

## Chromatic voice-leading patterns

Several common chromatic moves work as patterns the agent should recognize:

### Line clichés

A static chord with a chromatically descending (or ascending) inner line. Iconic example: a C minor chord with a line moving C → B → B♭ → A → A♭ → G in an inner voice.

This produces the chord sequence `Cm – Cm(maj7) – Cm7 – Cm6 – Fm/A♭ – Cm` (the line cliché). The inner voice walks `C → B → B♭ → A → A♭ → G` while the bass usually pedals on `C` (or moves to `A♭` for the fifth chord). Used in James Bond themes, "Stairway to Heaven", "Michelle", "My Funny Valentine". Adds drama through static harmony with internal motion.

### Descending chromatic bass

A bass line that walks down by half-step under any chord progression. Common pattern in C: `C – G/B – Am – Am7/G – F♯ø7 – F – C/E – D7 – G7 – C`. The bass: C–B–A–G–F♯–F–E–D–G–C.

### Chromatic ascending bass (less common but striking)

Bach uses this. Also common in modern rock and film.

### Plagal chromaticism (the IV-iv-I move)

`IV – iv – I`. The major IV with chromatic descent in an inner voice (often A → A♭ → G in the example C major). One of the most affecting moves in pop. The Beatles' "In My Life" and many others.

## Genre notes

- **Classical (Baroque)**: secondary dominants, Neapolitan, line clichés.
- **Classical (Romantic)**: aggressive chromatic harmony — augmented 6ths, chromatic mediants, modal mixture, deceptive cadences. Wagner, Liszt, Brahms, Mahler.
- **Jazz**: chromatic harmony is built into the language — secondary dominants are constant, modal mixture pervasive. See `jazz-harmony.md`.
- **Pop/rock**: modal mixture (especially `iv` and `♭VI/♭VII`) is everywhere; secondary dominants are less common but appear in 50s/60s songwriting and modern singer-songwriter.
- **R&B/neo-soul**: rich chromatic harmony, often with extensions stacked on borrowed chords. Stevie Wonder, D'Angelo.
- **Film/TV**: chromatic mediants and modal mixture are the language of suspense, wonder, and emotional depth. The "hero's journey" minor-to-major modal mixture is a cliché for a reason.
- **K-pop/J-pop**: heavy modal mixture, especially in bridges and pre-choruses. Borrowed `iv` is ubiquitous in ballads.

## Common pitfalls when advising

- **Don't suggest chromatic chords without justifying their resolution.** A Neapolitan that doesn't go to V is just a confusing chord.
- **Modal mixture is most effective when sparing.** A song that borrows `iv`, `♭VI`, `♭VII`, *and* `♭III` in the same chorus loses the contrast that makes any individual borrowing feel special.
- **Augmented 6ths are register-sensitive.** Voiced in low register they're muddy. Keep the ♯4 high enough to be heard.
- **Secondary dominants need rhythmic space.** Cramming `V/ii – ii – V/V – V – I` into one bar feels rushed; give each tonicization at least a beat to register.
- **Don't reduce all chromatic chords to "tension".** Chromatic chords have specific colors. `iv` is wistful; `♭VI` is heavy; `♯iv°` is brittle. Choose for the affect, not generic "more interesting".

## Quick decision matrix — chromatic chord by mood

| Want | Try |
|------|-----|
| Wistful, "smiling through tears" | Borrowed `iv` in major |
| Lifted, anthemic dark | `♭VI` and `♭VII` (in major) |
| Old Hollywood, lush | Augmented 6ths approaching V |
| Magical, uncanny | Chromatic mediant (e.g., I → III in major) |
| Driving, urgent cadence | Secondary dominant `V/V` |
| Bittersweet, archaic | Neapolitan `♭II⁶ – V – I` |
| Bluesy in a major key | `V/IV` (which is the I7) |
| Suspenseful, hovering | Common-tone diminished |
| Cinematic surprise | Deceptive cadence to `♭VI` instead of `vi` |

## Cross-references

- Functional context (why these chords resolve where they do) → `functional-harmony.md`
- Voice-leading specifics (especially augmented 6th resolution) → `voice-leading.md`
- Modulation (when the chromaticism stays — full key change) → `modulation.md`
- Modal music (when there's no functional motion to chromatically embellish) → `modal-harmony.md`
- Jazz extensions and substitutions (which use secondary dominants and tritone subs heavily) → `jazz-harmony.md`
- Reharmonization techniques that draw on chromatic harmony → `reharmonization.md`
- Chromatic mediants and neo-Riemannian transformations → `techniques/20th-century-techniques.md`
