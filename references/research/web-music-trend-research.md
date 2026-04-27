# Web Music Trend Research

> **Snapshot note:** Last content review snapshot: 2026-04-26. This file is a workflow, not a static trend report. Use it whenever the user asks for *current*, *recent*, *viral*, *market-specific*, *platform-specific*, or *reference-track-driven* guidance.

Music trends age quickly. Static genre files should explain durable craft principles; current facts should be checked on the web at the time of the user request.

## When to use active web research

Use web research when the user asks about:

- current or recent music trends
- "what is popular right now"
- platform-specific behavior: TikTok, YouTube Shorts, Spotify playlists, Apple Music charts, radio, sync/library music
- current K-pop/J-pop/C-pop/EDM/hip-hop/indie scenes
- current reference tracks or living-artist comparisons
- user-specific listening context from public playlists, streaming recaps, or user-shared service data
- current AI music tools, copyright, lawsuits, distributor policies, or platform rules
- release strategy, chart performance, playlisting, or market targeting

Do **not** rely only on the static skill files for these requests.

## Source hierarchy

Prefer sources with transparent data collection and primary access. A useful research pass triangulates at least two source types.

| Source type | What it is good for | Watch-outs |
|---|---|---|
| Official charts | What is actually charting in a market or globally | Charts measure different things: streams, sales, radio, video, UGC, or weighted composites |
| Platform charts | What users are playing on a specific platform | Platform demographic and playlist bias |
| Industry reports | Macro trends, revenue, format changes, regional growth | Often lag current scene-level taste |
| Local music press / label news | Scene context, new movements, artist narratives | Hype, PR framing |
| Social / short-form data | Viral hooks, memes, dance challenges, sound reuse | Fast-moving and noisy; viral does not always mean musically durable |
| User-provided streaming context | Personal taste, playlist fit, durable favorites, reference anchors | Never request credentials; user taste is not automatically market trend |
| Interviews / producer breakdowns | Arrangement and production details | May be anecdotal; verify with listening |

## Useful starting sources

Use the current versions of these sources, not cached assumptions:

| Market / question | Starting points |
|---|---|
| Global streaming / platform movement | Spotify Charts, Apple Music charts, YouTube Charts, Billboard Global 200 |
| Global industry macro trends | IFPI Global Music Report, national industry bodies |
| Korea / K-pop | Circle Chart, Melon / Genie / Bugs charts, Korean music press, official label channels |
| Japan / J-pop | Oricon, Billboard Japan, Apple Music Japan, Spotify Japan, local press |
| UK | Official Charts Company |
| US | Billboard charts, Luminate/Music Connect references where available, RIAA reports |
| YouTube-heavy markets | YouTube Charts plus local press and platform playlists |
| Short-form virality | TikTok Creative Center or official platform trend pages, then verify with chart/streaming movement |

## Research workflow

### 0. Check for user listening context when relevant

If the user is writing for their own taste, playlist fit, DJ set, or reference library, ask whether they use a streaming service and can share lightweight evidence: a public playlist, 5-10 track names, or a Replay/Wrapped/Last.fm summary. Load `user-listening-context-and-streaming-services.md` before treating public charts as the main signal.

### 1. Clarify the scope

Before searching, pin down:

- region: global, US, Korea, Japan, China, Southeast Asia, UK, etc.
- time window: this week, last 30 days, 2026 so far, last few years
- platform: streaming, radio, YouTube, TikTok, club, live, sync, game/film
- genre frame: K-pop, EDM, drill, ballad, indie rock, musical theatre, etc.
- output goal: analysis, composition advice, reference list, or trend summary

### 2. Pull a small evidence set

Aim for:

- one chart or platform data source
- one industry/reporting source
- one listening/reference source
- optional user-provided listening-context source if the user has one
- optionally one local-language source for regional scenes

Do not overfit to a single chart. A song can be huge on YouTube and weak on Spotify; a TikTok sound can be viral without becoming a durable song; an album can dominate physical charts without reflecting streaming behavior.

### 3. Translate trend facts into craft variables

The agent's job is not to recite chart positions. Convert findings into compositional choices:

| Trend observation | Composition variables |
|---|---|
| Short intros / early hooks | hook timing, intro length, first vocal entry |
| Dance challenge success | groove clarity, countable phrase shape, chantable hook |
| Ballad resurgence | tempo, vocal range, lyric density, harmonic pacing |
| Club genre crossover | drum pattern, bass register, drop architecture, loop length |
| Regional folk/traditional fusion | instrument idiom, rhythmic cycle, language prosody, ornamentation |
| Streaming playlist fit | dynamic contour, skip-risk moments, vocal entry, arrangement density |

### 4. Report uncertainty clearly

Use language like:

- "Current chart evidence suggests..."
- "On this platform, not necessarily across the whole market..."
- "This is a reference cluster, not a rule."
- "This looks like a short-form trend; check whether it also appears on full-song charts."

Avoid:

- "Everyone is doing..."
- "The sound of 2026 is..."
- "This genre now means..."
- "This artist proves the whole market..."

## Search query patterns

Use precise queries:

```text
site:spotify.com/charts global top songs weekly [genre or region]
Billboard Global 200 methodology official streams sales
YouTube Charts Top Songs methodology official views UGC lyric videos
Circle Chart Global K-pop weekly chart official
Oricon weekly combined singles chart official
[genre] production trends 2026 producer interview
[artist] [song] producer breakdown BPM key form
```

For regional scenes, search in the relevant language when possible, then cross-check English-language summaries. If the user is subscribed to a music service or has public playlists, ask them to use that service as a listening source rather than relying only on general web search.

## Copyright/style guardrail

When a trend or reference answer involves a living artist, current hit, protected lyrics, melody, samples, or AI-assisted release claims, also load `style-reference-and-copyright.md`.

## Output patterns for the agent

### Current trend summary

```md
I checked this as a current-trend question, so I'd treat the static genre file as background only.

Current signal:
- Platform/chart evidence:
- Local/industry context:
- Listening pattern:

Composition takeaway:
1. ...
2. ...
3. ...

Caveat:
- This appears platform-specific / region-specific / short-form-specific.
```

### Reference-driven composition advice

```md
Instead of copying the reference, extract its craft variables:

- Tempo / meter:
- Groove:
- Harmonic rhythm:
- Hook timing:
- Topline contour:
- Arrangement density:
- Signature sonic element:
- What to avoid copying directly:
```

## Snapshot policy for genre files

Genre files should include a `Snapshot note` when they mention living scenes, current artists, platform behavior, or recent industry norms. The note should:

1. give the last review date,
2. say what is stable vs. current-sensitive,
3. link to this document and `reference-track-digging.md`; use `style-reference-and-copyright.md` when references or living artists are involved.

Update the snapshot date only after checking the file against current sources.

## Cross-references

- User listening context → `user-listening-context-and-streaming-services.md`
- Regional trend evolution → `regional-trend-evolution-analysis.md`
- Reference digging → `reference-track-digging.md`
- Style/copyright guardrails → `style-reference-and-copyright.md`
- Trend/reference matrices → `../../assets/trend-and-reference-matrices.md`

## Quick asset

- Fast web-search cheatsheet → `../../assets/web-search-cheatsheet.md`
