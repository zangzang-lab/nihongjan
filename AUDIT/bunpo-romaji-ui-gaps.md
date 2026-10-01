# Bunpō Romaji UI Gap Audit

## Confirmed current gaps

### 1. Grammar pattern list/detail

Current GrammarRow and detail view call:

```tsx
<JapaneseText text={g.pattern}/>
```

without a reading/source anchor.

For N5/N4/N3 kanji-bearing patterns, this means Romaji cannot resolve safely from kanji alone.

Use the derived `grammar-readings.json` pattern anchor by grammar ID.

### 2. Grammar formation

Current formation view calls:

```tsx
<JapaneseText text={current.formation || "—"}/>
```

Formation strings mix placeholders and Japanese.

Example:

```
Verb-ます stem + 上げる
```

Do not pass the whole formula to a single reading prop.

Use a segment-aware formula renderer:

```
English placeholder
+
Japanese segment + reading + Romaji
```

Only Japanese segments receive the Romaji presentation.

### 3. Particle index

Current particle cards render:

```tsx
<h3 lang="ja">{p}</h3>
```

This bypasses global Romaji.

Use JapaneseText with a particle-aware reading map:

- は -> wa
- が -> ga
- を -> o
- に -> ni
- へ -> e
- で -> de
- と -> to
- も -> mo
- の -> no
- から -> kara
- まで -> made
- より -> yori
- や -> ya
- か -> ka
- ね -> ne
- よ -> yo

### 4. Conjugation reference labels

Current FORMS data renders:

```tsx
{f.label}<small lang="ja"> {f.jp}</small>
```

Use JapaneseText for the Japanese form labels.

Suggested readings:

- 辞書形 -> じしょけい
- ます形 -> ますけい
- て形 -> てけい
- た形 -> たけい
- ない形 -> ないけい
- なかった -> なかった
- 可能形 -> かのうけい
- 受身形 -> うけみけい
- 使役形 -> しえきけい
- 意向形 -> いこうけい
- 命令形 -> めいれいけい
- ば形 -> ばけい

### 5. Model verb conjugations

Current VERBS table renders raw Japanese forms:

```tsx
<strong>{v.forms[i]}</strong>
```

Attach an explicit reading array to each model verb and render:

```tsx
<JapaneseText text={v.forms[i]} reading={v.readings[i]}/>
```

This is deterministic and does not require sentence-level morphology.

### 6. Adjective models

Current ADJ table renders raw Japanese forms.

Attach explicit readings and use JapaneseText.

Examples:

- 高い -> たかい
- 高くない -> たかくない
- 高かった -> たかかった
- 高くなかった -> たかくなかった
- 高くて -> たかくて
- 高く -> たかく
- よくない -> よくない
- よかった -> よかった

- 静か -> しずか
- 静かだ -> しずかだ
- 静かです -> しずかです
- 静かではない -> しずかではない
- 静かじゃない -> しずかじゃない
- 静かだった -> しずかだった
- 静かではなかった -> しずかではなかった
- 静かで -> しずかで
- 静かな部屋 -> しずかなへや
- 静かに -> しずかに

### 7. Common mistakes

N4 has 12 common-mistake Japanese strings containing kanji.

These should not be passed through raw lang="ja" spans if the product requirement is truly "Romaji everywhere".

They need a derived reading anchor or a safe source ID.

Do not infer their readings from kanji at runtime.

## Priority

P0:
- grammar pattern Romaji
- formation segment renderer
- conjugation table
- adjective table

P1:
- particles
- common mistakes

## No canonical changes

This audit requires no canonical-data mutation.
