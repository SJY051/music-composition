# First Release Roadmap

This roadmap defines what “release-ready” means for the music-composition skill. It is intentionally practical: the goal is not to finish every possible genre, technique, or culture area, but to ship a stable first release that gives accurate, useful, safe, and extensible composition help.

## Release target

**First release goal:** a composition assistant skill that can reliably help users brainstorm, draft, analyze, revise, and learn music across common Western theory, popular songwriting, selected global genre frames, current-reference workflows, and user-agent collaboration sessions.

The first release should feel like a strong working composer / arranger / songwriting coach. It does not need to feel like a complete music encyclopedia.

## Release principles

1. **Accuracy before breadth.** A smaller correct skill beats a larger skill that repeats wrong theory confidently.
2. **Workflow before trivia.** The assistant should help the user make musical decisions, not just explain concepts.
3. **Currentness through process.** Living scenes, charts, streaming services, platform norms, AI tools, and copyright status should be handled through active research workflows, not frozen claims.
4. **Cultural specificity over broad labels.** Avoid continent-scale or “world music” shorthand. Name the tradition, scene, language, rhythm, instrument idiom, or source context.
5. **Templates are part of the product.** Output formats, brainstorming cards, diagnostic checklists, and decision logs make the skill reliable in real sessions.
6. **Automated checks are regression guards, not truth machines.** Scripts should catch broken links and known high-risk mistakes, but expert review still matters.

## Minimum viable first release

The first release is ready when the following are true.

### 1. Navigation and structure

- `SKILL.md` accurately describes the folder structure.
- `references/00-navigation.md` routes all major user request types to 1–3 relevant files.
- Every major new folder has at least one overview or routing file.
- All internal `.md` links resolve.
- Deprecated or renamed files are either removed cleanly or kept as redirect stubs.

### 2. Core music theory correctness

- High-use assets are clean: chord symbols, intervals, modes, cadences, jazz voicings, progressions.
- Known corrected regressions remain fixed: `C(no5)`, A5/m6 inversion, E7alt tension labels, relative-vs-parallel mode tables, augmented sixth enharmonic claims, maqam/makam reduction, 12-TET overgeneralization.
- Chord-symbol ambiguity guidance exists for common user notation variants.
- Scale-degree spelling guidance exists for Roman numerals, modal mixture, secondary functions, and altered tensions.

### 3. User-agent workflow

- The skill supports brainstorming, drafting, critique, revision, selection, and handoff.
- The assistant can keep a project card, decision log, branch tracker, do-not-change list, and before/after revision block.
- Vague user feedback can be translated into musical variables.
- The assistant can offer divergent options before converging.

### 4. Research and currentness

- Current-sensitive genre, AI, platform, and trend files have snapshot notes.
- The skill includes a general web trend research workflow.
- The skill includes a fast web-search cheatsheet.
- The skill includes reference-track digging, style/copyright safety, user listening context, streaming-service surfaces, regional trend evolution, and microgenre dispatch.
- The assistant never asks for passwords, tokens, or private account access to use streaming-service context.

### 5. Genre and idiom coverage

The first release should cover, at a practical starter level:

- Classical period conventions and common forms
- Jazz harmony and selected jazz styles
- Pop, rock, indie, hip-hop, R&B, electronic, film/TV, game, media/commercial, musical theatre
- K-pop/J-pop, C-pop / Southeast Asian pop
- Latin pop/reggaeton, Brazilian pop/funk, Afrobeats/amapiano, South Asian film-pop, MENA pop
- Korean traditional and K-trad fusion
- Country/Americana, metal/punk/hardcore, gospel/CCM
- Folk/roots/tradition-specific writing
- Regional scene starters, microgenres, and hybrid genres
- Instrument-idiom basics for piano, guitar, bass, drums/percussion, strings, winds, brass, and vocals

The first release does **not** require every subgenre to have a dedicated file. Microgenre and regional-scene hubs are acceptable when they route the assistant to research workflows and major-genre craft variables.

### 6. Safety and originality

- Style-reference requests are converted into craft variables.
- The assistant avoids copying protected melody, lyrics, riffs, samples, signature tags, or vocal identity.
- Traditional or regional material is treated with specificity, context, and collaboration cautions where appropriate.
- AI-assisted composition guidance clearly separates ideation, generation, selection, editing, ownership, and current legal uncertainty.

### 7. Validation

- `scripts/music_theory_sanity_check.py` passes.
- A first-release readiness checklist exists.
- A prompt smoke-test suite exists.
- Validation reports summarize file counts, broken-link status, snapshot coverage, known-regression checks, and remaining limitations.

## Suggested release phases

### Phase A — content lock

Finish all first-release structural content:

- release roadmap
- first-release readiness checklist
- prompt smoke-test suite
- chord-symbol ambiguity / parsing asset
- scale-degree spelling asset
- revision-loop workflow
- audit rubric

Exit criteria:

- No planned first-release file is missing.
- Navigation and `SKILL.md` are updated.
- Sanity checker passes.

### Phase B — correctness pass

Focus on correctness rather than expansion. Use `references/validation/phase-b-correctness-pass.md` as the maintainer-facing checklist for this phase.

Review order:

1. `assets/` high-use cheat sheets
2. `references/harmony/`
3. `references/fundamentals/`
4. `references/genres/korean-traditional.md`, `references/genres/mena-pop.md`, `references/genres/south-asian-film-pop.md`, `references/genres/folk-roots-and-traditions.md`
5. `references/research/` currentness and privacy boundaries
6. `references/creative-workflows/` output behavior

Exit criteria:

- No known P0/P1 theory errors remain.
- Culture-language shortcuts are absent from active guidance.
- Currentness claims are either snapshot-labeled or moved to active research workflows.

### Phase C — prompt simulation pass

Run the prompt smoke tests in `references/validation/prompt-smoke-tests.md`.

The assistant should be tested on:

- chord progression generation
- melody revision
- weak chorus diagnosis
- jazz reharmonization
- K-pop/J-pop reference request
- user streaming-service reference workflow
- microgenre request
- regional trend comparison
- traditional-fusion request
- style/copyright-safe request
- multi-turn revision loop
- teaching-mode explanation

Exit criteria:

- The assistant routes to the intended files.
- The answer is concrete, musical, and genre-aware.
- The answer does not over-research when a stable theory answer is enough.
- The answer does use active web research when currentness matters.
- The answer offers choices and preserves user agency.

### Phase D — release candidate

Prepare the first release package.

Required artifacts:

- final ZIP
- unified diff from previous release candidate
- validation report
- known limitations section or `KNOWN-LIMITATIONS.md`
- Phase C smoke-test result record
- changelog summary

Exit criteria:

- ZIP integrity passes.
- No `__pycache__`, temporary scratch folders, generated logs, or obsolete validation artifacts are included.
- File counts and expected-files list match the validation report.

## What not to build before first release

These are useful, but they should not block first release.

- A complete world-genre encyclopedia
- Full historical musicology coverage
- DAW operation, plugin manuals, sound-design recipes, mix/mastering instruction
- MIDI file generation or notation-software UI automation
- Exhaustive artist-by-artist style guides
- Every possible microgenre as a dedicated file
- A perfect music-theory parser for every notation edge case

## Post-release backlog

Good post-release expansions:

- Dedicated regional guides: regional Mexican, Punjabi pop, Turkish arabesk-pop, Maghreb/raï, gqom, singeli, kuduro, sertanejo/pagode/arrocha/piseiro
- More instrument-idiom files: harp, mallet percussion, accordion, organ, synth performance idioms, DJ/turntable-informed writing
- Deeper advanced harmony checks: chord-scale mapping, altered dominant spelling, secondary-function consistency, modal-mixture spelling, Nashville number parsing
- Larger prompt-evaluation harness with expected routing and expected answer shape
- Accessibility and wellness-oriented composition guidance
- Collaboration handoff docs for human co-writers, producers, arrangers, and performers

## Release status labels

Use these labels in validation reports and maintenance notes:

| Label | Meaning |
|---|---|
| `draft` | Useful but not reviewed enough for release reliance |
| `reviewed` | Human-reviewed for obvious errors and structure |
| `snapshot-current` | Current-sensitive claims checked at the named snapshot date |
| `stable-reference` | Mostly durable theory/craft reference |
| `needs-web-check` | Must be verified when answering current scene/platform/law/tool questions |
| `release-blocker` | Must be fixed before first release |
| `post-release` | Valuable, but not required for first release |

## Current first-release assessment

As of v1.0 packaging on 2026-04-27, the first-release phases are complete:

| Phase | Status |
|---|---|
| Phase A — content lock | Complete |
| Phase B — correctness pass | Complete |
| Phase C — prompt simulation pass | User-run pass recorded |
| Phase D — release-candidate packaging | Complete |
| v1.0 finalization | Complete |

RC1 was promoted to v1.0 without creating RC2 because no release blocker was found during the RC1 → v1.0 decision pass. Remaining desirable work is treated as post-release update/backlog material.

v1.0 packaging is complete when the following artifacts are present:

1. `RELEASE-NOTES-v1.0.md`,
2. `VALIDATION-v1.0.md`,
3. `KNOWN-LIMITATIONS.md`,
4. a clean v1.0 release ZIP,
5. a packaging diff from RC1,
6. a SHA256 checksum file,
7. a passing `scripts/music_theory_sanity_check.py` result,
8. a passing ZIP integrity check.

After v1.0, use the post-release backlog above to plan update patches. New features should be treated as v1.x additions unless they fix a release-blocking defect.
