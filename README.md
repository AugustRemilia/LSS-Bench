# LSS-Bench

LSS-Bench (Learner-State Stress Benchmark) is a structured benchmark for
testing educational risks introduced by persistent learner-state memory in LLM
tutoring systems. It evaluates the teaching plan produced after learner-state
information has been stored, maintained, retrieved, and used.

The benchmark asks two complementary questions:

1. Does stored learner information cause an educationally unjustified change
   that is unsupported by current learning evidence or inappropriate for the
   current instructional context?
2. Does the system preserve valid, evidence-supported personalization while
   controlling those risks?

## Status

Version 0.1.0 is the first private release candidate aligned with the current
paper methodology. It contains the five formal benchmark components, aggregate
reported results, licensing, and citation metadata. Raw API logs, development
pilots, identifiable reviewer files, and model-generated teaching-plan text
are excluded. The remaining checks before public release are tracked in
[RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md).

## Formal Components

| Component | Benchmark units | Plan checkpoints under five designs | Teaching plans |
|---|---:|---:|---:|
| Single-turn coverage | 180 items | Final plan | 900 |
| Single-turn stress | 60 items | Final plan | 300 |
| 16-turn coverage | 30 scenario families | Turns 4, 8, 12, and 16 | 600 |
| 16-turn stress | 12 scenario families | Turns 4, 8, 12, and 16 | 240 |
| 24-turn core stress | 5 scenario families | Turns 4, 8, 12, 16, 20, and 24 | 150 |

Together, the formal experiments produce 2,190 teaching plans.

## Memory-Management Designs

The paper evaluates the same benchmark item under five controlled designs:

- **DMU:** direct memory use;
- **PCMU:** prompt-cautioned memory use;
- **ELMU:** evidence-linked memory use;
- **MPP:** memory-prioritized planning; and
- **CLEAR-Mem:** claim construction, admission, revision, context selection,
  and instructional-use authorization.

LSS-Bench can also be applied to other tutoring systems. An external system
receives the same learning task, current evidence, instructional context, and
learner-state memory, then produces a teaching plan for assessment under the
common criteria in [`evaluation/criteria.md`](evaluation/criteria.md).

## Data Layout

```text
data/
  single_turn/
    coverage/items.csv
    stress/items.csv
  multi_turn/
    coverage_16turn/
    stress_16turn/
    core_stress_24turn/
evaluation/
  criteria.md
  blind_expert_review.md
results/
  educational_risk_rates.csv
  valid_personalization.csv
  expert_review_summary.csv
lss_bench/
  catalog.py
  validate.py
```

The source manifests retain several internal artifact fields for exact
traceability. These fields are not intended as general educational terminology.
Use [`data/category_mapping.csv`](data/category_mapping.csv) for the
reader-facing taxonomy.

## Validate the Release

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
python3 -m lss_bench.validate
python3 -m pytest
```

The validator checks file presence, record counts, family and checkpoint
structure, condition coverage, and category mappings.

## Data Source and Privacy

The initial mathematics scenarios were developed from the public MathDial
dataset and were extended by the research team to additional subjects and
learner-state memory risks. Released cases contain no identifiable learner
information. Identity-related and other sensitive cases are synthetic stress
tests, not records of real students.

LSS-Bench is not a naturalistic classroom corpus. Its stress-test rates must not
be interpreted as the prevalence of memory failures in ordinary classrooms.

See [DATA_CARD.md](DATA_CARD.md), [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md),
and [LICENSES/README.md](LICENSES/README.md) before redistribution.

## Related System

[CLEAR-Mem](https://github.com/AugustRemilia/CLEAR-Mem) is the companion
reference implementation evaluated with this benchmark.

## Citation

Use the metadata in [`CITATION.cff`](CITATION.cff) to cite this benchmark
release. The accompanying paper will be added as a preferred citation after
publication metadata are available.

## Licenses

The validation code is licensed under the
[Apache License 2.0](LICENSE). Benchmark data and evaluation materials are
licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International License](LICENSES/CC-BY-SA-4.0.txt).
See [LICENSES/README.md](LICENSES/README.md) and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the file-level scope and
MathDial attribution.
