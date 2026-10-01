# Romaji Style Rules — Phase 5.1

## Scope

Romaji is a presentation/derived layer. It does not belong in frozen canonical vocabulary, kanji, grammar, example, or grammar-example records.

## Base style

Keep the current project Hepburn-style conversion for lexical readings.

Do not introduce a second romanization convention.

## Grammatical particles

For sentence-level learner-facing pronunciation:

- `は` as a grammatical particle -> `wa`
- `へ` as a grammatical particle -> `e`
- `を` as a grammatical particle -> `o`

These replacements must be token/POS aware. They must not be applied to arbitrary characters inside words.

## Punctuation

Use ASCII presentation punctuation in the Romanized line where the existing project output maps Japanese punctuation directly:

- `？` -> `?`
- `！` -> `!`

Preserve meaningful punctuation itself; only normalize its representation.

## Sentence integrity

Completed sentence Romaji must not contain unresolved Japanese kana or kanji.

Punctuation and symbols may remain when they are intentional punctuation/symbols rather than Japanese script.

## Assessment safety

Romaji is hidden when it would directly reveal the answer, especially for reading, orthography, pronunciation, and answer-equivalent listening tasks.

Global Romaji preference does not override answer-leak protection.

## Canonical data protection

Never add or mutate canonical Romaji fields merely to support the presentation layer.
