# Release Notes — v1.0

Release: **music-composition v1.0**  
Release date: **2026-04-27**  
Base package: `music-composition-RC1-2026-04-27.zip`  
Release type: **first stable release**

## Release decision

v1.0 promotes RC1 to the first stable release. No RC2 was created because Phase B correctness work is complete, Phase C prompt smoke testing passed by user report, and the release-candidate packaging checks did not reveal a release blocker.

This release is intended to be a stable, practical music-composition skill for brainstorming, drafting, analysis, revision, teaching, reference research, and user-agent composition sessions. It is not intended to be a complete encyclopedia of every style, region, instrument, platform, or legal edge case.

## What changed from RC1

v1.0 does **not** add new runtime music content beyond RC1. The finalization pass adds release-final artifacts and updates release status wording only.

Added:

- `RELEASE-NOTES-v1.0.md`
- `VALIDATION-v1.0.md`
- `RC1-v1.0-decision-memo-2026-04-27.md`

Updated:

- `MAINTENANCE.md`
- `RELEASE-ROADMAP.md`
- `references/00-navigation.md`
- `references/validation/first-release-readiness.md`
- `scripts/music_theory_sanity_check.py`

The updates are release-finalization / validation updates, not new composition behavior.

## What is included

v1.0 includes:

- `SKILL.md` as the runtime entry point;
- `references/00-navigation.md` as the routing guide;
- short, quotable assets in `assets/`;
- longer theory, genre, workflow, research, orchestration, instrument-idiom, and validation references in `references/`;
- music-specific brainstorming, collaboration, revision, answer-calibration, and session-log workflows;
- web research, reference-track digging, user listening context, regional trend analysis, microgenre dispatch, and style/originality guardrails;
- genre and instrument-idiom starter guides;
- `KNOWN-LIMITATIONS.md`;
- `scripts/music_theory_sanity_check.py`.

## Release-readiness summary

| Area | v1.0 status |
|---|---|
| Phase A content lock | Complete |
| Phase B correctness pass | Complete |
| Phase C prompt smoke tests | Pass result recorded |
| Phase D RC packaging | Complete |
| v1.0 finalization | Complete |
| Automated sanity checker | Pass |
| Internal Markdown links | Pass |
| ZIP hygiene | Pass |
| Known limitations | Included |

## How to validate locally

From the repository root:

```bash
python3 scripts/music_theory_sanity_check.py
```

Expected output for this package:

```text
music_theory_sanity_check: PASS
Checked 115 markdown files.
```

If a future maintainer adds or removes Markdown files, the count may change; the validation report should then be updated.

## What to read first

For maintainers:

1. `RELEASE-ROADMAP.md`
2. `VALIDATION-v1.0.md`
3. `KNOWN-LIMITATIONS.md`
4. `references/validation/first-release-readiness.md`
5. `references/validation/phase-c-smoke-test-results.md`

For runtime behavior:

1. `SKILL.md`
2. `references/00-navigation.md`
3. the relevant files selected by the navigation guide

## Known limitations

See `KNOWN-LIMITATIONS.md`.

The most important caveat is that current music trends, artist activity, chart behavior, platform surfaces, streaming-service behavior, AI tools, copyright status, and living scenes must still be handled through active research workflows rather than frozen static claims.

## Post-release direction

After v1.0, treat new work as update patches rather than first-release blockers. Good next updates include dedicated regional guides, deeper parser-like validation, larger prompt-evaluation harnesses, more instrument idiom files, and additional currentness/research refinements.

## Cross-references

- Entry point → `SKILL.md`
- Maintenance guide → `MAINTENANCE.md`
- Release roadmap → `RELEASE-ROADMAP.md`
- v1.0 validation report → `VALIDATION-v1.0.md`
- RC1 → v1.0 decision memo → `RC1-v1.0-decision-memo-2026-04-27.md`
- RC1 validation report → `VALIDATION-RC1.md`
- Known limitations → `KNOWN-LIMITATIONS.md`
- Phase C results → `references/validation/phase-c-smoke-test-results.md`
- First-release readiness → `references/validation/first-release-readiness.md`
