# Source Provenance

This candidate was assembled from
`CLEAR/benchmarks/lss_bench_release_candidate_20260615` and reconciled with the
current methodology and results chapters on 2026-07-26.

Included formal components:

- single-turn coverage (`v34`, 180 items);
- single-turn stress (`v35 q60`, 60 items);
- 16-turn coverage (`L-Coverage`, 30 families);
- 16-turn stress (`L-Qualification`, 12 families); and
- 24-turn core stress (`L-High core`, 5 families).

Excluded:

- the `v36` development pilot;
- diagnostic 24-turn subsets outside the formal core;
- raw API responses, errors, retries, and internal condition keys;
- LLM-assisted diagnostic labels and model-generated plan text pending
  redistribution review;
- item-level reviewer files and internal reviewer identifiers; and
- development notes, self-check reports, and superseded result summaries.

Aggregate result tables were reconstructed from the current paper values and
checked against the chapter source. They should be regenerated from the final
public item-level release before the v1.0 tag.
