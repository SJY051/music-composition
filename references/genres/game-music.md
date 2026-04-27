# Game Music and Interactive Scoring

> **Snapshot note:** Last content review snapshot: 2026-04-26. Use this file for stable compositional conventions, but verify current artists, charts, platform norms, and scene-specific references with active web research. See `../research/web-music-trend-research.md` and `../research/reference-track-digging.md`.

This file covers composition for video games and other interactive media. Game music shares much DNA with film scoring — both are "music for picture", broadly speaking — but interactivity introduces specific compositional problems that don't exist in linear media. The score has to work without knowing what will happen next, has to loop or stretch indefinitely without becoming tedious, and has to respond to gameplay state in real time.

This file complements `film-tv-scoring.md` (linear media scoring; much of which transfers) and `../techniques/algorithmic-and-AI-assisted.md` (some game music is procedurally generated). For specific genre conventions a game's music draws on (orchestral, electronic, jazz, etc.), see the relevant `genres/*.md` file.

## When to consult this file

- Composing for a video game (any platform, any era)
- Designing music systems for interactive media (XR, interactive installations, themed entertainment)
- Adapting linear music for game contexts
- Working with adaptive / dynamic music middleware (Wwise, FMOD, Unity's audio system, etc.)
- Music for game trailers and promotional materials (which is usually closer to film/trailer scoring; see `film-tv-scoring.md`)

## What's different about game music

The defining constraint: **the composer doesn't know how long the music needs to play, what will happen next, or what the player will do**. Linear media tells you exactly when each cue starts and ends; games don't.

Practical consequences:

| Constraint | Implication |
|------------|-------------|
| Indefinite duration | Music must loop seamlessly or be designed to play indefinitely without obvious repetition |
| Unpredictable transitions | Music must transition smoothly from any current state to any plausible next state |
| Player agency | The player can stop, restart, repeat, skip — music must serve all paths |
| Performance constraints (older platforms) | Memory, CPU, and audio channels limit what can be heard |
| Adaptive systems | Music must respond to gameplay events, parameters, or state changes |
| Replay tolerance | Players hear the same music many times; it must reward repeated listening |

These shape every compositional decision.

## A short history of game music

Worth knowing because compositional conventions are rooted in technological eras:

### 1970s–early 1980s: arcade and earliest console (TIA, SN76489, custom chips)

Limited polyphony (often 1–3 channels), simple waveforms (square, triangle, noise). Music was often short loops or stinger cues, with sound effects sharing the audio channels. *Pac-Man*, *Donkey Kong*, *Space Invaders* — minimal "music" by modern standards but distinctive sonic identity.

### Late 1980s–early 1990s: chiptune era (NES, Game Boy, SMS, MSX)

Slightly expanded chip capabilities (NES: 5 channels — 2 pulse, 1 triangle, 1 noise, 1 DPCM). Composers like Koji Kondo (Mario, Zelda), Nobuo Uematsu (Final Fantasy), Yuzo Koshiro (Streets of Rage) wrote sophisticated multi-voice music within these constraints. The chiptune aesthetic — pulse waves, simple waveforms, characteristic "8-bit" sound — is now an entire genre revived in indie games and electronic music.

### Early-mid 1990s: PCM and FM synthesis era (SNES, Genesis, NeoGeo)

PCM samples on SNES (8-channel sample playback) and FM synthesis on Genesis (Yamaha YM2612). More instrument-like sounds; orchestral mockups become possible. Composers like Yasunori Mitsuda (Chrono Trigger, Chrono Cross), Michiru Yamane (Castlevania: Symphony of the Night), Hitoshi Sakimoto (Ogre Battle, FFXII) develop complex compositional language.

### Late 1990s–2000s: CD audio and live recording (PlayStation, PS2, Xbox)

CD-quality audio. Live orchestras enter game music (Final Fantasy VIII orchestra, Halo's choral writing). Streaming audio means hour-long detailed scores become possible. Game music begins to receive concert hall performances (Final Fantasy concerts, Distant Worlds tours).

### 2000s–onward: middleware and adaptive systems

Wwise, FMOD, Unity, Unreal — middleware systems that allow composers to design music as a system rather than fixed cues. Vertical layering, horizontal re-sequencing, parameter-driven music become standard. Composers like Jesper Kyd (Hitman, Assassin's Creed), Austin Wintory (Journey), Darren Korb (Bastion, Hades), Lena Raine (Celeste) make adaptive systems central to their craft.

### 2010s–onward: indie diversity

Indie games push game music in many directions: live-band recording, retro-chiptune revival, ambient drone, complex jazz (Persona 5), folk and traditional music (Hyper Light Drifter), full orchestral (God of War, Horizon).

## Looping — the basic technique

The simplest interactive music: a piece that loops seamlessly until something else happens. Compositional techniques for good loops:

### Loop point design

A loop must start and end without an audible "seam". Standard approaches:

- **Loop point coincides with a downbeat**: end of phrase aligns with start of phrase, both on a strong beat. Most common in classical-style game music.
- **Loop point at a pickup**: the piece ends just before a downbeat; the loop begins at the pickup; perfect continuity. Common in orchestral game music.
- **Crossfade**: an audio engine fades out the end as it fades in the start. Less common in modern game music (modern audio engines support sample-accurate looping).
- **Tail-into-head matching**: the last beat's content (final note, final chord, final percussion hit) is identical to the first beat's content. Crude but works.

### Avoiding loop fatigue

A loop the player hears for 20 minutes will exhaust them if it doesn't accommodate repetition.

- **Long loops**: 4–8 minutes per loop is more forgiving than 30 seconds; the listener doesn't immediately re-recognize.
- **Variation within the loop**: the loop itself contains internal variety (verse-chorus-bridge structure), so the listener doesn't experience the same 4 bars repeating.
- **Subtle, slow changes**: layered ambient music with elements drifting in and out, never quite repeating exactly. Brian Eno-style ambient is well suited to game contexts.
- **Stinger insertions**: occasional short "stingers" (8–32 bars of new material) interrupt the loop without changing it permanently.
- **Looping with start-of-day variations**: each time the loop starts fresh (new area, new visit), it begins with different material before settling into the main loop body.

### Length conventions by context

| Context | Typical loop length |
|---------|---------------------|
| Menu / title screen | 1:30–4:00 |
| Town / hub area | 2:00–6:00 |
| Combat / encounter | 1:30–4:00 |
| Boss battle | 2:00–5:00 |
| Field / exploration | 2:00–8:00 (longer for areas players spend time in) |
| Cutscene | Length-of-cutscene; often non-looping |
| Death / failure | 5–15 seconds (a stinger, not a loop) |
| Victory | 10–60 seconds (often non-looping) |

## Vertical layering

A widely-used adaptive technique: the music is composed as a layered stack (e.g., drums, bass, harmonic pad, melody, decorative percussion) and the engine adds or removes layers based on game state.

### Typical layered structure

| Game state | Active layers |
|------------|---------------|
| Quiet exploration | Pad + sparse melodic figure |
| Approaching enemies | Pad + figure + soft drums |
| Active combat | Pad + figure + drums + bass + intense melody |
| Boss encounter | All layers + extra brass / tension elements |

The layers are written together, in the same key, tempo, and form, so any combination sounds coherent. Layers fade in / out smoothly; transitions are imperceptible.

### Compositional rules for layered music

- **Each layer is independently coherent**: removing all other layers, a single layer should still make musical sense
- **Combined layers don't clash**: the layers harmonically and rhythmically combine without muddying the texture
- **Common harmonic frame**: all layers share the same chord progression and key (variations within that frame are fine)
- **Per-layer sonic separation**: layers occupy distinct frequency bands or stereo positions to maintain clarity when stacked
- **Smooth fade behavior**: each layer's start / stop sounds natural with fade in / out (no abrupt entrances or cuts)

This technique was used heavily in *No Man's Sky* (procedural generative score by 65daysofstatic), *Journey* (Austin Wintory), *Disco Elysium* (Sea Power), and many others.

## Horizontal re-sequencing

Different from vertical layering: the music is composed as multiple distinct sections that can be sequenced in different orders based on game state.

| Section | When played |
|---------|-------------|
| A | Default exploration |
| B | Light tension / nearby threat |
| C | Combat |
| D | Boss / climax |
| Transition cues | When state changes between sections |

The composer writes:
1. Each section as a self-contained loop
2. Short transition cues between adjacent sections (e.g., A→B, B→A, B→C, C→D)
3. The middleware plays section X until state changes, then plays the X→Y transition, then plays section Y

This approach gives sharper transitions than pure vertical layering. *Halo* (Marty O'Donnell) used horizontal re-sequencing extensively. Many modern AAA games use a hybrid of vertical layering and horizontal re-sequencing.

## Parameter-driven music

The most dynamic approach: the music is shaped by continuous game parameters, not just discrete state changes.

Examples:
- **Combat intensity**: a 0–1 parameter that fades layers, raises tempo, shifts harmony as combat heats up
- **Health**: as the player's health drops, the music adds tension (filter sweeps, dissonant elements, narrowing palette)
- **Time of day**: the music shifts smoothly across day/night cycles in an open-world game
- **Distance from objective**: tension layers fade in as the player approaches a key location

Implementation requires music designed with these parameters in mind — usually layered or modular music plus middleware logic that maps parameters to audio events.

## Stingers and oneshots

Discrete, non-looping musical events:

- **Stingers**: short cues for specific moments (item pickup, level-up, boss defeat, character introduction)
- **Hits**: percussive accents tied to gameplay (impact, damage, flourish on level transition)
- **Rules-based playback**: rare cues triggered by specific player actions (achievement unlocks, secret discovery)

These are non-adaptive but contextual. They interrupt or layer over background music.

## Diegetic vs. non-diegetic

As in film:

- **Diegetic**: music heard *in* the game world (radios, environmental music, NPCs singing). Often follows real-world conventions because it represents real-world music sources.
- **Non-diegetic**: music heard *over* the game world (the score). Adheres to game music conventions of looping, layering, etc.
- **Crossover**: music that appears to be diegetic but acts as score (the radio in *BioShock* — period jazz that sets atmosphere but operates as adaptive score), or score that responds as if diegetic (music that ducks when characters speak).

The distinction matters because diegetic music has different technical requirements (no looping required, real-world fidelity, often licensed music) and different audience expectations.

## Game music genre by era and genre

A rough genre map:

| Game type | Typical music idiom |
|-----------|----------------------|
| JRPG (Japanese RPG, e.g., Final Fantasy, Persona, Chrono Trigger) | Symphonic / orchestral with electronic elements; long memorable themes; character-specific motifs |
| WRPG (Western RPG, e.g., Skyrim, Witcher, Mass Effect) | Symphonic, often choral; folk-influenced for fantasy; sci-fi orchestral for space |
| Action / shooter (Halo, Call of Duty) | Cinematic orchestral with electronic edge; combat-driven layered systems |
| Stealth (Hitman, Splinter Cell) | Tense ambient with industrial or electronic elements; minimal during stealth, intense on detection |
| Indie narrative (Hades, Celeste, Disco Elysium) | Genre-experimental; specific stylistic identity often the game's signature |
| Platformer (Mario, Sonic, Celeste) | Catchy, melodic, often chiptune-influenced; level-themed music |
| Puzzle / casual (Tetris, candy-style) | Catchy short loops; light orchestration; non-distracting |
| Horror (Resident Evil, Silent Hill) | Dissonant, sparse, ambient with sudden stingers; often microtonal and noise-influenced |
| Racing (Forza, Need for Speed) | Often licensed contemporary music; original score for menus and key moments |
| Sports (FIFA, Madden) | Often licensed contemporary music; original score minimal |
| Simulation (Sim City, Civilization) | Long ambient or orchestral pieces; minimal interactivity |
| Open world (GTA, Red Dead) | Mix: licensed radio for diegetic; original score for missions and key moments |
| MOBA / multiplayer (LoL, DOTA, Overwatch) | Match-tempo orchestral; minimal during gameplay, intense at match milestones |
| Mobile / hyper-casual | Short catchy loops; designed to be muted |

## Specific composers worth studying

- **Koji Kondo** (Nintendo): foundational chiptune-era melodicism; *Super Mario*, *Zelda* themes
- **Nobuo Uematsu** (Square Enix): symphonic JRPG score; *Final Fantasy* series
- **Yasunori Mitsuda**: distinctive melodic / cinematic; *Chrono Trigger*, *Chrono Cross*, *Xenogears*
- **Hitoshi Sakimoto**: dense orchestral; *FFXII*, *Vagrant Story*, *Final Fantasy Tactics*
- **Yoko Shimomura**: melodic and emotional; *Kingdom Hearts*, *Street Fighter II*, *Xenoblade Chronicles*
- **Marty O'Donnell**: cinematic horizontal-resequencing; *Halo* trilogy
- **Jeremy Soule**: orchestral fantasy; *Skyrim*, *Guild Wars*, *Knights of the Old Republic*
- **Jesper Kyd**: electronic / orchestral hybrid; *Hitman*, *Assassin's Creed* (early)
- **Austin Wintory**: modern adaptive scoring; *Journey*, *Abzû*, *Banner Saga*
- **Darren Korb**: indie modern; *Bastion*, *Transistor*, *Hades*
- **Lena Raine**: indie modern; *Celeste*, *Chicory*, *Minecraft Caves & Cliffs*
- **Olivier Deriviere**: French modern; *A Plague Tale*, *11-11 Memories Retold*, *Streets of Rage 4*
- **Gareth Coker**: orchestral / world; *Ori and the Blind Forest*, *Ark*, *Halo Infinite*
- **Joris de Man**: orchestral / electronic hybrid; *Killzone* series, *Horizon Zero Dawn* (with Joe Henson, Alexis Smith)
- **Mick Gordon**: heavy industrial / metal; *Doom (2016)*, *Doom Eternal*, *Wolfenstein II*
- **Yuzo Koshiro**: chiptune / synth dance; *Streets of Rage*, *Actraiser*
- **65daysofstatic**: post-rock / electronic; *No Man's Sky* (procedural generative)
- **Toby Fox**: indie melodic chiptune-influenced; *Undertale*, *Deltarune*

Studying these composers' approaches to specific games (and the games' systems) is the best way to learn game music craft.

## Korean game music

Korean MMORPG and mobile game music has its own significant tradition: composers like Kim Jin-young (Black Desert Online), the team at NCsoft (Lineage, Aion, Blade & Soul), and others have developed a distinctive Korean game music idiom that often blends symphonic Western fantasy with Korean traditional elements (*gugak* instruments, traditional vocal techniques). For Korean traditional music itself, see `korean-traditional.md`.

## Composing game music — practical workflow

1. **Understand the game.** Read the GDD (game design document) if available; play prototypes; understand mood, world, character, gameplay loop.
2. **Identify the music architecture.** Is it linear cues only? Vertical layering? Horizontal re-sequencing? Parameter-driven? Hybrid? Talk to the audio director / programmer early.
3. **Identify the technical pipeline.** Wwise, FMOD, Unity native, Unreal native, custom? Each has different constraints.
4. **Establish thematic language.** Main theme, character themes, location themes, faction themes — what motivic material recurs?
5. **Compose with the system in mind.** Looping, layering, transitions, stingers — design each piece to fit its role.
6. **Test in-engine early.** A piece that sounds great in your DAW might not work in the game's audio system. Get rough mockups into the engine ASAP.
7. **Iterate based on gameplay testing.** Music that works in design rarely works perfectly first time in actual gameplay; expect revisions.
8. **Mix for the platform.** Game audio often has a wide dynamic range with sound effects and dialogue mixed alongside; the music has to leave room.

## Common pitfalls when advising

- **Don't compose linear cues for an adaptive context.** A 4-minute through-composed piece doesn't loop or layer well; design for the architecture.
- **Don't ignore loop fatigue.** A piece the player will hear for hours needs to tolerate repetition; one the player hears once doesn't.
- **Don't treat game music as second-class film music.** Game music has its own craft (interactivity, system design, thematic recursion in long-form gameplay) that linear scoring doesn't.
- **Don't underestimate technical constraints.** Old platforms have strict audio limits; modern platforms have memory and CPU budgets. Talk to the audio director.
- **Don't forget the sound effect mix.** Game music shares audio bandwidth with SFX, dialogue, ambience. Music has to leave room.
- **Don't ignore the platform.** Music for a phone played without headphones, music for a 7.1 surround AAA game, music for a VR title with binaural audio — all different.
- **Don't ignore replay value.** The player will hear the music many times; it must reward repeated listening (or at least tolerate it).
- **Don't compose only the "good" music.** Filler areas, menus, loading screens, defeat screens — these need music too, and tone matters for them just as much.
- **Don't apply film scoring conventions blindly.** Film cues have known durations and known emotional arcs; game cues don't. Adapt accordingly.
- **Don't forget themes.** Long-form games (RPGs, narrative adventures) reward strong recurring thematic material. The music can be the player's emotional anchor across hours of play.

## Quick decision matrix

| Want | Try |
|------|-----|
| Tight combat music | Driving, layered, with intensity parameter; quick transitions on encounter / disengagement |
| Atmospheric exploration | Long-loop ambient with subtle internal variation; vertical layering for "approaching threat" tension |
| Boss battle | Larger orchestration, distinctive theme (often related to character / story), 2–4 minute loop |
| JRPG town | Memorable melodic theme, 2–4 minute loop, full orchestration appropriate to setting |
| Stealth | Sparse, tense ambient; spike to action layer on detection |
| Horror | Sparse / silent; tension-building drones; sudden stingers on encounter |
| Indie game with distinctive music identity | Establish a specific stylistic palette (chiptune, jazz, folk, electronic, world) and let it permeate the score |
| Procedural / endless game | Ambient or layered music designed for indefinite playback; avoid prominent melodic recurrence |
| Mobile / casual game | Catchy short loops; non-distracting; assume player may mute |
| Diegetic music | Real-world music conventions for in-world sources; consider licensing existing tracks |
| Highly adaptive AAA game | Plan vertical layering + horizontal re-sequencing + parameter-driven elements; talk to audio director from start |
| Korean MMORPG / fantasy | Symphonic Western with optional *gugak* fusion elements |

## Cross-references

- Linear / film scoring (much technique transfers) → `film-tv-scoring.md`
- Algorithmic and AI-assisted composition (procedural game music) → `../techniques/algorithmic-and-AI-assisted.md`
- Korean traditional fusion (relevant to Korean game music) → `korean-traditional.md`
- Orchestration for game ensembles → `../orchestration/instruments-ranges-character.md`, `../orchestration/voicing-and-texture.md`, `../orchestration/arrangement-density.md`
- Energy and dynamics across sections → `../production-aware/energy-and-dynamics.md`
- Form and narrative (long-form games are narrative structures) → `../form/narrative-and-transitions.md`
- Thematic / motivic development (recurring themes are central) → `../melody/motivic-development.md`, `../techniques/theme-and-variation.md`
- Specific genres a game might draw on (jazz, electronic, folk, etc.) → corresponding `genres/*.md`
- Pre-production decisions for adaptive scoring → `../production-aware/pre-production-decisions.md`
