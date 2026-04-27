# Minor, Microgenre, and Hybrid Genre Handling

> **Snapshot note:** Last content review snapshot: 2026-04-27. Microgenre names, online-scene labels, and hybrid genre tags change quickly. Use this file as a handling framework, then verify current usage through active web research and reference listening.

This file is for genre names too small, too new, too local, too internet-native, or too hybrid to deserve a dedicated file yet. It helps the agent respond without pretending that a single paragraph can fully define a living scene.

Use this file when the user names a style such as:

- a microgenre: hyperpop, phonk, breakcore, witch house, vaporwave, future funk, blackgaze, slowcore, math rock, plugg, rage rap, etc.
- a platform-born or meme-driven tag
- a local scene label the skill does not yet cover (for regional popular scenes, also check `regional-scene-starters.md`)
- a hybrid label: "K-pop + Jersey club", "country-trap", "ambient gospel", "metalcore with J-pop chorus", etc.
- a genre term the agent does not recognize confidently

## Core principle

For minor and hybrid genres, the safest answer is:

```text
I will not over-define the scene. I will identify a few craft variables, verify current references if needed, and give a playable sketch that uses those variables without claiming to represent the whole genre.
```

## Microgenre triage workflow

### 1. Identify the genre type

| Type | Examples | First move |
|---|---|---|
| Internet microgenre | hyperpop, vaporwave, nightcore, drift phonk | check current reference cluster and platform context |
| Local club/dance form | Jersey club, footwork/juke, gqom, baile funk variant | verify tempo/groove grid and dance function |
| Guitar/band substyle | shoegaze, slowcore, math rock, post-rock, blackgaze | identify texture, riff language, form pacing |
| Rap/R&B substyle | plugg, rage, cloud rap, alt-R&B niche | identify drum pocket, synth palette, vocal/flow density |
| Metal/punk substyle | djent, doom, sludge, screamo, grindcore | identify tuning, riff rhythm, tempo/endurance, vocal role |
| Nostalgia/aesthetic genre | city-pop revival, synthwave, future funk, chillwave | identify era-signifiers vs modern form/low-end |
| Hybrid request | K-pop + amapiano, folk + hyperpop, gospel + drill | split into ingredients, then recombine intentionally |

### 2. Ask for one anchor if the label is unstable

```text
That tag can mean different things depending on platform and scene. Give me one reference track or artist that represents the exact lane, and I will extract craft variables rather than copying it.
```

If the user does not provide a reference, use active web research and say the result is approximate.

### 3. Build a craft-variable profile

```md
| Variable | What to check |
|---|---|
| Tempo / meter | BPM range, half-time/double-time feel, dance grid |
| Groove | drum pattern, swing, subdivision, loop length |
| Harmony | static vamp, modal center, functional changes, chromatic color |
| Melody/topline | chant, rap flow, maximalist leaps, narrow drone, noisy texture |
| Texture | distorted, glossy, lo-fi, dense, sparse, sidechained, wall-of-sound |
| Form | loop, verse/chorus, drop, build, breakdown, through-composed arc |
| Cultural/platform function | club, meme, playlist, live scene, fandom, video, underground label |
| Do-not-copy | signature sample, meme phrase, producer tag, artist vocal identity |
```

## Microgenre family notes

These are starting points, not definitions.

### Hyperpop / digicore / maximalist internet pop

Composition variables:

- compressed, high-contrast sections
- bright or distorted synth hooks
- pitch-shifted or heavily processed vocal identity
- abrupt modulations, tempo-feel shifts, or texture cuts
- short-form-friendly hook cells

Pitfall: copying a specific vocal-processing identity or one artist's melodic fingerprint.

Pair with `../genres/electronic-edm.md`, `../genres/pop-rock.md`, and `../research/style-reference-and-copyright.md`.

### Phonk / drift phonk / Memphis-rap-adjacent internet styles

Composition variables:

- looped minor motifs or dark modal centers
- hard, repetitive drum pattern; cowbell-like lead in some drift variants
- chopped vocal/sample aura
- car-edit/short-form or underground tape aesthetics depending on variant

Pitfall: treating all phonk as the same. Drift phonk, Brazilian phonk variants, and Memphis-rooted references can differ sharply.

Pair with `../genres/hip-hop-rnb.md`, `../genres/electronic-edm.md`, and `../research/web-music-trend-research.md`.

### Vaporwave / future funk / synthwave / chillwave

Composition variables:

- nostalgia-coded harmony, samples, timbres, or visual identity
- loop-based form and slow harmonic rotation
- sidechain or tape/lo-fi gestures depending on substyle
- disco/funk/city-pop-derived references in some branches

Pitfall: nostalgia aesthetics can become sample-dependent; avoid uncleared samples and rebuild ideas from scratch.

Pair with `../genres/electronic-edm.md`, `../genres/pop-rock.md`, and `../research/reference-track-digging.md`.

### Breakcore / jungle revival / footwork-juke-adjacent high-density rhythm

Composition variables:

- chopped breakbeats or rapid percussion edits
- high rhythmic density and abrupt form pivots
- bass repetition or sub pressure
- melodic material may be minimal, sentimental, noisy, or rave-derived

Pitfall: confusing breakbeat editing as random chaos. Strong tracks often have clear phrase logic.

Pair with `../rhythm-groove/rhythmic-devices.md`, `../genres/electronic-edm.md`, and `../form/narrative-and-transitions.md`.

### Jersey club / Baltimore club / regional club forms

Composition variables:

- dance-function first
- kick pattern and vocal chops as structural hooks
- call-and-response or chant-like fragments
- short loop cycles with strong drop points

Pitfall: borrowing the pattern without understanding dance/social function.

Pair with `../genres/electronic-edm.md`, `../genres/hip-hop-rnb.md`, and `../research/regional-trend-evolution-analysis.md`.

### Shoegaze / dream pop / slowcore / post-rock

Composition variables:

- texture as harmony: sustained guitars, blurred attacks, layered reverb/delay
- slower harmonic pacing or long crescendos
- vocal embedded in texture rather than always foregrounded
- simple motifs transformed by density

Pitfall: adding reverb to any guitar part and calling it shoegaze. The part must support the texture.

Pair with `pop-rock.md`, `../instrument-idiom/guitar.md`, and `../orchestration/arrangement-density.md`.

### Math rock / post-hardcore / emo-adjacent hybrids

Composition variables:

- irregular phrase lengths, odd meters, or additive accents
- clean interlocking guitar figures or angular riffs
- dynamic shifts between restraint and catharsis
- melodic hooks may be shouted, sung, or instrumental

Pitfall: using odd meter without a singable or memorable phrase identity.

Pair with `metal-punk-hardcore.md`, `pop-rock.md`, and `../rhythm-groove/odd-meters-polyrhythm.md`.

### Blackgaze / post-metal / doom / sludge-adjacent hybrids

Composition variables:

- heavy guitar texture plus long-form atmospheric build
- tremolo/riff cells, drones, pedal tones, modal centers
- extreme vocals may function as texture rather than lyric foreground
- slow or medium tempo can still feel intense through density

Pitfall: writing a normal metal riff and adding pads; the form and texture need to breathe.

Pair with `metal-punk-hardcore.md`, `../instrument-idiom/guitar.md`, and `../production-aware/energy-and-dynamics.md`.

### Plugg / rage / cloud-rap / alt-trap microstyles

Composition variables:

- synth/rhythm identity often more important than chord complexity
- loop economy, vocal pocket, ad-lib space
- beat may be minimal, glossy, distorted, or arcade-like depending on lane
- topline/flow density and vocal tone define much of the style

Pitfall: over-arranging. Many tracks need space for vocal identity and ad-libs.

Pair with `hip-hop-rnb.md`, `../rhythm-groove/groove-and-feel.md`, and `../production-aware/arrangement-for-mix.md`.

## Hybrid genre recipe

When the user requests "A + B":

### 1. Decide the anchor

Which ingredient controls the song's core identity?

| Anchor | Usually controls |
|---|---|
| Genre A as song form | verse/chorus/drop/bridge layout |
| Genre B as groove | drum pattern, bass, subdivision |
| Genre C as harmony | chord palette, cadences, voicings |
| Regional/traditional ingredient | rhythm cycle, mode, ornament, instrument idiom, language |
| Artist/reference ingredient | energy target only; avoid cloning |

### 2. Limit the number of signatures

For a first sketch, use **one primary signature element from each ingredient**.

Bad hybrid:

```text
K-pop section changes + hyperpop vocal processing + flamenco guitar + drill drums + gospel chords + orchestral strings + maqam melody.
```

Better hybrid:

```text
K-pop form anchor + Jersey-club-derived kick pattern + neo-soul color chords. Keep the topline simple and avoid adding more signatures until the hook works.
```

### 3. Use a merge table

```md
| Ingredient | Keep | Soften / avoid | Concrete move |
|---|---|---|---|
| K-pop | pre-chorus lift, post-chorus chant | overstuffed section count | 4-bar pre into 4-bar chant hook |
| Jersey club | kick pattern energy | exact sample-chop cliché | original vocal chop rhythm |
| Neo-soul | maj9/min9 voicings | too many reharm changes | 2-chord loop with chromatic passing chord |
```

## Unknown genre name protocol

If the agent does not recognize a genre term:

1. Do not guess confidently.
2. Use web research if the user needs accuracy.
3. Ask for one reference track if the answer can wait for user input.
4. If proceeding without clarification, say it is approximate.
5. Extract variables from available examples rather than defining the whole scene.

Response pattern:

```md
I don't want to over-define that tag from memory. Treating it as a current/scene-specific label, I'd check 3-5 references and look for shared tempo, groove, texture, form, and vocal behavior. For a first sketch, I would start with...
```

## Pitfalls

- **Do not turn a TikTok tag into a timeless genre rule.** Platform tags mutate quickly.
- **Do not assume a microgenre is only a sound palette.** Many are scenes with social, geographic, or platform contexts.
- **Do not over-hybridize.** Two strong ingredients usually beat six weak ones.
- **Do not use surface timbres as cultural shortcuts.** Name the specific tradition, scene, rhythm, or instrument idiom.
- **Do not copy memes, samples, or producer tags.** Make original material.

## Quick decision matrix

| User goal | Best response |
|---|---|
| "What is [microgenre]?" | Give cautious craft-variable summary + ask for reference or use web |
| "Make this more [microgenre]" | Change 1-3 variables: groove, texture, form, vocal approach |
| "Blend A and B" | Pick anchor, supporting ingredient, and one shared bridge variable |
| "Is this too close to reference?" | Load `../research/style-reference-and-copyright.md` and compare melody/lyrics/riff/sample/vocal identity |
| "Which references should I dig?" | Load `../research/reference-track-digging.md` + active web research |

## Cross-references

- Web trend research → `../research/web-music-trend-research.md`
- User listening context → `../research/user-listening-context-and-streaming-services.md`
- Regional trend evolution → `../research/regional-trend-evolution-analysis.md`
- Reference-track digging → `../research/reference-track-digging.md`
- Style/copyright guardrails → `../research/style-reference-and-copyright.md`
- Electronic / EDM → `electronic-edm.md`
- Hip-hop / R&B → `hip-hop-rnb.md`
- Pop / rock / indie → `pop-rock.md`
- Metal / punk / hardcore → `metal-punk-hardcore.md`
- Folk/roots or tradition-specific traditions → `folk-roots-and-traditions.md`
- Rhythm devices → `../rhythm-groove/rhythmic-devices.md`
- Instrument idiom overview → `../instrument-idiom/overview.md`

## Additional cross-references

- Regional scene starter map → `regional-scene-starters.md`
- Fast web-search cheatsheet → `../../assets/web-search-cheatsheet.md`
