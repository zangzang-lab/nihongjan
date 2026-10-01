# Candidate Derived Romaji Patch v2

Source application snapshot:
- ZIP: nihongjan(1).zip
- SHA-256: 81338539442d187f52db8db2f31f8cf379dddbb8d6d83c6c55621dbdeec417f8

Candidate package:
- file: NihongJan_Phase5.1_Candidate_Derived_Romaji_v2.zip
- SHA-256: 3cc352cd198681046ec32154506acea9d4e84d5ee3e3f2b54e8b3f3b1a7ad06d

Scope:
- derived sentence assets only
- 110 reviewed reading overrides
  - N5: 64
  - N4: 23
  - N3: 23
- Romaji regenerated locally from corrected kana readings for staging validation
- no canonical content included
- no UI/runtime production source included

Validation:
- N5 derived records: 1,381
- N4 derived records: 1,408
- N3 derived records: 3,826
- no missing derived records
- no Japanese kana/kanji remains in candidate Romaji fields under structural validation

Important:
This is a candidate staging artifact, not a production-approved data release. Final production sentence regeneration should use the project's intended morphology stack when available, and Japanese review remains required.
