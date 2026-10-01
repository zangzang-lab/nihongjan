# Legacy Romaji Usage Audit

## Active learner paths

The current active N5/N4/N3 learning modules use canonical loaders under:

- src/data/n5/vocab.ts
- src/data/n4/vocab.ts
- src/data/n3/vocab.ts
- src/data/n5/kanji.ts
- src/data/n4/kanji.ts
- src/data/n3/kanji.ts
- src/data/dokkai-model.ts
- src/components/shared/japanese-text.tsx

These are the paths that matter for the project-wide Romaji presentation system.

## Legacy/static Romaji fields

The repository also contains older/static structures with explicit Romaji fields:

- src/data/n4/index.ts
- src/data/n3/index.ts
- src/data/tryout-pool.ts
- src/lib/nihongjan-data.ts
- src/data/kanji-data.ts
- src/data/schema/legacy.ts
- src/data/kana-data.ts

Some are still consumed indirectly, some only for legacy compatibility, and some are historical/static representations.

## Important finding

Do NOT migrate every explicit legacy Romaji field into the new global presentation layer.

First determine whether it is:

1. active learner-facing content;
2. required by a current compatibility path; or
3. dead/legacy code.

For active canonical Japanese content, prefer the shared JapaneseText / derived reading architecture.

## Current specific consumers

- n4/index.ts and n3/index.ts are referenced by their level Dokkai adapters.
- n4/vocab.ts and n3/vocab.ts are the active Kotoba sources used by the level modules.
- tryout-pool.ts uses TryoutWord typing for pools built from current level vocabulary.
- lib/nihongjan-data.ts feeds exam-pools.ts as a legacy/static pool.

## Cleanup rule

Do not delete legacy Romaji fields during Phase 5.1.

Once active consumers are fully confirmed, legacy cleanup can be a separate post-Phase-5.1 task.