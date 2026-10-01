import json
import pathlib
import re
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / 'src' / 'data'
JP_SCRIPT = re.compile(r'[\\u3040-\\u30ff\\u3400-\\u4dbf\\u4e00-\\u9fff々]')

def items(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    values = data if isinstance(data, list) else data.get('items', data)
    return values.values() if isinstance(values, dict) else values

def main():
    failures = []
    for level in ('n5', 'n4', 'n3'):
        vocab_examples = list(items(DATA / level / 'canonical' / f'{level}_vocab_examples.json'))
        grammar_examples = list(items(DATA / level / 'canonical' / f'{level}_grammar_examples.json'))
        canonical = {x['id']: x['japanese'] for x in vocab_examples + grammar_examples}
        derived = json.loads((DATA / 'derived' / f'{level}-sentences.json').read_text(encoding='utf-8'))
        missing = sorted(set(canonical) - set(derived))
        orphan = sorted(set(derived) - set(canonical))
        mismatch = sorted(k for k in canonical.keys() & derived.keys() if canonical[k] != derived[k].get('japanese'))
        unresolved = sorted(k for k, v in derived.items() if JP_SCRIPT.search(v.get('romaji', '')))
        punctuation = sum(v.get('romaji', '').count('？') + v.get('romaji', '').count('！') for v in derived.values())
        sequences = sum(any(token in v.get('romaji', '') for token in ('ha', 'he', 'wo')) for v in derived.values())
        print(f'{level.upper()}: canonical={len(canonical)} derived={len(derived)} missing={len(missing)} orphan={len(orphan)} mismatch={len(mismatch)} unresolved_japanese={len(unresolved)} fullwidth_punct={punctuation} ha_he_wo_candidate_records={sequences}')
        if missing or orphan or mismatch or unresolved:
            failures.append(level)
    if failures:
        raise SystemExit('FAIL: ' + ', '.join(failures))
    print('PASS: structural derived-Romaji audit')

if __name__ == '__main__':
    main()