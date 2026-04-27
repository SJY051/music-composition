# Teaching Composition

This file is about how the agent helps users who are *learning* composition — as distinct from users who are *solving a specific compositional problem*. The two modes look similar at the surface but call for different responses: a learner needs scaffolding, exercises, and conceptual building; a problem-solver needs direct help. Mistaking one for the other wastes the user's time.

This file complements `workflow.md` (general advisory framework) and `critique-and-feedback.md` (evaluating finished work). Where `workflow.md` covers diagnostic questions for any user, this file focuses on the *pedagogical* mode — when the user wants to *learn* something, not just *do* something.

## When to consult this file

- The user is explicitly trying to learn composition
- "How do I learn [X]?" / "Teach me about [Y]"
- The user has a knowledge gap and wants to fill it
- Students or self-learners working through compositional problems
- The user has theory knowledge but lacks compositional practice (or vice versa)
- Cross-genre learning (a classical-trained user learning pop, or vice versa)
- The user wants exercises, not just answers

## Pedagogy mode vs. problem-solving mode

The agent should identify which mode the user is in. Signals:

| Pedagogy mode signal | Problem-solving mode signal |
|----------------------|------------------------------|
| "How do I learn..." | "How do I write..." |
| "Teach me..." | "Help me with..." |
| "Why does X work?" | "Make X work for me" |
| "What should I practice?" | "What should I do here?" |
| Student / hobbyist context | Professional / project context |
| Asking about general principles | Asking about specific work-in-progress |
| "I want to understand" | "I want to finish" |

These often blend. A user who's been writing for years might still want to *learn* a specific technique (modal harmony, fugue, K-pop song structure) while *solving* a current project's problems. The agent can be in both modes within a single conversation; the key is recognizing which mode any given exchange is in.

In pedagogy mode, the right response often *isn't* the direct answer. A user who asks "how does modal harmony work?" benefits more from a careful, layered explanation than from a one-paragraph definition followed by a chord chart.

In problem-solving mode, lecture is unwelcome. A user who asks "what scale should I use over Cm7 in this jazz solo?" wants a quick answer, not a tutorial on chord-scale theory.

## Where is the user in their learning journey

Different stages of learning need different help. Diagnose roughly:

### Complete beginner

No theory background, no compositional experience. May have technical instrument skill or just musical interest.

What helps:
- Concrete starting points (a single mode, a four-chord progression, a simple form)
- Pairing each concept with audible examples
- Avoiding jargon-dense explanations
- Encouragement to make many small finished pieces over fewer "perfect" ones
- Recommending listening, not just doing

What doesn't help:
- Comprehensive theoretical lectures
- Recommending advanced repertoire ("listen to Bach fugues") without bridging
- Treating notation as a prerequisite (many beginners benefit from working without notation initially)

### Theory-fluent, practice-light

Has studied theory (school, books, online), can analyze, recognizes terms — but has composed little or nothing. Common in classically-trained learners.

What helps:
- Permission to start producing work that isn't theoretically ambitious
- Exercises with strict constraints (write a 16-bar piece using only I-IV-V; write a melody using only stepwise motion)
- Connecting their existing analytical knowledge to specific compositional moves
- Encouragement to copy a model piece note-by-note as a learning exercise (not for publication)
- Listening to genres outside their training (a classical-trained learner studying pop hooks; a jazz student studying minimalism)

What doesn't help:
- More theory
- Pure brainstorming without constraints (they often freeze with too many options)
- Validation of their analytical skills as a substitute for compositional practice

### Practice-active, gap in specific skill

Composes regularly but has identified a specific weakness. "I can write good verses but my choruses don't hit"; "I can write good melodies but my harmonic choices are predictable"; "I can write pop but I want to learn jazz".

What helps:
- Direct engagement with the specific skill
- Exercises targeted at that skill
- Analytical study of pieces that exemplify it
- Trying the skill in a low-stakes context (an exercise, a sketch) before integrating it into "real" work
- Compounding feedback over multiple iterations

What doesn't help:
- Treating them as beginners
- Generic "study more theory" advice
- Refusing to engage with the specific gap

### Cross-genre learner

Trained or experienced in one tradition; wants to work in another. "I'm a jazz player who wants to write K-pop"; "I'm a classical composer who wants to score for film".

What helps:
- Identifying which skills transfer and which don't
- Highlighting the conventions of the target genre that aren't in their existing toolkit
- Recommending immersive listening in the target genre
- Acknowledging that genre-fluency takes time; first attempts will likely sound like "their existing genre with new flavors" rather than the target genre
- Working with practitioners of the target genre when possible

What doesn't help:
- Treating their existing expertise as irrelevant
- Underselling how different the target genre's logic is
- Letting them assume composition skills transfer fully

### Advanced learner

Has substantial composition experience; wants to deepen specific areas. May be working on advanced topics (12-tone, microtonality, advanced contrapuntal techniques) or refining craft in their established genre.

What helps:
- Engaging at their level; don't oversimplify
- Pointing at specific repertoire and analytical resources
- Treating exchanges as collaborative inquiry rather than instruction
- Acknowledging when their question goes beyond the agent's reliable knowledge

What doesn't help:
- Beginner-mode explanations
- Treating their work as if they need basic feedback
- Hiding uncertainty when the agent is at the edge of its competence

## Pedagogical principles

Drawing from broader composition pedagogy:

### Show, don't just tell

Concept + example + listening reference is the basic teaching unit.

- "A deceptive cadence is V→vi instead of V→I" (telling)
- "...and you can hear it dramatically in the second movement of Beethoven's 9th, after the choral entry — V wants I, but Beethoven gives you vi for one searing moment before resolving" (showing)
- "Try writing a 4-bar phrase that ends on a deceptive cadence" (doing)

The combination cements the concept. Telling alone produces students who can recognize a term without hearing what it does.

### Build from simple to complex

A learner studying chromatic harmony should already be comfortable with diatonic harmony. A learner studying Schoenberg should already understand tonal harmony deeply. The agent should diagnose the learner's foundation and build from there.

When a learner asks about an advanced topic before the foundation is solid, the agent has a choice:
- **Backfill the foundation first**: "this is great to learn, but I want to make sure the diatonic-harmony foundation is solid first; let's check..."
- **Skim the advanced topic with the caveat that some of it requires background to fully understand**: useful for a survey-level introduction
- **Refuse to engage at the requested level**: rarely the right choice; better to bridge than to gatekeep

### Connect abstract to listening

Every theoretical concept has audible expression. The agent should *always* pair concept with listening:

- "Modal mixture" → listen to The Beatles' "In My Life" (the borrowed iv)
- "Tritone substitution" → listen to almost any jazz standard's turnaround
- "Sentence structure" → listen to the opening of Beethoven's Op. 2 No. 1

Without listening references, the concept stays in the head; with them, it moves to the ear, which is where it belongs.

### Give exercises with strict constraints

Constraints generate creativity (see `techniques/constraint-based-composition.md`). For learners specifically:

- "Write a 4-bar phrase using only the notes of C major"
- "Write a 16-bar AABA using only I, IV, V, vi"
- "Write a melody where every note is a chord tone"
- "Write a 4-voice chorale ending in a Phrygian half cadence"
- "Set this lyric to a melody that doesn't go above the singer's middle range"

The constraint forces engagement with the concept being taught. A vague "write something using modal harmony" produces vague results; "write a 16-bar piece in D Dorian using only chords with major IV color" produces specific learning.

### Encourage analysis as teaching tool

Analyzing master composers' work is the deepest form of learning:

- Pick a piece in the genre / technique the user wants to learn
- Walk through it with them: form, harmony, melody, distinctive features
- Ask them to identify what makes it work
- Then have them try to apply one technique from it to their own piece

This is how composers have always learned — not by reading rules but by seeing what's been done and absorbing the logic.

### Validate experimentation

A learner who's only writing technically-correct music isn't learning quickly. They need to make mistakes — try things that don't work, hear why they don't, and refine. The agent should:

- Encourage trying ideas without prejudging them
- When something fails, diagnose *why* without making the failure feel shameful
- Treat experiments as data, not as moral judgments on the user's ability
- Distinguish "this didn't work but is a productive direction" from "this didn't work and isn't worth pursuing"

### Validate finishing as a skill

Many learners can start pieces but can't finish them. Finishing is itself a skill — it requires:

- Tolerating imperfection
- Making decisions and committing
- Closing off optionality

The agent should celebrate finished work, even imperfect work, as a real achievement. A finished mediocre piece teaches more than three abandoned promising ones.

## Common learning paths

These are common entry points; the agent can match its approach to which path the user is on.

### "I want to write a song"

A common starting point. The user usually has musical instinct but no formal training. Useful first moves:

1. Pick a target genre and study 3 reference songs in detail (form, key, melody, lyrics)
2. Learn basic chord voicings on guitar or piano
3. Write 4 chords in a 4-bar loop; sing over it
4. Build a verse / chorus around what emerges
5. Don't worry about polish; finish a sketch and start another

### "I want to learn music theory to compose better"

Common with self-taught composers who feel they're hitting a ceiling. Useful sequence:

1. Diatonic harmony (major and minor keys, primary chords, basic progressions)
2. Voice leading basics
3. Phrase structure (period, sentence)
4. Modulation (closely related keys first)
5. Modal mixture and secondary dominants
6. Chromatic harmony (Neapolitan, augmented sixths)
7. Modal harmony as a separate system
8. Jazz extensions and substitutions (if relevant to their work)
9. 20th-century techniques (if relevant)

The user should compose at every stage, not save composition for "after I finish theory". Theory studied without composition is largely abstract.

### "I want to learn jazz harmony / how to comp / how to solo"

Common for instrumentalists branching into jazz. Useful sequence:

1. ii-V-I in major and minor (the cellular unit)
2. Voicing 3-7 shells; then full rootless voicings
3. Chord-scale relationships (basic — Dorian over ii, Mixolydian over V, Ionian over I)
4. Basic substitutions (tritone sub, secondary dominants)
5. Reading a jazz standard and walking through its changes
6. Soloing over a 12-bar blues, then a standard's changes
7. Melodic-minor modes and altered scales
8. Reharm
9. Specific traditions: bebop language, modal jazz approach, contemporary jazz

### "I want to learn film scoring"

Useful sequence:

1. Watch film with the music in mind; identify what music is doing in each scene
2. Study a few specific scores (Williams, Zimmer, Goldsmith, Newman) — their themes, motifs, scoring techniques
3. Study film orchestration (instruments, ranges, doublings)
4. Compose to picture: take a 30-second clip and score it; iterate
5. Study trailer music and ad music (different conventions, useful for variety)
6. Eventually: study DAW work, mockup quality, tempo mapping

### "I want to learn K-pop / pop production"

Useful sequence:

1. Pick 5 reference K-pop tracks; analyze each fully (form, key, hook structure, production)
2. Replicate one of them as a learning exercise (don't release; learn the moves)
3. Study chord progressions used in K-pop ballads vs. dance tracks
4. Study how multiple hooks layer in a single song
5. Study production (Logic / Ableton / FL); production knowledge is non-negotiable for K-pop
6. Write original tracks applying the moves; iterate
7. Eventually: study Korean / English lyric craft for the genre

## Recommended exercise types

Across paths, certain exercises are reliable:

| Exercise | Teaches |
|----------|---------|
| **Bach chorale harmonization** | Voice leading, functional harmony, four-part texture |
| **Set a lyric to a melody** | Prosody, melody-text fit, phrase structure |
| **Reharmonize a familiar tune** | Reharm techniques, voice leading, harmonic vocabulary |
| **Write a melody using only one mode** | Modal vocabulary, characteristic notes |
| **Write a 12-tone row and a phrase derived from it** | Serial technique, atonal voice leading |
| **Compose a 16-bar AABA jazz tune** | Form, jazz harmony, head-writing |
| **Write a fugue exposition (3 voices)** | Counterpoint, imitation, subject construction |
| **Score a 30-second film clip** | Film-scoring craft, scene-music integration |
| **Write a song in an unfamiliar genre** | Genre conventions, expanding range |
| **Transcribe a piece by ear** | Ear training, analytical listening, repertoire knowledge |
| **Analyze a piece and write a piece in its style** | Analysis as composition tool |

The right exercise depends on what the learner needs. Pick one that targets their gap.

## Pitfalls in teaching composition

- **Don't lecture in pedagogy mode without checking comprehension.** Long explanations without check-ins lose the learner. Pause; ask if it makes sense; offer a small exercise.
- **Don't underestimate the learner's existing knowledge.** Asking what they already know prevents wasted explanation.
- **Don't assume one path fits all.** A classical-trained student learning pop has different needs from a self-taught songwriter learning theory.
- **Don't substitute analysis for composition.** Analytical knowledge is necessary but not sufficient. Composers learn by composing.
- **Don't treat mistakes as failures.** A learner who isn't making mistakes isn't learning. Failed experiments are data.
- **Don't gatekeep advanced topics.** A motivated learner can sometimes engage with advanced material without "earning" it through prerequisites. The teacher's job is to bridge, not to gatekeep.
- **Don't impose your aesthetic.** Teaching composition means helping the learner write *their* music, not yours.
- **Don't forget listening.** Composers learn primarily by ear. Theoretical instruction without paired listening references produces students who can talk about music but not hear it.
- **Don't conflate teaching with critiquing.** A learner sharing an exercise isn't asking for a finished-work critique. Match feedback depth to the work's purpose.
- **Don't move on too fast from a topic the learner hasn't actually absorbed.** Apparent understanding ("yes, I get it") often masks confusion. Confirm by asking for application.

## Quick decision matrix

| Situation | Approach |
|-----------|----------|
| User asks "teach me about X" | Pedagogy mode: definition + audible example + small exercise |
| User asks "help me with X in my piece" | Problem-solving mode: address the specific situation |
| Learner stuck on theory | Connect concept to audible example; assign small exercise |
| Learner can't finish work | Address finishing as a skill; encourage smaller-scope finishing |
| Cross-genre learner | Identify what transfers, what doesn't; recommend immersive listening |
| Beginner | Concrete starting points; pair every concept with a listening reference; encourage many small finished pieces |
| Advanced learner | Engage at their level; treat as collaborative inquiry; acknowledge knowledge limits honestly |
| Theory-fluent, practice-light | Constrained exercises; permission to produce non-theoretical work; pair with listening outside their training |
| Wants exercises | Pick one that targets their specific gap (table above) |
| Asks about advanced topic without foundation | Bridge: address the foundation while honoring the interest, or skim the topic with caveats |

## Cross-references

- General advisory framework → `workflow.md`
- Critique of finished work (different mode) → `critique-and-feedback.md`
- Analytical methodology (a key teaching tool) → `analysis.md`
- Constraint-based exercises → `techniques/constraint-based-composition.md`
- Counterpoint pedagogy (species method) → `counterpoint.md`
- Theme-and-variations as exercise structure → `techniques/theme-and-variation.md`
- Genre-specific conventions for each learning path → relevant `genres/*.md`
- Specific topic foundations → `fundamentals/`, `harmony/`, `melody/`, etc.
