# Source Provenance

## Lineage (2026-09-20)

The benchmark labelling layer reported in `results/educational_risk_rates.csv`
is unchanged. Independent expert review was extended to **full coverage of the
24-turn core stress test**: all 150 plans were judged by three teachers under
condition-blind review. `results/expert_review_summary.csv` was updated from the
v1 aggregation (119 of 154) to the re-reviewed counts (105 of 154 lenient,
68 of 154 majority); no CLEAR-Mem case was flagged under either criterion.

This candidate was assembled from
`CLEAR/benchmarks/lss_bench_release_candidate_20260615` and reconciled with the
current methodology and results chapters on 2026-07-26.

Included formal components:

- single-turn coverage (`v34`, 180 items);
- single-turn stress (`v35 q60`, 60 items);
- 16-turn coverage (`L-Coverage`, 30 families);
- 16-turn stress (`L-Qualification`, 12 families); and
- 24-turn core stress (`L-High core`, 5 families); and
- the complete teaching plans for the four cases shown in Table 11 of the
  accompanying paper, under `data/multi_turn/core_stress_24turn/case_plans/`.

Excluded:

- the `v36` development pilot;
- diagnostic 24-turn subsets outside the formal core;
- raw API responses, errors, retries, and internal condition keys;
- LLM-assisted diagnostic labels for the remaining released components, and
  model-generated plan text other than the four released case plans;
- item-level reviewer files and internal reviewer identifiers; and
- development notes, self-check reports, and superseded result summaries.

Aggregate result tables were reconstructed from the current paper values and
checked against the chapter source. They should be regenerated from the final
public item-level release before the v1.0 tag.
