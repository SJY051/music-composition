# Pre-Production Decisions

> **Snapshot note:** Last content review snapshot: 2026-04-27. Reference-track practice is current-sensitive. For live trend checks, user listening context, and reference-set building, see `../research/web-music-trend-research.md`, `../research/user-listening-context-and-streaming-services.md`, and `../research/reference-track-digging.md`.

This file is about the decisions a composer makes *before or during the earliest sketch phase* of a piece — choices that determine the shape of everything downstream. Key, tempo, length, instrumentation, and a few others. These look obvious in retrospect but are often where projects either find their footing or wander.

This file complements `arrangement-for-mix.md` (mix-aware arrangement choices) and `energy-and-dynamics.md` (production-side energy shaping). It also overlaps with `references/workflow.md` (the agent's process for helping a user start), but that file is about *how the agent advises*; this file is about *what the user is deciding*.

## When to consult this file

- The user is starting a new piece or song
- "What key should this be in?", "What tempo?", "How long should it be?"
- The user has a sketch but feels the foundation is wrong
- Picking a reference track and using it well
- Deciding when to commit to specific decisions vs. leave them flexible
- Demo-vs-production workflow questions

For starting techniques specifically (chord progression first, melody first, groove first), see `references/workflow.md`. For form templates by genre, see `references/form/popular-song-forms.md` and `assets/form-templates.md`.

## Why these decisions matter early

Most pre-production decisions are cheap to change at the sketch stage and expensive to change later. Switching keys after the vocal has been recorded is a re-record. Switching tempo after the song is mixed is rebuilding the song. Switching from "3-minute pop single" to "6-minute prog track" mid-process invalidates most of the formal decisions.

The agent's job at the pre-production stage is to help the user make these decisions deliberately rather than by default — and to flag when a "default" choice is going to cause problems later.

## Key selection

The most consequential early decision after deciding to start at all.

### Vocal range — the dominant constraint

For songs with a lead vocal, the singer's range usually dictates the key. Two things matter:

- **Tessitura match**: where the song "lives" should sit in the singer's comfortable middle. The chorus should *land* in the part of their range that sounds full, not strained.
- **Range coverage**: the song's lowest note and highest note should both be within the singer's reachable range, ideally with some headroom above the highest belt note.

Common pop / rock / R&B vocal range zones (untrained-to-pro):

| Voice type | Comfortable middle | Top end (with effort) |
|-----------|--------------------|------------------------|
| Female pop (mezzo / alto-leaning) | A3 – D5 | F5 – G5 |
| Female pop (soprano-leaning) | C4 – F5 | A5 – C6 |
| Male pop (baritone / tenor-leaning) | A2 – C4 | E4 – G4 |
| Male pop (high tenor / countertenor) | C3 – E4 | A4 – C5 |
| Mixed-genre belters (any sex) | varies | F5–G5 (female), G4–A4 (male) standard for "money note" |

These are rough zones. Always ask the singer what their actual comfortable middle is before picking a key. Many demos are written in keys that are too high or too low because the writer used their own voice as reference.

### Instrument-friendly keys

Some keys are easier for some instruments. Picking a key that suits the dominant instrumentation can make demos faster and arrangements more idiomatic.

| Instrument | Easy keys | Awkward keys |
|------------|-----------|---------------|
| Acoustic guitar (open chords) | E, A, D, G, C | E♭, A♭, F♯ (require capo or barre) |
| Electric guitar (rock) | E, A, D, G (drop-D adds C, B, F) | F, B♭ (less idiomatic riffs) |
| Piano | C, F, G | F♯/G♭ (all-black-key feel; some pianists prefer this) |
| Strings | D, G, A, E (open strings) | D♭, G♭ (uncomfortable for double stops) |
| Brass | F, B♭, E♭ (concert pitch); these are friendly transposed-instrument keys | C♯, F♯ (uncommon and difficult) |
| Saxophone (alto, B♭) | F, B♭, E♭ concert | E, A, D concert |

Conflicts happen — a singer's best key (E♭) might be awkward for the guitarist. Common solutions: capo for the guitarist, transpose the singer one step up or down, or accept the trade-off if vocal performance matters more than guitar idiom.

### Mood / character associations (weak signal but real)

Specific keys are sometimes felt as having character — partly cultural, partly because tunings and timbres vary across keys. These are weaker signals than tessitura or instrumentation but worth knowing:

- **Bright, "open" feel**: D, A, E
- **Warm, "rounded" feel**: F, B♭, E♭
- **Dark, melancholic feel**: B♭ minor, F minor, C♯ minor
- **"Heroic" / classical-feel**: E♭, D, A
- **Folk / singer-songwriter neutral**: G, C, D

Equal temperament removes most of the historical key-character associations (which existed because of unequal tunings), but instrument resonance, idiomatic voicing, and listener associations from popular tracks in those keys keep some of the character alive.

### Practical key-pick workflow

1. **Identify the singer** (if any). What's their comfortable middle and top?
2. **Identify the dominant instrument** (if any). What keys does it sit well in?
3. **Identify the chorus's highest note** (this is where the song "peaks" — make sure the singer can hit it).
4. **Pick the key** that lands the chorus peak at the singer's belt zone *and* is reasonable for the instrumentation.
5. **Test it.** Sing the chorus aloud. Play the verse on the chosen instrument. If it fights, try a half-step or whole-step shift.

Many demos start in the writer's voice's key and get transposed for the actual singer later. That's fine — but flag it explicitly so it doesn't get forgotten.

## Tempo selection

The second-most consequential early decision.

### Genre tempo conventions

See `references/fundamentals/rhythm-meter.md` for the full table. Quick reference for popular contexts:

| Style | Typical BPM range | Typical center |
|-------|-------------------|----------------|
| Pop ballad | 60–80 | 70 |
| Modern pop | 100–130 | 115–120 |
| K-pop dance | 110–130 | 120 |
| Hip-hop modern | 80–95 (or 140–160 in halftime) | 85 / 140 |
| House / EDM | 118–135 | 124 |
| Rock (mid-tempo) | 110–130 | 120 |
| Country | 80–130 | 110 |
| Film score (action) | 120–180 | 140 |
| Film score (drama) | 60–100 | 75 |
| Trailer music | 70–90 (often felt halftime) | 80 |
| Singer-songwriter | 70–110 | 95 |

Within a genre's range, BPM choice affects:

- **Energy level**: 105 BPM and 125 BPM in the same style feel notably different
- **Word density**: more BPM means less time per syllable, which constrains lyric density
- **Half-time / double-time feel**: a song at 140 BPM with a halftime drum pattern *feels* like 70, but the underlying grid is still 140 — this matters for production tempo settings

### Choosing between close tempi (115 vs. 120 vs. 125)

Small BPM differences can matter more than they look. Test:

- **Sing the chorus at the candidate tempo.** Does it feel rushed? Sluggish?
- **Walk to it.** Walking is roughly 100–120 BPM. Tracks that match walking pace feel natural; tracks that don't feel "energetic" or "lazy" relative to walking.
- **Compare to reference tracks.** If your song is supposed to feel like Track X, match its BPM (or be deliberate about differing).

### Tempo and structure interaction

A 4-bar phrase at 60 BPM lasts 16 seconds. A 4-bar phrase at 140 BPM lasts 7 seconds. So:

- Slow tempi can carry longer melodic phrases without the listener losing track
- Fast tempi need shorter phrases and more repetition to feel grounded
- Matching phrase length to tempo is part of why "this song feels rushed" or "this song drags" — usually a phrase-tempo mismatch

## Length and form commitment

Modern attention spans and platform conventions affect this more than they used to.

| Format | Typical length | Notes |
|--------|----------------|-------|
| TikTok / short-form social hook | 15–30 seconds | The hook is the entire song |
| Modern pop single | 2:30–3:15 | Streaming-era (skip rates incentivize shorter songs) |
| Traditional pop single | 3:00–3:45 | "Album track" length |
| Album cut (rock, indie) | 3:30–5:00 | Depends on band conventions |
| Prog / metal / extended track | 5:00–15:00+ | Form-justified length |
| EDM club mix | 5:00–7:30 | Designed for DJ mixing |
| EDM radio edit | 2:45–3:30 | Compressed version for radio |
| Film cue | 30 seconds – 5 minutes | Determined by scene length |
| Game music loop | 30 seconds – 2 minutes (loops) | Designed for seamless looping |

Decide the target length before writing. A song meant to be 2:45 should be sketched in sections that add up to 2:45, not "however long it ends up". A song meant to be 6:00 should plan for sustained development, not just stretch a 3-minute song with longer choruses.

## Reference tracks — using them well

A reference track (or "ref") is an existing song the user wants the new piece to feel like. References are powerful and dangerous in equal measure.

### What references are good for

- **Communicating a goal across collaborators**: "I want it to feel like *Track X*" tells the producer, mixer, and players what you mean.
- **Calibrating tempo, length, energy curve**: copy these specific parameters from a working example.
- **Identifying the genre frame**: a reference settles the "what genre is this?" question instantly.
- **Sound design / production aesthetics**: the timbral palette, drum sound, mix balance.

### What references are bad for

- **Melodic copying**: similarity to a reference's hook is how songs get sued. Use references for *vibe*, not for melodic content.
- **Excusing lazy decisions**: "I'll just do what they did" without understanding *why* leads to imitation that lacks the original's coherence.
- **Constraining the song's identity**: a song that's "X but with a Y twist" can become neither X nor Y. Sometimes the reference needs to be released once the song finds its own legs.

### A reference workflow

1. Pick 1–3 references early. Listen to them analytically.
2. Identify what specifically makes each reference work (form, tempo, key, instrumentation, hook structure).
3. Borrow the *parameters* (tempo, length, density profile) but compose original *content* (melody, harmony, lyrics).
4. After the first sketch, listen to the references again. Are you still aiming at the same target? Or has the song revealed its own direction?
5. If the song is becoming its own thing, let it. The references were scaffolding.

## Demo vs. production workflow

A frequent decision point: how polished should the early sketch be?

### Demo-first (most common for pop/rock songwriters)

- Quick, rough sketch with placeholder sounds
- Voice + piano/guitar, or voice + simple beat
- Goal: capture the song before deciding production direction
- Production happens later, with the song already proven on its own

Advantages: fast iteration, focuses on song quality, easy to pivot. Disadvantages: production-aware compositional moves can be missed (a song written on piano may not adapt cleanly to electronic production).

### Production-first (common for electronic / hip-hop / K-pop)

- Build the track sonically first — drums, bass, key sounds
- Topline (vocal melody and lyrics) added later, written *to* the track
- Goal: the production *is* the song, more or less

Advantages: track is sonically coherent from the start, productions tend to feel modern. Disadvantages: weak compositional bones can be hidden by production, songs that don't survive without production can feel hollow.

### Concurrent (common for film / orchestral)

- Composition and production move together (sequencing strings while writing them, for example)
- Goal: composition shaped by what the production will be

Advantages: no surprises in handoff. Disadvantages: slower iteration, harder to pivot.

When advising, ask which mode the user is in — it changes what advice is relevant. A demo-first songwriter doesn't need to worry about kick-bass spectral overlap yet; a production-first electronic producer should worry about it from the first bar.

## Cost-of-change for late decisions

When the user is past the sketch stage, some changes are very expensive. Flag this when relevant:

| Decision | Cheap to change at | Expensive after |
|----------|---------------------|------------------|
| Key | Any time before vocal recording | Vocal recorded |
| Tempo (small adjustment, ±5 BPM) | Pre-recording | Drums recorded |
| Tempo (large change, ±20 BPM) | Sketch stage only | Anything tracked |
| Form (add/remove section) | Pre-arrangement | Mixed |
| Time signature | Sketch only | Almost anything tracked |
| Genre / production direction | Pre-production (decision made before recording) | Recording started |
| Lyric (single line or word) | Almost any time | After all vocal takes done |
| Lyric (concept / theme) | Sketch only | Vocal tracked |

This isn't to discourage changes — sometimes a late change is necessary. But the user should know what it costs.

## Pre-production checklist

Before serious composition or recording starts:

- [ ] Genre / style identified (and primary vs. flavor if hybrid)
- [ ] Target length / format decided
- [ ] Tempo chosen (and tested by singing or walking to it)
- [ ] Key chosen (vocal-tested if there's a singer; instrument-friendly if relevant)
- [ ] Form template sketched (verse-chorus? AABA? through-composed?)
- [ ] Reference tracks selected and analyzed (1–3 max)
- [ ] If the user has a streaming service or playlist context, safe user-provided listening evidence considered
- [ ] Demo-vs-production workflow chosen
- [ ] Lead instrument and core instrumentation decided
- [ ] Lyrical concept (if applicable) clear enough to write the first verse

Not every project needs all of these settled before starting — but the agent should know which ones are open and which are closed when advising.

## Common pitfalls when advising

- **Don't pick the user's key for them without knowing the singer.** Range is everything for vocal music.
- **Don't recommend a tempo without testing.** What looks right on paper can feel wrong out loud.
- **Don't dismiss the cost of late changes.** A user planning to "just adjust the key in the mix" may not realize what that costs.
- **Don't over-lock decisions.** Some users benefit from leaving tempo/key flexible until the song reveals itself. Match the advice to the user's working style.
- **Don't confuse a reference with a destination.** A song aimed at a reference can never be the reference. The reference is the target zone, not the goal.
- **Don't forget mode and feel under "key".** "C major" and "C Mixolydian" are different keys for compositional purposes, even though they share a pitch collection.

## Quick decision matrix

| Stuck on | Consider |
|----------|----------|
| What key to pick | Sing the chorus melody at different transpositions; pick where the peak feels right in the singer's voice |
| What tempo to pick | Walk to candidates; pick where the chorus chant feels natural; check against reference tracks |
| Whether to commit to form yet | Decide format (single, album cut, EDM club mix) — this fixes target length, which constrains form |
| Demo or production first | Demo-first if writing in a singer-songwriter mode; production-first if writing electronic/hip-hop; concurrent for film |
| Whether to use a reference | Yes for vibe and parameters; no for melodic content; release the reference once the song finds its own identity |
| When a late change is necessary | Calculate the cost (re-record, re-arrange, re-mix); commit if the song requires it; don't if the change is cosmetic |

## Cross-references

- Tempo conventions and Italian tempo terms → `../fundamentals/rhythm-meter.md`
- Vocal range and tessitura by zone → `../melody/melodic-construction.md`, `../orchestration/instruments-ranges-character.md`
- Choral pre-production (key choice for SATB ensembles) → `../orchestration/choral-writing.md`
- Form templates and section length conventions → `../form/popular-song-forms.md`, `../../assets/form-templates.md`
- Mix-aware arrangement choices (after pre-production) → `arrangement-for-mix.md`
- Energy planning across the form → `energy-and-dynamics.md`, `../form/narrative-and-transitions.md`
- Starting techniques (which element to write first) → `../workflow.md`
- Genre-specific conventions for tempo, length, key → various `../genres/*.md`
- Current trend and platform-sensitive reference checks → `../research/web-music-trend-research.md`
- User listening context and streaming-service research → `../research/user-listening-context-and-streaming-services.md`
- Regional trend-evolution analysis → `../research/regional-trend-evolution-analysis.md`
- Reference-track matrix and anti-copy workflow → `../research/reference-track-digging.md`
- Game music length / loop / interactivity decisions → `../genres/game-music.md`
- Short-form / commercial duration decisions (15s, 30s, 60s formats) → `../genres/media-and-commercial-music.md`
