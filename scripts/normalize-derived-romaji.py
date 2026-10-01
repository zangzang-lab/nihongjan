import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DERIVED = ROOT / 'src' / 'data' / 'derived'
LEVELS = ('n5', 'n4', 'n3')
REPLACEMENTS = str.maketrans({'？': '?', '！': '!', '　': ' '})

def main():
    changed = 0
    for level in LEVELS:
        path = DERIVED / f'{level}-sentences.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        level_changed = 0
        for row in data.values():
            old = row.get('romaji', '')
            new = old.translate(REPLACEMENTS)
            if new != old:
                row['romaji'] = new
                level_changed += 1
        if level_changed:
            path.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
        changed += level_changed
        print(f'{level.upper()}: {level_changed} derived records normalized')
    print(f'TOTAL: {changed} derived records normalized')

if __name__ == '__main__':
    main()