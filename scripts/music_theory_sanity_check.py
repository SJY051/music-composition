#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Regression and release-readiness checks for the music-composition skill.

This catches broken internal Markdown references, known high-risk music-theory
regressions, snapshot-note gaps, and a small set of parser-like chord / scale
spelling sanity checks. It does not replace musical review, prompt smoke tests,
or current web research.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MD_PATH_RE = re.compile(r"(?<![\w./-])(?:\.\.?/)?[A-Za-z0-9_./#()\-]+\.md(?:#[A-Za-z0-9_./#()\-]+)?")

RISKY_PATTERNS = [
    (re.compile(r"\bexotic\b", re.I), "Avoid `exotic`; name the musical variable or cultural context."),
    (re.compile(r"foreign menace", re.I), "Avoid threat/othering cliché language."),
    (re.compile(r"exotic east", re.I), "Avoid vague/orientalist shorthand."),
    (re.compile(r"\btoemsae\b", re.I), "Use `toeseong` for 퇴성 unless a specific source says otherwise."),
    (re.compile(r"\bchangjo\b", re.I), "For pansori structure, prefer chang/sori, aniri, and balim."),
    (re.compile(r"C\(no5\)[^\n]{0,120}power chord", re.I), "C(no5) is not a power chord; C5 or C(no3) is."),
    (re.compile(r"E7alt[^\n]{0,160}A♯[^\n]{0,160}♯9", re.I), "In E7alt, A♯ is ♯11/♭5; G natural is ♯9."),
    (re.compile(r"Western music since roughly 1700 uses 12-TET", re.I), "12-TET history claim is too broad."),
    (re.compile(r"maqam[^\n]{0,80}24-TET subset", re.I), "Do not reduce maqam/makam to a 24-TET subset."),
    (re.compile(r"Spanish, Middle Eastern, Klezmer flavor", re.I), "Avoid broad culture-flavor shorthand for Phrygian dominant."),
    (re.compile(r"World music color", re.I), "Use tradition-specific instrument color and idiom, not `world music color`."),
    (re.compile(r"\bY flavor\b", re.I), "Prefer `Y influence` or a concrete musical variable over flavor shorthand."),
    (re.compile(r"ethnic flavor", re.I), "Avoid vague culture-as-flavor phrasing; name the specific tradition or musical variable."),
    (re.compile(r"\bethnic\b", re.I), "Avoid vague `ethnic` instrumentation labels; name the tradition, region, or percussion family."),
    (re.compile(r"Asian flavor", re.I), "Avoid continent-scale style shorthand; name the market, tradition, or craft variable."),
    (re.compile(r"world flavor", re.I), "Avoid vague `world` color phrasing; name the scene or idiom."),
    (re.compile(r"sounds foreign", re.I), "Avoid othering language; describe unfamiliarity or non-idiomatic fit precisely."),
    (re.compile(r"Jinyangjo[^\n]{0,80}18 beats", re.I), "Jinyangjo should not be reduced to an 18-beat cycle; use 6-beat / 24-beat phrase caveat."),
    (re.compile(r"Diminished \(half-whole\)[^\n]{0,160}E♭ E", re.I), "Half-whole diminished over C7 should spell the altered ninth as D♯, not E♭."),
    (re.compile(r"Whole[- ]tone[^\n]{0,160}C D E F♯ G♯ A♯", re.I), "Whole-tone dominant spelling should use B♭ for ♭7, with A♯ only as enharmonic caveat."),
]

SNAPSHOT_REQUIRED_DIRS = [
    ROOT / "references" / "genres",
    ROOT / "references" / "research",
]
SNAPSHOT_REQUIRED_FILES = [
    ROOT / "references" / "production-aware" / "pre-production-decisions.md",
    ROOT / "references" / "techniques" / "algorithmic-and-AI-assisted.md",
]

EXPECTED_INTERVAL_LINES = [
    "| Augmented 5th (A5) | 8 | d4 | C–G♯ |",
    "| Minor 6th (m6) | 8 | M3 | C–A♭ |",
]

EXPECTED_MODE_LINES = [
    "| **Ionian** | C D E F G A B | `W W H W W W H` |",
    "| **Lydian** | C D E F♯ G A B | `W W W H W W H` |",
    "| **Mixolydian** | C D E F G A B♭ | `W W H W W H W` |",
    "| **Aeolian** | C D E♭ F G A♭ B♭ | `W H W W H W W` |",
]

EXPECTED_FILES = [
    "RELEASE-ROADMAP.md",
    "KNOWN-LIMITATIONS.md",
    "RELEASE-NOTES-v1.0.md",
    "VALIDATION-v1.0.md",
    "RC1-v1.0-decision-memo-2026-04-27.md",
    "references/validation/first-release-readiness.md",
    "references/validation/prompt-smoke-tests.md",
    "references/validation/phase-b-correctness-pass.md",
    "references/validation/phase-c-smoke-test-results.md",
    "references/validation/rc1-packaging-checklist.md",
    "references/genres/country-americana.md",
    "references/genres/metal-punk-hardcore.md",
    "references/genres/gospel-and-ccm.md",
    "references/genres/brazilian-pop-and-funk.md",
    "references/instrument-idiom/overview.md",
    "references/instrument-idiom/piano-keyboards.md",
    "references/instrument-idiom/guitar.md",
    "references/instrument-idiom/bass.md",
    "references/instrument-idiom/drums-percussion.md",
    "references/instrument-idiom/strings.md",
    "references/instrument-idiom/winds.md",
    "references/instrument-idiom/brass.md",
    "references/instrument-idiom/vocals.md",
    "references/source-bibliography.md",
    "references/research/user-listening-context-and-streaming-services.md",
    "references/research/regional-trend-evolution-analysis.md",
    "references/genres/minor-and-hybrid-genres.md",
    "references/genres/regional-scene-starters.md",
    "references/genres/folk-roots-and-traditions.md",
    "references/creative-workflows/musical-brainstorming.md",
    "references/creative-workflows/user-agent-collaboration.md",
    "references/creative-workflows/revision-and-feedback-loops.md",
    "references/creative-workflows/answer-calibration.md",
    "assets/trend-and-reference-matrices.md",
    "assets/musical-brainstorming-cards.md",
    "assets/session-brief-and-decision-log.md",
    "assets/web-search-cheatsheet.md",
    "assets/chord-symbol-ambiguity-and-parsing.md",
    "assets/scale-degree-spelling-cheatsheet.md",
    "assets/music-theory-audit-rubric.md",
]

BASE_PITCH_CLASS = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
SEMITONE_TO_COMMON_TENSIONS = {
    0: {"1", "root"},
    1: {"♭9", "b9"},
    2: {"9", "M9"},
    3: {"♯9", "#9", "m3"},
    4: {"3", "M3"},
    5: {"11", "4"},
    6: {"♯11", "#11", "♭5", "b5"},
    7: {"5"},
    8: {"♯5", "#5", "♭13", "b13", "m6"},
    9: {"13", "6"},
    10: {"♭7", "b7"},
    11: {"7", "M7"},
}

# Parser-like C-root chord sanity cases. These are not exhaustive; they are
# high-use examples that should never regress.
EXPECTED_C_CHORD_PCS = {
    "C": {0, 4, 7},
    "Cm": {0, 3, 7},
    "Cdim": {0, 3, 6},
    "Caug": {0, 4, 8},
    "Csus4": {0, 5, 7},
    "Csus2": {0, 2, 7},
    "C5": {0, 7},
    "C(no3)": {0, 7},
    "C(no5)": {0, 4},
    "C7": {0, 4, 7, 10},
    "Cmaj7": {0, 4, 7, 11},
    "Cm7": {0, 3, 7, 10},
    "Cm7♭5": {0, 3, 6, 10},
    "Cø7": {0, 3, 6, 10},
    "Cdim7": {0, 3, 6, 9},
    "CmMaj7": {0, 3, 7, 11},
    "Cmaj7♯11": {0, 4, 7, 11, 6},
    "C7♭9": {0, 4, 7, 10, 1},
    "C7♯9": {0, 4, 7, 10, 3},
    "C7♭13": {0, 4, 7, 10, 8},
    "C13": {0, 4, 7, 10, 2, 9},
    "Cadd9": {0, 4, 7, 2},
    "C6/9": {0, 4, 7, 9, 2},
}

# Notes in C-root examples from the new parsing asset.
EXPECTED_C_CHORD_NOTES = {
    "C": ["C", "E", "G"],
    "Cm": ["C", "Eb", "G"],
    "Cdim": ["C", "Eb", "Gb"],
    "Caug": ["C", "E", "G#"],
    "Csus4": ["C", "F", "G"],
    "Csus2": ["C", "D", "G"],
    "C5": ["C", "G"],
    "C(no3)": ["C", "G"],
    "C(no5)": ["C", "E"],
    "C7": ["C", "E", "G", "Bb"],
    "Cmaj7": ["C", "E", "G", "B"],
    "Cm7": ["C", "Eb", "G", "Bb"],
    "Cm7♭5": ["C", "Eb", "Gb", "Bb"],
    "Cø7": ["C", "Eb", "Gb", "Bb"],
    "Cdim7": ["C", "Eb", "Gb", "Bbb"],
    "CmMaj7": ["C", "Eb", "G", "B"],
    "Cmaj7♯11": ["C", "E", "G", "B", "F#"],
    "C7♭9": ["C", "E", "G", "Bb", "Db"],
    "C7♯9": ["C", "E", "G", "Bb", "D#"],
    "C7♭13": ["C", "E", "G", "Bb", "Ab"],
    "C13": ["C", "E", "G", "Bb", "D", "A"],
    "Cadd9": ["C", "E", "G", "D"],
    "C6/9": ["C", "E", "G", "A", "D"],
}

EXPECTED_SCALE_SPELLING_LINES = [
    "| `♭II` | D♭ | D♭ F A♭ | lowered supertonic, not C♯ major |",
    "| `V7/vi` | E7 | E G♯ B D | Am |",
    "| C Lydian | ♯4 | C D E F♯ G A B |",
    "| ♯9 | G | raised ninth above E; enharmonic to minor third, but not labeled ♭3 in dominant context |",
]

IGNORED_EXAMPLE_REFS = {
    "old-filename.md",
    "path/file.md",
    "references/foo/bar.md",
    "assets/foo.md",
    "../workflow.md",
    "folk-and-world.md",
    "pop-rock.md",
}


def normalize_note_name(note: str) -> str:
    return note.strip().replace("♯", "#").replace("♭", "b").replace("𝄫", "bb").replace("𝄪", "##")


def note_pc(note: str) -> int:
    note = normalize_note_name(note)
    if not note:
        raise ValueError("empty note")
    letter = note[0].upper()
    if letter not in BASE_PITCH_CLASS:
        raise ValueError(f"bad note letter: {note}")
    pc = BASE_PITCH_CLASS[letter]
    rest = note[1:]
    while rest:
        if rest.startswith("bb"):
            pc -= 2
            rest = rest[2:]
        elif rest.startswith("##"):
            pc += 2
            rest = rest[2:]
        elif rest.startswith("b"):
            pc -= 1
            rest = rest[1:]
        elif rest.startswith("#"):
            pc += 1
            rest = rest[1:]
        else:
            raise ValueError(f"bad accidental in note: {note}")
    return pc % 12


def interval_semitones(root: str, note: str) -> int:
    return (note_pc(note) - note_pc(root)) % 12


def tension_label_is_plausible(root: str, note: str, label: str) -> bool:
    labels = SEMITONE_TO_COMMON_TENSIONS[interval_semitones(root, note)]
    normalized_label = label.replace("#", "♯").replace("b", "♭")
    return label in labels or normalized_label in labels


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def strip_anchor(path: str) -> str:
    return path.split("#", 1)[0]


def resolve_md_ref(source: Path, ref: str) -> Path | None:
    ref = strip_anchor(ref)
    if ref.startswith(("http://", "https://", "mailto:")):
        return None
    if "<" in ref or ">" in ref:
        return None

    candidates: list[Path] = []
    raw = Path(ref)

    if ref.startswith("./") or ref.startswith("../"):
        candidates.append((source.parent / raw).resolve())
        stripped = ref
        while stripped.startswith("../"):
            stripped = stripped[3:]
        if stripped.startswith(("assets/", "references/", "scripts/")):
            candidates.append((ROOT / stripped).resolve())
    elif ref.startswith(("references/", "assets/", "scripts/")):
        candidates.append((ROOT / raw).resolve())
    else:
        candidates.extend([
            (source.parent / raw).resolve(),
            (ROOT / raw).resolve(),
            (ROOT / "references" / raw).resolve(),
            (ROOT / "assets" / raw).resolve(),
        ])

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate
    return candidates[0] if candidates else None


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "__pycache__"}]
        for filename in filenames:
            if filename.endswith(".md"):
                files.append(Path(dirpath) / filename)
    return sorted(files)


def find_md_refs(text: str) -> set[str]:
    refs = set()
    for match in MD_PATH_RE.finditer(text):
        ref = match.group(0)
        if ref.startswith("http"):
            continue
        refs.add(ref)
    return refs


def check_links() -> list[str]:
    errors: list[str] = []
    for md in iter_markdown_files():
        text = strip_code_blocks(md.read_text(encoding="utf-8"))
        for ref in sorted(find_md_refs(text)):
            if ref in IGNORED_EXAMPLE_REFS:
                continue
            resolved = resolve_md_ref(md, ref)
            if resolved is None:
                continue
            if not resolved.exists():
                errors.append(f"Broken md ref: {md.relative_to(ROOT)} -> {ref}")
    return errors


def check_risky_terms() -> list[str]:
    errors: list[str] = []
    skip_files = {"MAINTENANCE.md", "scripts/music_theory_sanity_check.py"}
    for md in iter_markdown_files():
        rel = str(md.relative_to(ROOT))
        if rel in skip_files:
            continue
        lines = strip_code_blocks(md.read_text(encoding="utf-8")).splitlines()
        for lineno, line in enumerate(lines, start=1):
            low = line.lower()
            if any(token in low for token in ("avoid", "do not", "don't", "never", "replace", "removed")) or re.search(r"\bnot\b", low):
                continue
            for pattern, message in RISKY_PATTERNS:
                if pattern.search(line):
                    errors.append(f"Risky pattern in {rel}:{lineno}: {message}")
    return errors


def check_snapshots() -> list[str]:
    errors: list[str] = []
    files: list[Path] = []
    for directory in SNAPSHOT_REQUIRED_DIRS:
        if directory.exists():
            files.extend(sorted(directory.glob("*.md")))
    files.extend([p for p in SNAPSHOT_REQUIRED_FILES if p.exists()])

    for p in files:
        text = p.read_text(encoding="utf-8")
        if not any("Snapshot note" in line for line in text.splitlines()[:8]):
            errors.append(f"Missing snapshot note near top: {p.relative_to(ROOT)}")
    return errors


def check_interval_cheatsheet() -> list[str]:
    errors: list[str] = []
    p = ROOT / "assets" / "intervals-and-scale-formulas.md"
    if not p.exists():
        return ["Missing assets/intervals-and-scale-formulas.md"]
    text = p.read_text(encoding="utf-8")
    for line in EXPECTED_INTERVAL_LINES:
        if line not in text:
            errors.append(f"Expected interval inversion line not found: {line}")
    return errors


def check_expected_files() -> list[str]:
    errors: list[str] = []
    for rel in EXPECTED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"Expected expansion file missing: {rel}")
    return errors


def check_modes_cheatsheet() -> list[str]:
    errors: list[str] = []
    p = ROOT / "assets" / "modes-cheatsheet.md"
    if not p.exists():
        return ["Missing assets/modes-cheatsheet.md"]
    text = p.read_text(encoding="utf-8")
    for line in EXPECTED_MODE_LINES:
        if line not in text:
            errors.append(f"Expected parallel mode line not found: {line}")
    if "F-Em-Am-Bb" in text or "F–Em–Am–Bb" in text:
        errors.append("Lydian example regression: F-Em-Am-Bb contains B♭, not F Lydian's ♯4.")
    return errors



def check_symmetric_scale_spelling() -> list[str]:
    errors: list[str] = []
    expected_lines = {
        "assets/intervals-and-scale-formulas.md": [
            "| Whole tone | 1-2-3-♯4-♯5-♭7 (6 notes) | C D E F♯ G♯ B♭ |",
            "| Diminished (half-whole) | 1-♭2-♯2-3-♯4-5-6-♭7 (8 notes) | C D♭ D♯ E F♯ G A B♭ |",
            "| Altered (super Locrian) | ^7 | 1-♭9-♯9-3-♭5/♯11-♭13-♭7 in dominant-function spelling | C D♭ D♯ E G♭/F♯ A♭ B♭ |",
        ],
        "assets/modes-cheatsheet.md": [
            "| Whole tone | `W W W W W W` (6 notes) | C D E F♯ G♯ B♭ | Over 7♯5 / whole-tone dominant colors; B♭ is the dominant spelling of the enharmonic A♯ |",
            "| Diminished (half-whole) | `H W H W H W H W` (8 notes) | C D♭ D♯ E F♯ G A B♭ | Over dominant ♭9 chords; D♯ is ♯9 over C7 |",
            "| **Altered (super Locrian)** | ^7 | C D♭ D♯ E G♭/F♯ A♭ B♭ | **C7alt** (resolving dominants; functional spelling) |",
        ],
        "references/fundamentals/pitch-intervals-scales.md": [
            "| Whole-tone | `W W W W W W` (6 notes) | C D E F♯ G♯ B♭ | Over 7♯5 / whole-tone dominant colors; B♭ is the dominant spelling of the enharmonic A♯ |",
            "| Diminished (half-whole) | `H W H W H W H W` (8 notes) | C D♭ D♯ E F♯ G A B♭ | Over dominant ♭9 chords; D♯ is ♯9 over C7 |",
        ],
    }
    for rel, needles in expected_lines.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"Missing symmetric-scale file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"Expected symmetric-scale spelling line missing in {rel}: {needle}")
    return errors


def check_chord_tension_math() -> list[str]:
    errors: list[str] = []

    expected = [
        ("E", "A#", "♯11"),
        ("E", "G", "♯9"),
        ("E", "F", "♭9"),
        ("E", "C", "♭13"),
        ("C", "F#", "♯11"),
        ("C", "Db", "♭9"),
        ("C", "D#", "♯9"),
    ]
    for root, note, label in expected:
        if not tension_label_is_plausible(root, note, label):
            errors.append(f"Internal tension mapping failed: {root} to {note} should allow {label}.")

    jazz_voicings = ROOT / "assets" / "jazz-voicings.md"
    if jazz_voicings.exists():
        text = jazz_voicings.read_text(encoding="utf-8")
        if "| E7alt | G♯ - D - F - C (3, ♭7, ♭9, ♭13) |" not in text:
            errors.append("Expected corrected E7alt voicing line not found in assets/jazz-voicings.md")
        if "| E7♭9♯9 | G♯ - D - F - G (3, ♭7, ♭9, ♯9; altered-color subset) |" not in text:
            errors.append("Expected corrected E7♭9♯9 voicing line not found in assets/jazz-voicings.md")

    return errors


def check_chord_formula_spelling() -> list[str]:
    """Validate canonical chord-symbol spellings against pitch-class math."""
    errors: list[str] = []
    for symbol, expected_pcs in EXPECTED_C_CHORD_PCS.items():
        notes = EXPECTED_C_CHORD_NOTES[symbol]
        pcs = {note_pc(n) for n in notes}
        if pcs != expected_pcs:
            errors.append(f"Internal chord parser case failed: {symbol} -> {notes} -> {sorted(pcs)} expected {sorted(expected_pcs)}")

    chord_symbols = ROOT / "assets" / "chord-symbol-conventions.md"
    if chord_symbols.exists():
        text = chord_symbols.read_text(encoding="utf-8")
        required = [
            "| `C5` or `C(no3)` | C power chord (root + 5th, no 3rd) |",
            "`C(no5)` means the fifth is omitted, so it is **not** a power chord.",
            "| Dominant 7 sus4 | `C7sus` or `C7sus4` | `C7sus4` | C F G B♭ |",
        ]
        for needle in required:
            if needle not in text:
                errors.append(f"Expected chord-symbol convention line missing: {needle}")
    return errors


def check_chord_symbol_ambiguity_asset() -> list[str]:
    errors: list[str] = []
    p = ROOT / "assets" / "chord-symbol-ambiguity-and-parsing.md"
    if not p.exists():
        return ["Missing assets/chord-symbol-ambiguity-and-parsing.md"]
    text = p.read_text(encoding="utf-8")
    required = [
        "| `C(no5)` | omit fifth | C E |",
        "| `C9` | Dominant 9 unless otherwise marked | includes B♭, not B |",
        "| `C2` | Csus2 or Cadd9/add2 | likely Csus2 in guitar/pop charts | voicing or third matters |",
        "| ♯9 | D♯ | enharmonic to E♭ but functions as raised 9 over major 3 E |",
    ]
    for needle in required:
        if needle not in text:
            errors.append(f"Expected chord ambiguity/parsing line missing: {needle}")
    return errors


def check_scale_degree_spelling_asset() -> list[str]:
    errors: list[str] = []
    p = ROOT / "assets" / "scale-degree-spelling-cheatsheet.md"
    if not p.exists():
        return ["Missing assets/scale-degree-spelling-cheatsheet.md"]
    text = p.read_text(encoding="utf-8")
    for needle in EXPECTED_SCALE_SPELLING_LINES:
        if needle not in text:
            errors.append(f"Expected scale-degree spelling line missing: {needle}")
    bad_lines = [
        "C Lydian as C D E G♭ G A B",
        "A♯ as ♯9 over E",
    ]
    for bad in bad_lines:
        # These are allowed only in explicit warning lines that include do-not wording.
        for lineno, line in enumerate(text.splitlines(), start=1):
            if bad in line and not any(token in line.lower() for token in ("do not", "not ", "avoid")):
                errors.append(f"Scale-degree spelling warning phrase appears without warning context at line {lineno}: {bad}")
    return errors


def check_release_docs() -> list[str]:
    errors: list[str] = []
    roadmap = ROOT / "RELEASE-ROADMAP.md"
    limitations = ROOT / "KNOWN-LIMITATIONS.md"
    release_notes_v1 = ROOT / "RELEASE-NOTES-v1.0.md"
    validation_v1 = ROOT / "VALIDATION-v1.0.md"
    decision_memo = ROOT / "RC1-v1.0-decision-memo-2026-04-27.md"
    readiness = ROOT / "references" / "validation" / "first-release-readiness.md"
    smoke = ROOT / "references" / "validation" / "prompt-smoke-tests.md"
    phase_c = ROOT / "references" / "validation" / "phase-c-smoke-test-results.md"
    rc1 = ROOT / "references" / "validation" / "rc1-packaging-checklist.md"
    calibration = ROOT / "references" / "creative-workflows" / "answer-calibration.md"
    for p in (roadmap, limitations, release_notes_v1, validation_v1, decision_memo, readiness, smoke, phase_c, rc1, calibration):
        if not p.exists():
            errors.append(f"Missing release validation doc: {p.relative_to(ROOT)}")
    if roadmap.exists():
        text = roadmap.read_text(encoding="utf-8")
        for phrase in ("Minimum viable first release", "prompt smoke tests", "What not to build before first release", "v1.0 finalization", "KNOWN-LIMITATIONS.md"):
            if phrase not in text:
                errors.append(f"Release roadmap missing expected section phrase: {phrase}")
    if smoke.exists():
        text = smoke.read_text(encoding="utf-8")
        if text.count("| # | Prompt | Expected routing | Expected answer shape |") < 5:
            errors.append("Prompt smoke tests should cover multiple prompt categories.")
    if phase_c.exists():
        text = phase_c.read_text(encoding="utf-8")
        for phrase in ("Pass, based on user-run smoke testing", "No blocker fixes required", "Phase D"):
            if phrase not in text:
                errors.append(f"Phase C result doc missing expected phrase: {phrase}")
    if rc1.exists():
        text = rc1.read_text(encoding="utf-8")
        for phrase in ("Required inputs", "Packaging steps", "Release-hold conditions"):
            if phrase not in text:
                errors.append(f"RC1 checklist missing expected phrase: {phrase}")
    if limitations.exists():
        text = limitations.read_text(encoding="utf-8")
        for phrase in ("Known limitations", "Current trends", "Copyright / style", "Automated validation"):
            if phrase not in text:
                errors.append(f"Known limitations doc missing expected phrase: {phrase}")
    if release_notes_v1.exists():
        text = release_notes_v1.read_text(encoding="utf-8")
        for phrase in ("Release Notes — v1.0", "What changed from RC1", "How to validate locally", "Post-release direction"):
            if phrase not in text:
                errors.append(f"v1.0 release notes missing expected phrase: {phrase}")
    if validation_v1.exists():
        text = validation_v1.read_text(encoding="utf-8")
        for phrase in ("Validation Report — v1.0", "Ship v1.0", "Snapshot-note files", "Phase C prompt smoke tests"):
            if phrase not in text:
                errors.append(f"v1.0 validation report missing expected phrase: {phrase}")
    if decision_memo.exists():
        text = decision_memo.read_text(encoding="utf-8")
        for phrase in ("Promote RC1 to v1.0", "Why RC2 is not recommended now", "RC2 trigger conditions"):
            if phrase not in text:
                errors.append(f"RC1 → v1.0 decision memo missing expected phrase: {phrase}")
    if calibration.exists():
        text = calibration.read_text(encoding="utf-8")
        for phrase in ("Controlled variation bands", "Default answer budgets", "Loading calibration"):
            if phrase not in text:
                errors.append(f"Answer calibration doc missing expected phrase: {phrase}")
    return errors


def main() -> int:
    checks = [
        ("internal markdown links", check_links),
        ("risky terms / known regressions", check_risky_terms),
        ("snapshot notes", check_snapshots),
        ("interval cheatsheet", check_interval_cheatsheet),
        ("expected expansion files", check_expected_files),
        ("modes cheatsheet", check_modes_cheatsheet),
        ("symmetric scale spelling", check_symmetric_scale_spelling),
        ("chord / tension spelling", check_chord_tension_math),
        ("chord formula spelling", check_chord_formula_spelling),
        ("chord-symbol ambiguity asset", check_chord_symbol_ambiguity_asset),
        ("scale-degree spelling asset", check_scale_degree_spelling_asset),
        ("release docs", check_release_docs),
    ]

    all_errors: list[str] = []
    for name, fn in checks:
        errors = fn()
        if errors:
            all_errors.append(f"\n[{name}]")
            all_errors.extend(errors)

    if all_errors:
        print("music_theory_sanity_check: FAIL")
        print("\n".join(all_errors))
        return 1

    md_count = len(iter_markdown_files())
    print("music_theory_sanity_check: PASS")
    print(f"Checked {md_count} markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
