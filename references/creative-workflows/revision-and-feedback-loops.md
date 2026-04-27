# Revision and Feedback Loops

Use this file when the user is iterating on a musical idea across turns: “make it less cheesy,” “keep the chords but change the vibe,” “the second idea was closest,” “try again but darker,” “don’t change the hook,” or “combine option 1 and 3.”

For broader collaboration state, see `user-agent-collaboration.md`. For quick templates, see `../../assets/session-brief-and-decision-log.md`. For troubleshooting vague problems, see `../../assets/diagnostic-checklists.md`.

## Revision principle

A revision request usually contains three layers:

1. **Keep** — what the user liked.
2. **Change** — what did not work.
3. **Direction** — the musical axis to move along.

Do not rewrite the whole idea unless the user asks for a full reset. Preserve the liked material and change the smallest musical variable that could solve the problem.

## Parse the user's feedback

| User phrase | Likely meaning | Musical variables to try |
|---|---|---|
| “Too cheesy” | too predictable, too bright, too familiar, too sentimental | reharm one cadence, reduce diatonic lift, change rhythm, darker voicing, remove obvious stock progression |
| “Too boring” | not enough contrast or identity | contour peak, rhythmic hook, non-chord tone, register shift, texture entrance |
| “Too busy” | too many simultaneous changes | reduce rhythmic density, simplify bass, remove counterline, widen arrangement space |
| “Too sad” | affect overshoots target | brighten one chord, raise register, use warmer rhythm, avoid continuous descending bass |
| “Not sad enough” | affect undershoots target | borrowed iv, ♭VI, minor plagal color, darker topline, slower harmonic rhythm |
| “Too jazzy” | extensions/voice-leading exceed genre frame | simplify extensions, use triads, reduce ii–V movement, keep color in one passing chord |
| “Not modern enough” | texture/rhythm/form feels dated | update groove, hook timing, vocal rhythm, sparse intro, production-aware arrangement cue |
| “Too close to the reference” | originality risk | change contour, rhythm, harmonic rhythm, form placement, instrumentation role |
| “Keep the hook” | preserve identity element | do not alter contour/rhythm/lyric placement unless asked |
| “Use option 2 but darker” | branch merge with affect shift | retain form/groove, change harmony/voicing/register |

## Minimal revision protocol

Use this when the user gives feedback but not a full new prompt.

```md
What I’m keeping:
- ...

What I’m changing:
- ...

Revision:
[concrete musical output]

Why it moves closer:
- ...

Still adjustable:
- ...
```

## Before/after block

```md
Before:
| C | Am | F | G |

After — darker but same basic shape:
| C(add9) | Am7 | Fm6 | Gsus4 G |

Kept:
- 4-bar loop
- tonic opening
- dominant return

Changed:
- borrowed iv color in bar 3
- softer dominant setup
```

## Three revision depths

| Depth | Use when | What changes |
|---|---|---|
| Micro | user likes most of it | one voicing, one note, one rhythm, one bass note |
| Meso | user likes the direction but not the result | chord substitution, phrase contour, groove density, section contrast |
| Macro | user says the concept is wrong | form, genre frame, emotional lane, reference set |

Default to micro or meso. Macro revisions can feel like the agent ignored the user.

## Branch handling

When there are multiple versions, name them.

```md
Branch A — clean pop version
Branch B — darker borrowed-chord version
Branch C — rhythm-first version
```

When the user picks one:

```md
Selected branch: B — darker borrowed-chord version
Keep from branch A: simpler vocal rhythm
Discard from branch C: syncopated bass
```

## Similarity reduction loop

Use when the user says a draft is too close to a reference.

| Similarity area | How to diverge |
|---|---|
| Melody contour | invert the contour, move peak earlier/later, change leap size |
| Rhythm | shift syncopation, change note density, alter pickup placement |
| Harmony | change harmonic rhythm, substitute one functional chord, change bass motion |
| Form | move hook location, add/remove pre-chorus, change phrase length |
| Arrangement | change instrument role, register, texture, density arc |
| Lyric/prosody | change stress pattern, vowel target, rhyme placement |

Keep the desired energy, function, or emotional target; change protected or signature expression.

## Feedback questions that are worth asking

Ask one question only when the next revision would otherwise branch too widely.

Good questions:

- “Should I keep the chord progression and only change melody/texture?”
- “Do you want darker harmony or darker arrangement?”
- “Should the hook stay exactly the same rhythmically?”
- “Is the reference too close because of melody, groove, or instrumentation?”

Avoid asking vague questions like “What vibe do you want?” when the user has already given a direction. Convert their words into musical variables and proceed.

## Cross-references

- User-agent collaboration → `user-agent-collaboration.md`
- Musical brainstorming → `musical-brainstorming.md`
- Session brief and decision log → `../../assets/session-brief-and-decision-log.md`
- Diagnostic checklists → `../../assets/diagnostic-checklists.md`
- Style/reference safety → `../research/style-reference-and-copyright.md`
- Response templates → `../../assets/response-templates.md`
