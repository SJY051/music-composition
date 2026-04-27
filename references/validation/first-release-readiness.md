# First Release Readiness Checklist

Use this checklist before shipping the music-composition skill as a first release, and retain it as the audit trail for v1.0. It is maintainer-facing and should be used alongside `../../RELEASE-ROADMAP.md`, `../../scripts/music_theory_sanity_check.py`, `phase-b-correctness-pass.md`, `prompt-smoke-tests.md`, `phase-c-smoke-test-results.md`, `rc1-packaging-checklist.md`, and `../../KNOWN-LIMITATIONS.md`, and `../../VALIDATION-v1.0.md`.

## When to consult

Consult this file when preparing a release candidate, after a major patch, or before publishing the skill to users who will rely on it for real composition help.

## Release readiness scorecard

| Area | Required for first release | Status to record |
|---|---|---|
| Navigation | `SKILL.md` and `00-navigation.md` reflect all major folders/files | pass / fail / needs review |
| Links | Internal `.md` references resolve | pass / fail |
| High-use assets | Chord symbols, modes, intervals, cadences, voicings, progressions checked | pass / fail / spot-check only |
| Phase B correctness | `phase-b-correctness-pass.md` completed and corrections retained | pass / fail / partial |
| Known regressions | Prior P0/P1 errors remain fixed | pass / fail |
| User workflow | Brainstorming, collaboration, revision loop, critique, output templates present | pass / fail |
| Research workflow | Web search, trend research, streaming context, style/copyright, reference digging present | pass / fail |
| Snapshot notes | Current-sensitive files have snapshot notes | pass / fail |
| Cultural specificity | Broad shortcut labels replaced by specific source/scene/idiom language | pass / fail |
| Prompt smoke tests | Representative prompts tested for routing and answer quality | pass / fail / partial |
| Phase C result record | Prompt-smoke-test result recorded in `phase-c-smoke-test-results.md` | pass / fail / partial |
| Known limitations | `../../KNOWN-LIMITATIONS.md` present or limitations included in validation report | pass / fail |
| ZIP hygiene | No cache, scratch, temp, or obsolete files included | pass / fail |
| v1.0 validation | `../../VALIDATION-v1.0.md` present and consistent with package counts | pass / fail |

## First-release blockers

Treat these as release blockers:

- broken internal `.md` links,
- missing `references/00-navigation.md` routes for major new files,
- missing `SKILL.md` structural updates after a major folder addition,
- known high-risk theory regression in an `assets/` file,
- current-sensitive file without a snapshot note,
- user-account or credential request in streaming-service guidance,
- style-reference guidance that encourages copying melody, lyrics, riffs, samples, signature production tags, or vocal identity,
- cultural guidance that uses broad shortcut labels instead of naming the source tradition, scene, or musical variable,
- validation report claiming a check passed when the checker was not actually run,
- release-candidate package without known limitations or an equivalent limitations section.

## High-use asset review order

Review assets in this order because they are most likely to be quoted directly by the agent.

1. `assets/chord-symbol-conventions.md`
2. `assets/chord-symbol-ambiguity-and-parsing.md`
3. `assets/intervals-and-scale-formulas.md`
4. `assets/scale-degree-spelling-cheatsheet.md`
5. `assets/modes-cheatsheet.md`
6. `assets/jazz-voicings.md`
7. `assets/cadence-reference.md`
8. `assets/progressions-catalog.md`
9. `assets/response-templates.md`
10. `assets/diagnostic-checklists.md`
11. `assets/web-search-cheatsheet.md`
12. `assets/musical-brainstorming-cards.md`
13. `assets/session-brief-and-decision-log.md`
14. `assets/trend-and-reference-matrices.md`
15. `assets/music-theory-audit-rubric.md`

## Music-theory spot checks

Before release, spot-check at least these items manually.

| Item | Expected result |
|---|---|
| `C(no5)` | C and E; not a power chord |
| `C5` / `C(no3)` | root + fifth; power chord context |
| `A5` inversion | `d4` |
| `m6` inversion | `M3` |
| `E7alt` with A♯ | A♯ = ♯11 / ♭5, not ♯9 |
| E over G natural | G natural = ♯9 |
| F Lydian | contains B natural, not B♭ |
| German +6 enharmonic reinterpretation | can map to dominant 7th; Italian +6 does not have the full V7 pitch content |
| Maqam/makam | not reduced to a 24-TET subset |
| 12-TET history | modern default, not a universal “since 1700” claim |

## Output behavior checks

For each prompt smoke test, record whether the assistant did the following.

| Behavior | Pass condition |
|---|---|
| Genre framing | Named or inferred the genre frame, or asked only if needed |
| Concrete output | Gave chords, notes, rhythm, form map, or revision instructions |
| Options | Offered 2–4 usable directions when the user asked creatively |
| Rationale | Explained why each option changes the sound |
| User agency | Let the user choose, especially in brainstorming and revision |
| Currentness | Used web research only when current facts mattered |
| Safety/originality | Avoided copying protected expression |
| Cultural specificity | Avoided broad regional shortcuts |

## Validation report template

Use this structure for release-candidate validation reports.

```md
# Validation Report — RCx

## Package

- Package: `<filename>.zip`
- Base version: `<previous version>`
- Date: `<YYYY-MM-DD>`

## File counts

- Markdown files:
- Total files:
- New files:
- Modified files:
- Deleted files:

## Automated checks

- `scripts/music_theory_sanity_check.py`: PASS / FAIL
- Internal `.md` references:
- Snapshot notes:
- Known regression checks:
- ZIP integrity:

## Manual review

- High-use assets:
- Research/currentness:
- Cultural specificity:
- Prompt smoke tests:
- Phase C smoke-test results:

## Remaining limitations

- ...

## Release decision

- Ship / hold / ship with caveats
```

## Cross-references

- Release roadmap → `../../RELEASE-ROADMAP.md`
- v1.0 validation report → `../../VALIDATION-v1.0.md`
- RC1 validation report → `../../VALIDATION-RC1.md`
- Known limitations → `../../KNOWN-LIMITATIONS.md`
- Phase B correctness pass → `phase-b-correctness-pass.md`
- Prompt smoke tests → `prompt-smoke-tests.md`
- Phase C smoke-test results → `phase-c-smoke-test-results.md`
- RC1 packaging checklist → `rc1-packaging-checklist.md`
- Chord-symbol audit → `../../assets/chord-symbol-ambiguity-and-parsing.md`
- Scale-degree spelling → `../../assets/scale-degree-spelling-cheatsheet.md`
- Music-theory audit rubric → `../../assets/music-theory-audit-rubric.md`
- Maintenance guide → `../../MAINTENANCE.md`
