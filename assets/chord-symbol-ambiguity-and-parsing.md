# Chord Symbol Ambiguity and Parsing

Use this asset when the user gives chord symbols that could be read in more than one way, or when the agent needs to translate a chord symbol into concrete notes. This file complements `chord-symbol-conventions.md`; it is more operational and parser-like.

## Default assumption

For user-facing composition help, assume **lead-sheet chord symbols** unless the user clearly asks for Roman numerals, Nashville numbers, figured bass, or post-tonal labels.

When ambiguity does not affect the answer, proceed and name the assumption. When ambiguity affects the notes, ask or provide both readings.

## Parse order for lead-sheet symbols

Read a chord symbol in this order:

1. **Root** — `C`, `D♭`, `F♯`, etc.
2. **Core quality** — major, minor, diminished, augmented, sus2, sus4, power/no3.
3. **Seventh quality** — dominant 7, major 7, minor 7, diminished 7, half-diminished.
4. **Extensions** — 9, 11, 13.
5. **Alterations** — ♭5, ♯5, ♭9, ♯9, ♯11, ♭13.
6. **Add/omit instructions** — add9, no3, no5, omit5.
7. **Bass note** — slash chord after `/`.

## Quick parser table from C

| Symbol | Core reading | Notes |
|---|---|---|
| `C` | major triad | C E G |
| `Cm` / `C-` | minor triad | C E♭ G |
| `Cdim` / `C°` | diminished triad | C E♭ G♭ |
| `Caug` / `C+` | augmented triad | C E G♯ |
| `Csus4` / `Csus` | suspended 4th | C F G |
| `Csus2` | suspended 2nd | C D G |
| `C5` | power chord | C G |
| `C(no3)` | no third; usually power-chord-like | C G |
| `C(no5)` | omit fifth | C E |
| `C7` | dominant 7 | C E G B♭ |
| `Cmaj7` / `CΔ` | major 7 | C E G B |
| `Cm7` / `C-7` | minor 7 | C E♭ G B♭ |
| `Cm7♭5` / `Cø7` | half-diminished 7 | C E♭ G♭ B♭ |
| `Cdim7` / `C°7` | fully diminished 7 | C E♭ G♭ B𝄫 |
| `Cm(maj7)` / `CmMaj7` | minor-major 7 | C E♭ G B |
| `Cmaj7♯11` | major 7 plus raised 11 | C E G B F♯ |
| `C7♭9` | dominant 7 plus flat 9 | C E G B♭ D♭ |
| `C7♯9` | dominant 7 plus sharp 9 | C E G B♭ D♯ |
| `C7♭13` | dominant 7 plus flat 13 | C E G B♭ A♭ |
| `C13` | dominant 13; 11 often omitted | C E G B♭ D A |
| `Cadd9` | major triad plus 9, no 7 | C E G D |
| `C6/9` | major triad plus 6 and 9 | C E G A D |

## Common ambiguous symbols

| Symbol | Possible readings | Agent default | Clarify when |
|---|---|---|---|
| `C-` | C minor; rarely a dash separator | C minor in jazz/lead-sheet contexts | user is using plain-text separators |
| `C+` | C augmented triad; sometimes shorthand for a raised-5 chord | C augmented triad | extensions are missing but implied by context |
| `C2` | Csus2 or Cadd9/add2 | likely Csus2 in guitar/pop charts | voicing or third matters |
| `C4` | Csus4 or pitch C4 | chord symbol if in chord chart; pitch if in melody/register context | both chord and pitch notation appear together |
| `Cmaj` | C major triad or informal Cmaj7 | major triad unless seventh context implies otherwise | chart also uses `min`, `dom`, or other informal labels |
| `CΔ` | C major 7 in jazz; not a triangle chord | Cmaj7 | user is outside jazz and may not know delta notation |
| `C7+5` | C7♯5 | dominant 7 sharp 5 | user also uses `+` for augmented triads inconsistently |
| `C7-5` | C7♭5 in older charts | dominant 7 flat 5 | chart mixes minus for minor and flat |
| `Calt` | often C7alt but missing the 7 | C7alt in jazz context | non-jazz context or no dominant function |
| `C/D` | C triad over D bass, not necessarily D11 | slash chord | functional label matters |
| `D/C` | D triad over C bass or polychord shorthand | slash chord in lead sheets | upper/lower triad stack matters |

## Add, sus, and omit rules

| Marking | Meaning | Watch out |
|---|---|---|
| `add9` | Add 9 to a triad without adding a 7th | `Cadd9` is not `C9` |
| `C9` | Dominant 9 unless otherwise marked | includes B♭, not B |
| `Cmaj9` | Major 9 | includes B natural |
| `Cm9` | Minor 9 | includes E♭ and B♭ |
| `sus4` | replace 3 with 4 | `C7sus4` = C F G B♭ |
| `sus2` | replace 3 with 2 | `Csus2` = C D G |
| `no3` | omit the third | often power-chord-like if fifth remains |
| `no5` / `omit5` | omit the fifth | not a power chord |
| `add11` | add 11 to a triad | can clash with major 3 in close voicing |

## Altered dominant spelling from C

| Tension | Pitch | Enharmonic caution |
|---|---|---|
| ♭9 | D♭ | not C♯ in functional spelling from C |
| ♯9 | D♯ | enharmonic to E♭ but functions as raised 9 over major 3 E |
| ♯11 / ♭5 | F♯ / G♭ | choose by symbol and context |
| ♭13 / ♯5 | A♭ / G♯ | choose by symbol and context |

In jazz notation, altered dominants often contain enharmonic pitch classes. For explanation, label the function of the tension, not just the piano key.

## What to do in an answer

When the user writes an ambiguous chord:

```md
I’m reading `C2` as `Csus2` here because this looks like a pop/guitar chart. If you meant `Cadd9`, keep E in the chord: C–E–G–D. If you meant sus2, replace E with D: C–D–G.
```

When rewriting a chart:

```md
Original: | C2 | G/B | Am7 | Fadd9 |
Clearer:  | Csus2 | G/B | Am7 | Fadd9 |
```

## Pitfalls

- Do not interpret every slash chord as a polychord.
- Do not assume `C9` means “C add 9.” It usually means dominant 9.
- Do not call `C(no5)` a power chord.
- Do not treat `alt` as a free color on non-dominant chords unless the genre or voicing context makes that clear.
- Do not respell every accidental enharmonically for ease of reading if the functional label matters.

## Cross-references

- Chord symbol conventions → `chord-symbol-conventions.md`
- Chord construction → `references/harmony/chord-construction.md`
- Jazz harmony → `references/harmony/jazz-harmony.md`
- Jazz voicings → `jazz-voicings.md`
- Scale-degree spelling → `scale-degree-spelling-cheatsheet.md`
