# Maintenance Guide

This file is for whoever is *maintaining* this skill — not for the agent using it. The agent doesn't need to read this. It documents the skill's internal conventions, file-link structure, and the procedures for adding, renaming, or removing content without breaking anything.

For the skill's user-facing philosophy, see `SKILL.md`. For navigation logic the agent uses at runtime, see `references/00-navigation.md`. For the first stable release artifacts, see `RELEASE-NOTES-v1.0.md` and `VALIDATION-v1.0.md`; RC1 records remain in `RELEASE-NOTES-RC1.md` and `VALIDATION-RC1.md`.

## What lives where

```
SKILL.md                          — entry point for the agent; philosophy + structure
MAINTENANCE.md                    — this file; for the maintainer only
RELEASE-ROADMAP.md                — first-release phase plan and post-release backlog
RELEASE-NOTES-v1.0.md             — first stable release notes
VALIDATION-v1.0.md                — first stable release validation report
RC1-v1.0-decision-memo-2026-04-27.md — RC1 promotion decision record
RELEASE-NOTES-RC1.md              — release-candidate notes retained for audit trail
VALIDATION-RC1.md                 — release-candidate validation report retained for audit trail
KNOWN-LIMITATIONS.md              — first-release scope boundaries and caveats
assets/                           — short, quotable cheat-sheets
references/
├── 00-navigation.md              — routing table the agent reads first
├── workflow.md                   — meta-file: how the agent advises
├── analysis.md                   — methodology for analyzing existing music
├── counterpoint.md               — single-file topic
├── fundamentals/                 — pitch, rhythm, notation
├── harmony/                      — chord vocabulary and motion
├── melody/                       — line writing and development
├── rhythm-groove/                — meter manipulation and feel
├── form/                         — structural templates
├── orchestration/                — instrumentation, ensemble texture, density, choral writing
├── instrument-idiom/             — composition-facing playability and instrument-specific writing
├── songwriting/                  — lyric, hook, topline craft
├── techniques/                   — variation, 20th-C., constraint-based
├── production-aware/             — composition decisions touching the mix
├── research/                     — web trend research, reference digging, style/copyright guardrails
├── creative-workflows/           — brainstorming, answer calibration, and user-agent collaboration workflows
├── validation/                   — release readiness, Phase B/C records, RC packaging, smoke tests
├── source-bibliography.md        — maintainer-facing source map and verification guide
└── genres/                       — per-genre conventions
```

`assets/` files are short and can be quoted directly by the agent. `references/` files are longer and are meant to be synthesized, not quoted.

## File conventions

Every reference file (`references/**/*.md`) should have:

1. **Title** (`# File Title`) matching the topic
2. **Short opening paragraph** defining the topic in 2–4 sentences
3. **Cross-link paragraph** pointing to adjacent files for related topics
4. **`## When to consult this file`** section — bullet list of triggers
5. **Body** organized with `##` headers
6. **`## Common pitfalls when advising`** section near the end (where applicable)
7. **`## Quick decision matrix`** table near the end (where applicable)
8. **`## Cross-references`** section at the very end — bullet list of links

Asset files are looser but should still have a title, a one-paragraph framing, and at minimum a cross-references section at the end.

The `## When to consult this file` section is what the agent uses to decide whether to load the file. Write triggers as concrete user-asks, not abstract topic descriptions.

## Tone conventions

All files are written in the same advisory voice. Some patterns to keep consistent:

- **Direct second person ("you") is rare.** The file talks about the user as "the user" and the writer as "the composer"; second person sneaks in occasionally for instructional moments but isn't the default.
- **"The agent" refers to the AI agent itself** in workflow.md, navigation, and pitfalls sections.
- **Bullet lists are common, but never lists of one or two items.** If a list has fewer than three items, prose works better.
- **Tables are preferred for symbol-to-meaning mappings, comparison matrices, and decision matrices.** Use them aggressively.
- **No "moralizing" about technique.** Conventions are described as conventions, not as rules. Recurring phrase: "this is convention, not law".
- **Genre is taken seriously.** Pop voice-leading isn't "incorrect classical voice-leading"; it's pop voice-leading. Don't apply one genre's standards to another.
- **Examples are concrete.** When a technique is named, an example follows. Famous-song examples are preferred over invented ones because they let the agent point the user at something to listen to.
- **Em dashes are used liberally** for parenthetical clauses. Curly quotes are used in prose; straight quotes in code/symbol contexts.

## Notation conventions across the skill

Defined once in `SKILL.md` and used consistently:

- Chord symbols: `Cmaj7`, `Dm7`, `G7♭9`, `B♭/D` (lead-sheet style by default)
- Roman numerals: `I`, `vi`, `V7`, `ii⁶`, `vii°⁷`, `iiø7`, `♭VI`, `V/V`
- Pitches: `C4` = middle C (scientific pitch notation when register matters)
- Intervals: `m2 M2 m3 M3 P4 A4 d5 P5 m6 M6 m7 M7 P8`
- Scale degrees: `^1 ^2 ^3 ...` in compact notation
- Tempo: `120 BPM` or `♩=120`
- Accidentals: `♯` `♭` `♮` `𝄪` `𝄫` (Unicode glyphs, not ASCII `#` and `b`, except where the context is plain-text input from a user)

When adding new content, match these conventions. When the agent is asked about ASCII alternatives, `assets/chord-symbol-conventions.md` covers them.

## Cross-reference conventions

Cross-references between files use **relative paths from the linking file's location**:

- A file in `references/harmony/` linking to `references/melody/melodic-construction.md` writes `melody/melodic-construction.md` (sibling-folder relative)
- A file in `references/harmony/` linking to `references/workflow.md` writes `../workflow.md` is **not** the convention — most files use `workflow.md` or `references/workflow.md` depending on the file's depth. **Inconsistency exists; prefer the form that reads naturally.**
- A file in `references/` linking to `assets/` writes `assets/foo.md`
- A file in `assets/` linking to `references/` writes `references/foo/bar.md`

The agent is robust to these variations. Don't reformat existing links unless they're broken.

Each file's `## Cross-references` section is the *primary* link list. Inline links in the body should be sparse and only when the link is essential to the immediate point.

## Snapshot and currentness policy

Some files describe living scenes, current artists, platform behavior, AI tools, or market conventions. Those files should include a `Snapshot note` near the top.

A snapshot note should state:

1. the last content review date,
2. which parts are durable craft guidance,
3. which parts require current web verification,
4. links to `references/research/web-music-trend-research.md`, `references/research/user-listening-context-and-streaming-services.md`, and `references/research/reference-track-digging.md` when reference digging or user listening context matters.

Use snapshot notes for:

- `references/genres/*.md`
- `references/techniques/algorithmic-and-AI-assisted.md`
- `references/production-aware/pre-production-decisions.md` when reference-track selection is involved
- any future file that mentions current charts, living scenes, platform rules, AI/copyright status, recent artists, streaming-service behavior, or personal listening-context workflows

Do **not** update a snapshot date just because the file was edited. Update it only after checking the current-sensitive claims against active sources.

For current-source research, prefer official charts/platform pages, industry reports, regional/local sources, and primary documentation. Avoid turning a single viral track or platform trend into a universal genre rule.

## How to add new content

### Adding a new file to an existing folder

1. Write the file matching the conventions above (When to consult, body, Pitfalls, Quick decision matrix, Cross-references).
2. **Add it to `references/00-navigation.md`** — at minimum to the "Quick lookup" table; also to "Multi-file scenarios" if it crosses domains; also to "Cross-reference key" if it's part of a cluster.
3. **Update relevant existing files' Cross-references sections** to point to the new file. Don't update every file in the project — just the 2–4 files that are most directly related.
4. **Update `SKILL.md`** if the new file represents a meaningfully new topic that should be visible at the structural level (rare for files within existing folders).

### Adding a new top-level folder

When a topic is large enough to warrant 3+ files, it gets its own folder.

1. Create the folder under `references/`.
2. Write the first 1–3 files in it, each matching conventions.
3. **Update `SKILL.md`** — add the folder to the "Top-level structure" diagram and to any other places the structure is mentioned.
4. **Update `references/00-navigation.md`** — add a section for the new folder's topics in the "Quick lookup" table; add to "Multi-file scenarios" if relevant; add to "Cross-reference key" if it forms a cluster with existing folders.
5. Update existing files' Cross-references where the new folder is genuinely related.

### Adding a new asset file

1. Write the asset file. Asset files are shorter and looser than reference files but still need a title, opening paragraph, and Cross-references section.
2. **Update `references/00-navigation.md`** — add to the "Cheatsheets — when to use `assets/`" table.
3. **Update `SKILL.md`** — add to the asset list in the "Top-level structure" diagram if the asset is structurally significant.
4. Update related reference files' Cross-references to point to the new asset.

### Adding a new instrument-idiom file

Instrument-idiom files are composition-facing. They should help the agent write playable, idiomatic parts; they should not become method-book lessons for how to practice the instrument.

1. Write the file under `references/instrument-idiom/`.
2. Update `references/instrument-idiom/overview.md` so the new file is discoverable inside the cluster.
3. Update `references/00-navigation.md` in the quick lookup table, multi-file scenarios if needed, and the cross-reference key.
4. Add 2–4 direct cross-references from related files such as `orchestration/instruments-ranges-character.md`, `orchestration/voicing-and-texture.md`, or a relevant genre file.
5. Run `scripts/music_theory_sanity_check.py`.

### Adding a new genre file

Genre files are special because every other file potentially refers to them.

1. Write the genre file under `references/genres/`.
2. **Update `references/00-navigation.md`** — add to the "Genre routing" table.
3. **Update `SKILL.md`** — add to the genre list in the "Genre framing — always required" section.
4. **Update `MAINTENANCE.md`** (this file) if the genre is a major addition that affects skill philosophy or scope.
5. Don't update every other file's Cross-references — genre files are referenced from a long tail of places. Only update the most directly relevant ones (e.g., a new "Latin pop" file should be linked from `references/genres/pop-rock.md` and `references/genres/folk-roots-and-traditions.md`).

### Adding a microgenre, minor genre, or hybrid-scene file

If the topic is not large or stable enough for a dedicated major genre file, add coverage to `references/genres/minor-and-hybrid-genres.md` instead of creating many tiny files.

1. Add the tag or scene as a craft-variable note, not a definitive history.
2. Include a caution when the label is platform-born, local, or unstable.
3. Link to the relevant major genre files and research workflows.
4. If the topic grows large enough, split it into a dedicated `references/genres/<name>.md` file later.
5. Run `scripts/music_theory_sanity_check.py`.


### Adding a creative workflow file

Use `references/creative-workflows/` for user-agent process documents that are specifically about music-making sessions, not generic project management.

Checklist:

1. Define when the agent should consult the file.
2. Include concrete musical outputs: chords, motifs, rhythm grids, form maps, texture moves, or templates.
3. Keep user agency explicit: options before commands, decisions tracked, reversible assumptions.
4. Add reusable cards/templates to `assets/` when helpful.
5. Update `references/00-navigation.md`, `SKILL.md`, and `references/source-bibliography.md`.
6. Add the new file to `scripts/music_theory_sanity_check.py` expected files if it is a major expansion.

### Adding a validation or release-readiness file

Use `references/validation/` for maintainer-facing QA documents: first-release readiness, Phase B correctness passes, Phase C result records, prompt smoke tests, RC packaging checklists, release checklists, and validation procedures. Runtime composition answers should almost never load these files.

Checklist:

1. Define whether the file is a release blocker checklist, correctness pass, prompt test suite, or optional audit aid.
2. Link it from `references/00-navigation.md` only in maintainer / validation routes.
3. Update `RELEASE-ROADMAP.md` if the file changes first-release scope or quality gates.
4. Update `SKILL.md` if the validation folder structure changes.
5. Add critical validation files to `scripts/music_theory_sanity_check.py` expected files.
6. Keep validation claims factual: if a check was not run, mark it as not run.
7. If the file affects release-candidate packaging, update `KNOWN-LIMITATIONS.md` or the validation report template as needed.

### Adding a research workflow file

Research workflow files should help the agent gather evidence, not freeze current facts.

1. Place the file under `references/research/`.
2. Include a `Snapshot note` near the top.
3. State when to use the file, safe inputs, source hierarchy, output template, pitfalls, and cross-references.
4. If the file involves user-provided data, include privacy and credential boundaries.
5. Update `references/00-navigation.md`, `SKILL.md`, `references/source-bibliography.md`, and related research files.
6. Run `scripts/music_theory_sanity_check.py`.

### Renaming or moving a file

This is the most error-prone operation. There's no automatic refactoring; all links are plain-text relative paths.

1. **Search the whole project for the old path** before moving:
   ```
   grep -rn "old-filename.md" .
   ```
2. Move the file.
3. Update every link found in step 1.
4. **Re-run the search to verify zero hits on the old path.**

### Removing a file

1. Search for all links to the file (as in renaming).
2. Either delete the links (if the topic is being removed entirely) or redirect them to the replacement file.
3. Remove the file.
4. Update `00-navigation.md` and `SKILL.md` to remove references.

## A simple link-validation script

This isn't part of the skill — it's a maintenance helper. Save as `scripts/check-links.sh` (or run from the project root):

```bash
#!/usr/bin/env bash
# Find all backtick-wrapped `path/file.md` references and check whether
# the referenced file resolves. Filters false positives:
#  - Wildcard references like `genres/*.md` (idiomatic shorthand)
#  - Placeholder/example paths in MAINTENANCE.md
#  - Resolution attempts: same dir, project root, references/, assets/
set -e
cd "$(dirname "$0")/.." || exit 1

errors=0
total=0

while IFS=: read -r src_file src_line ref_match; do
  ref_path=$(echo "$ref_match" | sed -E 's/.*`([^`]+\.md)`.*/\1/')
  total=$((total + 1))

  # Skip wildcard shorthand
  case "$ref_path" in
    *\**) continue ;;
  esac

  src_dir=$(dirname "$src_file")
  if [[ -f "$src_dir/$ref_path" ]]; then continue; fi
  if [[ -f "./$ref_path" ]]; then continue; fi
  if [[ -f "./references/$ref_path" ]]; then continue; fi
  if [[ -f "./assets/$ref_path" ]]; then continue; fi

  case "$ref_path" in
    SKILL.md|MAINTENANCE.md) continue ;;
  esac

  echo "BROKEN: $src_file:$src_line -> $ref_path"
  errors=$((errors + 1))
done < <(grep -rn '`[^`]*\.md`' . --include='*.md' 2>/dev/null)

echo "---"
echo "Checked $total link instances; $errors broken."
```

Run after any file move, rename, or deletion. The script accepts that wildcard references (`genres/*.md`) are idiomatic shorthand in this skill and doesn't flag them. If you add new placeholder examples to `MAINTENANCE.md` itself, the script may flag them — check the output and decide case by case.

## What the agent should never have to know

A few things the maintainer cares about that the agent doesn't:

- **This file (`MAINTENANCE.md`).** It's not in the agent's load path.
- **Git history.** The agent treats the current state of the files as truth.
- **Planning notes / TODOs.** If a topic is incomplete, mark it inline in the relevant file (`# TODO: expand the Locrian section`) rather than tracking it in a separate planning doc — the agent sees the inline TODO and can flag the gap honestly to the user.

## Future expansion

All originally-planned topics have been implemented (see "Already implemented" below). Future expansion is now driven by emerging needs rather than backlog. Likely future candidates if they come up:

- **Sound design and synthesis fundamentals** → would be a new file in `production-aware/` or a top-level folder, depending on scope
- **DAW-specific workflow guides** → these intentionally aren't in this skill's scope (the skill is composition-focused, not production-tool-focused), but specific workflow notes for working with composers could go in `workflow.md`
- **Deeper regional pop / tradition-specific music practices** → current starter files cover Latin pop/reggaeton, Afrobeats/amapiano, MENA pop, South Asian film-pop, country/Americana, metal/punk/hardcore, gospel/CCM, Brazilian pop/funk, regional-scene starters, folk/roots/tradition-specific writing, and a general microgenre/hybrid handling file. Future work should go deeper by region/subgenre when a topic becomes stable and large enough (e.g., regional Mexican, sertanejo/pagode/arrocha, raï, Turkish arabesk-pop, Punjabi-specific pop, South African gqom, etc.)
- **Music for accessibility / therapeutic contexts** → music therapy, music for sensory processing, sleep / wellness music, etc.
- **Live performance composition** → composing with live performance constraints (bands, ensembles, soloists) where the score is also a performance plan
- **Sacred music traditions in depth** → Western liturgical, Jewish liturgical, Islamic *qira'at* and *naat*, Buddhist chant, Hindu *kirtan* — currently scattered across folk-and-world, classical-periods, and choral-writing
- **Scoring for dance / ballet / contemporary movement** → distinct from concert music or theatre music; specific structural and rhythmic constraints

When adding any of these, follow the procedures above and update `00-navigation.md`, `SKILL.md`, and any directly-related cross-references.

### Already implemented (formerly planned)

The skill's originally-planned topics, now implemented:

- **Korean traditional / fusion** → `references/genres/korean-traditional.md` ✓
- **Additional Asian pop traditions** → `references/genres/cpop-and-southeast-asian-pop.md` (C-pop, Cantopop, T-pop, V-pop, OPM, Indo-pop) ✓
- **Prosody across languages** → `references/fundamentals/prosody-and-language.md` ✓
- **Feedback / critique workflow** → `references/critique-and-feedback.md` (single-file approach; can split into a folder if it grows) ✓
- **Pedagogy / teaching composition** → `references/teaching-composition.md` (single-file approach) ✓
- **Choral writing** → `references/orchestration/choral-writing.md` ✓
- **Microtonal / xenharmonic systems** → `references/techniques/microtonal.md` ✓
- **Response templates** → `assets/response-templates.md` ✓
- **Diagnostic checklists** → `assets/diagnostic-checklists.md` ✓
- **Style/reference/copyright guardrails** → `references/research/style-reference-and-copyright.md` ✓
- **Latin pop / reggaeton starter** → `references/genres/latin-pop-and-reggaeton.md` ✓
- **Afrobeats / amapiano starter** → `references/genres/afrobeats-and-amapiano.md` ✓
- **South Asian film-pop starter** → `references/genres/south-asian-film-pop.md` ✓
- **MENA pop / maqam-adjacent starter** → `references/genres/mena-pop.md` ✓
- **Country / Americana / roots starter** → `references/genres/country-americana.md` ✓
- **Metal / punk / hardcore starter** → `references/genres/metal-punk-hardcore.md` ✓
- **Gospel / CCM / worship starter** → `references/genres/gospel-and-ccm.md` ✓
- **Brazilian pop / MPB / samba-pop / funk carioca starter** → `references/genres/brazilian-pop-and-funk.md` ✓
- **Instrument-specific idiom cluster** → `references/instrument-idiom/overview.md` plus piano, guitar, bass, drums/percussion, strings, winds, brass, and vocals ✓
- **Source bibliography and verification guide** → `references/source-bibliography.md` ✓
- **User streaming-service listening context workflow** → `references/research/user-listening-context-and-streaming-services.md` ✓
- **Regional trend-evolution analysis workflow** → `references/research/regional-trend-evolution-analysis.md` ✓
- **Minor / microgenre / hybrid genre handling** → `references/genres/minor-and-hybrid-genres.md` ✓
- **Musical brainstorming workflow** → `references/creative-workflows/musical-brainstorming.md` ✓
- **User-agent collaboration workflow** → `references/creative-workflows/user-agent-collaboration.md` ✓
- **Revision and feedback loop workflow** → `references/creative-workflows/revision-and-feedback-loops.md` ✓
- **Answer calibration / controlled variation workflow** → `references/creative-workflows/answer-calibration.md` ✓
- **Brainstorming prompt cards** → `assets/musical-brainstorming-cards.md` ✓
- **Session brief and decision log templates** → `assets/session-brief-and-decision-log.md` ✓
- **Web-search cheatsheet** → `assets/web-search-cheatsheet.md` ✓
- **Chord-symbol ambiguity and parsing asset** → `assets/chord-symbol-ambiguity-and-parsing.md` ✓
- **Scale-degree spelling cheatsheet** → `assets/scale-degree-spelling-cheatsheet.md` ✓
- **Music-theory audit rubric** → `assets/music-theory-audit-rubric.md` ✓
- **Regional scene starter map** → `references/genres/regional-scene-starters.md` ✓
- **Folk/roots/tradition-specific guide** → `references/genres/folk-roots-and-traditions.md` ✓
- **Trend and reference matrices** → `assets/trend-and-reference-matrices.md` ✓
- **Game / interactive scoring** → `references/genres/game-music.md` (kept separate from film-tv-scoring; the interactive dimension is large enough to warrant a dedicated file) ✓
- **Media music (advertising, podcasts, trailers, library, branded content)** → `references/genres/media-and-commercial-music.md` ✓
- **Algorithmic / AI-assisted composition** → `references/techniques/algorithmic-and-AI-assisted.md` ✓
- **First release roadmap** → `RELEASE-ROADMAP.md` ✓
- **Release readiness checklist** → `references/validation/first-release-readiness.md` ✓
- **Phase B correctness pass** → `references/validation/phase-b-correctness-pass.md` ✓
- **Prompt smoke tests** → `references/validation/prompt-smoke-tests.md` ✓
- **Phase C smoke-test result record** → `references/validation/phase-c-smoke-test-results.md` ✓
- **RC1 packaging checklist** → `references/validation/rc1-packaging-checklist.md` ✓
- **Known limitations for first release** → `KNOWN-LIMITATIONS.md` ✓
- **v1.0 release notes, validation, and promotion decision** → `RELEASE-NOTES-v1.0.md` + `VALIDATION-v1.0.md` + `RC1-v1.0-decision-memo-2026-04-27.md` ✓

## Versioning

The skill is versionless by default — files are edited in place. If the maintainer wants version markers, add a `## Changelog` section at the bottom of `SKILL.md` rather than per-file changelogs.


## Optional automated validation

Run `scripts/music_theory_sanity_check.py` after structural edits, cheat-sheet edits, or new genre additions. It checks:

- broken internal `.md` references
- risky culture-shortcut or threat-coding terms
- known high-risk theory patterns fixed in previous patches
- basic interval inversion sanity checks
- required snapshot notes in current-sensitive folders
- expected expansion files for major patch additions
- basic mode-cheatsheet formula sanity checks
- basic chord/tension spelling sanity checks for common altered-extension claims
- expected research/microgenre/creative-workflow/validation expansion files
- basic chord-symbol parser sanity for common C-root symbols
- scale-degree spelling regression checks for modal, borrowed, and altered-dominant examples
- symmetric-scale spelling regressions for whole-tone and half-whole diminished examples
- Phase B correctness-pass documentation presence
- Phase C result and RC packaging documentation presence
- v1.0 release-note / validation documentation presence
- Known limitations documentation presence

The script is not a substitute for musical judgment or web/currentness review. It is a guardrail for regressions.
