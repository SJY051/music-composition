# Music-Theory Audit Rubric

Use this asset for manual review of theory-heavy files. Automated scripts catch regressions; this rubric catches musical reasoning problems that scripts cannot reliably detect.

## Severity labels

| Severity | Meaning | Example |
|---|---|---|
| P0 | Wrong information likely to be repeated directly by the agent | omit-fifth chord mislabeled as a power chord |
| P1 | Overbroad or misleading claim that can damage user trust | “Western music since 1700 uses 12-TET” |
| P2 | Correct in one context but missing a needed caveat | “tritone substitutions can replace any chord” |
| P3 | Style, clarity, or maintainability issue | inconsistent link style, unclear heading |

## Audit dimensions

| Dimension | Questions to ask |
|---|---|
| Pitch spelling | Are accidentals spelled by function, not just pitch class? |
| Chord construction | Do chord symbols map to the listed notes? |
| Function | Does the Roman numeral match the key and chord quality? |
| Voice-leading | Are resolution tendencies described as tendencies, not universal moral rules? |
| Genre context | Is the advice valid for the named style? |
| Currentness | Does the claim require active web verification? |
| Cultural specificity | Does the text name the tradition/scene/idiom rather than using broad labels? |
| Output usefulness | Can the agent turn the paragraph into a concrete answer? |

## High-risk files

Review these most carefully before release.

| File | Why it is high-risk |
|---|---|
| `assets/chord-symbol-conventions.md` | Directly quotable notation guidance |
| `assets/chord-symbol-ambiguity-and-parsing.md` | Directly maps symbols to notes |
| `assets/intervals-and-scale-formulas.md` | Foundational formulas |
| `assets/scale-degree-spelling-cheatsheet.md` | Prevents enharmonic/function errors |
| `assets/modes-cheatsheet.md` | Common source of relative/parallel confusion |
| `assets/jazz-voicings.md` | Altered tension mistakes are easy and visible |
| `assets/progressions-catalog.md` | Famous-song examples can be overclaimed |
| `references/harmony/jazz-harmony.md` | Advanced harmony needs caveats |
| `references/harmony/modulation.md` | Enharmonic reinterpretation can be misstated |
| `references/genres/korean-traditional.md` | Specialized terminology requires care |
| `references/genres/mena-pop.md` | Maqam-adjacent guidance can be oversimplified |
| `references/research/style-reference-and-copyright.md` | Safety/originality guidance needs currentness |

## Audit checklist for a single file

```md
File:
Reviewer:
Date:

Scope check:
- [ ] File title and “When to consult” match the contents.
- [ ] The file does not duplicate a better existing file.
- [ ] Cross-references are relevant and resolve.

Theory check:
- [ ] Chord symbols map to correct notes.
- [ ] Roman numerals match key, mode, and quality.
- [ ] Enharmonic spellings are functionally justified.
- [ ] Examples do not overclaim famous-song transcriptions.
- [ ] Genre caveats are present when needed.

User-output check:
- [ ] The agent can extract concrete advice.
- [ ] Examples include playable/usable materials.
- [ ] The file avoids long abstract explanation without application.

Currentness/culture check:
- [ ] Snapshot note exists if needed.
- [ ] Current artists/platforms/legal claims are not frozen as permanent facts.
- [ ] Cultural references are specific and respectful.

Decision:
- [ ] Release-ready
- [ ] Needs minor edit
- [ ] Needs major review
- [ ] Release blocker
```

## Red-flag phrases

These phrases are not automatically forbidden in every possible context, but they deserve review:

| Phrase type | Better direction |
|---|---|
| broad culture-as-color labels | name instrument, rhythm, language, scene, or tradition |
| “rules of music” | convention, tendency, style norm, voice-leading habit |
| “always resolve” | usually resolves, strongly tends to resolve, conventional resolution |
| “the song uses…” without source | “a simplified common chart often shows…” |
| “current trend” without date/source | add snapshot or active web-research requirement |
| “AI copyright law says…” | jurisdiction, date, and current-source check required |

## Cross-references

- Release readiness → `references/validation/first-release-readiness.md`
- Prompt smoke tests → `references/validation/prompt-smoke-tests.md`
- Chord ambiguity → `chord-symbol-ambiguity-and-parsing.md`
- Scale-degree spelling → `scale-degree-spelling-cheatsheet.md`
- Maintenance guide → `MAINTENANCE.md`
