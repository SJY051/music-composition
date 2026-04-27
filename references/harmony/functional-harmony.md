# Functional Harmony

Functional harmony organizes chords by the role they play in establishing and resolving tension toward a tonic. It is the dominant framework for tonal Western music — most classical music from ~1650 to ~1900, the bulk of pop, rock, country, R&B, and gospel, and conservative jazz harmony all operate inside it. Modal music and post-tonal music use different organizing principles (see `modal-harmony.md` and `techniques/20th-century-techniques.md`).

## When to consult this file

- The user asks about chord progressions, "what chord goes here", "why does X→Y sound good"
- Cadences and how to end phrases
- Diatonic motion in major or minor keys
- The bedrock harmonic logic of pop, rock, country, gospel, and most film/TV
- Explaining *why* a progression "works"

Pair with `chromatic-harmony.md` whenever non-diatonic chords (secondary dominants, borrowed chords, Neapolitan, augmented 6ths) appear. Pair with `jazz-harmony.md` for extended chords, substitutions, and ii-V-I in a jazz context. Pair with `modal-harmony.md` when the user describes music that "doesn't seem to land on a regular tonic" or uses a modal framework (Dorian rock, Mixolydian folk, Phrygian flamenco-adjacent pop).

## The three functions

Every diatonic triad in a major or minor key belongs to one of three functional groups, defined by what the chord *does* — where the ear expects it to go.

### Tonic (T) — `I`, `vi`, `iii`

The home. Tonic chords sound stable; the ear treats them as an arrival, not a question. `I` is the prototype. `vi` and `iii` share two of `I`'s three notes, so they can substitute for tonic with a softer, more bittersweet character — `vi` more clearly than `iii`. `iii` is the rarest of the three: it straddles tonic and dominant, sharing two notes with `V` as well.

In minor: `i`, `♭VI`, `♭III` play the corresponding roles.

### Predominant / Subdominant (PD or S) — `ii`, `IV`, `vi`

The chords that prepare a dominant. They generate gentle motion away from tonic. `IV` is bright and stepwise from `V`; `ii` is rougher and pulls more strongly toward `V` (its root is a fifth above `V`'s root, the strongest root motion in tonal music). `vi` is functionally ambiguous: tonic-ish in one context, predominant in another (especially when followed by `ii` or `IV`).

In minor: `iiø` (half-diminished) and `iv` are the standard predominants. `♭VI` can also serve.

### Dominant (D) — `V`, `vii°`

The strongest tension chord. The leading tone (^7) and the dominant 7th's ♭7 both want to resolve — the former up to ^1, the latter down to ^3. `vii°` is `V7` with the root removed, so it serves the same dominant function with a softer color and a leading-tone bass.

In natural minor, the V chord is minor (`v`), which has no leading tone and feels modal. To get functional dominant motion in minor, you raise ^7, producing the `V` chord and (incidentally) the harmonic-minor scale.

A typical phrase moves **T → PD → D → T**. Skipping PD is fine and common (`I → V → I`). Skipping D is rarer in classical practice but normal in pop (`I → IV → I` plagal motion). Going *backwards* (D → PD) is felt as retrograde motion and used deliberately for a stalled or static effect.

## Why functional harmony works

Three perceptual mechanisms drive the system:

1. **Leading-tone resolution.** The half-step from ^7 to ^1 is felt as gravity — the ear strongly anticipates the resolution. `V` contains ^7; `I` contains ^1.
2. **Tritone resolution.** `V7` contains the tritone between ^4 and ^7. Tritones are perceptually unstable and resolve inward (^4→^3 and ^7→^1) or outward, but most strongly inward by half-step contraction. This is why dominant 7th chords are *the* tension chord of the system.
3. **Root motion by descending fifth (or ascending fourth).** The strongest root motion in tonal music is by descending fifth (`V → I`, `ii → V`, `vi → ii`...). This generates the cycle: `iii → vi → ii → V → I`. Each step has the same kinematic feel — partly because each new chord's root was the previous chord's fifth, so there's a felt continuity.

If the user remembers nothing else: ^7 wants ^1, the tritone wants to collapse inward, and roots like to drop by a fifth.

## Cadences (essential)

A cadence is a punctuation mark — how a phrase ends. The choice of cadence determines whether the phrase feels concluded, paused, surprised, or unresolved. See `assets/cadence-reference.md` for the full table; the four most important:

- **Perfect Authentic Cadence (PAC)**: `V → I` with both chords in root position and ^1 in the soprano of the `I`. Maximum closure. The musical equivalent of a period.
- **Imperfect Authentic Cadence (IAC)**: `V → I` with weaker conditions (inverted, or ^3/^5 in the soprano). Closure, but lighter — like a comma at the end of a clause.
- **Half Cadence (HC)**: phrase ends on `V`. Sounds like a question. Often used as the antecedent in a period.
- **Deceptive Cadence**: `V → vi` (instead of expected `V → I`). The ear is surprised; tonal weight delays. Common in pop bridges and in classical dramatic moments.

Plagal (`IV → I`) is gentle and "amen"-flavored; common in rock and gospel as a soft ending. Phrygian half cadence (`iv⁶ → V` in minor) is bittersweet and archaic, common in Baroque slow movements.

## Common diatonic progressions

These are the workhorses. Memorize them, but understand they're not laws — they're high-probability patterns whose ubiquity is itself a fact about how trained ears expect to hear music.

### Major key

- **`I – IV – V – I`** — the rock/folk/country backbone. Energetic and clear.
- **`I – V – vi – IV`** ("axis progression") — the most common pop progression of the last 30 years. Bright, anthemic. Can be rotated to start on any chord (`vi – IV – I – V`, `IV – I – V – vi`, etc.); each rotation has its own emotional shading.
- **`I – vi – IV – V`** ("'50s progression" / doo-wop) — nostalgic, rolls easily.
- **`ii – V – I`** — the basic jazz cadence, but also pervasive in classical and pop. Smooth, propulsive.
- **`I – iii – IV – V`** — more lyrical/lifted than `I – IV – V – I` because the `iii` has a tonic-ish softness.
- **`I – V/vi – vi – V – I`** — tonicizes the relative minor for color. Common in film and ballads.
- **`vi – ii – V – I`** — a deferred opening; starts in the relative-minor mood and lands in major.
- **`I – V⁶ – vi – iii⁶ – IV – I⁶ – ii⁶ – V`** ("Pachelbel canon" sequence) — descending stepwise bass in long form.

### Minor key

- **`i – iv – V – i`** (with raised ^7 on `V`) — tense, classical. Note that `V` requires harmonic minor's raised ^7; `v` (natural minor) sounds modal/unfinished.
- **`i – ♭VI – ♭III – ♭VII`** (or any rotation) — the natural-minor / Aeolian rock progression. Doesn't need a leading tone; epic, modal-flavored.
- **`i – ♭VII – ♭VI – V`** ("Andalusian cadence") — descending tetrachord bass; flamenco-/Phrygian-adjacent.
- **`i – iv – ♭VII – ♭III – ♭VI – iiø – V – i`** (full minor cycle of fifths) — Bach territory.
- **`i – V – i – ♭VII – ♭VI – V`** (lament bass) — descending tetrachord again, but with the V holding the tension. Used in baroque laments and modern ballads.

## Functional harmony in pop vs. classical

Same toolkit, different priorities:

- **Classical** values voice leading, careful preparation of dissonance, and strong cadences at structural points. Functional motion is felt as the primary engine; melody emerges from the harmony.
- **Pop / rock** often inverts this — melody and groove come first, and harmony serves them. Pop tolerates static harmony (one chord for 8 bars), parallel motion, and "wrong" voice leading because the rhythm and timbre carry the energy. Pop also blurs the major/minor distinction more freely and uses modal-flavored progressions (especially Mixolydian and Aeolian) that aren't strictly functional.
- **R&B / gospel** treats functional harmony as a starting point, then enriches it with extensions, secondary dominants, modal mixture, and chromatic passing chords (see `chromatic-harmony.md` and `jazz-harmony.md`).
- **Country** is conservative — `I IV V` plus `vi` and `ii` covers most of the genre. Pedal steel and vocal harmony do the emotional work; the chords themselves stay simple.
- **Film/TV underscore** uses functional harmony for clarity in clear emotional moments (love themes, victory cues), but reaches for modal and post-tonal language for ambiguity, fear, and otherworldliness.

## Tonicization (briefly)

A *tonicization* is a moment where another diatonic chord is briefly treated as a temporary tonic, usually by inserting its dominant before it. `V/V` (the dominant of the dominant) is the most common. In C major: `D7` → `G` is `V/V → V`. The ear momentarily treats G as a local tonic, which makes the eventual return to `C` feel earned.

Full treatment is in `chromatic-harmony.md`. For functional purposes: tonicization extends the system without breaking it. Modulation (which goes further and stays in the new key) is in `modulation.md`.

## Voice leading at the cadence

Voice leading isn't strictly part of "functional harmony", but the dominant→tonic resolution depends on it. The two crucial moves at the V→I:

- **^7 → ^1** (leading tone resolves up). In `V → I` in C major: B → C. Don't double the leading tone in `V` — you'll get parallel octaves on resolution.
- **^4 → ^3** (the tritone resolves inward). In `V7 → I` in C major: F → E.

Both moves are handled automatically by sensible voice leading. Full treatment in `voice-leading.md`.

## Functional tendencies you can rely on

These are not hard rules, but they're robust enough to give the user as defaults — and to break deliberately for effect.

- **`V` strongly wants `I`**. The strongest expectation in tonal music.
- **`vii°` resolves to `I`** like `V` does, but more softly.
- **`V/x` strongly wants `x`** (any tonicization).
- **Predominants prefer `V` next**. `IV → V` and `ii → V` are extremely common; `IV → I` is plagal (also common, but feels different).
- **Chords with the leading tone (V, vii°) don't comfortably go to predominants.** Going `V → IV` in classical is a "regression" and feels stalled; in rock it's ubiquitous and fine.
- **`vi` after `V`** is the standard deception — the V→vi deceptive cadence.
- **Root motion by 2nd, 3rd, and 5th** are all common, ranked by strength: descending fifth > descending third > ascending second > the rest. Ascending fifth (e.g., I→V) is also very common as the *expected* setup move, before the descent home.

## Common pitfalls when advising

- **Don't impose classical voice-leading rules on pop.** A user writing a guitar-strummed indie song is not going to thank you for warning about parallel fifths.
- **Don't reduce every progression to function names.** Sometimes a progression *is* `vi – IV – I – V`; sometimes it's `Em – C – G – D` and the names tell the player what to do. Use whichever vocabulary the user is using.
- **Predominant doesn't have to be `IV` or `ii`.** `vi` can act predominantly. `iii` rarely does, but can. Function is contextual — a chord's role is set by what's around it.
- **Modal progressions ≠ broken functional progressions.** A song in Mixolydian (`I – ♭VII – I`) isn't a "wrong" major-key song; it's modal. Don't try to "fix" it by inserting a leading tone unless the user asks for that sound.
- **A progression isn't strong or weak in isolation.** `I – IV – I – V` sounds strong as a verse and weak as the climax. Strength is contextual.
- **Beware the phrase "this progression is sad/happy/etc."** Mode (major/minor) and tempo and instrumentation usually matter more than progression. `I – V – vi – IV` at 60 BPM with strings is "sad"; the same chords at 140 BPM with distorted guitars is "anthemic".

## Quick decision matrix

When the user wants a feeling, not a specific technique:

| User wants | Try |
|------------|-----|
| Open, anthemic, bright | `I – V – vi – IV` or `I – IV – V – I`; major key |
| Nostalgic, '50s-flavored | `I – vi – IV – V` |
| Pensive, walking | `I – iii – IV – V` or `I – V/vi – vi – IV` |
| Sad but lifted | `vi – IV – I – V` (axis rotation) |
| Mournful, classical | `i – iv – V – i` in minor |
| Epic, modal-rock | `i – ♭VI – ♭III – ♭VII` |
| Flamenco-/Phrygian-adjacent, dramatic | `i – ♭VII – ♭VI – V` (Andalusian) |
| Suspended, unresolved | end the phrase on V (HC) or on iii or vi |
| Delayed resolution | `V → vi` deceptive, then back to `V → I` next phrase |
| Static, hypnotic | one chord for many bars, or a 2-chord oscillation (`I ↔ vi`, `i ↔ ♭VII`) |

Always pair with rhythm, tempo, and timbre suggestions — chord choice alone rarely conveys the user's full intent.

## Cross-references

- Cadence catalog → `assets/cadence-reference.md`
- Standard progression catalog by mood/genre → `assets/progressions-catalog.md`
- Chromatic chords (secondary, borrowed, Neapolitan, +6) → `harmony/chromatic-harmony.md`
- Jazz extensions, ii-V-I as a jazz construct, substitutions → `harmony/jazz-harmony.md`
- Voice-leading rules → `harmony/voice-leading.md`
- Modulation (going to a new key for real) → `harmony/modulation.md`
- Modal harmony (when there's no functional motion at all) → `harmony/modal-harmony.md`
- Reharmonization (replacing functional chords with substitutes) → `harmony/reharmonization.md`
