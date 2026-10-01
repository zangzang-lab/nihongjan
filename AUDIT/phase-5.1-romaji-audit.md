# Phase 5.1 Romaji Audit

## Source snapshot

Latest uploaded application snapshot:

- ZIP: `nihongjan(1).zip`
- SHA-256: `81338539442d187f52db8db2f31f8cf379dddbb8d6d83c6c55621dbdeec417f8`
- Audit date: 2026-10-01

The full application ZIP is being treated as the authoritative local snapshot for this zero-Lovable-credit audit. This clean GitHub repository currently contains the audit/patch workspace; the application ZIP itself is not being rewritten or uploaded as a binary source tree in this step.

## Derived sentence assets

| Level | Records | Missing fields | Japanese letters in Romaji | Full-width ?/! before | Full-width ?/! after |
|---|---:|---:|---:|---:|---:|
| N5 | 1,381 | 0 | 0 | 202 | 0 |
| N4 | 1,408 | 0 | 0 | 8 | 0 |
| N3 | 3,826 | 0 | 0 | 8 | 0 |
| **Total** | **6,615** | **0** | **0** | **218** | **0** |

The full-width punctuation count above is character-count based. The affected-record count before normalization was 204.

The earlier N3 `・` finding was a false positive from the audit regex: U+30FB is punctuation, not kana/kanji. No Japanese letters remain in the current Romaji fields after using a letters-only Japanese-script check.

## Safe changes made in the local snapshot

### Derived data punctuation

Only the derived sentence assets were normalized for presentation punctuation:

- `？` -> `?`
- `！` -> `!`
- full-width space -> ASCII space

No canonical data was changed.

### Runtime presentation

`src/lib/romaji.ts` now normalizes derived Romaji punctuation at presentation time as an additional safety layer.

### Generator

`scripts/derive-romaji.py` now uses the morphological token POS to normalize grammatical particles safely:

- particle `は` -> `wa`
- particle `へ` -> `e`
- particle `を` -> `o`

The override is applied only when the token's major POS is `助詞` (particle), so lexical strings such as `はやく` are not incorrectly rewritten.

## Important rejected approach

A character-only heuristic for replacing every `は`, `へ`, or `を` produced false positives (for example, lexical `はやく`). That approach was rejected.

Do not bulk-rewrite the existing 6,615 records with a character-only heuristic.

The safe path is:

1. keep canonical Japanese and canonical readings frozen;
2. use the existing morphological reading pipeline;
3. apply particle pronunciation overrides only at particle-token level;
4. regenerate the derived assets in an environment with the existing Fugashi/Unidic/Pykakasi dependencies;
5. re-run structural validation.

## Remaining work

- Regenerate N5/N4/N3 derived Romaji using the corrected token-aware generator in an environment with its declared Python dependencies.
- Review unresolved/ambiguous Japanese reading cases from the regenerated assets.
- Browser verification for N4/N3.
- Mobile verification.
- Full TimedQuiz/Tryout smoke verification.
- Final Phase 5.1 acceptance after the above passes.

Choukai remains blocked until Phase 5.1 is complete.
