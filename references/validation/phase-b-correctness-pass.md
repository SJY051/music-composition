# Phase B Correctness Pass

Use this document to prepare the skill for first release without running the Phase C prompt-smoke-test suite. Phase B is a content and correctness hardening pass: it checks the files most likely to be quoted directly by the agent, the theory files most likely to propagate mistakes, and the cultural/currentness files most likely to overclaim.

## Scope

Phase B covers:

1. high-use `assets/` cheat sheets,
2. `references/harmony/`,
3. `references/fundamentals/`,
4. culturally specific files with higher overclaim risk,
5. `references/research/` currentness, privacy, and originality boundaries,
6. release-readiness documentation and automated regression checks.

Phase B does **not** require running the user-facing prompt-smoke-test suite. That belongs to Phase C.

## Review order and acceptance criteria

| Area | Files | Acceptance criteria | Status |
|---|---|---|---|
| High-use assets | chord symbols, intervals, modes, jazz voicings, progressions, response templates | no known P0/P1 theory regression; ambiguous notation handled with defaults and caveats | reviewed for release-prep |
| Harmony | chord construction, functional harmony, chromatic harmony, jazz harmony, modulation, reharmonization, voice leading | altered tensions, augmented-sixth claims, dominant substitutions, and voice-leading rules are context-aware | reviewed for release-prep |
| Fundamentals | notation, pitch/interval/scale, rhythm/meter, prosody/language | no overbroad tuning/history/language claims; spelling examples match function | reviewed for release-prep |
| Cultural / regional | Korean traditional, MENA, South Asian, folk/roots, regional starters | traditions are not reduced to scales, samples, or broad labels; collaboration caveats are present | reviewed for release-prep |
| Research/currentness | web research, streaming context, style/copyright, reference digging, regional trends | no credential requests; no stale-current claims without snapshot/web-check language | reviewed for release-prep |

## Manual corrections applied in this pass

| Severity | File | Correction |
|---|---|---|
| P0/P1 | `references/genres/korean-traditional.md` | Replaced the overly fixed `Jinyangjo = 18 beats` line with a 6-beat-cycle / 24-beat-phrase caveat; clarified large-beat vs subdivision descriptions for faster `jangdan`. |
| P1 | `assets/intervals-and-scale-formulas.md`, `assets/modes-cheatsheet.md`, `references/fundamentals/pitch-intervals-scales.md` | Corrected C whole-tone dominant spelling to use B♭ for ♭7; corrected C half-whole diminished spelling to use D♯ for ♯9 rather than E♭. |
| P1 | `assets/chord-symbol-conventions.md`, `references/harmony/chord-construction.md` | Tightened `C7alt` explanation so natural 5 is not presented as part of the default altered pitch set; clarified altered dominants use selected subsets. |
| P1 | `references/harmony/chord-construction.md` | Corrected upper-structure triad caveats: `D♭/C7` includes a natural 11 that clashes with the 3rd if the shell includes E; `F♯/C7` needs enharmonic explanation for the ♭7. |
| P2 | `references/fundamentals/pitch-intervals-scales.md` | Softened the *diabolus in musica* claim and perfect-consonance explanation; added strict-harmony caveat for P4 above the bass. |
| P2 | `references/fundamentals/pitch-intervals-scales.md` | Softened pentatonic-over-chords language so it is treated as a common flexible strategy, not a universal guarantee. |
| P2 | `references/harmony/voice-leading.md` | Replaced absolute “never double” wording with strict common-practice cautions and genre-aware exceptions. |
| P2 | `references/rhythm-groove/odd-meters-polyrhythm.md` | Clarified that tala is a named performance framework, not just a time signature; separated Indian tala from Middle Eastern/Turkish iqa'/usul-like cycle concepts. |
| P2 | `references/genres/korean-traditional.md` | Replaced fixed-pitch implication around *hwangjong* and softened claims about all professional *gugak* musicians reading both Western notation and `jeongganbo`. |
| P2 | `references/genres/film-tv-scoring.md` | Replaced generic “ethnic percussion” labels with “tradition-specific / regional” language. |

## Spot-check checklist

Before RC1, the maintainer should still spot-check these by hand, especially if any file changes after this pass.

| Check | Expected result |
|---|---|
| `C(no5)` | omit-fifth chord, not a power chord |
| `C7alt` | dominant shell plus selected altered tensions; natural 5 not listed as default altered pitch |
| `E7♯9` | G natural is ♯9; A♯ is ♯11 / ♭5 territory |
| C whole-tone dominant color | C D E F♯ G♯ B♭ when spelling ♭7 function |
| C half-whole diminished over C7 | C D♭ D♯ E F♯ G A B♭; D♯ is ♯9 |
| F Lydian | F G A B C D E; no B♭ |
| German +6 | can be enharmonically reinterpreted as dominant 7; Italian +6 is not a full V7 pitch set |
| `Jinyangjo` | 6-beat cycle with common 24-beat phrase grouping caveat, not a simple 18-beat claim |
| Maqam/raga/tala | not reduced to Western scale/time-signature presets |
| Streaming context | asks for user-shared public/lightweight evidence only; no credentials |
| Style-reference/copyright | extracts craft variables; does not copy melody, lyrics, riffs, samples, signature tags, or vocal identity |

## Phase B exit decision

Phase B can be marked prepared/complete when:

- `scripts/music_theory_sanity_check.py` passes,
- internal Markdown links resolve,
- the corrections above are present,
- current-sensitive files retain snapshot notes,
- no active guidance uses broad culture-as-color labels,
- Phase C prompt tests remain available but unrun.

## Cross-references

- Release roadmap → `../../RELEASE-ROADMAP.md`
- First-release readiness → `first-release-readiness.md`
- Prompt smoke tests, Phase C only → `prompt-smoke-tests.md`
- Music-theory audit rubric → `../../assets/music-theory-audit-rubric.md`
- Sanity checker → `../../scripts/music_theory_sanity_check.py`
