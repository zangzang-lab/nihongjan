# Phase 5.1 — Final Patch Specification

This is the final handoff for the implementation step. The newest application snapshot already contains the major Phase 5.1 Romaji architecture.

## Do not touch

- Frozen N5/N4/N3 canonical vocabulary, kanji, vocabulary examples, grammar, and grammar examples.
- Current SRS identities, timing, progress, history, Tryout attempt persistence, and level routing.

## Already implemented in newest snapshot

- Global Romaji toggle in `src/components/shared/japanese-text.tsx`.
- Shared `JapaneseText` renderer.
- Dokkai passage token rendering through `JapaneseText`.
- Kanji onyomi/kunyomi rendering through `JapaneseText`.
- Review Center Kotoba rendering through `JapaneseText`.
- TimedQuiz answer-sensitive Romaji policy.
- Tryout answer-sensitive Romaji policy.
- Kotoba meaning/example reveal rules.

Do not ask Lovable to rebuild any of these unless browser verification demonstrates a real regression.

## Remaining data work

### A. Reviewed reading corrections

A zero-credit audit identified 117 high-confidence candidate corrections to derived sentence readings:

- N5: 65
- N4: 23
- N3: 29

These corrections are derived-data candidates only.

They must be applied to the derived reading/Romaji layer, never to the frozen canonical datasets.

### B. Broader Romaji rule families

The audit covers more than particles:

1. Hepburn consonants
2. yōon / contracted sounds
3. sokuon / gemination
4. moraic ん and apostrophe disambiguation
5. grammatical particles は/へ/を
6. long-vowel convention
7. punctuation normalization
8. word-boundary formatting
9. irregular lexical readings
10. context-sensitive kanji readings
11. counters and calendar expressions
12. rendaku / compound voicing
13. numerals and counters
14. foreign/loanword and chōonpu handling
15. proper names
16. assessment safety
17. canonical data boundary

See `AUDIT/romaji-rule-matrix-expanded.md`.

### C. Derived sentence punctuation

The newest snapshot currently contains full-width `？`/`！` in the derived Romaji layer:

- N5: 193 characters across 191 records
- N4: 2 characters across 2 records
- N3: 2 characters across 2 records
- total: 197 characters across 195 records

Safe normalization:

- `？` -> `?`
- `！` -> `!`
- full-width spaces -> ASCII spaces

This does not change canonical Japanese.

## Sentence-reading regeneration

The existing generator uses:

- Fugashi
- Unidic
- Pykakasi

Do not replace that stack with a naive character converter.

Do not run a character-wide particle replacement.

The safe generator strategy is token-aware:

- particle は -> wa
- particle へ -> e
- particle を -> o

and must preserve lexical は/へ/を inside words.

Regenerate derived Romaji only when the intended morphology dependencies are available.

## Important semantic examples

Known context-sensitive cases include:

- 行った -> いった when meaning 'went'
- 行う -> おこなう
- 一日 -> いちにち or ついたち depending on context
- 今日中 -> きょうじゅう
- 空く -> すく in the 'become less crowded' sense
- 被る -> かぶる in the 'put on/wear' sense
- 二十歳 -> はたち
- 三羽 -> さんわ
- 二羽 -> にわ
- 曜日 -> び inside weekday compounds

Do not force an alternate reading merely because a different reading is also valid.

## Dokkai questions

The current Dokkai question model contains English/context questions and choices. The existing `suppressRomaji` behavior must not be loosened blindly.

Keep answer-leak protection.

Only expose Romaji in a Dokkai assessment item when the content and question semantics prove that it cannot reveal the answer.

## Runtime code candidate

One safe hardening candidate is:

`src/lib/romaji.ts`

Normalize derived presentation punctuation before returning a derived Romaji string.

This is optional if the derived assets themselves are normalized and tests prove the UI is clean.

Do not add AI/API/runtime sentence generation.

## Browser/mobile verification

Required before Phase 5.1 can close:

- N5 Kotoba / Kanji / Bunpō / Dokkai / TimedQuiz / Tryout
- N4 same smoke tests
- N3 same smoke tests
- Romaji ON/OFF
- Furigana ON/OFF
- answer-leak protection
- SRS
- refresh/resume
- mobile layout

## Credit-saving rule

Do not spend Lovable credits on:

- sentence data generation
- broad Romaji audits
- canonical-data audits
- rule discovery
- repository-wide refactors

Do those in the audit/staging workflow.

Lovable should be used only for the final browser verification or a concrete UI/runtime defect that cannot be safely patched through the repository.

## Current phase gate

Phase 5.1 is still OPEN.

Choukai remains blocked until:

- derived Romaji quality is accepted
- remaining code paths are verified
- N5/N4/N3 browser checks pass
- mobile checks pass
- canonical datasets remain untouched
