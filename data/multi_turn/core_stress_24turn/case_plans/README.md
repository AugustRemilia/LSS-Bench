# Case plans shown in Table 11

`teaching_plans_cases.jsonl` contains the complete teaching plans for the four
representative risk cases displayed in Table 11 of the accompanying paper: four
scenario families of the 24-turn core stress test, each at the checkpoint used
in that table, under all five designs.

| Case (category, subject) | family_id | checkpoint | plans |
|---|---|---|---|
| Loop debugging (MT-R4, computer science) | `LHH-STALE-CS-LOOP` | T24 | B0, B1, B2, B3, CLEAR |
| Debugging after frustration (MT-R1, computer science) | `LHH-AFFECT-CS-FRUSTRATION` | T12 | B0, B1, B2, B3, CLEAR |
| Contour map reading (MT-R7, geography) | `LHH-SENSITIVE-GEO-LANGUAGE` | T24 | B0, B1, B2, B3, CLEAR |
| Fraction addition (MT-R8, mathematics) | `LHH-WRONGEOWNER-FRACTIONS` | T24 | B0, B1, B2, B3, CLEAR |

Conditions map to the paper as follows: `B0` = DMU, `B1` = PCMU, `B2` = ELMU,
`B3` = MPP, `CLEAR` = CLEAR-Mem.

Each record carries `plan_id` (`<family>:<condition>:T<checkpoint>`), the
family and condition identifiers, the checkpoint turn, and the full `plan`
object with the fields `diagnosis`, `instructional_goal`, `support_level`,
`next_teacher_move`, `uses_learner_state`, and `cited_evidence_ids`.

Checkpoints were fixed on 2026-09-19 under the cumulative criterion: for MT-R4,
MT-R7, and MT-R8 the four comparison designs all carry a risk judgment at T24; for
MT-R1, T12 is the only checkpoint at which all four comparison designs are judged
risky. CLEAR-Mem has no risk judgment at any checkpoint of any of the four
cases. These plans are the model outputs underlying Table 11; they carry no
reviewer material and no personal data.
