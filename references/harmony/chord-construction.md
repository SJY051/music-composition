# Chord Construction

This file covers how chords are built — their qualities, extensions, alterations, and notation. It's the vocabulary file. For *function* (what chords do in a key), see `functional-harmony.md`. For *connection* (how chords move between each other), see `voice-leading.md`. For *voicing* (how a chord is laid out across registers and instruments), see `orchestration/voicing-and-texture.md` and `assets/jazz-voicings.md`.

## When to consult this file

- The user asks "what is a Cmaj7♯11" or any chord-spelling question
- The user wants to add color (extensions, alterations) but doesn't know which to use
- Notation/symbol questions ("how do I write half-diminished")
- Choosing between chord qualities for a given mood
- Understanding what a chord *contains* (its component notes/intervals)

## Triads

A triad is three notes stacked in thirds: root, third, fifth. The four qualities differ in the size of the two thirds.

| Quality | Symbol | Stacking | Example (root C) | Sound |
|---------|--------|----------|------------------|-------|
| Major | `C`, `CM`, `Cmaj` | M3 + m3 | C E G | Bright, stable |
| Minor | `Cm`, `Cmin`, `C-` | m3 + M3 | C E♭ G | Dark, stable |
| Diminished | `C°`, `Cdim` | m3 + m3 | C E♭ G♭ | Tense, unstable (tritone between root and 5th) |
| Augmented | `C+`, `Caug` | M3 + M3 | C E G♯ | Tense, ambiguous (symmetric — divides octave equally) |

Major and minor are stable (consonant fifth); diminished and augmented are unstable (dissonant or symmetrically ambiguous fifth) and almost always resolve.

### Inversions

A triad's bass note determines its inversion:

- **Root position** — root in bass (`C` = C-E-G with C below)
- **First inversion** — third in bass; figured `⁶` in classical, `C/E` in lead-sheet
- **Second inversion** — fifth in bass; figured `⁶/₄`, written `C/G`

Second inversion (the "6/4 chord") is unstable in classical practice and used only in specific contexts (cadential, passing, neighboring — see `voice-leading.md`). In pop and rock, slash chords with the fifth in the bass are common and unproblematic.

## Seventh chords

Add a seventh on top of a triad. Now there are seven common qualities, distinguished by the quality of both the underlying triad and the seventh interval (M7 or m7) above the root.

| Quality | Symbol | Notes (root C) | Built from | Common context |
|---------|--------|----------------|------------|----------------|
| Major 7 | `Cmaj7`, `CΔ`, `CM7` | C E G B | major triad + M7 | Tonic chord in jazz/pop; lush, restful |
| Dominant 7 | `C7` | C E G B♭ | major triad + m7 | The functional dominant; tense, unresolved |
| Minor 7 | `Cm7`, `C-7` | C E♭ G B♭ | minor triad + m7 | All-purpose minor; jazz, R&B, neo-soul |
| Half-diminished | `Cm7♭5`, `Cø7`, `Cø` | C E♭ G♭ B♭ | dim triad + m7 | The `iiø7` of minor ii-V-i; melancholy |
| Fully diminished | `C°7`, `Cdim7` | C E♭ G♭ B𝄫 (=A) | dim triad + d7 | Symmetric (stacked m3s); tense passing chord |
| Minor-major 7 | `CmMaj7`, `Cm(maj7)`, `C-Δ` | C E♭ G B | minor triad + M7 | "James Bond" sound; line cliché destination |
| Augmented major 7 | `Cmaj7♯5`, `C+Δ` | C E G♯ B | aug triad + M7 | Ambiguous, glassy/bright-tension; jazz and impressionist |

Two more, less common:
- **Augmented 7** (`C7♯5` / `C+7`): C E G♯ B♭ — altered dominant; appears in altered V chords
- **Diminished major 7** (`C°Maj7`): C E♭ G♭ B — rare, very dissonant and coloristic; not symmetric like a fully diminished 7th chord

### Inversions of 7th chords

| Inversion | Bass | Lead-sheet | Figured |
|-----------|------|------------|---------|
| Root position | root | `C7` | `7` |
| First | third | `C7/E` | `⁶/₅` |
| Second | fifth | `C7/G` | `⁴/₃` |
| Third | seventh | `C7/B♭` | `²` or `⁴/₂` |

## Extensions: 9, 11, 13

Stack thirds beyond the seventh: 9 (root + M9 or compound 2nd), 11 (compound 4th), 13 (compound 6th). These add color without changing the chord's underlying function.

### Default (unaltered) extensions per chord type

| Chord | 9 | 11 | 13 | Notes |
|-------|---|----|----|-------|
| Major 7 | natural 9 | ♯11 (avoid natural 11 — clashes with major 3rd) | natural 13 | Lydian color preferred |
| Dominant 7 | natural 9 | natural 11 (rare; usually as sus4 or omit) | natural 13 | The 11 is uncomfortable above the M3 |
| Minor 7 | natural 9 | natural 11 | natural 13 (rarely used) | Dorian-flavored full extensions |
| Half-diminished | natural 9 or ♭9 | natural 11 | ♭13 | `Locrian ♮2` is common in jazz minor ii–V–i; plain Locrian/♭9 is also possible by context |
| Fully diminished | natural 9 (sometimes ♭9) | natural 11 | ♭13 | Symmetric; many extensions sound OK |
| Minor-major 7 | natural 9 | natural 11 | natural 13 | Melodic minor flavor |

The "avoid note" concept: an extension that clashes too harshly with a chord tone. The most famous is the natural 11 over a major 7th (clashes with the M3 by a m9 — the harshest interval in jazz). The fix is to either omit, alter to ♯11, or treat as sus4 (which omits the 3rd).

### Altered extensions

For dominant 7 chords specifically — the chord that *wants* tension — extensions are routinely altered to increase the pull toward resolution.

| Alteration | What it means | Effect |
|------------|---------------|--------|
| ♭9 | flatten the 9th (so D♭ over C7) | Phrygian-dominant flavor; common in V→i in minor |
| ♯9 | sharpen the 9th (so D♯/E♭ over C7) | "Hendrix chord" with M3 below; bluesy bite |
| ♭5 / ♯11 | flatten the 5th or sharpen the 11th (G♭/F♯ over C7) | Lydian dominant flavor; same note, different naming |
| ♯5 / ♭13 | sharpen the 5th or flatten the 13th (G♯/A♭ over C7) | Whole-tone or altered scale flavor |

An altered dominant draws from the altered-scale color (7th mode of melodic minor): ♭9, ♯9, ♭5/♯11, and ♭13/♯5 are available, usually as a selected subset rather than all crammed into one voicing. A common notation: `C7alt` or a more specific label such as `C7♯9♭13`.

### Sus chords

Replace the 3rd with a 4th (`sus4`) or 2nd (`sus2`). The chord has no 3rd, so it's neither major nor minor — quality is suspended.

| Symbol | Notes (root C) | Notes |
|--------|----------------|-------|
| `Csus4` (or `Csus`) | C F G | Most common; "wanting to resolve down to 3" |
| `Csus2` | C D G | More open, modern; less directional |
| `C7sus4` (or `C7sus`) | C F G B♭ | Dominant 7 with sus 4; common in pop, gospel, jazz |
| `C9sus4` | C F G B♭ D | Adds the 9th; very common in jazz/pop ("Maiden Voyage" chord) |

`sus4` traditionally resolves down to a 3 (Csus4 → C). In modern pop and jazz it often doesn't — it's used for its own flavor.

### Add chords (no 7th)

Add an extension to a triad without the 7th in between:

| Symbol | Notes (root C) | Notes |
|--------|----------------|-------|
| `Cadd9` | C E G D | Major triad + 9; common in pop ballads, John Mayer territory |
| `Cmadd9` | C E♭ G D | Minor add9; melancholy and lush |
| `C6` | C E G A | Major 6 — "old-fashioned" or jazz-flavored alternative to Cmaj7 |
| `Cm6` | C E♭ G A | Minor 6 — Dorian flavor (note: A is the natural 6 of C minor in Dorian) |
| `C6/9` | C E G A D | "Six-nine"; standard final-chord alternative to Cmaj7 in jazz |

`add9` differs from `9` in that `9` implies a 7th is present, while `add9` does not.

## Slash chords

`X/Y` means chord X with bass note Y. Two flavors:

1. **Inversions** — Y is a chord tone of X. `C/E` is C major in first inversion. Used to control bass motion (often stepwise).
2. **Polychord-flavored** — Y is *not* a chord tone of X. `C/D` is C major over a D bass — functionally close to `D9sus4` but voiced differently. `F/G` is a common dominant substitute (`G9sus4`-like).

Pop and gospel use slash chords heavily for stepwise bass lines: `C – G/B – Am – Em/G – F – C/E – Dm – G`.

## Polychords and upper-structure triads

A polychord stacks two triads, written as `top chord / bottom chord` (e.g., `D/C` = D major triad over C major triad).

Upper-structure triads (UST) are a jazz technique: pick a triad whose notes are tensions over the underlying dominant 7. For `C7`:

| UST | Resulting chord tones | Tensions |
|-----|----------------------|----------|
| D/C7 | D F♯ A | 9, ♯11, 13 (Lydian dominant) |
| D♭/C7 | D♭ F A♭ | ♭9, 11, ♭13; useful color, but the natural 11 clashes with the 3rd if the shell includes E |
| E♭/C7 | E♭ G B♭ | ♯9, 5, ♭7 (Hendrix flavor) |
| F♯/C7 | F♯ A♯ C♯ | ♯11, enharmonic ♭7, ♭9; respell A♯ as B♭ when explaining function |
| A♭/C7 | A♭ C E♭ | ♭13, root, ♯9 |

Players use USTs as voicings — left hand plays the C7 shell (3 + ♭7), right hand plays the upper triad. Quick way to get rich, alterations-loaded voicings without thinking note-by-note.

## Quartal and quintal voicings

Stack 4ths or 5ths instead of 3rds. The result has no clear root and no clear quality (major/minor); it's chord-as-color.

- **Quartal** (stacked 4ths): C–F–B♭–E♭ — standard McCoy Tyner / modern jazz / "So What" voicing.
- **Quintal** (stacked 5ths): C–G–D–A — open, ambient, common in film and ECM-style jazz.

Use for modal contexts, ambiguous tonality, or when you want a less "vertical" sound. See `assets/jazz-voicings.md` for shapes.

## Clusters

Stacked 2nds. Chromatic clusters (C–C♯–D) are extremely dissonant; diatonic clusters (C–D–E) are dissonant but more usable. Used for color, texture, or shock — Bartók, Lutosławski, modern film, certain jazz.

## Symbol notation conventions

Different traditions write the same chord differently. The agent should recognize all and use the one that matches the user's vocabulary.

| Chord | Real Book / jazz | Pop / lead-sheet | Roman numeral | Nashville |
|-------|------------------|------------------|---------------|-----------|
| C major | `C` | `C` | `I` (in C major) | `1` |
| C minor | `C-` | `Cm` | `i` | `1m` |
| C major 7 | `CΔ` or `Cmaj7` | `Cmaj7` | `IΔ` | `1Δ` |
| C dominant 7 | `C7` | `C7` | `V7` (where applicable) | `1 7` |
| C minor 7 | `C-7` | `Cm7` | `i7` | `1m7` |
| C half-dim | `Cø7` | `Cm7♭5` | `viiø7` (in minor) | varies |
| C diminished | `C°7` | `Cdim7` | `vii°7` | `1°7` |

Idiom hints:
- The Real Book uses `Δ` (delta) for major 7.
- Pop and rock often write `Cmaj` or `Cmaj7`; rarely use `Δ`.
- Some jazz scores use `m` and others use `-` for minor.
- Roman numerals use case (capital = major, lowercase = minor); always specify the key.

## Voicing vs. spelling

A chord's *spelling* (its abstract pitch-class content) is fixed. Its *voicing* (how those pitch classes are distributed across registers and instruments) is open.

Common voicing approaches (full treatment in `orchestration/voicing-and-texture.md` and `assets/jazz-voicings.md`):

| Approach | Notes |
|----------|-------|
| Close position | All chord tones within one octave, no gaps |
| Open position | Wider spacing, often with chord tones an octave apart |
| Drop 2 | Take the 2nd voice from top and drop it an octave (jazz guitar, piano LH) |
| Drop 3 | Take the 3rd from top and drop it an octave |
| Rootless | Omit the root (rhythm section bass plays it); typical of jazz piano comping |
| Shell | Just root + 3 + 7 (dropping the 5; jazz piano LH) |
| Quartal | Stacked 4ths (modal, McCoy Tyner, modern) |
| Spread | Wide voicing, 2-octave+ spread; cinematic |

A chord's mood depends as much on voicing as on spelling. `Cmaj7` close voiced (C-E-G-B) is restful. The same chord spread (low C, then E G B in upper register) is open and cinematic. With ♯11 in the top voice (C-E-G-B-F♯) it becomes Lydian-flavored. The user's mood request often translates more to voicing than to chord choice.

## Six quick voicing rules

1. **Don't pile up close intervals in low register.** Below middle C, m2/M2 intervals turn muddy. Spread the voicing in the bass.
2. **The 3rd defines the chord's quality.** If you're going to omit something, omit the 5th (the most expendable note), not the 3rd.
3. **The 7th defines the chord's flavor in jazz.** It's even more important than the 3rd in many jazz voicings.
4. **Tensions (9, 11, 13) want to be on top.** Putting tensions in the middle creates muddy clusters.
5. **The bass is half the chord.** Slash chords and inversions change the chord's affect more than altering an inner voice.
6. **For piano, your LH should rarely play more than 4 notes.** Three is often plenty. Save space.

## Cross-references

- Function (what chords do in a key) → `functional-harmony.md`
- How to connect chords smoothly → `voice-leading.md`
- Non-diatonic chords (secondary dominants, borrowed, Neapolitan, +6) → `chromatic-harmony.md`
- Jazz extensions, ii-V-I, alterations in context → `jazz-harmony.md`
- Voicing distribution across instruments → `orchestration/voicing-and-texture.md`
- Specific voicing shapes (rootless, drops, quartal) → `assets/jazz-voicings.md`
- Modes and which extensions belong to which mode → `modal-harmony.md`, `assets/modes-cheatsheet.md`
- Chord symbol notation across systems (jazz, pop, RN, Nashville) → `assets/chord-symbol-conventions.md`
