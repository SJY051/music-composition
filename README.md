[English](./README.md) | [한국어](./README.ko.md)

# Music Composition Agent Skill

![Version](https://img.shields.io/badge/version-1.0-blue) ![Docs License](https://img.shields.io/badge/docs-CC%20BY%204.0-green) ![Code License](https://img.shields.io/badge/code-MIT-blue) ![Skill](https://img.shields.io/badge/AI%20skill-Claude%20compatible-orange)

A modular knowledge and workflow skill for an AI music-composition assistant.

This repository is designed to help an agent turn vague creative requests — “make the chorus hit harder,” “give me a darker K-pop bridge,” “reharmonize this like jazz but not too dense,” “find reference tracks for my playlist” — into concrete musical decisions: chords, melody shapes, grooves, forms, arrangement moves, diagnostic feedback, and research workflows.

**Current release:** `v1.0`  
**Release date:** `2026-04-27`

---

## What this skill is for

Use this skill when an AI agent needs to help with:

- composition brainstorming
- chord progressions and harmonic direction
- melody, motif, phrase, and topline writing
- song forms, transitions, and narrative structure
- rhythm, groove, meter, and feel
- orchestration, arrangement, voicing, and instrument idiom
- genre-aware writing across pop, jazz, classical, game, media, regional, traditional, and hybrid styles
- critique and revision of a work in progress
- teaching music concepts in a practical composition-first way
- current music trend research and reference-track digging
- user-agent collaborative workflows across multiple turns

The skill is not a DAW, audio engine, MIDI generator, transcription engine, legal service, or substitute for a human specialist in culturally specific traditions. It is a structured reference and workflow layer for an AI assistant.

---

## Core design philosophy

The skill is built around a few practical principles:

1. **Composition is decision-making, not rule-following.**  
   Music theory is treated as a map of possible effects, not a list of commandments.

2. **Give playable, actionable output.**  
   Prefer concrete examples such as chord charts, scale-degree melodies, groove sketches, voicing suggestions, and revision blocks.

3. **Preserve user agency.**  
   Offer options, explain tradeoffs, and let the user choose a direction.

4. **Use only the references needed.**  
   The agent should usually start with `SKILL.md`, route through `references/00-navigation.md`, and load only the most relevant 1–3 files.

5. **Treat current music trends as research tasks.**  
   Static genre files provide stable craft conventions. Recent artists, charts, platform norms, and scene-specific references should be checked through active web research.

6. **Avoid shallow cultural shortcuts.**  
   Tradition-specific and region-specific music should not be reduced to generic “flavor.” The skill encourages naming the source tradition, function, language, rhythm system, instrumentation, and collaboration needs.

---

## Repository structure

```text
.
├── SKILL.md
├── MAINTENANCE.md
├── RELEASE-ROADMAP.md
├── KNOWN-LIMITATIONS.md
├── RELEASE-NOTES-v1.0.md
├── VALIDATION-v1.0.md
├── assets/
├── references/
│   ├── 00-navigation.md
│   ├── creative-workflows/
│   ├── form/
│   ├── fundamentals/
│   ├── genres/
│   ├── harmony/
│   ├── instrument-idiom/
│   ├── melody/
│   ├── orchestration/
│   ├── production-aware/
│   ├── research/
│   ├── rhythm-groove/
│   ├── songwriting/
│   ├── techniques/
│   └── validation/
└── scripts/
    └── music_theory_sanity_check.py
```

### Important files

| File | Purpose |
|---|---|
| `SKILL.md` | Root operating instructions for the agent. Start here. |
| `references/00-navigation.md` | Routing map for choosing the right reference files. |
| `assets/` | Short cheat sheets and response templates for quick use. |
| `references/creative-workflows/` | Brainstorming, revision, answer calibration, and user-agent collaboration. |
| `references/research/` | Web trend research, reference-track digging, streaming-service-aware research, and style/copyright guardrails. |
| `references/genres/` | Genre and regional starter guides. |
| `references/instrument-idiom/` | Composition-facing playability and idiomatic writing guides. |
| `references/validation/` | Release readiness, smoke tests, correctness passes, and packaging checklists. |
| `scripts/music_theory_sanity_check.py` | Regression checker for links, known theory errors, risky terminology, snapshot notes, and required files. |

---

## Suggested agent workflow

For most user requests:

```text
1. Read SKILL.md.
2. Use references/00-navigation.md to identify the smallest useful document set.
3. Load only the relevant reference files, usually 1–3.
4. Generate concrete musical output.
5. Explain why the choices work.
6. Offer a small number of next-step options.
```

For example:

| User request | Likely routing |
|---|---|
| “Give me a sad but not cliché progression.” | `harmony/functional-harmony.md`, `harmony/modal-harmony.md`, `assets/progressions-catalog.md` |
| “The chorus does not hit.” | `assets/diagnostic-checklists.md`, `songwriting/hooks-and-memorability.md`, `production-aware/energy-and-dynamics.md` |
| “Make this more playable on guitar.” | `instrument-idiom/guitar.md`, plus the relevant harmony or arrangement file |
| “Brainstorm three directions.” | `creative-workflows/musical-brainstorming.md`, `assets/musical-brainstorming-cards.md` |
| “Find current J-pop references.” | `research/web-music-trend-research.md`, `research/reference-track-digging.md`, `assets/web-search-cheatsheet.md` |
| “Use my playlist as a reference.” | `research/user-listening-context-and-streaming-services.md`, `assets/trend-and-reference-matrices.md` |

---

## Currentness policy

Some files include a snapshot note. These files contain information that can become outdated, especially around:

- current genre trends
- charts and streaming-platform behavior
- artist references
- regional scenes
- AI-assisted music tools
- copyright and policy developments

The snapshot note does not mean the file is permanently current. It means the file was last reviewed as of that snapshot date. For fresh claims, use the research documents and verify current sources.

Useful research files:

```text
references/research/web-music-trend-research.md
references/research/reference-track-digging.md
references/research/user-listening-context-and-streaming-services.md
references/research/regional-trend-evolution-analysis.md
references/research/style-reference-and-copyright.md
assets/web-search-cheatsheet.md
```

---

## Style, originality, and copyright guardrails

This skill is intended to help generate original musical ideas. It should not be used to copy protected expression from existing songs or artists.

When a user asks for a specific artist or song style, the agent should translate the reference into craft variables such as:

- tempo range
- groove type
- harmonic density
- form
- vocal range and phrasing style
- arrangement density
- instrumentation
- energy curve
- production-era cues

The agent should avoid reproducing or imitating protected elements such as:

- melody
- lyrics
- distinctive riffs
- samples
- signature producer tags
- highly specific vocal identity
- recognizable arrangement sequences from a particular recording

See:

```text
references/research/style-reference-and-copyright.md
KNOWN-LIMITATIONS.md
```

---

## Cultural and regional specificity

The skill contains guides for traditional, regional, and hybrid styles. These are composition-facing starter references, not replacements for cultural expertise, native-language knowledge, or practitioner collaboration.

When working with culturally specific material, prefer:

```text
specific tradition / region / language / function / rhythm / instrument idiom / performance context
```

Instead of vague labels such as:

```text
generic world flavor / ethnic color / Asian flavor / Middle Eastern flavor
```

Relevant files include:

```text
references/genres/korean-traditional.md
references/genres/folk-roots-and-traditions.md
references/genres/mena-pop.md
references/genres/south-asian-film-pop.md
references/genres/regional-scene-starters.md
references/research/regional-trend-evolution-analysis.md
```

---

## Validation

The v1.0 package passed the release validation recorded in:

```text
VALIDATION-v1.0.md
references/validation/first-release-readiness.md
references/validation/phase-b-correctness-pass.md
references/validation/phase-c-smoke-test-results.md
```

To run the sanity checker:

```bash
python scripts/music_theory_sanity_check.py
```

The checker looks for issues such as:

- broken internal Markdown references
- known high-risk music-theory regressions
- risky cultural shortcut terminology
- missing snapshot notes in current-sensitive files
- required release and validation files
- selected interval, mode, chord-symbol, and altered-dominant sanity checks

This checker is a regression tool, not a complete proof of musical correctness.

---

## Maintenance

Before changing the repository:

1. Read `MAINTENANCE.md`.
2. Update `references/00-navigation.md` when adding or moving files.
3. Keep high-use assets concise and accurate.
4. Use snapshot notes for current-sensitive files.
5. Run `scripts/music_theory_sanity_check.py`.
6. Record substantial validation work in the relevant validation document.

Recommended versioning:

| Change type | Suggested version |
|---|---|
| Typo, link, or small validation-script fix | `v1.0.x` |
| P0/P1 correctness hotfix | `v1.0.x` hotfix |
| New genre, workflow, or research documents | `v1.1` |
| Larger parser/evaluation harness improvements | `v1.1` or `v1.2` |
| Major structure change or file reorganization | `v2.0` candidate |

---

## Known limitations

See `KNOWN-LIMITATIONS.md` for the full list.

In brief, this skill does not directly provide:

- audio transcription
- DAW control
- MIDI export
- audio mixing or mastering
- legal advice
- guaranteed current trend knowledge without web research
- exhaustive expertise in every local or traditional music practice

---

## License

This repository uses a split license:

- Skill documents, references, assets, release notes, and validation documents are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
- Code in `scripts/` is licensed under the **MIT License**.

See `LICENSE.md` for details.
