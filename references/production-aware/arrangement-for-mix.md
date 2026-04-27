# Arrangement for the Mix

Modern recorded music is a hybrid art: composition + arrangement + production + mixing. This file is about the *arrangement* decisions that affect how a track will mix — frequency distribution, instrumental ranges, parts that may compete or complement each other in the mix.

This skill doesn't cover mixing itself (compression, EQ, reverb, stereo placement) — that's a different specialty. But the composer/arranger makes choices that determine whether the mix will be easy or hard, clear or muddy. This file is about those choices.

For density and layering generally, see `orchestration/arrangement-density.md`. For voicing across instruments, see `orchestration/voicing-and-texture.md`. For energy and dynamics across sections, see `energy-and-dynamics.md`.

## When to consult this file

- The user has an arrangement that "sounds muddy" or "doesn't feel full"
- Mix-aware composition decisions
- Multiple instruments competing in the same range
- Frequency-conscious arrangement choices
- Kick + bass relationship (the perennial challenge)
- "Why does my song sound smaller than [reference track]?"
- Arrangement choices that aid mixing later

## The frequency spectrum

Audio occupies a frequency range from roughly 20 Hz to 20 kHz. The spectrum is divided (informally) into zones:

| Zone | Frequency | What lives here |
|------|-----------|-----------------|
| Sub-bass | 20–60 Hz | The lowest fundamentals — sub-kick, 808 sub bass, deep synth bass |
| Bass | 60–200 Hz | Bass guitar fundamentals, kick drum body, low piano notes |
| Low-mids | 200–500 Hz | Piano LH, low strings, lower vocal range, "warmth" |
| Mids | 500 Hz–2 kHz | Most instruments' fundamentals — vocals, guitars, lower brass, snare body |
| High-mids / presence | 2–6 kHz | Vocal clarity, guitar bite, snare crack, cymbal sticks |
| Highs | 6–12 kHz | Hi-hats, cymbals, vocal "air", string brilliance |
| Air | 12–20 kHz | Cymbal shimmer, reverb tails, "openness" |

Each zone can support some instruments. When two instruments occupy the same zone with similar timbres, they "fight" in the mix — frequency masking.

A well-arranged track has each zone "filled" by something distinct, with limited overlap. A poorly arranged track has multiple instruments competing in the same zone.

## The mid-range problem

Most instruments live in the 200 Hz – 2 kHz range. This is where:

- Vocals sit (the bulk of vocal energy)
- Guitars (most chords, strums, leads)
- Pianos (mid-range chords)
- Synths (most pads and leads)
- Brass (most parts)
- Most strings (violin and viola sit here)

Result: mid-range gets crowded fast. The mix engineer has to carve space with EQ, but the arranger can help by:

- **Limiting the number of mid-range instruments** at any given moment.
- **Distributing instruments to different mid-range zones** (one in 300 Hz, another in 600 Hz, another in 1 kHz).
- **Using extreme registers when possible** (high piano, low cellos) to free the middle.
- **Designing parts that don't all play at once** (one mid-range instrument plays during the verse, another during the chorus).

## Kick and bass — the perennial challenge

Kick drum and bass guitar (or sub bass) both occupy the 60–200 Hz range. They constantly compete.

Solutions:

- **Frequency separation**: kick has more energy at 60–80 Hz; bass at 100–200 Hz. Or vice versa. The key is choosing complementary spectral profiles.
- **Sidechaining**: the bass ducks (briefly drops in volume) every time the kick hits. Common in EDM. Creates "pumping" effect.
- **Rhythmic complementarity**: kick on 1 and 3, bass on 2 and 4 (or vice versa). They don't hit at the same time.
- **Note choice**: when kick hits, bass plays the root (matches the kick's fundamental); when kick rests, bass can play other notes more freely.
- **Layered kick**: a kick drum that's tuned to the song's key (or has tonal center) so it harmonizes with the bass.

A well-arranged track has a clear kick-and-bass relationship that's been thought through. A poorly arranged track has them stepping on each other.

## Stereo space

Mono is the center of the stereo field. Stereo allows panning — placing instruments left or right.

### Standard panning conventions

| Element | Position |
|---------|----------|
| Lead vocal | Center (always) |
| Kick drum | Center |
| Snare | Center or slightly off-center |
| Bass | Center (low frequencies don't pan well in headphones / club systems) |
| Hi-hats | Slightly to one side (stereotypically right for pop) |
| Cymbals | Spread across stereo field |
| Rhythm guitars (doubles) | Hard left + hard right (the "double-tracked" effect) |
| Lead guitar | Often center, sometimes off-center |
| Synth pads | Spread wide |
| Backing vocals | Spread to fill stereo field around lead |
| Strings | Spread (high strings to one side, low strings to other) |

### Mono compatibility

Many listeners hear music in mono — phone speakers, club PA systems, voice-call systems. The arrangement should still work in mono. This means:

- Don't put critical elements only on one side.
- Avoid out-of-phase stereo effects that will collapse in mono.
- Test mixes by listening in mono.

The composer/arranger contributes to mono compatibility by choosing panning that works in both formats.

## Headroom and dynamics

A track that's "loud" throughout has no dynamic range — every section sounds the same volume. A track with dynamics has loud and quiet moments.

For arrangement:

- **Verses should be quieter than choruses** in terms of average volume.
- **The pre-chorus build creates dynamic motion** — getting louder.
- **The bridge often has a dynamic dip** (quieter moment) that lets the final chorus hit harder.

Modern mastering typically compresses everything to high loudness, but the *arrangement* should still have dynamic shape; otherwise the mastering produces a flat, fatiguing result.

## The mid-side perspective

Audio engineers think in "mid" (mono content) and "side" (stereo content). The arranger can help by:

- **Putting the most important elements in the mid** (vocal, kick, bass, snare).
- **Putting decorative elements in the sides** (atmospheric synths, doubled guitars, ambience, reverb tails).
- **Keeping bass mono** — sub frequencies don't have stereo information naturally.

## Layering — frequency-aware

When adding layers, think frequency, not just "another instrument".

- **Adding a 2nd guitar in the same range as the 1st**: doubling — works if intentional, but doesn't add density.
- **Adding a high-pitched instrument** (piccolo, glockenspiel): adds top end, complements existing parts.
- **Adding a low instrument** (sub bass, low string): adds bottom, fills out the spectrum.
- **Adding mid-range instrument when mids are full**: clutter; will fight existing parts.

The skill is layering complementarily.

## Common arrangement-for-mix mistakes

### Too many things in the mid

Lead vocal + 3 mid-range synths + acoustic guitar + electric guitar all in 500 Hz – 2 kHz. The mix engineer has to carve enormously to make space; the result is thinned.

Fix: redistribute or remove some elements.

### Bass guitar in the same register as the kick fundamentals

Bass playing low E, F, G can muddle with kick fundamentals. The bass becomes inaudible, the kick becomes flabby.

Fix: have the bass play in a higher register, or shape kick to leave bass-friendly space.

### Vocal doubled at the same range

Lead vocal + harmony vocal an octave below in the same range — they fight.

Fix: pan the harmony off-center, or put the harmony in a different range (typically a 3rd or 5th above).

### High-frequency clutter

Multiple cymbals, hi-hats, and high synths all hitting at the same time. The high end becomes a wash of noise.

Fix: rhythmic complementarity (one element at a time on the high frequencies) or remove some elements.

### No sub-bass

Modern productions need sub-bass content (60 Hz and below) for clubs, headphones, and modern speakers. Without it, the track sounds "thin" on professional systems.

Fix: add a sub-bass synth or layered kick with sub content.

### Stereo collapse

Critical content (e.g., the lead riff) panned hard right. In mono, it's perfectly there; in stereo on headphones, the listener tilting their head can lose it.

Fix: keep critical content in or near center.

### Frequency masking between parts

Snare and lead guitar both occupy 200–500 Hz. They conflict.

Fix: arrange them not to play simultaneously, or put one in a different range.

## Genre-specific considerations

### Pop

- Vocal is everything. All other parts must clear space for the vocal in the mid-range.
- Kick and bass tightly produced; sidechained.
- Stereo wide for choruses (more layers spread across the stereo field) and tighter for verses.
- Reverb and delay used selectively — too much washes the vocal.

### Rock

- Guitar-centric. The arrangement is usually about guitars + drums + bass + vocals.
- Doubled rhythm guitars (hard panned) is the standard rock production trick.
- The kick and bass guitar relationship is critical; modern rock production tightens both.

### Hip-hop

- 808 sub-bass below the kick; the two together create the foundation.
- Drums are highly compressed and processed.
- Vocal is up-front, often with reverb but tightly mixed.
- Sample-based tracks have to work around the original recording's frequency content.

### EDM

- Sub-bass is foundational; modern productions have heavy 60 Hz – 100 Hz content.
- Kick and bass sidechained explicitly.
- Wide stereo on synths and pads; mono on the bass.
- Drops are designed to sound massive — frequency content from sub to air.

### R&B / neo-soul

- Vocal often sits forward with subtle layering.
- Bass is heavy; deep low end common.
- Drums often sound vintage (sampled or analog-emulated).
- Pads and atmospheric synths fill the mid-side space.

### Country

- Vocal is paramount; everything serves it.
- Acoustic guitar in mid; electric guitar (or pedal steel) often slightly off-center.
- Bass and kick more prominent than in many pop genres.
- Less aggressive frequency processing than pop or EDM.

### Classical / orchestral

- Natural acoustic recording approach often preferred.
- Sections of the orchestra placed in stereo according to seating.
- Less frequency-conscious arrangement; the room's acoustics matter more.
- But scoring choices affect how the orchestra balances on its own.

## A workflow for arrangement-aware composition

If the user is composing with the eventual mix in mind:

1. **Plan the frequency budget.** Decide which zones each instrument will occupy. Aim for at least one element per zone (sub, bass, low-mid, mid, high-mid, high) without crowding any.
2. **Set up kick-and-bass relationship.** Decide which has more 60 Hz content, which has 100–200 Hz. Plan their rhythmic relationship.
3. **Identify the lead element** (usually vocal). Reserve clear space for it in mid-range; arrange other parts to avoid its register.
4. **Design layers in pairs.** Each new element you add should complement an existing one, not duplicate it.
5. **Plan dynamic arc.** Identify which sections are quieter/louder; arrange parts accordingly.
6. **Consider mono compatibility.** Test (or imagine) the mix in mono; ensure critical elements are center.
7. **Think about transitions.** What instruments enter and exit at section breaks? What's added at the chorus, what's removed at the bridge?
8. **Reference checking.** Compare your arrangement to professional tracks in the same genre. Where are their elements in the spectrum? What's the kick-bass relationship?

## Common pitfalls when advising

- **Don't ignore the mix.** Composition decisions become mix problems. Arrange thoughtfully now to save mix work later.
- **Don't assume more layers = better.** Modern pop is highly produced but selectively layered. Each layer must earn its place.
- **Don't write all the parts in the mid-range.** The mid is where the vocal lives; other parts need to make space.
- **Don't ignore the kick-bass relationship.** It's the foundation; if it's muddy, everything sounds muddy.
- **Don't forget about mono.** Many listeners will hear in mono. Test arrangements in mono.
- **Don't over-process at the arrangement stage.** Arrangement is about parts; processing is about mixing. They're related but distinct.
- **Don't skip referencing.** Always compare to professional tracks in the same genre. Arrangement standards differ enormously by genre.

## Quick decision matrix

| Want | Try |
|------|-----|
| Bass that doesn't fight kick | Sidechain bass to kick; or have bass play in different register from kick fundamentals |
| Crowded mid-range fix | Remove one element; or push one to a different zone |
| Punchy vocal | Carve mids around vocal range; minimal compression-fighting elements there |
| Big stereo image | Doubled guitars panned wide; reverb tails spread wide; lead in center |
| Mono-compatible mix | Critical elements in center; avoid out-of-phase stereo tricks |
| Modern pop sound | Sub bass + sidechained bass; kick sample with character; tight vocals; wide pads |
| Fuller chorus than verse | Add mid-frequency layer (rhythm guitar, pad); add backing vocals; widen stereo |
| Thinner verse | Strip to vocal + minimal accompaniment; let chorus add layers |
| Rock production | Hard-panned rhythm guitars; tight kick + bass; vocal in center |
| Hip-hop low end | 808 sub + tuned kick + sidechained bass content; tight 100–200 Hz |
| EDM drop massive | Sub bass + main bass + lead synth + chord stab + drums all hitting; full frequency spectrum |

## Cross-references

- Density and layering → `orchestration/arrangement-density.md`
- Voicing and texture → `orchestration/voicing-and-texture.md`
- Instrument ranges (informs frequency planning) → `orchestration/instruments-ranges-character.md`
- Energy and dynamics across sections → `energy-and-dynamics.md`
- Pre-production decisions (key, tempo, length — set before arrangement) → `pre-production-decisions.md`
- Genre-specific production conventions → various `genres/*.md` files (especially pop-rock, hip-hop-rnb, electronic-edm, kpop-jpop)
- Form and arrangement (how density changes across sections) → `form/popular-song-forms.md`, `form/narrative-and-transitions.md`
