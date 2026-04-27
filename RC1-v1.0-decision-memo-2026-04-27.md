# RC1 → v1.0 / RC2 Decision Memo

Date: 2026-04-27  
Package reviewed: `music-composition-RC1-2026-04-27.zip`

## Decision

**Promote RC1 to v1.0. Do not create RC2 unless a new release blocker appears during final v1.0 packaging.**

RC2 is not recommended right now. The current remaining work is mostly expansion, deeper evaluation, or tooling polish, not first-release blocking correction.

## Evidence reviewed

- `VALIDATION-RC1.md`
- `RELEASE-NOTES-RC1.md`
- `RELEASE-ROADMAP.md`
- `KNOWN-LIMITATIONS.md`
- `references/validation/phase-c-smoke-test-results.md`
- RC1 package file list and validation structure
- Local sanity-check rerun from extracted RC1 package

Local sanity-check rerun:

```text
music_theory_sanity_check: PASS
Checked 112 markdown files.
Elapsed: 0:25.98
```

The checker runtime is somewhat noticeable, but acceptable for RC1/v1.0 validation. Optimizing it can be treated as post-v1.0 tooling polish unless it becomes disruptive in routine use.

## Why v1.0 is the better next step

RC1 has already cleared the gates that matter for a first release:

| Gate | Status | Decision impact |
|---|---|---|
| Phase A content lock | Complete | No RC2 needed |
| Phase B correctness pass | Complete | No RC2 needed |
| Phase C prompt smoke tests | Passed by user report | No RC2 needed |
| Phase D packaging | Complete | No RC2 needed |
| Sanity checker | Re-ran and passed | No RC2 needed |
| ZIP/package structure | Already validated in RC1 | No RC2 needed |
| Known limitations | Explicitly shipped | No RC2 needed |

The release roadmap already says to hold after RC1 only if a release blocker appears. No such blocker is currently visible.

## Why RC2 is not recommended now

A new RC should fix a meaningful release-risk problem. At this point, the likely RC2 candidates would be:

- more regional or microgenre guides;
- a deeper chord-symbol / scale-degree parser;
- faster validation tooling;
- broader prompt-evaluation harnesses;
- more source mapping and bibliography detail;
- additional instrument-idiom files.

All of these are useful, but they are better as v1.1 / v1.2 work. Adding them before v1.0 would increase churn without reducing a known first-release risk.

## Final v1.0 packaging scope

The v1.0 pass should be **metadata-only / release-finalization only**:

- add or rename final release notes as `RELEASE-NOTES-v1.0.md`;
- add `VALIDATION-v1.0.md`;
- update `RELEASE-ROADMAP.md` from “RC1 packaged” to “v1.0 shipped”;
- update `MAINTENANCE.md` release artifact list;
- optionally keep RC1 notes for traceability or replace them with v1.0 notes, but avoid duplicate/confusing release-state language;
- generate `music-composition-v1.0-2026-04-27.zip`, patch, and SHA256 file;
- do not add new runtime content during v1.0 packaging.

## RC2 trigger conditions

Create RC2 instead of v1.0 only if one of these appears during the final packaging pass:

1. sanity checker fails;
2. ZIP integrity or hygiene fails;
3. internal `.md` links break;
4. a newly found P0/P1 music-theory error appears in high-use assets;
5. a privacy/currentness/style/copyright/cultural-specificity blocker appears;
6. a serious mismatch appears between `SKILL.md`, `references/00-navigation.md`, and actual files;
7. a validation report claims a check passed when it was not actually run or cannot be reproduced;
8. a Phase C failure pattern reappears and affects core routing or answer shape.

## Post-v1.0 backlog

Treat these as v1.1 / v1.2 candidates:

- dedicated deep guides for regional Mexican, Punjabi pop, Turkish arabesk-pop, Maghreb/raï, gqom, singeli, kuduro, sertanejo/pagode/arrocha/piseiro;
- additional instrument idiom files for harp, mallet percussion, organ, accordion, synth performance idioms, and DJ/turntable-informed writing;
- larger prompt-evaluation harness with routing traces;
- deeper symbolic music-theory parser for chord symbols, Nashville numbers, altered dominants, modal mixture, and scale-degree spelling;
- validation script performance optimization;
- more source citations and bibliography mapping for high-risk cultural/currentness files;
- accessibility and wellness-oriented composition guidance.

## Final recommendation

**Proceed directly from RC1 to v1.0 packaging.**

Hold RC2 in reserve only for blocker fixes discovered during the final packaging pass.
