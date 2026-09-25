# Full 24-turn high-pressure set (8 scenario families)

This directory contains the **complete** 24-turn high-pressure scenario set:
8 families spanning risk categories LH1, LH2, LH4, LH5, LH6, LH7 and LH8.

## Relation to the core subset used in the paper

The manuscript reports the 24-turn core stress test using a **5-family subset**
(`data/multi_turn/core_stress_24turn/`), selected from these 8 families:

| family_id | category | in core subset |
|---|---|---|
| LHH-STALE-CS-LOOP | LH2 | yes |
| LHH-AFFECT-CS-FRUSTRATION | LH6 | yes |
| LHH-SENSITIVE-GEO-LANGUAGE | LH7 | yes |
| LHH-WRONGOWNER-FRACTIONS | LH8 | yes |
| LHH-CROSSSESSION-PHYSICS | LH8 | yes |
| LHH-LOCKIN-WRITE-TEMPLATE | LH1 | no |
| LHH-LAUNDER-MATH-SLOPE | LH4 | no |
| LHH-SELFEDIT-ALGEBRA | LH5 | no |

The subset was chosen because these families show the clearest and most stable
differences among the designs, which makes them the most informative basis for
comparison. **The remaining families are not discarded**; they are retained here
as the full 24-turn set.

## Contents

`families.jsonl` provides, for each family, the scenario definition: subject
domain, grade band, the learner-state risk mechanism targeted, the risk event,
the delayed task, the counter-evidence event, and the expected safe and risky
instructional paths.

Generated teaching-plan text and item-level expert labels are intentionally not
included in this public candidate, pending redistribution, anonymization and
consent checks (see `results/README.md`).
