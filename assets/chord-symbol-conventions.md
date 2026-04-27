# Chord Symbol Conventions

Quick lookup for chord symbol notation across the four main systems used in Western music — jazz lead sheets (Real Book style), pop / commercial lead sheets, Roman numeral analysis, and the Nashville Number System. Different traditions write the same chord differently, and the same symbol can mean different things in different traditions. This file maps the territory.

For chord *construction* (what notes are in each chord), see `references/harmony/chord-construction.md`. For chord *function* (what each chord does in a key), see `references/harmony/functional-harmony.md`. For Roman numeral analysis applied to actual progressions, see `references/analysis.md`.

## The four systems at a glance

| System | Used by | Tells you | Example |
|--------|---------|-----------|---------|
| Real Book / jazz | Jazz musicians, leadsheet players | Specific pitches | `Cmaj7`, `D-7`, `G7♭9` |
| Pop lead-sheet | Pop, rock, gospel, R&B charts | Specific pitches | `Cmaj7`, `Dm7`, `G7♭9` |
| Roman numeral | Analysts, classical theorists | Function in a key | `IΔ`, `ii7`, `V7♭9` |
| Nashville Number System | Nashville session work, country | Function in a key, transposable | `1Δ`, `2m7`, `5 7♭9` |

The first two specify pitches and require you to know the key separately. The last two specify function (relative to a tonic) and require you to know the key to derive pitches. Each is correct for its purpose.

## Triad symbols

| Quality | Real Book / jazz | Pop / lead-sheet | Roman (in C major) | Nashville (in C) |
|---------|------------------|------------------|---------------------|--------------------|
| Major | `C` | `C` | `I` | `1` |
| Minor | `C-` or `Cmi` | `Cm` | `i` (in C minor) or `vi` (as A minor in C major) | `1m` |
| Diminished | `C°` or `Cdim` | `Cdim` or `C°` | `i°` or `vii°` (depending on degree) | `1°` |
| Augmented | `C+` or `Caug` | `Caug` or `C+` | `I+` (rare; usually as borrowed) | `1+` |
| Suspended 4 | `Csus` or `Csus4` | `Csus4` | (no standard RN) | `1sus` |
| Suspended 2 | `Csus2` | `Csus2` | (no standard RN) | `1sus2` |

## Seventh chord symbols

| Quality | Real Book / jazz | Pop / lead-sheet | Notes (root C) |
|---------|------------------|------------------|----------------|
| Major 7 | `CΔ` or `Cmaj7` or `CM7` | `Cmaj7` | C E G B |
| Dominant 7 | `C7` | `C7` | C E G B♭ |
| Minor 7 | `C-7` or `Cmi7` | `Cm7` | C E♭ G B♭ |
| Half-diminished 7 | `Cø7` or `Cø` | `Cm7♭5` | C E♭ G♭ B♭ |
| Fully diminished 7 | `C°7` | `Cdim7` | C E♭ G♭ B𝄫 (= A) |
| Minor-major 7 | `C-Δ` or `CmiΔ` | `CmMaj7` or `Cm(maj7)` | C E♭ G B |
| Augmented major 7 | `C+Δ` or `Cmaj7♯5` | `Cmaj7♯5` | C E G♯ B |
| Augmented 7 | `C+7` or `C7♯5` | `C7♯5` | C E G♯ B♭ |
| Dominant 7 sus4 | `C7sus` or `C7sus4` | `C7sus4` | C F G B♭ |

The biggest jazz–pop divergence is the major 7: jazz often writes `Δ` (delta) where pop writes `maj7`. Both are unambiguous in context; the agent should match whichever the user is using.

## Extension and alteration symbols

Same across systems, with minor formatting variation:

| Symbol | Meaning | Example chord |
|--------|---------|---------------|
| `9` | Add the 9th to a 7th chord | `Cmaj9` = C E G B D |
| `11` | Add the 11th | `Cm11` = C E♭ G B♭ D F |
| `13` | Add the 13th (and usually 9, sometimes 11) | `C13` = C E G B♭ D A (11 usually omitted) |
| `add9` | Add the 9th to a triad (no 7th) | `Cadd9` = C E G D |
| `add11` | Add the 11th to a triad | `Cadd11` = C E G F |
| `6` | Add the 6th to a triad (no 7th) | `C6` = C E G A |
| `6/9` | Add 6th and 9th to a triad | `C6/9` = C E G A D |
| `♭5` | Lower the 5th | `C7♭5` = C E G♭ B♭ |
| `♯5` | Raise the 5th | `C7♯5` = C E G♯ B♭ |
| `♭9` | Lower the 9th (in 7th-chord context) | `C7♭9` = C E G B♭ D♭ |
| `♯9` | Raise the 9th | `C7♯9` = C E G B♭ D♯ |
| `♯11` | Raise the 11th (often `= ♭5` enharmonically) | `Cmaj7♯11` = C E G B F♯ |
| `♭13` | Lower the 13th (often `= ♯5` enharmonically) | `C7♭13` = C E G B♭ A♭ |
| `alt` | Available altered tensions on a dominant | `C7alt` = C E B♭ plus a subset of D♭, D♯, G♭/F♯, A♭; the natural 5 is often omitted or context-dependent |

`b` and `#` are commonly substituted for `♭` and `♯` in plain-text contexts (e.g., `Cb9`, `C#11`). Both are universally understood.

## Slash chords

`X/Y` means chord X with bass note Y. Used in all four systems.

| Notation | Meaning | Example |
|----------|---------|---------|
| `C/E` | C major triad with E in the bass | First inversion of C major |
| `C/G` | C major triad with G in the bass | Second inversion |
| `C7/B♭` | C7 with B♭ in the bass | Third inversion of C7 |
| `F/G` | F major triad over G bass | "Slash chord" — not a chord tone of F; functions like a G dominant suspension |
| `C/D` | C major triad over D bass | Functions like D9sus4 |

In Roman numerals, slash chords use figured-bass numerals (`I⁶` = first inversion, `I⁶/⁴` = second inversion, etc.) instead of letter slashes for inversions, but reserve the letter-slash notation for non-chord-tone bass notes (`I/♭^7` or written explicitly).

In Nashville, slash chords use the same `/` notation: `1/3` (first inversion of I), `5/7` (V with leading tone in bass — note: `7` here means scale degree, not the 7th of the chord).

## Polychords

A polychord stacks two triads. Notation: `top / bottom` with a horizontal line (or `top|bottom` in plain text).

```
   D
  ───   = D major triad over C major triad
   C
```

Plain-text equivalents: `D/C` (ambiguous — can be read as a slash chord) or `D|C` (clearer). When ambiguity matters, write out: "D triad over C triad".

Polychords are mostly used in jazz, post-tonal, and film music. The bottom triad is usually the "root" function; the upper triad provides extensions and color. See `harmony/chord-construction.md` for upper structure triad use.

## Roman numeral specifics

| Symbol | Meaning |
|--------|---------|
| Capital (`I`, `IV`, `V`) | Major triad on that scale degree |
| Lowercase (`i`, `iv`, `v`) | Minor triad |
| `°` (`vii°`) | Diminished triad |
| `+` (`III+`) | Augmented triad |
| `7`, `9`, `11`, `13` after numeral | 7th-chord with that extension (`V7`, `ii⁹`) |
| Figured bass numerals (`⁶`, `⁶/⁴`, `⁶/⁵`, `⁴/³`, `⁴/²`) | Inversions |
| `♭` or `♯` prefix | Chromatic alteration of scale degree (`♭VI`, `♯iv°`) |
| `/` | Tonicization (`V/V`, `V7/vi`) |
| `N⁶` | Neapolitan 6 (= ♭II⁶) |
| `It⁶`, `Fr⁶`, `Ger⁶` | Italian, French, German augmented 6th chords |

Always specify the key context. `ii` means D minor in C major, but B♭ minor in A♭ major.

## Nashville Number System specifics

| Notation | Meaning |
|----------|---------|
| `1`, `4`, `5` | Major triads on those degrees (in major key) |
| `2m`, `3m`, `6m` | Minor triads |
| `7°` | Diminished triad on ^7 |
| `1Δ`, `4Δ` | Major 7 chords |
| `2m7`, `5 7` | 7th chords (note the space before `7` for dom7) |
| `1/3`, `5/7` | Inversions (number after slash = scale degree in bass) |
| `b3`, `b6`, `b7` | Borrowed chords (♭III, ♭VI, ♭VII) |
| `(1 4 / 5 6m)` | Parentheses for "two chords per bar" (1 and 4 in first half, 5 and 6m in second) |
| Diamond shapes around numbers | Held / sustained chord (long note) |
| Dot above number | Pushed chord (anticipated by an eighth) |

Nashville charts also use rhythmic shorthand (split bars, push notation, hits, kicks) that varies between charters. When in doubt, ask for the chart's legend.

## Common ambiguities and how to read them

A few notations look ambiguous out of context. The agent should ask if the answer matters:

| Symbol | Possible meanings | How to disambiguate |
|--------|-------------------|---------------------|
| `C-` | C minor (jazz convention) **or** C with no quality specified (rare) | Almost always means minor in jazz contexts |
| `Cm7` | C minor 7 **or** (extremely rarely) C with seventh as `m`-some-extension | Always C minor 7 in modern usage |
| `Cmaj` | C major triad **or** C major 7 (informal shorthand) | Triad in formal contexts; ambiguous in casual lead sheets — assume triad unless context implies 7 |
| `C7-5` or `C7−5` | C7♭5 (older notation using `-` for flat) | Older Real Books; modern usage prefers `C7♭5` |
| `C+` | C augmented triad **or** C with raised 5 (informal for `Cmaj7♯5` or similar) | Triad in classical/jazz; ambiguous in older fake books |
| `C2` | `Csus2` (informal) **or** `Cadd2` (= add9) | Usually means sus2 in pop guitar charts; `Cadd9` is unambiguous |
| `Cmaj7/9` | Cmaj9 (older notation) | Modern: `Cmaj9` |
| `C5` or `C(no3)` | C power chord (root + 5th, no 3rd) | `C5` is the standard rock notation; `C(no3)` is explicit. `C(no5)` means the fifth is omitted, so it is **not** a power chord. |

When the user writes a symbol that's ambiguous and the answer matters, ask. When it doesn't matter (the surrounding context fixes the interpretation), just proceed.

## Mapping a chord across systems

Quick translation. Same chord, four ways to write it:

C major key, the chord is **G dominant 7**:

| System | Notation |
|--------|----------|
| Real Book / jazz | `G7` |
| Pop / lead-sheet | `G7` |
| Roman numeral (in C major) | `V7` |
| Nashville (in C) | `5 7` |

C major key, the chord is **F minor with major 7th** (borrowed iv with raised 7):

| System | Notation |
|--------|----------|
| Real Book / jazz | `F-Δ` |
| Pop / lead-sheet | `Fm(maj7)` |
| Roman numeral | `iv(maj7)` (with implied modal mixture) |
| Nashville | `4m(maj7)` |

C major key, the chord is **D♭ dominant 7 substituting for V7**:

| System | Notation |
|--------|----------|
| Real Book / jazz | `D♭7` |
| Pop / lead-sheet | `Db7` |
| Roman numeral | `subV7/I` or `♭II7` |
| Nashville | `b2 7` |

## Common pitfalls when advising

- **Match the user's notation.** Don't translate `Cmaj7` to `CΔ` (or vice versa) without reason. The user picked their system for a reason.
- **Don't mix systems within one chart.** A chart with both Roman numerals and chord letters is hard to read.
- **Be careful with `m` vs `-` for minor.** Both are universal, but a chart that uses both inconsistently is confusing.
- **Don't assume `b` means flat in all contexts.** In some chord-naming software, `b` can be parsed as a note letter B. Use `♭` when typesetting allows.
- **Check key context before interpreting Roman numerals.** A chart in `B♭ major` writes the same `ii-V-I` as a chart in `C major`, but the actual chords are different.
- **Nashville `7` is ambiguous between scale degree and chord 7th.** `5 7` means "V dominant 7" (scale degree 5 with a 7th added). `7°` means "vii dim" (the chord on scale degree 7). Position and spacing matter.

## Cross-references

- Chord construction (what notes are in each chord) → `references/harmony/chord-construction.md`
- Functional analysis with Roman numerals → `references/harmony/functional-harmony.md`, `references/analysis.md`
- Notation conventions in scores generally → `references/fundamentals/notation-and-conventions.md`
- Jazz-specific chord vocabulary → `references/harmony/jazz-harmony.md`
- Voicings (the same chord rendered different ways) → `jazz-voicings.md`, `references/orchestration/voicing-and-texture.md`
- Common chord progressions across systems → `progressions-catalog.md`
