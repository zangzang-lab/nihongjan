# Phase 5.1 — Final Patch Specification

This document is the handoff for the final implementation step. The current application snapshot already contains the major Phase 5.1 Romaji work.

## Do not touch

- Frozen N5/N4/N3 canonical vocabulary, kanji, vocabulary examples, grammar, and grammar examples.
- Current SRS identities, timing, progress, history, Tryout attempt persistence, and level routing.

## Already implemented in the newest snapshot

- Global Romaji toggle in src/components/shared/japanese-text.tsx.
- Shared JapaneseText renderer.
- Dokkai passage token rendering through JapaneseText.
- Kanji onyomi/kunyomi rendering through JapaneseText.
- Review Center Kotoba rendering through JapaneseText.
- TimedQuiz answer-sensitive Romaji policy.
- Tryout answer-sensitive Romaji policy.

## Remaining implementation candidates

### A. Derived sentence presentation normalization

Scope: src/data/derived/n5-sentences.json, n4-sentences.json, n3-sentences.json.

Safe normalization only:

- ？ -> ?
- ！ -> !
- full-width space -> ASCII space

No Japanese sentence or reading may change.

### B. Offline generator pronunciation rule

Scope: scripts/derive-romaji.py.

Use the existing Fugashi token POS to render grammatical particles:

- particle は -> wa
- particle へ -> e
- particle を -> o

Never perform character-wide replacement.

Regenerate derived assets only in an environment that has the project's existing Fugashi + Unidic + Pykakasi dependencies.

### C. Runtime presentation safety

Optional hardening: normalize derived Romaji punctuation in src/lib/romaji.ts before display.

Do not change sentence data at runtime.

### D. Dokkai comprehension questions

Current prompt/choices use suppressRomaji unconditionally.

Do NOT loosen this automatically. First audit the question types. Only expose Romaji where it cannot reveal the answer. If question semantics are unknown, keeping Romaji suppressed is safer than leaking the answer.

### E. Browser/mobile verification

Required before closing Phase 5.1:

- N5, N4, N3 Kotoba smoke test.
- N5, N4, N3 Kanji smoke test.
- N5, N4, N3 Bunpō smoke test.
- N5, N4, N3 Dokkai smoke test.
- N5, N4, N3 TimedQuiz semantic Romaji test.
- N5, N4, N3 Tryout semantic Romaji test.
- mobile viewport smoke test.

## Preferred execution order

1. Run audit-romaji.py.
2. Apply safe derived punctuation normalization.
3. Regenerate derived Romaji only when the morphology environment is available.
4. Re-run audit-romaji.py.
5. Run browser tests.
6. Only then consider any Lovable patch for a real code defect.

## Credit policy

Do not spend Lovable credits generating or reviewing the 6,615 derived records. Data work belongs in the audit/staging flow.

Lovable should only be used for a concrete UI/runtime defect that cannot be applied safely through the repository.