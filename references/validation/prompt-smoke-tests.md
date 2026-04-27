# Prompt Smoke Tests

Use these prompts to test whether the skill routes correctly and answers in the intended shape. These are not unit tests for factual truth; they are behavioral smoke tests for the user-agent workflow.

## How to run the smoke tests

For each prompt:

1. identify which files the agent should consult,
2. answer using only the necessary files,
3. verify the answer has concrete musical output,
4. verify the answer avoids known pitfalls,
5. record pass / fail / partial with notes.

A passing answer does not need to be long. It needs to be useful, accurate, and appropriately scoped.

## Core generation prompts

| # | Prompt | Expected routing | Expected answer shape |
|---|---|---|---|
| 1 | “Give me a melancholy but not cliché 8-bar progression in C minor.” | `assets/progressions-catalog.md`, `harmony/functional-harmony.md`, maybe `harmony/chromatic-harmony.md` | 2–3 progressions, Roman numerals, why each works |
| 2 | “Make this melody less boring: C D E G E D C.” | `melody/melodic-construction.md`, `melody/motivic-development.md` | 2–4 revisions using contour, rhythm, sequence, target notes |
| 3 | “My chorus doesn’t hit.” | `assets/diagnostic-checklists.md`, `production-aware/energy-and-dynamics.md`, `songwriting/hooks-and-memorability.md` | diagnosis matrix + concrete fixes |
| 4 | “Write a jazzier reharm for I–vi–IV–V.” | `harmony/reharmonization.md`, `harmony/jazz-harmony.md`, `assets/jazz-voicings.md` | reharm versions, functions, optional voicings |
| 5 | “I want a 30-second ad cue that feels optimistic but not cheesy.” | `genres/media-and-commercial-music.md`, `production-aware/energy-and-dynamics.md`, `assets/response-templates.md` | timed form map, harmonic lane, instrumentation, ending button |

## Workflow prompts

| # | Prompt | Expected routing | Expected answer shape |
|---|---|---|---|
| 6 | “Let’s brainstorm three directions for a song about leaving home.” | `creative-workflows/musical-brainstorming.md`, `assets/musical-brainstorming-cards.md` | safe/fresh/wild lanes, each with musical seed |
| 7 | “Use the second idea, but keep the chorus hook from the first.” | `creative-workflows/user-agent-collaboration.md`, `creative-workflows/revision-and-feedback-loops.md`, `assets/session-brief-and-decision-log.md` | project card update, preserved element, revised direction |
| 8 | “I like the chords but hate the vibe.” | `creative-workflows/revision-and-feedback-loops.md`, `assets/diagnostic-checklists.md` | separates harmonic content from texture/groove/register/density |
| 9 | “Give me a handoff summary for another producer.” | `assets/session-brief-and-decision-log.md`, `references/workflow.md` | compact summary with decisions, branches, do-not-change list |

## Research/currentness prompts

| # | Prompt | Expected routing | Expected answer shape |
|---|---|---|---|
| 10 | “What’s current in K-pop hooks right now?” | `research/web-music-trend-research.md`, `research/regional-trend-evolution-analysis.md`, `genres/kpop-jpop.md` | web check required; distinguishes evidence from inference |
| 11 | “I use Apple Music. Help me dig J-pop references I can actually listen to.” | `research/user-listening-context-and-streaming-services.md`, `assets/web-search-cheatsheet.md`, `research/reference-track-digging.md` | service-aware digging steps; no account access request |
| 12 | “Find reference tracks for a hyperpop-meets-country hook.” | `genres/minor-and-hybrid-genres.md`, `genres/country-americana.md`, `research/reference-track-digging.md` | hybrid matrix, craft variables, anti-copy guardrails |
| 13 | “Compare Korean and Japanese pop trend changes over the last five years.” | `research/regional-trend-evolution-analysis.md`, `research/web-music-trend-research.md`, relevant genre files | web check required; separates platform, industry, prosody, arrangement |

## Style/originality prompts

| # | Prompt | Expected routing | Expected answer shape |
|---|---|---|---|
| 14 | “Make this sound like a specific living artist.” | `research/style-reference-and-copyright.md`, `research/reference-track-digging.md` | refusal to clone; craft-variable alternative |
| 15 | “It sounds too close to my reference track.” | `research/style-reference-and-copyright.md`, `assets/diagnostic-checklists.md`, `creative-workflows/revision-and-feedback-loops.md` | similarity risk diagnosis + divergence moves |
| 16 | “Use the melody from this song but change the chords.” | `research/style-reference-and-copyright.md` | avoid copying protected melody; suggest original contour/mood alternative |

## Cultural and regional prompts

| # | Prompt | Expected routing | Expected answer shape |
|---|---|---|---|
| 17 | “Give this a Korean traditional fusion feel.” | `genres/korean-traditional.md`, `genres/folk-roots-and-traditions.md`, `research/reference-track-digging.md` | asks/infers tradition; rhythm/ornament/instrument context; no generic color |
| 18 | “I want maqam-adjacent MENA pop color.” | `genres/mena-pop.md`, `techniques/microtonal.md`, `research/reference-track-digging.md` | explains scale is not enough; suggests phrase/ornament/collaboration caution |
| 19 | “Make a regional Mexican / urbano hybrid.” | `genres/regional-scene-starters.md`, `genres/latin-pop-and-reggaeton.md`, `research/web-music-trend-research.md` | hybrid-role matrix; web check for current scene if specificity matters |

## Instrument-idiom prompts

| # | Prompt | Expected routing | Expected answer shape |
|---|---|---|---|
| 20 | “This guitar part is hard to play.” | `instrument-idiom/guitar.md`, maybe `orchestration/voicing-and-texture.md` | playable voicing alternatives, tuning/capo/fretboard logic |
| 21 | “Make the bassline more active without cluttering the vocal.” | `instrument-idiom/bass.md`, `production-aware/arrangement-for-mix.md` | rhythmic fills, register boundaries, root/approach-tone strategy |
| 22 | “Write a brass stab for a funk-pop chorus.” | `instrument-idiom/brass.md`, `orchestration/voicing-and-texture.md`, relevant genre file | playable voicing, rhythm, range caution |
| 23 | “The vocal line is too hard to sing.” | `instrument-idiom/vocals.md`, `songwriting/topline-craft.md`, `fundamentals/prosody-and-language.md` | range, vowel, breath, leap, stress fixes |

## Teaching prompts

| # | Prompt | Expected routing | Expected answer shape |
|---|---|---|---|
| 24 | “Teach me why borrowed iv sounds sad.” | `harmony/chromatic-harmony.md`, `teaching-composition.md` | simple explanation + playable example + exercise |
| 25 | “Explain ii–V–I without assuming I know jazz.” | `harmony/jazz-harmony.md`, `teaching-composition.md` | plain explanation + one voicing + listening/playing task |

## Recording results

After running the suite, record the outcome in `phase-c-smoke-test-results.md`. If the suite is only partially run, state which groups passed, which were skipped, and which failures require routing or template changes.

## Pass criteria

A prompt passes when the assistant:

- consults the right routing cluster,
- gives concrete musical material,
- names assumptions when needed,
- asks no unnecessary clarification when it can make a safe assumption,
- avoids copying protected expression,
- avoids broad cultural shortcut labels,
- uses web research when currentness matters,
- does not use web research for stable theory questions unless the user asks for sources.

## Cross-references

- Release readiness → `first-release-readiness.md`
- Release roadmap → `../../RELEASE-ROADMAP.md`
- Response templates → `../../assets/response-templates.md`
- Diagnostic checklists → `../../assets/diagnostic-checklists.md`
- Musical brainstorming → `../creative-workflows/musical-brainstorming.md`
- User-agent collaboration → `../creative-workflows/user-agent-collaboration.md`
- Revision loops → `../creative-workflows/revision-and-feedback-loops.md`
- Answer calibration → `../creative-workflows/answer-calibration.md`
- Phase C results → `phase-c-smoke-test-results.md`
