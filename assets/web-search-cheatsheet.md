# Web Search Cheatsheet for Music Composition Research

> **Snapshot note:** Last content review snapshot: 2026-04-27. Search engines, platform charts, and social discovery surfaces change quickly. Use this as a compact workflow, then verify current platform behavior when the answer depends on freshness.

This is a fast lookup sheet for active web research. It complements the longer research files:

- `../references/research/web-music-trend-research.md`
- `../references/research/reference-track-digging.md`
- `../references/research/user-listening-context-and-streaming-services.md`
- `../references/research/regional-trend-evolution-analysis.md`

## Search rule of thumb

```text
query = music object + scene/region + time window + evidence type
```

Examples:

```text
"amapiano" "2026" producer interview groove
"Jersey club" K-pop choreography trend 2025
site:charts.spotify.com city chart Seoul K-pop
site:youtube.com/charts Top Songs Shorts Brazil
"regional Mexican" "corridos tumbados" songwriter interview
```

## Operator basics

Common operators and filters:

| Tool | Use | Example |
|---|---|---|
| quotes | exact phrase | `"Top Songs on Shorts"` |
| minus | exclude a term | `phonk -playlist -mix` |
| `site:` | search one site/domain | `site:billboard.com amapiano global` |
| date tools | recent results | search, then filter by past month/year |
| language/region filters | local-market research | search in Spanish, Korean, Japanese, Portuguese, etc. |
| file type / PDF filters | reports and methodology docs | `IFPI music report filetype:pdf` |

Caveat: search operators and ranking behavior can change. Official search help should override this cheatsheet.

## Source hierarchy for music trend questions

| Question | Best first sources | Why |
|---|---|---|
| What is charting? | official chart pages, platform chart pages | direct popularity signal |
| What is emerging? | viral charts, short-form trend tools, local press | velocity signal |
| What does the scene call it? | local-language press, artist interviews, label pages | vocabulary signal |
| How is it made? | producer interviews, live sessions, stems, tutorials from credible practitioners | craft signal |
| Is it safe to imitate? | style/copyright guardrail + reference triangulation | originality signal |

## Platform-specific quick searches

### Spotify

Use for: streaming popularity, regional/city charts, viral movement, playlist lanes.

Search ideas:

```text
Spotify Charts [country/city] [genre]
site:charts.spotify.com [city] [genre]
"Local Pulse" [city] Spotify [genre]
```

Interpretation:

- Global/regional charts = broad platform consumption.
- Viral charts = buzz/velocity, not just total plays.
- City/Local Pulse = local concentration; useful for regional influence.

### Apple Music

Use for: top charts, city charts, user-accessible listening references, Replay if user shares it.

Search ideas:

```text
Apple Music Top Charts [country/genre]
Apple Music City Charts [city]
Apple Music Replay top songs artists user shared
```

Interpretation:

- City charts can surface local listening differences.
- Replay/Wrapped-style summaries are useful only if the user shares them voluntarily.

### YouTube / YouTube Music / Shorts

Use for: video-driven music, regional chart visibility, short-form reuse, official + UGC dynamics.

Search ideas:

```text
YouTube Charts Top Songs [country]
YouTube Charts Top Songs on Shorts [country]
site:support.google.com/youtube YouTube Charts Top Songs Shorts
```

Interpretation:

- YouTube Top Songs may combine official videos, lyric videos, and UGC using the official song.
- Shorts-specific signals may emphasize hookable clips rather than full-song structure.

### TikTok Creative Center

Use for: short-form velocity, songs/hashtags/creators/videos by region.

Search ideas:

```text
TikTok Creative Center songs [region] [genre]
site:ads.tiktok.com/business/creativecenter "Songs" "Trend Discovery"
```

Interpretation:

- Strong for short-form behavior.
- Weak for full-song craft unless triangulated with charts and reference listening.

### Bandcamp / SoundCloud / Beatport

Use for: niche scenes, microgenres, independent scenes, DJ/electronic lanes.

Search ideas:

```text
site:bandcamp.com [microgenre] [city]
site:soundcloud.com [scene tag] [producer]
site:beatport.com [subgenre] top tracks
```

Interpretation:

- Good for scene vocabulary and underground signals.
- Requires reference listening; don't generalize from one upload.

### Local-language searches

Use local language for region-specific scenes.

Examples:

```text
Korean: "요즘" "인디" "플레이리스트" "인터뷰"
Japanese: "最新" "シティポップ" "インタビュー"
Portuguese: "funk carioca" "tendência" "produtor"
Spanish: "corridos tumbados" "productor" "entrevista"
Arabic/Turkish/Persian/Hindi/Punjabi/etc.: use native terms when possible.
```

If the agent is not confident in a language, it should say so and treat findings cautiously.

## Evidence confidence labels

Use these labels in answers when the trend claim matters.

| Label | Meaning |
|---|---|
| High confidence | official chart/methodology + multiple current references agree |
| Medium confidence | current platform signal + specialist/local press agree |
| Low confidence | one platform or one article only; good as a lead, not a conclusion |
| Anecdotal | forum/community/source-limited; use only as scene clue |

## Query recipes

### Current genre trend

```text
[genre] [country/region] trend 2026 chart producer interview
[genre] "top songs" [platform] [country]
[genre] "what is" "2026" local music press
```

### Reference-track digging

```text
[genre] playlist [year] [platform]
[artist/track] producer interview arrangement harmony tempo
[genre] "songwriter" "interview" "chorus"
```

### Microgenre / obscure tag

```text
"[tag]" music genre references
"[tag]" Bandcamp SoundCloud producer interview
"[tag]" "BPM" "drum pattern"
```

### Regional comparison

```text
[region A] [genre] charts 2026 vs [region B]
[genre] [country] streaming charts YouTube Spotify Apple Music
[local-language genre term] "interview" "producer"
```

### Copyright/style safety

```text
[reference artist] songwriting interview influences
[genre] common features tempo harmony groove
[artist] signature sound analysis avoid copying melody riff lyrics
```

## What not to do

- Do not treat one playlist as a whole genre.
- Do not treat TikTok velocity as full-song structure.
- Do not treat global charts as local taste.
- Do not use SEO listicles as primary evidence when official charts, local press, or practitioner interviews exist.
- Do not ask for the user's streaming login, password, tokens, or private account access.
- Do not copy melodies, lyrics, riffs, samples, or signature artist identifiers from references.

## Output template

```md
**What I checked**
- Sources:
- Time window:
- Region/platform:

**Trend signal**
- High-confidence:
- Medium-confidence:
- Low-confidence / leads:

**Composition translation**
- Tempo/groove:
- Harmony:
- Topline:
- Arrangement:
- Form/hook timing:

**Caveat**
- What still needs reference listening or local validation:
```
