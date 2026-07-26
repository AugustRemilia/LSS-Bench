# Benchmark Data

## Single-Turn Components

Each row in `single_turn/*/items.csv` contains a learning task, learner
response, current learning evidence, instructional context, learner-state
memory views, and expected safe and risky planning paths. The coverage file has
180 items; the stress file has 60.

The CSV files preserve several implementation-facing columns from the formal
experiment artifacts. In particular, names beginning with `clear_` describe
the executable test representation and are not proposed as general
learner-modeling terminology.

## Multi-Turn Components

Each multi-turn directory contains:

- `families.jsonl`: one record per scenario family;
- `turns.jsonl` or `turns.csv`: the complete 16- or 24-turn history; and
- `checkpoints.csv`: one planning request per family, checkpoint, and
  memory-management design.

The condition identifiers `B0`, `B1`, `B2`, and `B3` are artifact identifiers
for DMU, PCMU, ELMU, and MPP. `CLEAR` identifies CLEAR-Mem. Reader-facing risk
and positive-case identifiers are defined in `category_mapping.csv`.

## Record Counts

Run `python3 -m lss_bench.validate` from the repository root. The validator
checks all formal counts and the expected five-design checkpoint structure.
