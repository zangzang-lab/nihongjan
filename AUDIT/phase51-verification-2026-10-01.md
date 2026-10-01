# NihongJan Phase 5.1 — Verification Report (2026-10-01)

## Source baseline
- Snapshot: `nihongjan(1).zip`
- SHA-256: `81338539442d187f52db8db2f31f8cf379dddbb8d6d83c6c55621dbdeec417f8`
- Verification performed against an exact extraction of that snapshot.
- Verified candidate patch applies cleanly with exit code 0.

## Verified PASS
- Derived sentence records: N5 1,381; N4 1,408; N3 3,826; total 6,615.
- Derived sentence ID integrity: no missing IDs; no extra IDs.
- Reviewed reading corrections: 138 unique IDs (N5 87 / N4 23 / N3 28).
- Candidate correction fields: only `reading` and `romaji` changed; Japanese source text unchanged.
- Derived Romaji punctuation normalization: full-width `？`, `！`, and `\u3000` removed from candidate sentence Romaji.
- Grammar pattern anchors: N5 9 / N4 26 / N3 51.
- Grammar formation coverage: 0 unmapped kanji-containing Japanese runs after validated common fragments, including `希望` in `ぜひ + request/希望`.
- Dokkai title anchors: N5 12 / N4 10 / N3 16; review-status titles remain gated off.
- N3 missing Dokkai token anchors: 7, all high-confidence and reading-backed.
- Grammar examples referenced by canonical grammar: 398 unique; all 398 exist in derived sentence assets.
- Modified TypeScript/TSX syntax: PASS under TypeScript 5.8.3 transpilation.
- Canonical safety: 0 unexpected changes outside the explicitly allowed derived/presentation paths.
- SRS/progress/history/tryout persistence source paths are untouched by the candidate patch.

## Fixed during verification
1. `loadRomajiSource()` previously routed `grammar-example-*` IDs to the grammar asset loader because of a broad `startsWith("grammar-")` check. It now routes only canonical `grammar-n[345]-<digits>` IDs to grammar assets; `grammar-example-*` continues through sentence assets.
2. The common grammar formula fragment map had `使役形` as `shieki`; corrected to `shiekikei`.
3. Added validated `希望 -> kibou` as a common mixed-formula fragment so the N4 `ぜひ + request/希望` formation resolves completely.
4. Normalized all candidate derived sentence Romaji full-width question/exclamation marks and full-width spaces.

## Remaining release blockers
- Full project `tsc --noEmit` cannot complete in this verification container because `node_modules` is absent and the snapshot references `vite/client`; the dependency install could not complete here.
- Browser verification has not been run in this environment.
- Mobile layout verification has not been run in this environment.
- Sentence-level morphology-aware particle conversion is not release-approved. Existing derived Romaji still contains conventional `ha/he/wo` in sentence strings where grammatical `は/へ/を` should be `wa/e/o`. Final production regeneration should use the project's intended Fugashi + Unidic + Pykakasi stack; no naive global replacement was applied.

## Historical document note
The GitHub staging branch contains an older `candidate_reading_changes: 117` manifest. The current verified candidate is the later reconciled 138-correction result documented in the v3 validation history and this report. The older manifest should be treated as historical, not as the current count.

## Phase gate
Phase 5.1 remains OPEN pending browser/mobile checks and final morphology-backed sentence Romaji regeneration/review. Choukai remains blocked.
