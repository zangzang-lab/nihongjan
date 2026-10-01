# Non-Particle Romaji Findings — Phase 5.1

The Romaji audit is broader than は/へ/を.

## High-confidence families found in the current N5/N4/N3 derived sentence layer

### 1. Irregular lexical readings
Examples requiring correction:
- お兄さん -> おにいさん
- お姉さん -> おねえさん
- お父さん -> おとうさん
- お母さん -> おかあさん
- 一昨日 -> おととい
- 一昨年 -> おととし
- 二十歳 -> はたち
- 八つ -> やっつ

### 2. Context-sensitive kanji readings
Examples:
- 行った -> いった when the meaning is "went"
- 今日中 -> きょうじゅう
- 空く -> すく when meaning "become less crowded"
- 被る -> かぶる when meaning "put on/wear"
- 表 -> おもて in paper/box "front/outer side"
- 米 -> こめ in rice context
- 管 -> くだ in the attached "pipe" vocabulary sense
- 縁 -> ふち in edge/border context
- 直に -> じかに in "directly" context
- 停留所 -> ていりゅうじょ
- 仏 -> ほとけ in Buddha context

### 3. Rendaku / compound voicing
A recurring confirmed failure is 曜日:
- かようび
- きんようび
- げつようび
- すいようび
- もくようび
- どようび
- にちようび

The current derived layer repeatedly produced ようひ.

This is not a particle problem; it is lexical compound reading/voicing.

### 4. Counters and calendar expressions
Confirmed correction families include:
- 二日 -> ふつか
- 四日 -> よっか
- 七日 -> なのか
- 六日間 -> むいかかん
- 三羽 -> さんわ
- 二羽 -> にわ
- 六個 -> ろっこ
- 一回 -> いっかい
- 十分 (10 minutes) -> じっぷん / じゅっぷん
- 十人 -> じゅうにん
- 十年 -> じゅうねん
- 二十歳 -> はたち
- 七十五日 -> ななじゅうごにち
- 十四日 -> じゅうよっか

The current generator often preserved digits in the reading field or selected an incorrect basic numeral reading.

### 5. Numeric expressions
Examples in the current dataset requiring explicit reading resolution:
- ６個
- 10年
- 30センチ
- 20センチ
- 5メートル
- １回
- 70メートル
- 2メートル
- 第２課
- 10時
- ７時
- ８時
- 3月
- 7色
- 3時
- 2時
- 1日に2回
- 12月
- 10度
- 3度
- 20度
- 10分
- 10人

Never treat a numeric character as proof that the pronunciation is its basic Sino-Japanese reading.

### 6. Sokuon / small っ
The audit found:
- legitimate gemination that must remain correct
- a true special case: standalone あっ was converted to atsu

Do not change あっ to an invented tsu reading. It requires an interjection-specific representation.

### 7. Moraic ん
The audit found recurring n-before-vowel/y boundaries.

The current derived output already uses apostrophes in many cases, but not consistently before y.

For a modified-Hepburn baseline, an apostrophe is used before a following vowel or y when needed to disambiguate the syllabic n.

Examples needing review include:
- kin'yōbi-style boundaries
- kon'ya-style boundaries
- shashin'yo-style boundaries
- hanbun'... boundaries

This should be implemented by phonological/token-aware rules, not by blind `n` string replacement.

### 8. Long vowels
The current NihongJan style remains ASCII-friendly for this phase:
- kyou
- shuu
- oneesan
- otousan

Do not mix macrons into only some records.

### 9. Word division
The existing derived sentences are largely unspaced.

A formal romanization baseline uses spaces between words, but a safe Japanese segmentation policy is required before mass spacing is introduced.

Do not perform a blanket whitespace rewrite during Phase 5.1.

### 10. Loanwords / chōonpu
Katakana loanword readings must preserve prolonged-vowel semantics without leaving Japanese kana in the Romaji output.

Review rather than blindly converting every long sound mark.

## Current risk counts

N5 / N4 / N3 derived sentence assets currently contain:

| Pattern | N5 | N4 | N3 |
|---|---:|---:|---:|
| sokuon in reading | 173 | 274 | 413 |
| moraic n before vowel/y | 36 | 34 | 47 |
| full-width punctuation in Romaji | 200 records | 2 records | 2 records |
| digits remaining in reading | 23 | 1 | 5 |
| Kunrei-style si/ti/tu/hu/zi | 0 | 0 | 0 |

These are audit/risk counts, not confirmed error counts.

## High-confidence semantic corrections already identified

The first reviewed set contains 110 high-confidence sentence-reading corrections after excluding ambiguous alternate-reading cases.

Do not treat the remaining alternate-reading queue as errors.

Known alternate-reading cases intentionally remain in review, including:
- 昨夜
- 毎月
- 毎年
- 明日
- 日本
- 年月
- 市場
- 身体
- 工場
- 球
- 描く
- 注ぐ
- 得る
- 方々
- 居る
- 悪口

These can have multiple valid Japanese readings and must not be overwritten just because the generator selected a different valid reading.

## Reference baseline

Library of Congress, Japanese Romanization Table (2022):
https://www.loc.gov/catdir/cpso/romanization/japanese.pdf

The reference specifies modified Hepburn and an apostrophe between syllables when a preceding syllable ends in n and the following syllable begins with a vowel or y; it also provides word-division guidance.

NihongJan may adapt presentation details for a learner UI, but it should not mix incompatible romanization conventions casually.
