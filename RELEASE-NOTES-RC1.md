# Release Notes — RC1

Release candidate: **music-composition RC1**  
Snapshot date: **2026-04-27**  
Base package: `music-composition-patched-2026-04-27-v8.zip`

## Release decision

RC1 is ready for review. Phase B correctness work is recorded, Phase C prompt smoke testing has a pass result recorded, and the final packaging sanity checks pass.

This release candidate is intended to be a stable first release of the music-composition skill, not a final encyclopedia of every style, region, instrument, or workflow.

## What is included

RC1 includes:

- a runtime entry point in `SKILL.md`;
- routing in `references/00-navigation.md`;
- short quotable assets in `assets/`;
- longer composition references in `references/`;
- user-agent workflow guides for brainstorming, collaboration, revision, answer calibration, and session logging;
- research workflows for web trend research, reference-track digging, user listening context, regional trend analysis, microgenre dispatch, and style/originality boundaries;
- genre and instrument-idiom starter guides;
- release-readiness and validation documentation;
- `KNOWN-LIMITATIONS.md`;
- `scripts/music_theory_sanity_check.py`.

## Release-readiness summary

| Area | RC1 status |
|---|---|
| Phase A content lock | Complete for RC1 |
| Phase B correctness pass | Complete |
| Phase C prompt smoke tests | Pass result recorded |
| Phase D packaging | Complete |
| Automated sanity checker | Pass |
| Internal Markdown links | Pass |
| ZIP hygiene | Pass |
| Known limitations | Included |

## Changes from v8

RC1 does not add major new runtime capability. The v8 content is preserved and packaged as a release candidate with:

- this release-notes file;
- `VALIDATION-RC1.md`;
- roadmap wording updated from “ready for RC packaging” to “RC1 packaged”;
- maintenance documentation updated to list the RC release artifacts.

## How to validate locally

From the repository root:

```bash
python3 scripts/music_theory_sanity_check.py
```

Expected output:

```text
music_theory_sanity_check: PASS
Checked 112 markdown files.
```

The exact Markdown count should remain stable unless a maintainer intentionally adds or removes files and updates the validation report.

## What to read first

For maintainers:

1. `RELEASE-ROADMAP.md`
2. `VALIDATION-RC1.md`
3. `KNOWN-LIMITATIONS.md`
4. `references/validation/first-release-readiness.md`
5. `references/validation/phase-c-smoke-test-results.md`

For runtime behavior:

1. `SKILL.md`
2. `references/00-navigation.md`
3. the relevant files selected by the navigation guide

## Release caveat

This RC is a strong first-release candidate, but it still relies on active web research for living scenes, charts, platform behavior, AI/copyright status, current artist activity, and rapidly changing music trends.

## Cross-references

- Entry point → `SKILL.md`
- Maintenance guide → `MAINTENANCE.md`
- Release roadmap → `RELEASE-ROADMAP.md`
- Validation report → `VALIDATION-RC1.md`
- Known limitations → `KNOWN-LIMITATIONS.md`
- RC packaging checklist → `references/validation/rc1-packaging-checklist.md`
- Phase C results → `references/validation/phase-c-smoke-test-results.md`
