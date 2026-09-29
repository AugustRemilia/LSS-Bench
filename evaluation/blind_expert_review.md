# Blind Expert Review

Three experienced teachers independently reviewed **all 150 plans of the 24-turn
core stress test** (30 plans per design) under condition-blind review. Before
reviewing, they received brief training on a shared rubric that distinguished:

- negative cases in which learner-state memory led to an educationally
  unjustified instructional change; and
- positive cases in which learner-state memory appropriately supported
  personalized instruction.

For each case, reviewers examined the current learning evidence, the
learner-state information available to the tutoring system, and the resulting
teaching plan.

For the safety-oriented analysis reported with the paper, a case was treated as
expert-supported risk when at least one reviewer identified an educationally
unjustified memory-guided adjustment.

Aggregate results are reported in `results/expert_review_24turn_full.csv`. Under
the lenient criterion (at least one of three reviewers) the counts are 16, 16,
14, 20, and 0 for DMU, PCMU, ELMU, MPP, and CLEAR-Mem; under the majority
criterion (at least two of three) they are 14, 13, 12, 17, and 0. Agreement
across the 450 judgments was Fleiss' kappa = 0.749.

An earlier mixed sample of 154 cases (potential-risk cases and non-risk controls
drawn from the single-turn stress test and from the 24-turn core stress test) is
retained in `results/expert_review_summary.csv` for provenance only. It is not
the expert-validation result reported in the paper.

Item-level review files are not included in this candidate because reviewer
anonymization and release consent are not yet complete.
