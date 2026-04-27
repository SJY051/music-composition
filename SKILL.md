---
name: music-composition
description: Use this skill whenever the user asks for help with music composition, music theory, songwriting, harmony, melody, counterpoint, arrangement, orchestration, or musical analysis — across classical, jazz, pop, rock, hip-hop, R&B, electronic, film/TV, K-pop/J-pop, folk, or musical theatre. Triggers include explicit theory questions ("what scale fits over Cm7", "explain ii-V-I", "modulate from C to E♭"), craft questions ("write a chord progression for a melancholy bridge", "make this melody more memorable", "voice this chord on piano"), and vague creative problems that map to compositional techniques ("the chorus feels weak", "this transition is awkward", "my song sounds generic"). Use this skill even when the user describes the goal in non-technical terms — translating fuzzy creative problems into concrete compositional moves is exactly what this skill is for. Do NOT use for DAW operation, MIDI file generation, audio engineering, mixing/mastering, sound design, or notation software UI.
---

# Music Composition

A comprehensive composition skill covering music theory and compositional craft for both DAW-based and acoustic/score-based workflows. This skill does NOT handle DAW automation, MIDI generation, audio engineering, or notation software — those belong to other skills.

## Core philosophy

Composition is a series of decisions, not a list of rules to follow. When advising:

- **Frame techniques as options, not commandments.** A "rule" in voice-leading is a probability distribution that creates a certain sound. Breaking it makes a different sound, which may be exactly what's wanted. Always know which sound the user is after.
- **Explain *why* a technique produces its effect.** Cite the perceptual or contextual reason — "the leading tone resolves up because the half-step gravity is strong and the ear expects closure". This lets the user reason about novel situations rather than memorize rules.
- **When the user describes a feeling or goal, give multiple options.** "I want this to feel uneasy" has many valid solutions (tritone substitution, modal mixture, polychords, rhythmic displacement). Offer 2–4 with their trade-offs rather than picking one.
- **Be concrete.** "Try a iv chord" beats "try modal mixture." "Voice this with the 3rd on top in close position, low E in the bass" beats "make it tighter." Always give the user something they can play.
- **Respect genre conventions but don't be enslaved by them.** A "wrong" choice in jazz might be perfect in indie rock. Always know which genre frame the user is operating in.
- **When the user describes a vague creative problem, translate it before answering.** "The chorus feels weak" decomposes into: melodic range, harmonic surprise, dynamic contrast, arrangement density, rhythmic activity, lyric/syllable density. Diagnose, then prescribe.
- **Don't moralize about technique.** Parallel fifths aren't immoral. They're a sound. Bach avoided them; Debussy used them; the user's track might want them.

## What this skill does NOT cover

- **DAW operation** — keyboard shortcuts, plugin parameters, automation lanes (separate skill).
- **MIDI file generation or direct manipulation** — handled elsewhere.
- **Audio engineering / mixing / mastering / sound design** — frequency-aware *composition* is in `production-aware/`, but EQ, compression, and synthesis decisions are out of scope.
- **Music history trivia** unconnected to composition technique. (Stylistic conventions of a period ARE in scope.)
- **Music notation software operation** (Sibelius, Finale, Dorico, MuseScore UI).
- **Performance pedagogy or instrumental exercise routines** for becoming a player. Composition-facing playability and idiomatic writing are in `references/instrument-idiom/`, but this skill does not replace a private teacher, method book, or technique practice plan.

## Navigation

The bulk of this skill lives in `references/`. **Always start by reading `references/00-navigation.md`** — it maps user requests to the specific reference files you need.

Don't load every reference. Load only what's directly relevant to the current question. For most requests, 1–3 reference files is enough. If you would need 5+, the question is too broad — narrow it first, or pick the dominant aspect and answer that.

For quick lookups (chord progression catalogs, mode formulas, voicing libraries), check `assets/`. Asset files are short and can be quoted directly. Reference files should be synthesized, not quoted.

## Top-level structure

```
references/
├── 00-navigation.md              ← Read this first, every time
├── fundamentals/                 ← Pitch, intervals, scales, rhythm, notation, prosody
├── harmony/                      ← Chords, voice leading, modulation, jazz, modal, reharm
├── melody/                       ← Construction, motivic development, phrase structure
├── counterpoint.md               ← Species → tonal → fugue
├── rhythm-groove/                ← Rhythmic devices, groove/feel, odd meters
├── form/                         ← Classical & popular forms, narrative
├── orchestration/                ← Instruments, voicing, texture, density, choral writing
├── instrument-idiom/             ← Composition-facing playability for piano, guitar, bass, drums, strings, winds, brass, vocals
├── genres/                       ← Per-genre conventions (incl. Korean traditional, C-pop / SE Asian, Latin, Afrobeats, MENA, South Asian, country, metal, gospel, Brazilian, game, media/commercial)
├── songwriting/                  ← Lyrics, hooks, topline
├── analysis.md                   ← Roman numeral, form, Schenker, set theory
├── techniques/                   ← Theme & variation, 20th C., constraint-based, microtonal, algorithmic / AI-assisted
├── production-aware/             ← Pre-production, composition-mix interface, energy
├── research/                     ← Web trends, user listening context, regional trend evolution, reference digging, style/copyright guardrails
├── creative-workflows/           ← Musical brainstorming, answer calibration, revision loops, and user-agent collaboration patterns
├── validation/                   ← Release readiness, Phase B/C records, RC packaging, and prompt smoke tests
├── source-bibliography.md        ← Maintainer-facing source map and verification guide
├── workflow.md                   ← Starting, revising, hybrid-genre advising
├── critique-and-feedback.md      ← Evaluating user's existing work (critique mode)
└── teaching-composition.md       ← Pedagogy mode, learning paths, exercises

scripts/
└── music_theory_sanity_check.py   ← Optional validation and regression helper for maintainers

assets/
├── progressions-catalog.md
├── response-templates.md
├── diagnostic-checklists.md
├── trend-and-reference-matrices.md
├── musical-brainstorming-cards.md
├── session-brief-and-decision-log.md
├── web-search-cheatsheet.md
├── chord-symbol-ambiguity-and-parsing.md
├── scale-degree-spelling-cheatsheet.md
├── music-theory-audit-rubric.md
├── cadence-reference.md
├── modes-cheatsheet.md
├── intervals-and-scale-formulas.md
├── jazz-voicings.md
├── form-templates.md
└── chord-symbol-conventions.md
```

## Typical response workflow

1. **Identify the user's actual ask.** Surface goal (e.g., "write a sad chord progression in C") and underlying goal (e.g., "I want emotional weight without sounding cliché"). They're often different.
2. **Identify the genre frame.** A "sad chord progression" means very different things in chamber music, neo-soul, lo-fi hip-hop, and K-pop ballad. If unstated and ambiguous, ask. If implied, work with it but name the assumption.
3. **Read `references/00-navigation.md`** to find the relevant reference files.
4. **Load the minimal set** of reference files needed.
5. **Translate theory into concrete options.** Don't dump theory — produce 2–4 actionable suggestions with brief rationale and a clear sample (chord names, notes, rhythm).
6. **Note adjacent considerations** the user may not have thought of (e.g., "this works in C, but if you modulate to the relative minor at the bridge, you open up `iv–i–V–i`, which is darker still").
7. **Stop before over-explaining.** A concise, useful answer beats a comprehensive lecture.

## Notation conventions

Use these consistently throughout the skill:

- **Chord symbols** (lead-sheet / jazz style): `Cmaj7`, `Dm7`, `G7♭9`, `F♯dim7`, `B♭/D` (slash chord), `Cmaj7♯11`.
- **Roman numerals**: capital = major triad, lowercase = minor; `°` = diminished, `+` = augmented; arabic for inversions and 7ths (`I`, `vi`, `V7`, `ii⁶`, `V⁶/⁵`, `vii°⁷`, `iiø7`); `♭` and `♯` prefix for chromatic alterations of scale degree (`♭VI`, `♯iv°`); `/` for tonicization (`V/V`, `V7/vi`).
- **Pitches**: scientific pitch notation when register matters (C4 = middle C); plain letter names when unambiguous. Sharp = `♯`, flat = `♭`, double-sharp = `𝄪`, double-flat = `𝄫`.
- **Intervals**: `m2 M2 m3 M3 P4 A4 d5 P5 m6 M6 m7 M7 P8`; "tritone" acceptable when style is informal.
- **Scale degrees**: `^1 ^2 ^3 ...` when concise; "tonic / supertonic / mediant / subdominant / dominant / submediant / leading tone" in prose.
- **Tempo**: BPM (`120 BPM`); `♩=120` when discussing notation.

## Genre framing — always required

The same musical question has different answers in different genres. Before applying any technique, identify the genre frame:

- Classical (which period?)
- Jazz (which sub-style?)
- Pop / rock / indie
- Hip-hop / R&B / neo-soul
- Electronic (which sub-style?)
- Film / TV (what dramatic context?)
- Game / interactive media (what platform / interactive system?)
- Advertising / podcast / branded content / trailer / library music
- K-pop / J-pop
- C-pop / Cantopop / T-pop / V-pop / OPM / Indo-pop
- Latin pop / reggaeton / urbano
- Brazilian pop / MPB / samba-pop / funk carioca
- Afrobeats / amapiano
- South Asian film-pop / raga-derived pop
- MENA pop / maqam-adjacent fusion
- Korean traditional (*gugak*) and K-trad fusion
- Country / Americana / roots
- Metal / punk / hardcore
- Gospel / CCM / worship
- Folk / roots / tradition-specific writing
- Regional scene starters and local-pop idioms
- Minor / microgenre / hybrid scenes
- Musical theatre

If the user hasn't named one and context doesn't make it obvious, ask. Don't default silently — you'll give wrong-feeling advice.

## Extensibility

This skill is designed to grow. To add new content:

1. **New genre or sub-genre**: add `references/genres/<name>.md`, update `00-navigation.md`'s genre table.
2. **New technique**: add to the most relevant existing folder, or create a new sub-folder if the topic is large enough to warrant 3+ files.
3. **New cheatsheet / matrix asset**: add to `assets/`, update `00-navigation.md`'s asset map.
4. **New instrument idiom**: add `references/instrument-idiom/<instrument>.md`, update `instrument-idiom/overview.md` and `00-navigation.md`.
5. **New current-research workflow**: add to `references/research/`, include a snapshot note, update `00-navigation.md`, and link from related genre files.
6. **New user-agent creative workflow**: add to `references/creative-workflows/`, update `00-navigation.md`, and add quick templates in `assets/` if the workflow benefits from reusable cards. Use `creative-workflows/answer-calibration.md` for bounded variation, answer length, and loading discipline.
7. **New validation / release-readiness file**: add to `references/validation/`, update `00-navigation.md`, `RELEASE-ROADMAP.md` if relevant, and add expected-file checks when it becomes release-critical. Ship `KNOWN-LIMITATIONS.md` or include its caveats in release validation reports.

When adding files, keep them under ~600 lines (split if longer), one topic per file, descriptive names. Always update `00-navigation.md` so the agent can find new content.

Recent expansion includes game/interactive scoring, microtonal/xenharmonic systems, choral writing, music for media, Korean traditional / K-trad fusion, C-pop / Southeast Asian pop, prosody, and algorithmic / AI-assisted composition. Recent expansion also includes response templates, diagnostic checklists, trend/reference matrices, musical brainstorming cards, session/decision-log templates, a web-search cheatsheet, style/copyright guardrails, user streaming-service listening context, regional trend-evolution analysis, regional scene starters, minor/microgenre handling, genre idiom files for Latin pop/reggaeton, Afrobeats/amapiano, South Asian film-pop, MENA pop, country/Americana, metal/punk/hardcore, gospel/CCM, and Brazilian pop/funk, plus composition-facing `instrument-idiom/`, `creative-workflows/`, and `validation/` folders, release-readiness docs, Phase C smoke-test result recording, RC1 packaging guidance, known-limitations documentation, answer-calibration workflow guidance, chord-symbol/scale-degree audit assets, and a maintainer-facing source bibliography. Future additions should prioritize prompt-smoke-test runs, deeper regional genre idioms, instrument-family expansions where needed, style-specific reference libraries, and stronger automated validation; the Phase B correctness-prep checklist now lives in `references/validation/phase-b-correctness-pass.md`.

## Honesty about gaps

If a user asks about a topic this skill doesn't yet cover, say so explicitly: "This skill doesn't have a dedicated reference for [X] yet — I'll work from general principles and flag what I'm uncertain about." Then do that. Don't fabricate confident answers from gaps.
