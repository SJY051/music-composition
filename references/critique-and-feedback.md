# Critique and Feedback

This file is about how the agent gives critique and feedback on a user's existing work — a finished or in-progress piece, a sketch, a recording, a lyric. Critique is a different mode from generative help (where the agent suggests what to write); it requires listening / reading first, identifying what's working and what isn't, and delivering observations in a way that respects the user's vision and supports their decision-making.

This file complements `workflow.md` (the agent's general advisory framework) and `analysis.md` (the methodology for analytically understanding a piece). Critique builds on analysis but adds an *evaluative* layer — and, more importantly, a *communicative* layer that determines whether feedback actually helps the user.

## When to consult this file

- The user shares a piece (audio, score, lyric, chart) and asks for feedback
- "What do you think?" / "Is this good?" / "What's wrong?"
- Comparing the user's work to a reference track they're aiming at
- Diagnosing why a piece "isn't working" without a specific symptom
- Helping the user evaluate their own work
- Late-stage critique (mixing review, mastering review — though mostly out of scope; see `production-aware/`)
- The user wants the agent to argue the case for or against a creative decision

## What kind of feedback is the user asking for

Different requests look similar but want different responses. The agent should identify which type before responding.

| User says | They probably want |
|-----------|---------------------|
| "What do you think?" | Open-ended response; usually validation + light critique |
| "Is this good?" | Quality judgment; often validation-seeking but might want honest assessment |
| "What's wrong with this?" | Specific problem identification; user has noticed something off |
| "How do I make this better?" | Generative critique with concrete options |
| "Critique this honestly" | Permission to be direct; user is ready for sharp observations |
| "Compare this to [reference]" | Benchmark assessment; specific comparative analysis |
| "Does this work for [genre/purpose]?" | Genre-fit assessment, not absolute quality |
| "I'm not sure about [specific element]" | Targeted critique on that element only |
| "This part feels weird but I can't tell why" | Diagnostic; user has the symptom, needs the cause |
| "My [collaborator/audience] said [criticism]" | Validate or refute the external feedback; meta-critique |

If unclear, ask: "Are you looking for honest critique, brainstorming for improvements, or just wanting to share?"

## Listen / read first, evaluate second

The most important rule of critique: don't critique what isn't there yet. Spend time engaging with the actual material before forming evaluative opinions.

For audio: listen multiple times. Try to feel its intent before naming its flaws. Then map the form, identify the strongest moments, identify what catches your ear (positively or negatively).

For a score / chart: read through, ideally hearing it internally. Identify the form, key plan, melodic identity, motivic structure.

For a lyric: read it as a poem first, then as a sung text. Notice imagery, structure, flow, emotional arc.

Forming critique without engaging fully with the material produces generic or wrong feedback. The agent should resist the temptation to start critiquing as soon as the user shares material.

## Lead with what's working

Genuine, specific praise before critique serves several purposes:

- **Calibrates the user's reading**: they know you've engaged with the actual work, not just pattern-matched to a generic critique
- **Identifies what to preserve**: improvements should not break what's already strong
- **Builds trust**: the user accepts critique more easily after seeing you appreciate the work
- **Models specific observation**: showing you can name a strong moment teaches the user how to identify them themselves

Avoid generic praise ("nice melody", "good vibe"). Specific praise: "the descending line in bar 12 lands the resolution beautifully" or "the contrast between the dense pre-chorus and the sparser chorus is a strong move".

If you genuinely can't find something that works, pause. Either the work is unusually weak (in which case ask the user what their goals are before critiquing) or you haven't engaged with it deeply enough yet.

## Critique frameworks

Different aspects of a piece can be evaluated against different criteria. The agent's job is to identify which framework applies to which observation, and to communicate that.

### Compositional dimensions

A piece can be examined along these axes (drawing from the rest of this skill):

- **Form**: section pacing, transitions, energy arc, length
- **Harmony**: progression choices, chromatic interest, voice leading, cadential weight
- **Melody**: contour, range, climax placement, motivic identity, memorability
- **Rhythm**: groove, syncopation, density, meter use
- **Lyrics** (if present): prosody, imagery, structure, point of view
- **Arrangement / orchestration**: instrument choices, voicing, density, layering
- **Production / mix** (if applicable): frequency balance, dynamic range, sonic identity
- **Performance**: vocal expression, instrumental phrasing, ensemble cohesion

Strong critique identifies *which dimension* is the problem, not just that "something feels off". A piece can have strong harmony but weak form; a piece can have a great hook but a weak bridge. Naming the dimension is half the work.

### Genre fit vs. absolute quality

A piece that doesn't work for its target genre might be excellent for a different genre. Distinguish:

- **Genre-fit critique**: "This isn't quite working as K-pop because [specific genre convention]"
- **Absolute critique**: "This doesn't work because [universal compositional issue]"
- **Cross-genre observation**: "This isn't K-pop, but it might work as something else"

Genre-fit critique requires identifying the target genre. If the user hasn't named it, ask. If they have, evaluate by that genre's conventions, not by some abstract standard.

### Intent vs. execution

A piece can be poorly executed in pursuit of a clear intent, or well executed but with unclear intent. The diagnosis matters:

- **Unclear intent + good execution**: the piece sounds professional but you can't tell what it's trying to do. Critique points at communication / focus.
- **Clear intent + poor execution**: you understand what they were going for but specific moments don't deliver. Critique points at technique.
- **Unclear intent + poor execution**: the broader, harder problem. Critique should start with intent before tackling execution.

When critique seems hard to formulate, this is often the underlying issue — you're trying to evaluate execution before knowing what it's executing.

### Personal artistic choice vs. compositional issue

Some apparent "problems" are deliberate artistic choices the agent should respect, not fix. Distinguish:

- **A choice that sounds wrong because it's wrong**: voice leading errors, prosody misalignment, technically unintentional dissonance
- **A choice that sounds wrong because it's unconventional**: deliberate dissonance, unusual structure, anti-genre move
- **A choice that sounds wrong because of the listener's frame**: the listener expected genre A; the user is making genre B

Only the first deserves "fix" framing. The other two deserve "this is a choice; here's what it costs and what it gains" framing.

When uncertain, ask: "Was the [unusual element] intentional?" If yes, treat it as a choice; if no, treat it as an issue.

## Communicating critique well

Beyond identifying what's wrong, the agent needs to deliver the observation in a way that helps the user act on it.

### Specific over general

- **Bad**: "The chorus could be stronger"
- **Better**: "The chorus melody peaks early — bar 2 is the highest note, and bars 3–4 don't have anywhere to go. Try saving the high note for bar 3 or 4."

Generic critique tells the user something is wrong but doesn't help them fix it. Specific critique points at the moment and suggests a direction.

### Options, not commands

- **Bad**: "Change the bridge to be in the relative minor"
- **Better**: "The bridge feels like it's not contrasting enough with the chorus. A few options: modulate to the relative minor, drop to half-time, strip the arrangement back to voice + piano. Pick the one that fits the song's emotional arc."

The user is the composer; the agent supplies options and rationale, not directives.

### Diagnose, then prescribe

Critique is most useful when the diagnostic frame and the prescriptive frame are connected. "The chorus doesn't hit because the verse already used the same harmony and density" is a diagnosis; "raise the chorus tessitura by a fourth and add a layered chorus vocal" is a prescription. Both serve.

The diagnostic frame matters because:
- It teaches the user to spot similar issues in future work
- It explains *why* the prescription should help
- It exposes alternative prescriptions the user can choose from

### Calibrate the dose

Some pieces need broad-strokes feedback; some need fine detail. Match:

- **Early sketch**: focus on broad structural / directional questions; don't critique production details that haven't been finalized
- **Working draft**: detailed compositional critique appropriate; production critique still premature
- **Near-final**: fine-grained critique at the level of specific bars, transitions, vocal lines
- **Released or about-to-release**: only critique on request; the piece is committed; offer perspective rather than prescription

### Order matters

When delivering multiple observations, sequence them well:

1. Lead with strengths (genuine, specific)
2. Address the most important issue next
3. Address smaller issues after
4. Close with options or a question that invites the user to direct further work

A critique that opens with "the form is off" and then mentions five smaller things buries the most important point. A critique that ends "what do you want to focus on next?" hands control back to the user.

## Defensive responses — when the user pushes back

Users sometimes resist critique. Reasons vary:

- They want validation, not critique
- The critique exposes anxiety about a section they were already worried about
- They disagree on artistic grounds
- The critique misunderstood the piece's intent
- The critique was technically correct but poorly framed

The agent should:

- **Acknowledge the disagreement without retreating from honest observation**. "I hear you — your intent there was X, and that does change my reading of that bar" is different from "you're right, I was wrong" or doubling down.
- **Distinguish technical issues from artistic choices**. If the disagreement is about a deliberate choice, that's fine — the user is the composer. If it's about a technical issue (voice leading error, prosody mismatch), the agent can hold the position while explaining why.
- **Offer to drop the topic**. If the user clearly doesn't want to engage, "let's leave that aside; what else can I help with?" respects their autonomy.
- **Don't get sycophantic when challenged**. Backing down from a well-founded observation in response to mild disagreement leaves the user without honest information. Hold positions calmly when they're well-founded; release positions when they're not.

## Critique in different stages

The right kind of critique depends on where the user is.

### Idea / concept stage

Critique here is mostly about whether the idea has compositional weight, whether it could go somewhere, and what the next move might be. Don't critique unwritten music; critique the seed.

Useful: "This concept is strong because [reason]; it suggests [direction]; the risk is [pitfall]."

Not useful: "The chorus might not hit." (No chorus exists yet.)

### Sketch / draft stage

Critique focused on form, key choices, structural decisions. Production-level critique premature.

Useful: "The verse-chorus relationship is clear; the bridge feels tacked on. Try connecting it to the chorus by [specific motivic / harmonic move]."

Not useful: "The kick isn't punchy enough." (Production isn't finalized.)

### Working draft

Most generative critique fits here. Compositional issues, motivic development, transition quality, lyric specificity all in scope.

### Near-final / mix-ready

Fine-grained critique. Specific bars, specific phrases, specific production decisions. Be careful — late-stage changes are expensive (see `production-aware/pre-production-decisions.md`).

### Released / committed work

Critique becomes retrospective rather than prescriptive. "This works because X; if I were doing this from scratch I might try Y" rather than "fix this".

## Pitfalls in critique

- **Don't critique what you didn't engage with.** Forming opinions before listening / reading thoroughly produces generic or wrong critique.
- **Don't impose your taste as truth.** "I would have done X" is your taste; "this doesn't work because Y" requires Y to be supported by something more than preference.
- **Don't critique unfinished elements.** A demo doesn't need mix critique; a sketch doesn't need polish critique. Match the depth of your critique to the stage of the work.
- **Don't blow up an entire piece for one issue.** "This whole piece doesn't work" is rarely true and rarely actionable. Identify specific issues; the piece probably has redeemable elements.
- **Don't avoid critique to spare feelings.** Sycophancy disguised as kindness leaves the user without honest information. Direct critique delivered respectfully is the kindness.
- **Don't pile critique high.** Five specific observations are more useful than fifteen. Prioritize.
- **Don't forget to check the user's goal.** Critique that ignores what the user was trying to do can be technically correct and entirely useless.
- **Don't moralize.** "This should be better" is moralizing; "this could be more X if Y" is critique. Stay in the descriptive-practical register.
- **Don't validate when you mean to critique, and don't critique when validation is warranted.** Both errors damage trust.

## When critique should turn into something else

Sometimes a "critique request" really wants something different:

- **The user is anxious and needs to be heard before being critiqued.** Listen / read; acknowledge the work's effort; ask what they want before evaluating.
- **The user is stuck and needs new options, not evaluation.** Switch to generative mode: brainstorm extensions, alternatives, fresh directions.
- **The user is comparing to a reference unrealistically.** Reframe: "this isn't [reference] because [reason]; that's a different goal — your piece has its own goal".
- **The user is processing failure.** Sometimes a piece they shared was rejected, didn't land with audiences, or didn't get them what they hoped. Critique here can sting. Acknowledge the context; offer perspective rather than dissection.

## Quick decision matrix

| User signal | Response mode |
|-------------|---------------|
| Excited share, fresh from finishing | Lead with what's working; offer light critique only if invited |
| "What do you think?" with low specificity | Validation-leaning; offer one or two specific observations; ask if they want more |
| "Is this good?" | Honest evaluative response with caveats about genre/goal/intent |
| "Critique this honestly" | Direct; pull punches less; still respectful, still specific |
| "What's wrong with [specific section]?" | Targeted diagnosis; don't drift to other sections unless invited |
| "How can I make this better?" | Generative critique: identify issues + concrete options |
| Sharing late-stage work | Match critique depth to stage; don't critique early-stage elements that have been finalized |
| Sharing released work | Retrospective framing; comment on what works and what was an interesting choice |
| Disagreement / pushback | Hold defensible positions; offer to drop the topic; don't get sycophantic |
| Visible distress about the work | Acknowledge effort; ask what they want before continuing critique |

## Cross-references

- The agent's general advisory framework → `workflow.md`
- Methodology for analyzing existing music → `analysis.md`
- Compositional dimensions to evaluate against → harmony files, melody files, form files, etc.
- Pre-production stage and what's appropriate to critique when → `production-aware/pre-production-decisions.md`
- Genre-specific evaluation criteria → relevant `genres/*.md`
- Pedagogical critique (when teaching, not when collaborating) → `teaching-composition.md`
- Production critique (frequency, mix) → `production-aware/arrangement-for-mix.md`, `production-aware/energy-and-dynamics.md`
- Lyric-specific critique → `songwriting/lyric-writing.md`
- Hook-specific critique → `songwriting/hooks-and-memorability.md`
