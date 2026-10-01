import { toRomaji } from "wanakana";

export type DerivedSentence = { japanese: string; reading: string; romaji: string };

const sentences = new Map<string, DerivedSentence>();
const pending = new Map<string, Promise<void>>();
const cache = new Map<string, string>();
const kanji = /[\u3400-\u9fff々]/u;

const loaders: Record<string, () => Promise<Record<string, DerivedSentence>>> = {
  n5: () => import("@/data/derived/n5-sentences.json").then(m => m.default),
  n4: () => import("@/data/derived/n4-sentences.json").then(m => m.default),
  n3: () => import("@/data/derived/n3-sentences.json").then(m => m.default),
};

/** Keep derived Romaji learner-facing punctuation consistent without touching canonical Japanese. */
function normalizeDerivedRomaji(value: string): string {
  return value.replaceAll("？", "?").replaceAll("！", "!").replaceAll("　", " ");
}

/** Sentence assets are loaded only when a visible sentence requests its level. */
export function loadSentenceReading(sourceId: string): Promise<void> | undefined {
  const level = /(?:^|[-_])(n[345])(?:[-_]|$)/i.exec(sourceId)?.[1]?.toLowerCase();

  if (!level || !loaders[level]) return undefined;

  if (!pending.has(level)) {
    pending.set(
      level,
      loaders[level]().then(rows => {
        for (const [id, row] of Object.entries(rows)) sentences.set(id, row);
      }),
    );
  }

  return pending.get(level);
}

/** No reading is inferred from kanji. Unknown sentences stay without Romaji. */
export function resolveRomaji(
  text: string,
  reading?: string,
  sourceId?: string,
): string | undefined {
  if (sourceId) {
    const record = sentences.get(sourceId);

    if (
      record?.japanese === text &&
      !kanji.test(record.reading) &&
      !kanji.test(record.romaji)
    ) {
      return normalizeDerivedRomaji(record.romaji);
    }

    return undefined;
  }

  if (
    !reading ||
    kanji.test(reading) ||
    !/[\u3040-\u30ff]/u.test(reading)
  ) {
    return undefined;
  }

  if (!cache.has(reading)) cache.set(reading, toRomaji(reading));
  return cache.get(reading);
}

/** Assessment text may be romanized only when the task does not test its sound or spelling. */
export function hideAssessmentRomaji(
  instruction: string,
  answer: string,
  text: string,
  reading?: string,
  listening = false,
): boolean {
  if (
    listening ||
    /reading|orthography|pronunciation|select the kana|select the romaji|kanji reading/i.test(
      instruction,
    )
  ) {
    return true;
  }

  const romanized = reading ? resolveRomaji(text, reading) : undefined;
  return Boolean(
    romanized &&
      romanized.toLowerCase().replace(/[^a-z]/g, "") ===
        answer.toLowerCase().replace(/[^a-z]/g, ""),
  );
}
