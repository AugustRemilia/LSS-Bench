# Aggregate Results

`educational_risk_rates.csv` reports risk counts and rates among the risk cases
in each formal component. `valid_personalization.csv` reports correct handling
of the 88 positive cases. `expert_review_summary.csv` reports the 154-case
priority-review sample; `expert_review_24turn_full.csv` reports the fully
confirmed 24-turn core stress test (all 150 plans), which is the expert-validation
result reported in the manuscript.

The expert-review set contained 154 mixed potential-risk and non-risk cases.
Counts by design are reported for identified risks; the file does not imply an
equal review denominator for every design.

## Lineage (2026-09-20)

`educational_risk_rates.csv` reports the benchmark labelling layer and is
unchanged: the 24-turn core stress rows remain the rule-based / LLM-assisted
values (70.0%, 63.3%, 73.3%, 73.3%, and 0.0% for CLEAR-Mem).

**Independent expert review was extended to full coverage of that component.**
All 150 plans of the 24-turn core stress test were judged by three experienced
teachers under condition-blind review, so for this component the review is a full
confirmation rather than a sample (see `expert_review_summary.csv` and the
manuscript's blind-expert-review subsection). The manuscript reports the benchmark
labelling layer as its main result and uses the expert review as an independent
validation of the pattern, so that all five components remain comparable.

`expert_review_summary.csv` reports both criteria: 105 of 154 reviewed cases
flagged under the lenient rule (>=1 of 3 reviewers) and 68 under the majority
rule (>=2 of 3). The long-turn portion of that sample was re-reviewed with
corrected materials; the earlier v1 aggregation (119 of 154) is superseded.
No CLEAR-Mem case was flagged under either criterion.

## Full coverage of the 24-turn component (2026-09-21)

`expert_review_24turn_full.csv` reports the review of **all 150 plans** of the
24-turn core stress test (30 per design), judged by three teachers working
independently under condition-blind review. Under the lenient criterion
(>=1 of 3 reviewers) the counts are 16, 16, 14, 20, and 0; under the majority
criterion (>=2 of 3) they are 14, 13, 12, 17, and 0. This table, not the
154-case sample, carries the manuscript's expert-validation result.

## Earlier pilot review (2026-09-21)

The retained-reviewer file also contains **62 single-turn high-pressure cases**
(`source = S-High q60`) from an **earlier pilot review** of the benchmark's
case-construction and diagnostic rules. They are retained to document how those
rules were iterated and checked with teachers. They contain **no CLEAR-Mem
plans**, so they cannot support the headline comparison, and they are **not part
of the expert-validation results reported in the manuscript**, which rest on the
fully confirmed 24-turn core stress test (all 150 plans, with all 30 CLEAR-Mem
plans confirmed free of expert-identified risk). The counts for these 62 cases
are preserved here for provenance and are not a separate reported result.

These aggregate tables are aligned with the current paper. Generated
teaching-plan text and item-level expert labels are intentionally excluded from
this public candidate until redistribution, anonymization, and consent checks
are complete.
