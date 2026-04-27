# Workflow

This file is about how the agent should approach composition advice — what questions to ask, in what order, and how to deliver useful guidance. It's the meta-file: not about music itself, but about how to help with music. It complements `00-navigation.md` (which handles file routing) by providing the diagnostic and advisory framework.

For navigating between files, see `00-navigation.md`. For analytical methodology (understanding existing music), see `analysis.md`. Other files cover the actual composition content.

## When to consult this file

- Starting any composition advice session
- The user's question is vague or under-specified
- Multiple possible directions exist; need to narrow down
- The user wants iterative feedback on a work in progress
- Diagnosing what's wrong with a piece
- Pedagogical contexts (teaching composition)
- Whenever the agent needs a sanity check on its approach

## The agent's role in composition

The agent is not the composer. The user is. The agent is a knowledgeable assistant who:

1. **Asks clarifying questions** before assuming.
2. **Provides options, not commands** — composition has no single right answer.
3. **Connects principles to the user's specific situation** rather than reciting general theory.
4. **Defers to the user's aesthetic judgment** while flagging potential issues.
5. **Encourages experimentation** — "try X, see if it works for you" rather than "do X".

Avoid:

- Issuing rules as commandments
- Dismissing user choices as "wrong" without explanation
- Imposing one stylistic framework (e.g., common-practice tonality) on music that's clearly in a different idiom
- Assuming the user wants what the textbook prescribes

## The diagnostic phase

Before giving advice, understand the situation. Common dimensions to clarify:

### Genre and style

What kind of music is the user writing?

- Period (classical era? Romantic? modern?)
- Genre (pop, rock, hip-hop, jazz, classical, film, etc.)
- Sub-style within genre (modal jazz vs. bebop vs. fusion)
- Reference points (specific composers / songs they're drawing on)

If the user hasn't specified, *ask* — don't assume. The advice differs enormously between, say, "a slow R&B ballad" and "a string quartet movement".

### Multi-genre and hybrid requests

Many real-world requests cross genres: "a K-pop song with jazz harmony", "a synth-pop track with classical counterpoint in the bridge", "a film cue that sounds like A Tribe Called Quest". These aren't confused — they're specific creative briefs. The agent's job is to identify which genre is the *primary frame* (the one whose conventions the listener will hear as the "style") and which is providing a **secondary influence** (a coloring or craft layer applied within the primary frame).

Diagnostic questions for hybrid requests:

| Dimension | What it usually anchors to |
|-----------|----------------------------|
| Form / song structure | Primary genre (a "K-pop song" stays K-pop in form even with jazz chords) |
| Production / sonic palette | Primary genre (drums, mix, instrumentation say "this is a hip-hop track") |
| Harmonic vocabulary | Often the secondary influence layer (jazz extensions over a pop progression, modal mixture in a rock chorus) |
| Rhythmic feel / groove | Often primary, occasionally flavor (Latin clave inside an R&B groove is flavor; Latin clave anchoring the whole tune is primary) |
| Melodic / vocal style | Can go either way; ask if unclear |

A useful frame: **the primary genre tells you what the listener will *call* the song; the secondary influence layer tells you what makes the song stand out within that category.** Stevie Wonder's "Sir Duke" is funk/soul (primary) with jazz harmonic vocabulary (secondary influence). Steely Dan tracks are pop/rock (primary, in form and length) with jazz harmony and bebop solo language (secondary influence). BTS's "Black Swan" is K-pop (primary) with cinematic / orchestral elements (secondary influence).

When the user names two genres without specifying which is which, ask:

- "Which genre's *form* are you working in?" — answers the primary genre most of the time
- "Which one is the listener supposed to identify the song as?" — same
- "What's the reference track — what existing song captures what you want?" — usually clarifies both layers at once

When the user is *deliberately* trying to blur the line (genre-bending, fusion, post-genre), the agent should drop the "primary + flavor" framing and treat each dimension independently. That's a different mode of advising — closer to "compose what you want, evaluate by the result" than to applying any genre's conventions.

### What stage they're at

- **Idea phase**: brainstorming, no notes on paper
- **Sketch phase**: rough draft, deciding direction
- **Working out details**: revising specific moments
- **Polishing**: making fine adjustments
- **Stuck**: not sure how to proceed
- **Diagnosing**: there's a problem, what is it?

Different stages call for different help. Brainstorming wants generative options; polishing wants targeted critique.

For detailed musical brainstorming workflows, use `creative-workflows/musical-brainstorming.md`. For long multi-turn sessions, use `creative-workflows/user-agent-collaboration.md` and `../assets/session-brief-and-decision-log.md`.

### Specific problem or open exploration

- "I have a verse that doesn't lead well to the chorus" — specific
- "How do I write a good chorus" — generic
- "Help me with my song" — too open

For specific problems, give targeted advice. For open requests, ask what they want to focus on.

### What they have

If the user can share the music (chord chart, melody, audio), engage with the actual material. Generic advice without the music is much weaker.

If they can't share, ask them to describe in detail: key, tempo, form, the parts that are working, the parts that aren't.

### What they want

Not always obvious. Some users want:

- Direct advice ("here's what to do")
- Options to choose from ("here are three approaches")
- Validation ("does this work?")
- Pedagogy ("explain why")
- Critique ("what's wrong with this?")
- Brainstorming ("give me ideas")

Match the response style to the user's apparent need.

## Asking good questions

Before assuming, ask clarifying questions:

| Situation | Questions to ask |
|-----------|------------------|
| User says "I have a song" | What genre? What's the form? What's working? What's stuck? |
| User wants to "learn composition" | What kind of music? What level? What goal? |
| User says "this doesn't sound right" | What specifically sounds wrong? Where in the song? What did you intend? |
| User asks for a chord progression | For what genre? What mood? Major or minor? |
| User asks how to write a melody | Over what chords? For what voice/instrument? In what genre? |
| User is comparing two options | What are you trying to achieve? Which feels closer to that? |

Don't barrage the user with questions; ask only what's needed to give useful advice. One or two clarifying questions are usually enough.

## Diagnosis: when something is "wrong"

Common symptoms and likely causes:

| Symptom | Likely causes |
|---------|---------------|
| "Doesn't go anywhere" | No clear arc; static energy; phrases not building |
| "Sounds boring" | Insufficient contrast (verse vs. chorus too similar); melodic monotony; predictable harmony |
| "Sounds wrong" | Voice-leading errors; non-idiomatic for the genre; prosody mismatch |
| "Feels stuck" | Lack of motion; too much repetition without development; static harmony |
| "Sounds amateur" | Generic / cliché choices; obvious in melody, chord progression, or rhythm |
| "Doesn't groove" | Microtiming issues; rhythmic mismatch between parts; lacking ghost notes or syncopation |
| "Chorus doesn't hit" | Insufficient contrast from verse; weak melodic hook; pre-chorus not building |
| "Sounds muddy" | Too many low / mid-range instruments; voicing too close in low register |
| "Sounds thin" | Not enough mid-range; sparse arrangement |
| "Lyrics don't fit" | Prosody mismatch; vowel choices wrong for the melody |
| "Melody feels off" | Wrong notes against the chord; awkward leaps; no climax; range issues |

For each diagnosis, the relevant file in this skill provides specific fixes:

- Energy / motion → `form/narrative-and-transitions.md`
- Voice leading → `harmony/voice-leading.md`
- Melodic problems → `melody/melodic-construction.md`
- Phrase issues → `melody/phrase-structure.md`
- Hook weakness → `songwriting/hooks-and-memorability.md`
- Texture problems → `orchestration/voicing-and-texture.md`, `orchestration/arrangement-density.md`
- Mix-ready problems → `production-aware/arrangement-for-mix.md`
- Genre conventions → relevant `genres/*.md`

## Workflow templates for common scenarios

### Scenario 1: User wants to start a new song

1. **Clarify the goal**: What genre? What feeling? Reference points?
2. **Suggest a starting point**: chord progression, lyric concept, melodic motif, or groove.
3. **Provide a skeleton**: 4 bars of chords, or a 4-line lyric prompt, or a tempo + drum pattern.
4. **Encourage iteration**: "try this; see if it sparks something".

### Scenario 2: User has a verse and wants help with the chorus

1. **Get the verse**: chords, melody, lyric, key, tempo.
2. **Identify the verse's tessitura and energy**: where is the chorus heading from?
3. **Suggest contrast**: higher tessitura, denser arrangement, hook-forward melody, possible modulation.
4. **Provide specific options**: "try these three chord changes for the chorus; here's a possible hook melody".

### Scenario 3: User has a song that "doesn't feel right"

1. **Get the song**: as much detail as possible.
2. **Listen / read carefully**: what's the actual problem?
3. **Diagnose**: which dimension(s) are off? Energy? Melody? Form? Voice leading? Production?
4. **Prioritize**: usually 1–2 issues are the main problem; fix those first.
5. **Provide targeted suggestions**: specific changes, not general advice.

### Scenario 4: User wants to learn a new style

1. **Identify the style** they want to learn.
2. **Recommend reference listening**: specific pieces that exemplify the style.
3. **Identify the style's characteristic features**: harmony, rhythm, form, etc. (using genre files).
4. **Suggest exercises**: write a piece using these specific techniques; analyze a sample piece; etc.
5. **Encourage gradual progress**: master one feature at a time.

### Scenario 5: User is stuck in the middle of a piece

1. **Get the section so far**: chords, melody, what's happening.
2. **Identify what's needed next**: build? release? contrast? return?
3. **Suggest specific moves**: "after this section, try a modulation to vi"; "here's a possible bridge".
4. **Test and iterate**: "try this; if it doesn't work, here's another option".

### Scenario 6: User wants critique on a finished piece

1. **Listen / read carefully** before critiquing.
2. **Identify what's working**: name specific moments and why they work.
3. **Identify what's not working**: name specific moments and what's off.
4. **Provide options for fixes**: not "do this"; "here are 2-3 ways to address this".
5. **Respect the user's vision**: they may disagree with your critique; their choice.

## When to defer to other files

The agent should:

- **Use this file** for meta-questions about workflow and approach.
- **Use `00-navigation.md`** when figuring out which content file applies.
- **Use specific content files** for specific topics. Don't try to recreate the whole skill in any single response.

When in doubt, route to the most specific applicable file:

| User asks | Direct to |
|-----------|-----------|
| "How do I voice this chord?" | `harmony/voice-leading.md`, `orchestration/voicing-and-texture.md`, `assets/jazz-voicings.md` |
| "What scale fits this chord?" | `harmony/jazz-harmony.md`, `fundamentals/pitch-intervals-scales.md` |
| "How do I write a hook?" | `songwriting/hooks-and-memorability.md` |
| "How do I structure a song?" | `form/popular-song-forms.md` (or `form/classical-forms.md`) |
| "Why doesn't my melody work?" | `melody/melodic-construction.md` |
| "How does this differ from [genre]?" | Two relevant `genres/*.md` files |
| "Show me a typical pop progression" | `assets/progressions-catalog.md` |
| "How do I modulate?" | `harmony/modulation.md` |
| "What's a sentence vs. a period?" | `melody/phrase-structure.md` |

The skill is comprehensive; specific questions usually have a specific answer file.

## Pedagogical principles

When the user is learning (rather than producing):

- **Show, don't just tell**. "Here's why this works" with a concrete example.
- **Build from simple to complex**. Master diatonic harmony before chromatic.
- **Connect abstract concepts to listening**. "This is what a deceptive cadence sounds like in [reference song]".
- **Give exercises**. "Try writing a 4-bar phrase ending in a deceptive cadence".
- **Encourage analysis**. Looking at how master composers solve problems is the best teacher.
- **Validate experimentation**. Mistakes are how composers learn.

## Pitfalls in advice-giving

- **Don't be didactic.** "You must do X" is rarely helpful. "Try X; here's why it might work" is.
- **Don't impose theoretical orthodoxy.** Common-practice voice leading is one set of constraints; many genres have different ones.
- **Don't dismiss the user's intuition.** If they think their chord change works and it does work for the genre, don't insist it shouldn't.
- **Don't over-explain.** Concise, targeted advice is usually better than 3 paragraphs of theory.
- **Don't reach beyond your competence.** If a question requires deep specialist knowledge (microtonal tuning, ethnomusicology, music engraving), say so and recommend specialist resources.
- **Don't mistake convention for necessity.** "Pop choruses are typically 8 bars" is convention, not law. The user can break it deliberately.
- **Don't forget the user's goal.** A user writing for a TikTok hook has different needs than one writing a string quartet movement.
- **Don't ignore available listening context.** If the user wants playlist fit or personal taste matching, ask for safe user-provided listening evidence before guessing from general trends.

## When to refer outside this skill

Some questions go beyond what this skill covers:

- **Specific software / DAW questions**: this skill is composition-focused, not production / DAW-focused. Recommend they consult software documentation or production tutorials.
- **Mixing and mastering**: covered briefly in `production-aware/arrangement-for-mix.md` and `production-aware/energy-and-dynamics.md`, but not in detail. Refer to specialized mixing resources.
- **Performance technique**: this skill doesn't cover instrumental technique, vocal training, etc. Recommend instrument-specific or pedagogical resources.
- **Copyright and music business**: not covered here. Refer to specialist legal / business resources.
- **Deep ethnomusicology**: this skill gives orientation to non-Western traditions but isn't a substitute for specialist study. Encourage collaboration with practitioners.

## A typical interaction shape

1. **User states their need** (composition help, critique, question).
2. **Agent clarifies** if needed (1-2 questions max).
3. **Agent identifies** the relevant content file(s) (often 1-3).
4. **Agent provides** advice tailored to the user's situation, citing relevant principles.
5. **Agent offers** options or alternatives.
6. **User responds** with feedback or follow-up.
7. **Agent iterates** based on the response.

The interaction is a conversation, not a lecture.

## Quick checklist for any composition advice

Before responding, consider:

- [ ] Is the user's situation clear, or do I need to ask?
- [ ] Have I identified the relevant content file(s)?
- [ ] Is my advice specific to the user's case, or am I just reciting theory?
- [ ] Am I providing options, not commands?
- [ ] Am I respecting the genre's conventions while encouraging exploration?
- [ ] Am I being concise rather than overwhelming?
- [ ] Am I deferring to the user's aesthetic judgment?
- [ ] If current trends, personal listening context, or microgenre labels matter, have I loaded the relevant research workflow?

## Cross-references

- File navigation → `00-navigation.md`
- Analysis methodology → `analysis.md`
- Critique mode (evaluating user's existing work) → `critique-and-feedback.md`
- Teaching mode (helping a user *learn*, not just solve a problem) → `teaching-composition.md`
- Pre-production decisions (key, tempo, length, references) → `production-aware/pre-production-decisions.md`
- User listening context → `research/user-listening-context-and-streaming-services.md`
- Musical brainstorming → `creative-workflows/musical-brainstorming.md`
- User-agent collaboration → `creative-workflows/user-agent-collaboration.md`
- Revision and feedback loops → `creative-workflows/revision-and-feedback-loops.md`
- Web/current trend research → `research/web-music-trend-research.md`
- Regional trend evolution → `research/regional-trend-evolution-analysis.md`
- Minor/hybrid genres → `genres/minor-and-hybrid-genres.md`
- Specific topic files → all other files in this skill
- Relevant `genres/*.md` for genre-specific guidance
- The SKILL.md root file for the skill's overall philosophy and scope
