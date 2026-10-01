"""Offline derived reading asset; never modifies canonical source files.
Requires fugashi + unidic-lite + pykakasi for regeneration. Inspect output before release.
"""

import json
import pathlib
import sys

sys.path.insert(0, "/tmp/jp-reading")

import fugashi
from pykakasi import kakasi

root = pathlib.Path(__file__).resolve().parents[1] / "src/data"

tagger = fugashi.Tagger()
converter = kakasi()

records = {}
unresolved = []

PARTICLE_ROMAJI = {"は": "wa", "へ": "e", "を": "o"}
PUNCT_REPLACEMENTS = {"？": "?", "！": "!"}


def token_romaji(token):
    """Romanize one morphological token while respecting particle pronunciation."""
    surface = token.surface

    if getattr(token.feature, "pos1", None) == "助詞" and surface in PARTICLE_ROMAJI:
        return PARTICLE_ROMAJI[surface]

    kana = token.feature.kana or surface
    return "".join(x["hepburn"] for x in converter.convert(kana))


for level in ("n5", "n4", "n3"):
    canon = root / level / "canonical"

    for filename in (
        f"{level}_vocab_examples.json",
        f"{level}_grammar_examples.json",
    ):
        data = json.loads((canon / filename).read_text())

        for item in data if isinstance(data, list) else data["items"]:
            text = item["japanese"]
            tokens = list(tagger(text))
            reading = "".join(t.feature.kana or t.surface for t in tokens)
            romaji = "".join(token_romaji(t) for t in tokens)
            romaji = "".join(PUNCT_REPLACEMENTS.get(ch, ch) for ch in romaji)

            if any("\u3400" <= c <= "\u9fff" for c in reading + romaji):
                unresolved.append(
                    {"id": item["id"], "text": text, "reading": reading}
                )
            else:
                records[item["id"]] = {
                    "reading": reading,
                    "romaji": romaji,
                    "japanese": text,
                }

    output = {
        k: v
        for k, v in records.items()
        if k.startswith((f"example-{level}", f"grammar-example-{level}"))
    }
    (root / "derived" / f"{level}-sentences.json").write_text(
        json.dumps(output, ensure_ascii=False, separators=(",", ":")) + "\n"
    )

(root / "derived" / "unresolved.json").write_text(
    json.dumps(unresolved, ensure_ascii=False, indent=2) + "\n"
)

print("resolved", len(records), "unresolved", len(unresolved))
