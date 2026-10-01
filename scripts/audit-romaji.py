"""Audit derived N5/N4/N3 sentence Romaji without modifying canonical content.

This script intentionally performs deterministic structural checks only. Japanese
semantic reading correctness still requires human/native review for flagged cases.
"""

from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
DERIVED = ROOT / "src/data/derived"
LEVELS = ("n5", "n4", "n3")
JP_LETTER = re.compile(r"[ぁ-ゖァ-ヺ㐀-䶿一-鿿々]")


def load(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    failures = 0
    print("# NihongJan derived Romaji audit")

    for level in LEVELS:
        data = load(DERIVED / f"{level}-sentences.json")
        missing = []
        japanese_left = []
        invalid_ids = []
        fullwidth_punctuation = []

        for sid, row in data.items():
            if not all(row.get(k) for k in ("japanese", "reading", "romaji")):
                missing.append(sid)
            if JP_LETTER.search(row.get("romaji", "")):
                japanese_left.append((sid, row["romaji"]))
            if "？" in row.get("romaji", "") or "！" in row.get("romaji", ""):
                fullwidth_punctuation.append(sid)
            if not (
                sid.startswith(f"example-{level}-")
                or sid.startswith(f"grammar-example-{level}-")
            ):
                invalid_ids.append(sid)

        print(f"{level.upper()}: {len(data)} records")
        print(f"  missing fields: {len(missing)}")
        print(f"  Japanese letters left in Romaji: {len(japanese_left)}")
        print(f"  full-width ?/! still in Romaji: {len(fullwidth_punctuation)}")
        print(f"  unexpected source IDs: {len(invalid_ids)}")

        if missing or japanese_left or invalid_ids:
            failures += 1

        if japanese_left:
            print("  Japanese-text samples:")
            for item in japanese_left[:10]:
                print("   ", item)

        if fullwidth_punctuation:
            print("  punctuation samples:")
            for sid in fullwidth_punctuation[:10]:
                print("   ", sid, data[sid]["romaji"])

    unresolved = (
        load(DERIVED / "unresolved.json")
        if (DERIVED / "unresolved.json").exists()
        else []
    )
    print(f"unresolved reading records listed by generator: {len(unresolved)}")
    return failures


if __name__ == "__main__":
    raise SystemExit(main())
