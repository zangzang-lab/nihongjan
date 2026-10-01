# NihongJan Project-Wide Romaji Rule Matrix (Expanded)

Romaji is a learner-facing reading aid. The canonical Japanese and canonical readings remain the source of truth; Romaji is derived/presentation data.

## 1. Hepburn consonant mapping
- し -> shi
- ち -> chi
- つ -> tsu
- ふ -> fu
- じ -> ji
Do not fall back to Kunrei spellings such as si/ti/tu/hu/zi.

## 2. Yōon / contracted kana
Preserve kya/kyu/kyo, sha/shu/sho, cha/chu/cho, nya/nyu/nyo, hya/hyu/hyo, mya/myu/myo, rya/ryu/ryo and legitimate loanword combinations (fa/fi/fe/fo, va/vi/ve/vo, she, che, je, ti, di, wi, we, etc.).

## 3. Sokuon っ / ッ
Render geminate consonants from the following sound: kitte, zasshi, issho, matcha, kotchi.
A standalone っ at utterance end must not become tsu. Example: あっ currently becomes atsu and requires a special/manual rule.

## 4. Moraic ん
Use n by default. Insert an apostrophe before a following vowel or y when needed for separation: ten'in, hon'yaku, shin'etsu.
Do not insert apostrophes randomly.

## 5. Grammatical particles
Use wa/e/o for は/へ/を only when they are grammatical particles. This must be token/POS-aware, never a character-wide replacement.

## 6. Long vowels
For the current NihongJan UI, keep the existing ASCII-friendly style for this phase: kyou, shuu, oneesan, otousan, etc. Do not mix macrons into only some records.
The project may consider a future explicit macron migration separately.

## 7. Punctuation
Preserve punctuation semantics. Normalize derived presentation width only: ？ -> ?, ！ -> !, full-width space -> ASCII space.
Centered dot ・ is punctuation/symbol, not unresolved Japanese script.

## 8. Word division
Romanized Japanese is easier to read with word boundaries, and formal cataloging guidance uses spaces between words. However, do not insert spaces between every morphological token.
Until reliable Japanese word segmentation is implemented, do not perform a mass spacing rewrite. Keep the existing project style consistent rather than mixing spaced and unspaced records.

## 9. Irregular lexical readings
Do not derive an irregular word from its individual kanji. Use the validated lexical reading.
Examples in this dataset include お兄さん=おにいさん, お姉さん=おねえさん, お父さん=おとうさん, お母さん=おかあさん, 一昨日=おととい, 一昨年=おととし, 二十歳=はたち, 八つ=やっつ.

## 10. Context-sensitive kanji readings
A kanji can have multiple valid readings. Use the reading appropriate to the sentence sense.
Examples discovered in the current dataset: 行った=いった when meaning 'went'; 開く may be あく or ひらく depending on sense; 今日中=きょうじゅう; お腹が空いた/空きました uses すく/すいた in the hungry sense.

## 11. Counters and calendar expressions
Handle irregular counters/dates explicitly and contextually: 一日=いちにち/ついたち, 二日=ふつか, 四日=よっか, 七日=なのか, 八つ=やっつ, 二十歳=はたち, 三羽=さんわ, 二羽=にわ.
Do not assume the numeric kanji's basic reading is correct inside a counter expression.

## 12. Rendaku / compound voicing
Compound readings must preserve voiced sounds where lexicalized. A confirmed example is 曜日=び inside the weekday compounds: かようび, きんようび, げつようび, すいようび, もくようび, どようび, にちようび.

## 13. Numerals and counters
Arabic numerals in the Japanese source are a separate high-risk area. A derived Romaji line must not pretend that 10年, 50万円, 12月, 6個, etc. are fully phonetic if the numeric reading has not been resolved.
These records go to a dedicated numeric-reading review queue rather than being silently converted by a simplistic digit-to-word map.

## 14. Foreign/loanword and chōonpu handling
Keep katakana loanword pronunciation consistent: taxi-like long vowels remain in the project's current ASCII convention, and prolonged sound marks must not become stray Japanese characters in the Romaji field.
Validate combinations such as -tion/foreign syllable approximations rather than relying on English spelling.

## 15. Proper names
Japanese names and places need their validated reading. Do not infer readings from kanji alone. Existing Latin-script names should remain Latin text.

## 16. Assessment safety
Romaji may be shown when it does not reveal an answer. Hide it for reading/orthography/pronunciation/listening items when it directly exposes the tested answer.

## 17. Canonical boundary
Never add Romaji to frozen canonical content merely to make rendering easier. Never use Romaji for SRS identity, question identity, or scoring.

## 18. External reference baseline

The Library of Congress 2022 Japanese Romanization Table uses modified Hepburn, specifies an apostrophe before a following vowel or y after a syllabic n, and states that romanized Japanese generally uses spaces between words. NihongJan is not a bibliographic catalog, so these rules are used as a reference baseline rather than copied blindly into the UI.

Source: https://www.loc.gov/catdir/cpso/romanization/japanese.pdf
