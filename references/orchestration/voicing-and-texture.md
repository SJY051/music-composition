# Voicing and Texture

This file is about how to distribute musical material across instruments and registers — *voicing* (the vertical arrangement of notes in a chord) and *texture* (the overall fabric created by all the parts together). These are the decisions that turn a chord-and-melody sketch into actual orchestration.

For instrument ranges and character, see `instruments-ranges-character.md`. For decisions about how many things should be playing at once, see `arrangement-density.md`. For chord spelling itself, see `harmony/chord-construction.md`. For voicing in voice-leading terms (how voices move chord-to-chord), see `harmony/voice-leading.md`.

## When to consult this file

- The user has a chord progression and asks how to voice it
- A piece sounds "muddy", "thin", or "harsh" — usually a voicing/texture issue
- Decisions about close vs. open voicing
- Doubling decisions (which notes to double across instruments)
- Texture types (homophony, polyphony, heterophony)
- Layering pads, strings, or synths

## Texture types

Texture is the overall fabric of a piece — how many independent musical lines are happening, and how they relate to each other.

### Monophony

A single melodic line with no accompaniment. Just one voice (one player or many in unison/octave).

Where it appears:

- Plainchant
- Solo vocal/instrumental lines (introduction of a theme; cadenzas)
- Unison playing in folk and traditional music
- The opening of a piece (often a single line establishes the theme)

Effect: focused, intimate, exposed. Every note is highlighted.

### Homophony

A melody with chord accompaniment. The melody is the "voice" the listener tracks; the chords support it.

This is the dominant texture in:

- Most pop, rock, country, R&B
- Hymns and chorales
- Most film scoring (melody + harmony)
- Romantic art songs
- Solo voice plus piano or guitar

Subtypes:

- **Melody-dominated homophony**: a clear lead melody, with subordinated chordal accompaniment.
- **Chordal homophony**: all parts move together rhythmically (block chords); typified by hymns and traditional choral writing.

### Polyphony / Counterpoint

Multiple independent melodic lines happening simultaneously. Each voice has its own contour and identity. See `counterpoint.md` for full treatment.

Where it appears:

- Bach fugues, inventions
- Renaissance motets and madrigals
- Some contemporary classical and jazz
- Limited use in pop (countermelodies, harmonized backing vocals)

### Heterophony

Multiple voices playing variants of the same melody simultaneously. One voice plays the basic line; others play decorated versions. The lines aren't independent (as in polyphony) but they're not unison either.

Common in:

- Many tradition-specific musics (Gamelan, Indian classical, some African traditions)
- Some folk music
- Modern classical pieces explicitly using heterophony

### Mixed texture

Most music uses combinations. A pop song might be primarily homophonic but include moments of monophony (vocal-only intro), brief counterpoint (a countermelody), and momentary heterophony (backing singers harmonizing in different rhythms).

## Voicing — vertical arrangement of notes

Voicing is how you distribute the notes of a chord across registers. The same chord can be voiced dozens of ways, each producing a different feel.

### Close vs. open voicing

**Close voicing**: all chord tones within a single octave, tightly packed. The voices are as close together as possible.

Example: Cmaj7 close: C E G B (all within an octave).

**Open voicing**: chord tones spread across multiple octaves with gaps.

Example: Cmaj7 open: C (low) – E (middle) – G (middle) – B (high), with gaps between voices.

| Quality | Close | Open |
|---------|-------|------|
| Sound | Compact, "blocky" | Spacious, "spread" |
| Texture | Dense, tight | Airy, full |
| Common use | Choral singing, jazz piano | Orchestral writing, film scoring |
| Risk | Muddy in low register | Loses chord identity if too spread |

### Drop voicings (jazz)

Take a close voicing of a chord and "drop" one voice down an octave. Standard jazz technique.

- **Drop 2**: take the 2nd voice from the top, drop it an octave. The most common jazz guitar voicing.
- **Drop 3**: take the 3rd voice from the top, drop it an octave.
- **Drop 2+4**: drop both 2nd and 4th from top.

Drop voicings open up close-position chords without losing their identity. They voice well on guitar and piano.

For chord-by-chord shapes, see `assets/jazz-voicings.md`.

### Spread voicings

Wide intervals across multiple octaves, often with chord tones an octave apart. Common in cinematic and film scoring.

A "spread" voicing of Cmaj7 might be:
- Bass: C2
- Pad mid: G3
- Strings: C5 E5
- Top: B5

The chord covers nearly four octaves. Big, lush, "movie sound".

### Quartal and quintal voicings

Stack 4ths or 5ths instead of 3rds. Less rooted, more modern.

Example: D3 G3 C4 F4 (quartal) — the famous "So What" voicing.

Used in modal jazz (McCoy Tyner, Herbie Hancock), modern film, and contemporary classical.

For more, see `harmony/chord-construction.md` and `assets/jazz-voicings.md`.

### Cluster voicings

Stack 2nds (chromatic or diatonic). Highly dissonant; used for color, texture, or specific effect.

Example: C D E F (diatonic cluster). Or C C♯ D D♯ (chromatic cluster).

Common in: 20th-century classical (Bartók, Ligeti, Penderecki), avant-garde jazz, some film scoring (especially horror).

## Voicing principles

Six rules of thumb (with style-dependent exceptions):

### 1. Don't pile close intervals in low register

Below middle C, intervals smaller than a 3rd or 4th turn muddy. The lower the register, the wider the spacing should be.

A bass note plus a 3rd above it (e.g., C2 + E2) is muddy. A bass note plus a 5th or 6th or octave (C2 + G2 or C2 + C3) is clear.

Rule: give the bass space. Don't crowd it.

### 2. The 3rd defines the chord's quality

If you must omit something, omit the 5th. The 3rd tells the listener whether it's major or minor; without it, the chord is ambiguous.

The exception: power chords (root + 5th, no 3rd) are deliberately ambiguous. That's their character.

### 3. The 7th defines the chord's flavor in jazz

Even more important than the 3rd in many jazz voicings. A `Cmaj7` with no 7th is just a C major triad. The 7th is the difference.

Many jazz piano left-hand voicings include just root (or no root) + 3 + 7. The 5 is omitted; the 3 and 7 carry the chord.

### 4. Tensions want to be on top

Extensions (9, 11, 13) and altered tones (♯9, ♭9, ♯11, ♭13) sound best in the upper register. Stuffing them in the middle creates muddy clusters.

A `Cmaj9` voiced C E G B D (all close) is muddy. C E G B with D up an octave on top is clear.

### 5. The bass is half the chord

Slash chords and inversions change the chord's affect more than altering an inner voice. A `Cmaj7/E` (E in bass) feels lighter and brighter than a root-position `Cmaj7`. A `Cmaj7/G` feels suspended.

When voicing for emotional effect, consider the bass first.

### 6. Avoid more than 4 simultaneously sounding parts in any register

Beyond 4 voices in a single register, distinguishing parts becomes difficult. Spread voices across registers; don't pile 6 voices into a single octave.

Exception: choral SATB writing (4 voices in two octaves works because of vocal timbres) and clusters (where the dissonance is the point).

## Doubling decisions

Doubling = giving two or more instruments the same line. Common doublings and their effects:

### Octave doublings

Same line, two octaves apart. Effect: rich, hymnic, "big".

| Doubling | Effect |
|----------|--------|
| Soprano + tenor (octave apart) | Strong vocal melody |
| Violin I + cello (octave apart) | Lush string melody |
| Flute + clarinet (octave apart) | Bright, slightly thinner than strings |
| Trumpet + horn (octave apart) | Powerful brass melody |

### Unison doublings

Same line, same octave. Effect: combined timbre; thicker than either instrument alone.

| Doubling | Effect |
|----------|--------|
| Violin + cello in tenor register | Warm, glowing |
| Flute + violin | Sweet, ethereal |
| Trumpet + clarinet (mid register) | Bright, full |

Unison can be warmer than either instrument alone, but if the timbres clash, the doubling sounds smudged. Test combinations.

### Doubling at the third (or other intervals)

Two instruments harmonize the line at a 3rd, 6th, 4th, or other interval. Effect: parallel motion, harmonized line.

This is *not* counterpoint — it's still one line, harmonized. Common in pop backing vocals, brass section writing, country music.

### Doubling for orchestral support

A sustained melodic line can have multiple instruments doubling at unison, octave above, and octave below for full orchestral richness. Common in late Romantic and film scoring.

### When NOT to double

- When the line has too much detail (rapid runs, articulations) — doubling loses precision.
- When you want a solo to feel "alone" — doubling negates that.
- When two instruments don't blend (e.g., trumpet + electric guitar usually sounds messy).
- When the doubled line dominates over the rest of the texture.

## Voicing for specific ensembles

### Piano (solo)

- Left hand handles bass and inner harmony; right hand handles melody.
- Bass typically a single note or octave; LH chord either rootless or with root in bass.
- Avoid more than 4 notes per hand in most cases.
- Use pedal sparingly to sustain harmonies; clear pedal at chord changes.

### String quartet

- 4 voices: violin I, violin II, viola, cello.
- Standard practice: melody in V1 (or sometimes cello, viola); inner voices in V2 and viola; bass in cello.
- Avoid voice crossings in chorale-style writing; allow them in fugal/contrapuntal writing.
- Use the cello's high register for solo passages; the viola's high register for warmer solos.

### Symphony orchestra

- Strings provide harmonic foundation and melodic backbone.
- Woodwinds add color, often doubling strings or playing solo.
- Brass adds power for climaxes and fanfares; often plays sustained chords behind active strings.
- Percussion accents and provides rhythmic punctuation.
- Orchestrate from the bass up: bass line first, then chord, then melody.

### Choir (SATB)

- Soprano: melody (usually).
- Alto: inner harmony, often doubled with tenor an octave above or below the soprano.
- Tenor: middle voice, often the harmonic anchor.
- Bass: foundation.
- Avoid leaps larger than an octave in any voice; aim for stepwise motion in inner voices.
- Doubling rules (`harmony/voice-leading.md`) matter: don't double the leading tone, etc.

### Pop band (drums, bass, guitar, keys, vocals)

- Bass: root (mostly) or melodic line; foundation.
- Drums: rhythm.
- Guitar(s): chordal accompaniment, riff, lead, or color.
- Keys (piano/synth): chord pad, secondary melody, color.
- Vocals: melody (lead) + backing harmonies.
- Voicings often kept simple for groove; complexity in production rather than voicings.

### Pop production / DAW

- Bass: kick + bass guitar / synth bass, often sidechained for groove.
- Mid layer: rhythm guitars, electric piano, pad synth.
- High layer: lead vocal (with double, harmonies), arpeggios, plucks, top synths.
- Effects layer: reverbs, delays, risers, atmospherics.

A common approach: voice the rhythm guitar in close voicing in mid register (E3–E5 zone), the synth pad in spread voicing across the full range, the lead vocal as the highest sustained melodic voice.

## Texture techniques in arrangement

### Melody + bass + chord (most common pop texture)

Bass on the bottom (single note line), chord in the middle (close voicing), melody on top.

Simple but effective. The sweet spot for pop, country, folk, rock.

### Melody + countermelody + bass

Add a second independent melodic line in a middle register. The melody and countermelody can be heard as dialogue.

Example: a violin melody on top, a cello countermelody in middle register, a bass below. Three independent voices.

### Pad + lead

In synth-based music: a sustained chordal pad fills the harmonic space, while a lead synth or vocal carries the melody. The pad is often spread across multiple octaves; the lead is in a clear single register.

### Layered texture

Multiple parts at different rhythmic densities:

- Sustained pad (very slow, sometimes one chord per bar)
- Mid-rhythm part (rhythm guitar at quarter notes or eighth notes)
- Active part (16th-note hi-hat or arpeggio)
- Lead (melody at variable density)

Each layer occupies a different rhythmic and registral space. Combined, they fill the texture without competing.

### Call and response

Two voices (or groups) alternate. Common in gospel, blues, Latin, African music. The two voices share the texture across time rather than simultaneously.

### Hocket

A medieval technique (and modern revival): a single melodic line is split between two voices, with each voice playing every other note. Creates a stuttering, distributed melodic line.

Modern uses: Steve Reich, prog rock, certain electronic music.

## Diagnosing texture problems

When the user says "it sounds wrong" texturally, common diagnoses:

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Muddy" | Too many low notes; close voicing in bass register | Spread the bass; remove inner voices below middle C |
| "Thin" | Not enough mid-range; too much top, too much bottom, gap in middle | Add a mid-register part (alto-range instrument or chord pad in mid) |
| "Cluttered" | Too many active parts at once | Thin out: have some parts hold while others move |
| "Lifeless" | All parts moving together rhythmically | Add rhythmic independence; let parts hold against moving parts |
| "Lopsided" | One side of the spectrum (high or low) dominates | Balance: if all parts are high, add bass; if all low, add top |
| "Doubling sounds smudged" | Two instruments doubling don't blend | Try a different doubling combination, or keep them at the octave instead of unison |
| "Melody can't be heard" | Melody in same range as accompaniment | Push the accompaniment to a different register, or thin its density |
| "Static / boring" | Texture doesn't change across sections | Vary texture: solo verse, full chorus, contrasting bridge |

## Texture by genre — quick reference

| Genre | Typical texture |
|-------|-----------------|
| Solo classical piano | Two-hand homophony; LH bass + chords, RH melody |
| Romantic symphony | Layered orchestral textures; melody + counter + harmony + bass |
| Choral SATB | Homophonic chordal or polyphonic |
| Bach fugue | Strict polyphony |
| Pop ballad | Melody + bass + chord; piano or guitar accompaniment |
| Modern pop production | Layered: kick/bass + rhythm guitar + pad + lead + atmosphere |
| Hip-hop | Beat (drums + bass) + sample/loop + vocal |
| Trap | Drum + 808 bass + melodic synth + vocal |
| EDM | Layered drums + bass + lead + pad + atmosphere |
| Jazz combo | Walking bass + drums + piano comping + horn melody |
| Big band | Rhythm section + horn section harmonized in 3-5 voices |
| Country | Vocal + acoustic guitar + bass + drums + (often) pedal steel/fiddle |
| Folk | Vocal + acoustic guitar (or piano), minimal additions |
| Indian classical | Drone + sitar/sarod (melodic) + tabla (rhythmic) |
| Gamelan | Heterophonic layers of metallophones at different rhythmic densities |

## Common pitfalls when advising

- **Don't recommend a "lush" voicing without specifying.** "Add lushness" could mean: spread voicing, octave doublings, more layers, modal interchange chords, etc. Be specific.
- **Don't ignore the genre's texture conventions.** A spread orchestral voicing in a country song would feel strange. A close jazz voicing in a film cue might feel cramped.
- **Don't pile up doublings without thinking.** Every additional doubling reduces clarity. Add doublings sparingly and with purpose.
- **Don't ignore the dynamic balance.** A muted trumpet doubling a forte string section will be inaudible. Match dynamics to the doubling intent.
- **Don't forget that texture changes across the song.** A song with the same texture throughout is monotonous. Plan texture variation as part of the form.
- **Don't conflate texture with arrangement density.** A song can have a thin texture (just two voices) with high density (very busy rhythm) or thick texture (many voices) with low density (sustained chords). Both are independent dimensions.

## Quick decision matrix

| Want | Try |
|------|-----|
| Intimate, exposed feeling | Monophony or sparse two-voice texture |
| Pop default | Melody + bass + chord (homophonic) |
| Big movie sound | Spread orchestral voicing across full range |
| Lush ballad | Close voicing in mid register + bass + sustained pad above |
| Modal jazz feel | Quartal voicings, McCoy-style stacked 4ths |
| Renaissance feel | Polyphonic SATB, equal voice independence |
| Cinematic chord | Spread voicing with octave doublings (low cello, mid winds, high strings, top piccolo) |
| Funk pocket | Tight close voicing on rhythm guitar/keys; bass independent; drums prominent |
| Synth pop | Layered: kick + sub bass + mid synth + arpeggio + lead + pad |
| K-pop chorus | Big spread voicing, vocal layering with harmonies, full instrumentation |
| Ambient | Sustained pad voicing, very slow harmonic rhythm, no rhythmic activity |

## Cross-references

- Instrument ranges and characters → `instruments-ranges-character.md`
- Density and how many parts at once → `arrangement-density.md`
- Choral writing (4-part vocal voicing, doubling, spacing) → `choral-writing.md`
- Chord spelling and qualities → `../harmony/chord-construction.md`
- Voice leading (chord-to-chord motion of voices) → `../harmony/voice-leading.md`
- Specific voicing shapes (drop 2, drop 3, rootless, etc.) → `../assets/jazz-voicings.md`
- Counterpoint → `../counterpoint.md`
- Production-side voicing decisions → `../production-aware/arrangement-for-mix.md`
- Genre-specific texture → various `../genres/*.md` files
