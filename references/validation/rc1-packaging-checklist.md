# RC1 Packaging Checklist

Use this checklist after Phase B and Phase C are complete and before publishing a first release candidate. It is a maintainer-facing release artifact checklist, not a runtime composition guide.

## Required inputs

| Input | Required status |
|---|---|
| `../../RELEASE-ROADMAP.md` | Phase D criteria current |
| `first-release-readiness.md` | No open release blockers |
| `phase-b-correctness-pass.md` | Completed or updated after latest corrections |
| `phase-c-smoke-test-results.md` | Phase C result recorded |
| `../../KNOWN-LIMITATIONS.md` | Present and linked |
| `../../scripts/music_theory_sanity_check.py` | Run after final edits |

## Packaging steps

1. Start from the latest clean working tree.
2. Run `scripts/music_theory_sanity_check.py` from the repository root.
3. Confirm internal Markdown links pass.
4. Confirm snapshot-note coverage for current-sensitive files.
5. Confirm there are no cache, scratch, temp, `.pyc`, `.DS_Store`, or obsolete generated files.
6. Create the release ZIP.
7. Create a unified diff against the previous patch or release candidate.
8. Create a validation report using the template in `first-release-readiness.md`.
9. Include known limitations in the validation report or ship `../../KNOWN-LIMITATIONS.md` with the package.
10. Open the ZIP listing and confirm expected files are present.

## RC validation report minimum

A release-candidate validation report should include:

```md
# Validation Report — RC1

## Package
- Package:
- Base version:
- Date:

## Automated checks
- Sanity checker:
- Internal links:
- Snapshot notes:
- Known regression checks:
- ZIP integrity:

## Manual / user-run checks
- Phase B correctness:
- Phase C prompt smoke tests:
- High-use assets:
- Research/currentness/privacy:
- Cultural specificity:

## Known limitations
- See KNOWN-LIMITATIONS.md

## Release decision
- Ship / hold / ship with caveats
```

## Release-hold conditions

Hold RC1 if any of these are true:

- the sanity checker fails;
- a known P0/P1 music-theory regression reappears;
- a new major file is not routed from `../00-navigation.md`;
- `../../SKILL.md` misstates the folder structure;
- current-sensitive files lack snapshot notes;
- Phase C is not recorded or is marked partial without explanation;
- the ZIP contains cache/scratch/temp files;
- the validation report claims a check passed without actually running or receiving that check.

## Useful commands

From the repository root:

```bash
python3 scripts/music_theory_sanity_check.py
find . -name '__pycache__' -o -name '*.pyc' -o -name '.DS_Store'
find . -type f | sort
```

For a ZIP integrity check:

```bash
unzip -t <release-package>.zip
```

## Cross-references

- Release roadmap → `../../RELEASE-ROADMAP.md`
- Known limitations → `../../KNOWN-LIMITATIONS.md`
- First-release readiness → `first-release-readiness.md`
- Phase B correctness pass → `phase-b-correctness-pass.md`
- Phase C results → `phase-c-smoke-test-results.md`
- Prompt smoke tests → `prompt-smoke-tests.md`
- Music-theory audit rubric → `../../assets/music-theory-audit-rubric.md`
