# Contributing

LSS-Bench version 0.1.0 is a controlled release candidate. Contributions
should preserve the benchmark's experimental structure and licensing
boundaries.

Before proposing a change:

1. do not add identifiable learner information, credentials, or raw API logs;
2. document the provenance and license of every added benchmark item;
3. keep development pilots separate from the five formal components;
4. update the release validator and tests when the schema or counts change; and
5. run `python3 -m lss_bench.validate` and `python3 -m pytest`.

Code contributions are accepted under Apache License 2.0. Contributions to the
benchmark data and evaluation materials are accepted under CC BY-SA 4.0.
