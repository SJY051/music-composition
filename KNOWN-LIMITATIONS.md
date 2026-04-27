# Known Limitations for First Release

This file records what the first release of the music-composition skill is **not** trying to solve yet. It should be shipped with release candidates so maintainers and evaluators can distinguish genuine bugs from intentionally deferred scope.

## First-release boundary

The first release is designed to be a strong composition assistant: it can help users brainstorm, draft, revise, diagnose, analyze, learn, and prepare reference-informed musical ideas. It is not a complete music encyclopedia, a DAW manual, a legal service, or a replacement for expert performers and tradition-bearers.

Use this file with `RELEASE-ROADMAP.md`, `references/validation/first-release-readiness.md`, and `references/validation/phase-c-smoke-test-results.md` when preparing a release candidate.

## Known limitations

| Area | Limitation | Expected behavior |
|---|---|---|
| Current trends | Static genre files cannot stay current on charts, platform norms, viral scenes, or artist activity. | Use `references/research/web-music-trend-research.md` and active web verification for current claims. |
| User listening data | The skill cannot access private streaming libraries or account data by itself. | Ask only for safe user-provided evidence: public playlist links, track lists, Replay/Wrapped summaries, or screenshots. Never request credentials. |
| Copyright / style | The skill cannot guarantee legal clearance or produce legal advice. | Avoid copying melody, lyrics, riffs, samples, vocal identity, signature tags, or protected expression. Extract craft variables instead. |
| Cultural / traditional music | Starter guides are not substitutes for practitioner knowledge, language expertise, or tradition-specific study. | Name the tradition, scene, language, rhythm, ornament, function, and collaboration need instead of using broad labels. |
| Audio analysis | The skill does not transcribe audio directly, detect exact chords from recordings, or verify every famous-song progression. | Treat user-provided charts as approximate unless a reliable source is supplied; flag uncertainty. |
| MIDI / notation generation | This skill is text guidance, not a MIDI or score-generation engine. | Provide chord charts, scale degrees, form maps, rhythm grids, or notation-like sketches. |
| DAW / production operation | It does not teach DAW UI, plugin operation, detailed synthesis, mixing, or mastering. | Stay composition-facing: arrangement density, register, energy, and pre-production decisions. |
| Performance pedagogy | Instrument-idiom files are about writing playable parts, not training performers. | Give playability constraints and idiomatic writing moves, not technique-practice regimens. |
| Full genre coverage | Many scenes remain covered only by starter or dispatch documents. | Work from available genre files plus research workflows; say when a dedicated file does not exist. |
| Automated validation | The sanity checker catches regressions and broken links, not all musical truth. | Use manual review for nuanced harmony, genre, cultural, and currentness claims. |

## Non-blocking gaps for RC1

The following are useful but should not block a first release:

- dedicated deep guides for regional Mexican, Punjabi pop, Turkish arabesk-pop, Maghreb / raï, gqom, singeli, kuduro, sertanejo, pagode, arrocha, piseiro, and related local scenes;
- additional instrument idiom files for harp, mallet percussion, organ, accordion, synth performance idioms, and DJ / turntable-informed writing;
- a larger prompt-evaluation harness with automatically recorded routing traces;
- a deeper symbolic music-theory parser covering every chord symbol, Nashville number, and enharmonic edge case;
- comprehensive source citations inside every reference file;
- notation-software, DAW, audio-transcription, and MIDI-export workflows.

## When a limitation becomes a release blocker

A limitation becomes a blocker if it causes the agent to answer with false confidence rather than scoped uncertainty.

| Situation | Treat as blocker? | Why |
|---|---|---|
| A missing dedicated genre file, but the agent says it has one | Yes | Misrepresents coverage. |
| A current trend answer without web verification | Yes, when currentness matters | Static files should not freeze living scenes. |
| A cultural shortcut such as generic “world” or broad culture-as-color guidance | Yes | Violates the cultural-specificity principle. |
| A stable-theory answer that asks for web research unnecessarily | Usually no | Annoying behavior, but not false; improve routing if frequent. |
| A reference-style answer that copies a melody/riff/lyric/sample | Yes | Violates originality and safety guardrails. |
| A validation report claims unrun tests passed | Yes | Breaks release trust. |

## Recommended wording when a gap appears

Use a compact disclosure rather than a long apology:

```md
This skill does not have a dedicated guide for [scene] yet. I’ll treat it as a current scene question, verify recent references, and translate what I find into tempo, groove, harmony, topline, form, and arrangement variables.
```

For tradition-specific requests:

```md
I can sketch a respectful starting point, but this is not a substitute for a practitioner or native-language collaborator. I’ll name which musical variables I’m borrowing and avoid treating the tradition as generic color.
```

For exact transcription requests:

```md
I can analyze the chart or notes you provide, but I won’t claim this is the exact recording transcription unless you provide a reliable score or source.
```

## Cross-references

- Release roadmap → `RELEASE-ROADMAP.md`
- First-release readiness → `references/validation/first-release-readiness.md`
- Phase C results → `references/validation/phase-c-smoke-test-results.md`
- Web trend research → `references/research/web-music-trend-research.md`
- User listening context → `references/research/user-listening-context-and-streaming-services.md`
- Style/reference guardrails → `references/research/style-reference-and-copyright.md`
- Source bibliography → `references/source-bibliography.md`
