# Modulation

Modulation is a real change of key — not a tonicization that comes back, but a passage that establishes a new tonic and stays there long enough for the listener to accept it. This file covers the techniques for getting from one key to another, and how to choose between them based on the kind of move you want.

## When to consult this file

- The user asks about key changes, modulating, "going up a step at the last chorus"
- Pivot chords, common tones, enharmonic moves
- Distant key relationships and how to bridge them
- The "truck driver modulation" and other pop-specific patterns
- Form-level modulation (development sections, bridges)

For chromatic chords that don't change key (secondary dominants, borrowed chords), see `chromatic-harmony.md`. For key relationships in formal context (sonata form, AABA bridges), see `form/classical-forms.md` and `form/popular-song-forms.md`.

## Tonicization vs. modulation — the boundary

There's no sharp line. The difference is one of duration, structural weight, and whether the new key gets a cadence.

| Feature | Tonicization | Modulation |
|---------|--------------|------------|
| Duration | A beat to a few bars | Several bars to entire sections |
| Cadence in new key? | No | Yes (typically PAC or strong V→I) |
| Returns to original key? | Yes, immediately | May or may not |
| Listener perception | Color in the original key | A new key has been established |

A `V/V – V – I` is tonicization. A passage that goes to the dominant key, cadences there, sits there for 8 bars, then returns is modulation. Some passages (Romantic music especially) live in the gray zone — you've gone "to" the new key but you're never quite settled.

## Key relationships

Keys differ in *closeness* by how many sharps or flats away they are on the cycle of fifths.

### Closely related keys

For a major key, the closely related keys (sharing six of seven scale notes — differing by one accidental) are:

- The dominant (V) — e.g., C major → G major
- The subdominant (IV) — e.g., C major → F major
- The relative minor (vi) — e.g., C major → A minor
- The supertonic minor (ii) — e.g., C major → D minor
- The mediant minor (iii) — e.g., C major → E minor
- The relative minor of the subdominant (vi of IV / iv of I) — e.g., C major → D minor or A minor (overlap with above)

In practice: V, IV, and the relative minor are the "easy" modulations. They share the most chords with the original key.

For a minor key, the closely related keys are: the relative major (♭III), the dominant minor (v), the subdominant minor (iv), the submediant major (♭VI), the supertonic diminished (rarely used as a key center), and the leading-tone subtonic major (♭VII).

### Distant keys

Anything more than one accidental away. Most striking distant relationships:

- **Up a half-step** (e.g., C → D♭): the "truck driver" modulation in pop
- **Up a whole step** (e.g., C → D): also common pop modulation, slightly less abrupt
- **Tritone** (e.g., C → F♯): far apart but enharmonically reachable through tritone sub
- **Chromatic mediants** (e.g., C → E or C → A♭): no shared diatonic chords, very colorful

Distant keys require more setup — you can't just slide in. The longer the distance, the more the modulation needs preparation or boldness to feel earned.

## Modulation techniques

### 1. Pivot chord (common chord) modulation

The most stable, classical technique. Find a chord that exists in both the original key and the destination key. Approach it as a chord of the original key, leave it as a chord of the destination key.

Example: modulating from C major to G major.

- The chord `Am` is `vi` in C major and `ii` in G major.
- Set up: `C – F – Am` (functioning as `I – IV – vi` in C)
- Reinterpret: `Am – D7 – G` (now functioning as `ii – V – I` in G)

The pivot chord isn't heard as a key change yet. The change is felt only when the destination key's dominant arrives (D7 in this example) and resolves to G.

Common pivot chord choices for moving to a closely related key:

| From → To | Common pivots |
|-----------|---------------|
| C major → G major | Am (vi=ii), Em (iii=vi), C (I=IV) |
| C major → F major | Dm (ii=vi), Am (vi=iii), F (IV=I) |
| C major → A minor | C (I=♭III), F (IV=♭VI), G (V=♭VII), Am (vi=i) |
| C major → D minor | F (IV=♭III), Am (vi=v), Dm (ii=i) |

Pivot chord modulation is the workhorse of classical and many pop modulations.

### 2. Direct (phrase) modulation

Just *change keys* with no preparation. The new key's tonic appears suddenly. Surprising and abrupt; usually at a clear formal boundary (start of a verse, chorus, or new section).

Effect: dramatic, especially when the new key is distant. A Beatles trademark — many of their songs modulate by direct juxtaposition between sections.

Pop "truck driver" modulations are usually direct: end the chorus on the original key, repeat the chorus a half-step or whole-step higher. Done correctly, the listener feels the lift; done lazily, it feels gimmicky.

### 3. Common-tone modulation

Hold a single note (or a small set of notes) across the change, and reinterpret it in the new key. The ear latches onto the held tone as continuity while everything else shifts.

Example: a C major chord (C-E-G) → reinterpret E as the tonic of E major. Hold E, change G→G♯ and C→B. Suddenly you're in E major, with E as the common tone.

Common-tone modulation is favorite of Schubert and Romantic composers. Distant keys can be reached almost effortlessly by spotting a shared tone.

### 4. Sequential modulation

A short passage repeats at successively transposed pitch levels until it lands in a new key. Common in Baroque and Classical music; used in Romantic for build-ups.

Example: a 2-bar phrase repeated up a step, then up another step, then resolved in the new key.

Effect: feels like a journey, accumulating energy. Movie trailer music uses this constantly.

### 5. Chromatic modulation

Chromatic voice leading drives the change. The chords don't share diatonic membership, but stepwise voice motion makes the transition feel inevitable.

Most often involves a fully diminished 7 chord (which is a pivot in disguise — `°7` chords belong to multiple keys at once because of their symmetry) or a German 6 reinterpreted as a dominant 7.

### 6. Enharmonic modulation

Reinterpret a chord by spelling its notes differently. Two famous cases:

**German 6 ↔ dominant 7**: A `Ger⁶` in one key has the same pitch content as a dominant 7th in a key a half-step above. In C major, the German 6 (A♭ C E♭ F♯) is enharmonically A♭7 (A♭ C E♭ G♭) — `V7` of D♭. Reinterpret and you're in D♭. An `It⁶` has only three distinct notes, so it can lead into this move by voice expansion, but it is not itself enharmonically identical to a full `V7`.

**Diminished 7 chord**: A `°7` chord is symmetric (stacked m3s), so enharmonically it has four possible roots and can resolve into four different keys. `B°7 = D°7 = F°7 = A♭°7` (with appropriate spelling). It can be the `vii°7` of C, E♭, G♭, or A. Pick which interpretation you want and resolve there.

Enharmonic modulation is the magician's trick — it lets you teleport between keys that look unrelated on paper.

### 7. Modal pivot

Reinterpret the current tonic as a different scale degree of a destination key. This works because the same chord can serve as different functions in different keys.

E.g., the C major chord can be the `I` of C, `IV` of G, `V` of F, or `♭VI` of E minor (if borrowed). Land in C with the previous key's logic, then approach C as if it were `IV` of G — and you've modulated to G.

## Pop-specific modulation patterns

### "Truck driver" modulation (up a half-step or whole-step)

The defining pop modulation: at the last chorus, the entire song shifts up a half-step or whole-step. No preparation, no pivot, just a direct lift.

Examples:
- "Man in the Mirror" (Michael Jackson) — half-step up at the final chorus
- "Living on a Prayer" (Bon Jovi) — half-step up at the final chorus
- "Love on Top" (Beyoncé) — multiple consecutive half-step modulations

Effect: a sudden injection of energy, often paired with a vocal climax. Cliché but reliable.

How to set it up: the bar before the modulation is often a `V7` of the new key (so `V7` of D♭ before modulating up a half-step from C to D♭). This makes it feel earned rather than abrupt.

### Modulation to the relative minor (or back)

A song in major modulates briefly to the relative minor for the bridge, then returns. Works because they share the same key signature — the modulation is more of a shift in tonal center than a change of pitch material.

### Modulation by chorus-shift in K-pop / J-pop

K-pop ballads often modulate within a section — the chorus might start in one key, shift to a new key for the second half, and the song never returns. This produces an ascending emotional contour across the song.

### Modal modulation

Stay in the same set of pitches but shift the tonal center. C major → A minor is technically modulation but uses no new pitches. Common in folk, modal jazz, and some film.

## Setting up a modulation that feels earned

Beyond technique, the *placement* and *preparation* matter:

- **Modulate at structural points.** End of verse → bridge in new key. End of bridge → final chorus a step higher. Don't modulate mid-phrase unless you want it to feel jarring.
- **Pre-domesticate the new key.** A bar or two of the new key's V or V7 before landing on the new tonic helps the ear adjust.
- **Match modulation distance to emotional weight.** A half-step up is energetic. A tritone away is uncanny. A modulation to the relative minor is reflective. Pick the distance that fits the moment.
- **Repetition reinforces the new key.** A modulation that immediately leaves doesn't feel like a real modulation — it's a tonicization.
- **Cadence in the new key.** A V→I (or ii–V–I) in the new key seals the modulation. Without it, the listener is suspicious.

## Returning to the original key

Modulating away is half the work; coming back is the other half. Options:

1. **Cadential return**: end the modulated section with a cadence that resolves into the original key's tonic. Often this means ending on the dominant of the original key.
2. **Pivot back**: same technique as the outbound modulation, in reverse.
3. **Direct return**: just put the original key's tonic at the next formal boundary. Fine if there's been enough time in the new key to make the original feel "fresh" again.
4. **Don't return**: stay in the new key. Common in modulating songs that build energy by climbing keys.

## Genre notes

- **Classical**: pivot chord modulation is standard. Sonata form requires modulation from tonic to dominant (or relative major in minor-key sonatas) in the exposition; development modulates further; recapitulation returns. Modulation is the structural engine.
- **Jazz**: ii-V-I sequences let you modulate freely — chain ii-Vs that target any key. Jazz often doesn't "modulate" in the classical sense; instead, the harmonic ground shifts continuously.
- **Pop**: most songs don't modulate at all (constraints of memorability and verse-chorus structure). When they do, it's usually truck-driver style or a brief bridge-key excursion.
- **R&B/neo-soul**: more modulation than pop average; key shifts at bridges and outros are common.
- **K-pop**: heavy modulation, especially in ballads and dramatic concept songs. Multiple key changes within a single song are common.
- **Film/TV**: modulation is constant — themes are presented in different keys to match scene contexts. Cinematic modulations often use chromatic mediants and enharmonic moves for emotional effect.
- **Musical theatre**: songs often modulate at the bridge to "open up" or at the final chorus to enhance the climax. Used self-consciously and often for narrative reasons.

## Common pitfalls when advising

- **Don't suggest a modulation without thinking about how to come back (or commit to staying).** A modulation that hangs in the new key without resolution feels incomplete.
- **Don't modulate to a distant key without setup.** A surprise modulation can be exciting, but it has to be motivated — usually by a strong sectional break or a specific emotional event.
- **Don't modulate too often.** A song that changes key every 8 bars feels homeless. The listener needs time to settle into each key for the modulation to mean anything.
- **Don't confuse mode shift with modulation.** Going from C major to C minor is modal mixture (or change of mode), not modulation in the technical sense — the tonal center stays.
- **Don't ignore the melody during modulation.** Your vocal line has to land on stable tones in the new key. A modulation that strands the singer on a chromatic note feels unprepared.

## Quick decision matrix

| Want | Use |
|------|-----|
| Smooth, stable modulation to a related key | Pivot chord |
| Sudden energy lift (pop chorus) | Direct (truck driver) modulation up a half/whole step |
| Magical, distant key transition | Common-tone modulation (Schubert flavor) |
| Cinematic build-up | Sequential modulation through ascending steps |
| Surprise reveal of a far-away key | Enharmonic modulation (German 6 → dom 7, or °7 reinterpretation) |
| Reflective shift to "the same place but minor" | Modulate to relative minor |
| Bridge-key excursion in a pop song | Modulate to ♭VI, ♭III, or IV for the bridge |

## Cross-references

- Chromatic chords used as pivots → `chromatic-harmony.md`
- Functional cadences in the destination key → `functional-harmony.md`
- Voice-leading at the modulation point → `voice-leading.md`
- Sonata-form modulation → `form/classical-forms.md`
- Pop-form modulation patterns → `form/popular-song-forms.md`
- K-pop modulation conventions → `genres/kpop-jpop.md`
- Jazz key-change techniques → `jazz-harmony.md`
- Film-score modulation usage → `genres/film-tv-scoring.md`
