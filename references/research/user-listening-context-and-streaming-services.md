# User Listening Context and Streaming-Service Research

> **Snapshot note:** Last content review snapshot: 2026-04-27. Platform features, APIs, chart pages, privacy rules, and personalized recap products change quickly. Use this workflow for personal-listening context, but verify current platform details with active web research when needed.

This file helps the agent use the user's own listening ecosystem as a composition-research input. It is especially useful when the user says they want something that fits their taste, playlist, local market, favorite scene, DJ set, label pitch, or reference library.

The agent should **not** claim it can access a streaming account unless a separate tool or explicit user-provided data is available. The normal workflow is to ask the user to share lightweight, privacy-safe evidence: playlist links, track names, screenshots, top-song lists, public charts, or a short description of what they listen to.

## When to use this file

Use this file when the user asks for:

- references that match their taste
- current style digging based on what they already listen to
- a playlist-compatible song idea
- music for a DJ set, playlist pitch, or personal release strategy
- market research where the user's available streaming service matters
- a comparison between platform charts and the user's own library
- guidance like "I have Spotify / Apple Music / YouTube Music / Melon — what should I check?"

Pair this with:

- `web-music-trend-research.md` for current market signals
- `reference-track-digging.md` for turning tracks into craft variables
- `style-reference-and-copyright.md` for living-artist or too-close imitation requests
- `regional-trend-evolution-analysis.md` when the user asks about region/time-shift patterns

## Safety and privacy baseline

Never ask the user for passwords, account tokens, private login links, or anything that requires account takeover.

Safe inputs include:

- public playlist links
- track/artist names copied from a playlist
- 5-20 reference tracks typed by the user
- screenshots the user chooses to share
- year-end or monthly recap summaries the user chooses to quote
- exported listening logs from a service or scrobbling tool, if the user already has them
- charts or editorial playlists visible without private account access

If the user shares listening-history data, treat it as taste evidence, not identity evidence. Do not infer sensitive traits. Stick to musical variables.

## First question pattern

When personal listening context would materially improve the answer, ask a small, optional question:

```text
Do you use a streaming service for reference digging — Spotify, Apple Music, YouTube Music, Melon, Genie, Bugs, SoundCloud, Bandcamp, Last.fm, or something else? If yes, share 5-10 track names or a public playlist link. No login details needed.
```

If the user does not answer, continue with public charts and general reference-track workflow.

## Service-aware research map

| Service / source | Useful user-provided signal | Useful public signal | Watch-outs |
|---|---|---|---|
| Spotify | public playlists, liked-track excerpts, top tracks if user provides them | Spotify Charts: global, country, city, genre, local-pulse views | Playlist ecosystem can bias taste toward platform/editorial norms |
| Apple Music | Replay summaries, playlists, library excerpts | Apple Music top charts, city charts, editorial playlists | Personal Replay is account-specific; ask user to summarize rather than requesting account access |
| YouTube / YouTube Music | playlists, liked videos, shorts/sound references | YouTube Charts, official videos, UGC-heavy signals, creator ecosystem | Video virality and full-song streaming can diverge |
| Melon / Genie / Bugs / VIBE | Korean chart/listening context, playlists, favorites | domestic Korean chart and platform signals | Use with Circle Chart for broader K-pop market context |
| Oricon / Billboard Japan / local Japan services | user references and playlists | local chart signals for Japan | Physical, download, streaming, and combined charts tell different stories |
| SoundCloud | public likes/reposts/playlists, underground references | tag pages and community charts | Strong for emerging scenes, weak as a whole-market proxy |
| Bandcamp | collections, wishlists, label pages | labels, tags, scene pages, fan collections | Good for niche/indie scenes; not a mainstream popularity proxy |
| Last.fm / scrobbling logs | long-term listening history, top tracks by time period | artist/tag pages and community data | Great for taste mapping if the user already scrobbles; still self-selecting |
| TikTok / short-form platforms | saved sounds or trend links | official creative/trend pages and sound usage | Sound virality is noisy; verify with full-track listening and charts |

## What to extract from a user's listening data

Do not just list the user's favorite artists. Convert their listening context into compositional variables.

| Evidence | Composition variable |
|---|---|
| Many tracks around one BPM band | likely tempo comfort zone or playlist slot |
| Repeated drum/groove family | pocket, subdivision, kick/snare density |
| Similar vocal registers | topline tessitura and performance energy |
| Repeated form pattern | intro length, hook timing, bridge/drop/post-chorus expectations |
| Repeated harmonic color | modal, functional, minor-loop, neo-soul, gospel-adjacent, blues-derived, etc. |
| Repeated language/region | prosody, pronunciation, local lyric density, rhythmic accent |
| Repeated release era | production density, arrangement pacing, nostalgia layer |
| Repeated platform context | playlist fit, video/short-form hook, club/DJ utility, radio fit |

## Minimal workflow

### 1. Ask for the lightest useful evidence

Use one of these:

```text
Share 5 tracks that are exactly the lane, plus 2 tracks that are close but wrong.
```

```text
Share a public playlist link or paste the first 10 tracks. I will treat it as a reference cluster, not something to copy.
```

```text
If you use Apple Music Replay / Spotify Wrapped / Last.fm, paste your top 10 artists or tracks and tell me which ones are relevant to this project.
```

### 2. Separate taste from target

The user may listen to one thing and want to write another. Ask or infer:

- Is this for your personal taste?
- Is this for a specific audience or platform?
- Are these references emotional, sonic, structural, or commercial?
- Which reference is the anchor, and which is just context?

### 3. Build a reference grid

```md
| Source | Role | What to extract | What to avoid copying |
|---|---|---|---|
| User playlist track 1 | anchor | tempo/groove/hook timing | melody, lyrics, signature riff |
| User playlist track 2 | boundary | what feels too bright/clubby | exact drum fill |
| Public chart track | market signal | current form/arrangement norm | chart-chasing cliché |
```

### 4. Compare personal taste vs market signal

| Scenario | Advice |
|---|---|
| User taste and charts align | Use the user's references as anchors; charts confirm the lane |
| User taste is older than current charts | Add a modern arrangement variable while preserving the user's core taste |
| User taste is niche but project is mainstream | Keep one niche signature element; simplify form/groove for broader fit |
| User taste is mainstream but project wants distinct identity | Use boundary references to avoid generic defaults |
| Platform signals conflict | Explain which platform the advice is optimizing for |

## Platform-specific prompts

### Spotify-oriented reference pass

```text
Check your public playlists, top tracks if available, and Spotify Charts for the target region/genre. Extract: tempo band, intro length, hook timing, groove family, vocal entry, loop length, and density arc.
```

### Apple Music-oriented reference pass

```text
Use your Replay/monthly insights or playlists to identify durable favorites, then compare them with Apple Music top charts or city charts for the target region. Extract: artist cluster, song length, lyric density, chorus lift, and arrangement polish.
```

### YouTube / short-form-oriented reference pass

```text
Use YouTube Charts and saved music/short-form references to see which hooks work visually or socially. Then verify whether the full song has a strong structure, not just a viral 10-second moment.
```

### Korean-platform-oriented reference pass

```text
For K-pop or Korean domestic pop, compare the user's Melon/Genie/Bugs/VIBE references with Circle Chart and current label/artist releases. Extract: topline density, section contrast, choreography-friendly hook, fan-chant or singalong affordance, and ballad vs dance-market expectations.
```

### Niche-scene pass

```text
For Bandcamp/SoundCloud/Last.fm-heavy scenes, prioritize tags, labels, community playlists, and user-liked tracks. Use mainstream charts only as contrast, not as the main truth source.
```

## Output template

```md
Your listening-context signal:
- Personal anchors:
- Boundary tracks:
- Platform/market signal:

Craft variables to use:
1. Tempo/groove:
2. Harmony:
3. Topline:
4. Form/hook timing:
5. Arrangement density:

Avoid copying:
- Exact melody/lyrics/riff/sample/vocal identity

Concrete next move:
- 4-8 bar sketch / reference matrix / playlist-compatible arrangement plan
```

## Pitfalls

- **Do not overfit to the user's top songs.** A top track may be emotionally important but irrelevant to the current project.
- **Do not equate playlist popularity with composition quality.** It is a signal, not a law.
- **Do not ask for private credentials.** Use public links or user-pasted summaries.
- **Do not assume one platform equals the whole market.** Each service has different demographics, catalog emphasis, and chart rules.
- **Do not copy the user's references.** Extract variables and generate a new composition.

## Cross-references

- Current trend research → `web-music-trend-research.md`
- Reference-track digging → `reference-track-digging.md`
- Style/copyright guardrails → `style-reference-and-copyright.md`
- Regional trend evolution → `regional-trend-evolution-analysis.md`
- Pre-production decisions → `../production-aware/pre-production-decisions.md`
- Prosody and language → `../fundamentals/prosody-and-language.md`
- Response templates → `../../assets/response-templates.md`

## Quick asset

- Fast web-search cheatsheet → `../../assets/web-search-cheatsheet.md`
