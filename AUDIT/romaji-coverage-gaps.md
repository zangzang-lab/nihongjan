# Phase 5.1 Romaji Coverage Gaps

This is a coverage audit for the goal of showing Romaji throughout Japanese learning content.

## N3 Bunpō pattern/formula gap

The canonical N3 grammar dataset has 182 grammar records.

The current JapaneseText calls in GrammarHub do not receive reading/sourceId for the grammar pattern and formation strings.

Therefore any kanji-bearing pattern/formula cannot resolve sentence Romaji from the current derived sentence assets.

Counts:

- 51 N3 grammar patterns contain kanji.
- 50 N3 grammar formation strings contain kanji.

Examples:

- 上げる
- 合う
- 別に～ない
- 中
- 気味
- 一度に
- 一方だ
- 一体
- 代わりに
- 結果
- 結局
- 決して～ない
- 切れない
- 切る
- 込む
- 向け
- 向き
- 直す
- に違いない
- に反して
- に関する / に関して
- に比べて
- に慣れる
- に対して
- を中心に
- を込めて
- を通じて / を通して
- 際に
- 最中に
- 確かに
- 例えば
- ても構わない
- と共に
- 途中で / 途中に
- 通す
- 上で
- 上に
- 割に
- ような気がする
- ように見える

The canonical grammar records do not currently contain a dedicated reading field for these patterns/forms.

### Safe solution

Create a derived grammar-reading asset keyed by canonical grammar ID and field:

- grammar pattern
- grammar formation

Do not add Romaji or reading fields to the canonical grammar dataset.

The derived asset should be populated from validated Japanese readings, not from a character-only kanji converter.

## N3 Dokkai token gap

The N3 reading source has 16 passages.

Seven kanji-bearing tokens currently have no reading:

| Passage | Token |
|---|---|
| n3-p1 | 行く |
| n3-p2 | 行く |
| n3-p3 | 入れて |
| n3-p4 | 入って |
| n3-p6 | 思う |
| n3-p6 | 物 |
| n3-p6 | 人 |

These tokens therefore cannot reliably display Romaji through JapaneseText because JapaneseText intentionally does not infer readings from kanji.

### Safe solution

Provide validated token readings in a derived Dokkai-reading layer or through existing source readings where available.

Do not guess at runtime.

Do not weaken JapaneseText to infer kanji readings from the kanji string.

## N4 Dokkai

All 906 N4 Dokkai tokens containing kanji currently have a reading.

## N5 Dokkai

The N5 reading-data token audit found no kanji-bearing token calls without a supplied reading.

## Dokkai titles

All 10 N4 and all 16 N3 Dokkai titles contain Japanese kanji but currently have no dedicated reading field.

N5 title data also contains Japanese titles without a separate reading field.

These titles currently render through JapaneseText without a sourceId/reading, so they do not reliably expose Romaji for kanji-bearing titles.

### Safe solution

Treat Dokkai titles as a separate derived-reading asset if the product requirement is truly "Romaji everywhere".

Do not infer title readings from kanji at runtime.

## Decision boundary

This coverage gap is intentionally separate from sentence Romaji quality.

A sentence can have perfect Romaji data while a grammar pattern or Dokkai title still lacks the reading anchor needed to display it.

The project-wide Romaji architecture should therefore have:

canonical Japanese content
→ validated reading anchor
→ derived Romaji
→ shared JapaneseText renderer

rather than:

canonical Japanese content
→ guess reading from kanji
→ Romaji

## No canonical changes

This audit does not modify:

- canonical N5/N4/N3 vocabulary
- canonical N5/N4/N3 kanji
- canonical N5/N4/N3 examples
- canonical N5/N4/N3 grammar
- canonical N5/N4/N3 grammar examples

Choukai remains blocked.
