# Answer Calibration and Controlled Variation

This file helps the agent keep composition answers useful, bounded, and appropriately variable. Use it when smoke tests show random but acceptable variation, when the user asks for repeated alternatives, or when a session risks becoming too verbose, too random, or too rigid.

For broader multi-turn collaboration, see `user-agent-collaboration.md`. For reusable formats, see `../../assets/response-templates.md`. For quick decision logging, see `../../assets/session-brief-and-decision-log.md`.

## When to consult this file

Use this file when:

- the user asks for multiple options, but not an essay;
- the user says “try again” or “give me another version”;
- a generated idea should vary without abandoning the chosen direction;
- the assistant is tempted to load many files or over-explain;
- a smoke test or review finds the answer shape good but inconsistent in length or scope;
- the user wants brainstorming, but the session needs convergence.

## Calibration principle

A composition assistant should be **predictable in structure** and **creative in material**.

Stable parts:

- routing discipline,
- response format,
- assumptions,
- user-chosen constraints,
- safety and originality boundaries.

Variable parts:

- chord voicings,
- melodic contours,
- rhythmic cells,
- texture choices,
- arrangement density,
- option labels and examples.

The agent should not make the whole workflow random just because the musical content is creative.

## Default answer budgets

| Task type | Recommended size | Good output |
|---|---:|---|
| Quick theory lookup | 1–3 short paragraphs | definition + example + caveat |
| Chord/progression generation | 2–4 options | chart + Roman numerals if useful + why it works |
| Melody/topline revision | 2–4 revisions | scale degrees or notes + contour/rhythm explanation |
| Vague problem diagnosis | compact matrix | highest-impact fix first |
| Brainstorming | 3 lanes | safe / fresh / wild or 3 named concepts |
| Iterative revision | one focused revision | keep/change/direction + before/after |
| Current trend answer | concise research summary | evidence vs inference + composition translation |
| Teaching | example first | explanation + tiny exercise |

If the user asks for “more,” expand the chosen lane rather than adding unrelated lanes.

## Controlled variation bands

When giving multiple creative options, vary along one or two axes at a time.

| Band | Use when | Variation level | Example |
|---|---|---|---|
| Safe | user wants usable material quickly | familiar form, clear harmony, low risk | diatonic progression with one color chord |
| Fresh | user wants identity | one unusual variable | borrowed chord, asymmetrical rhythm, register move |
| Wild | user wants exploration | several unusual variables, but still playable | meter shift + modal color + texture concept |

Do not present three options that differ only in labels. Each option should change an audible variable.

## Revision stability rules

When the user says “again,” “darker,” “less cheesy,” “more modern,” or “use option 2,” preserve the session identity.

| Preserve by default | Change only if requested |
|---|---|
| chosen branch | branch identity |
| key / tonal center | key center |
| tempo / meter | tempo grid |
| hook contour | hook rhythm / lyric stress |
| liked chords | harmonic function |
| reference role | direct reference material |
| do-not-change list | protected elements |

A revision should state what was kept and what changed. If both changed, the user may feel the assistant ignored them.

## Loading calibration

Use the smallest file set that can answer the current turn.

| Situation | Load budget |
|---|---:|
| stable theory lookup | 1 file, maybe 1 asset |
| genre-specific generation | genre file + one topical file |
| vague creative diagnosis | diagnostic asset + one relevant craft file |
| current trend / reference request | research file + relevant genre file + maybe web-search cheatsheet |
| multi-turn revision | collaboration/revision file + session template |
| release validation | validation docs only; do not load during normal composition |

If five or more files seem necessary, answer the dominant aspect first and name the adjacent area rather than loading everything.

## Assumption calibration

State assumptions only when they affect the result.

Good:

```text
I'll assume midtempo 4/4 alt-pop so the sketch is playable. I can reframe it for jazz or EDM later.
```

Too much:

```text
I need genre, tempo, instrumentation, vocal range, DAW, reference tracks, mix target, and release market before I can answer.
```

Bad:

```text
[Silently assumes a piano ballad when the user wanted metalcore.]
```

## Currentness calibration

Separate durable craft from current evidence.

```md
Durable frame: [genre conventions that do not depend on this week's chart]
Current signal: [what needs web/platform verification]
Composition move: [how to turn the signal into groove/form/hook/arrangement]
```

Do not use web research for stable interval/chord/mode facts unless the user explicitly asks for sources. Do use web research for recent artists, platform trends, current charts, software/tool status, law/policy, and living-scene claims.

## User-agency calibration

End creative responses with a decision point that helps the user move.

Good endings:

- “Pick A if the lyric matters most; pick B if the groove matters most.”
- “I’d prototype Option 2 first because it changes the chorus without rewriting the verse.”
- “The safest next edit is to keep the chords and only change the topline rhythm.”

Weak endings:

- “Let me know.”
- “There are many possibilities.”
- “It depends.”

## Common calibration failures

| Failure | Symptom | Fix |
|---|---|---|
| Too much theory | user asked for a progression, answer becomes lecture | put playable material first; explain after |
| Too many options | user gets five unrelated directions | limit to 2–4 and label trade-offs |
| Hidden randomness | repeated answer changes key/tempo/style | preserve project card constraints |
| Over-reading | answer pulls many unrelated files | pick dominant task and one adjacent file |
| Under-specificity | advice says “add energy” but gives no notes/chords | provide a bar, rhythm, voicing, or form move |
| False certainty | current scene claim stated as stable fact | mark evidence/inference and use web research |
| Over-questioning | asks for details that can be safely assumed | make a reversible assumption and proceed |

## Cross-references

- User-agent collaboration → `user-agent-collaboration.md`
- Musical brainstorming → `musical-brainstorming.md`
- Revision loops → `revision-and-feedback-loops.md`
- Response templates → `../../assets/response-templates.md`
- Diagnostic checklists → `../../assets/diagnostic-checklists.md`
- Session brief and decision log → `../../assets/session-brief-and-decision-log.md`
- Web-search cheatsheet → `../../assets/web-search-cheatsheet.md`
- Phase C smoke-test results → `../validation/phase-c-smoke-test-results.md`
