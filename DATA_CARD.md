# LSS-Bench Data Card

## Summary

LSS-Bench evaluates whether persistent learner-state memory leads an LLM
tutoring system to propose educationally unjustified instruction and whether
valid personalization remains available.

## Composition

The release candidate contains:

- 180 single-turn coverage items;
- 60 single-turn stress items;
- 30 sixteen-turn coverage families;
- 12 sixteen-turn stress families; and
- 5 twenty-four-turn core stress families.

Risk cases cover unsupported or overgeneralized learner judgments, outdated
state, lost observation conditions, fixed learning paths, misuse of sensitive
or support information, and cross-session or cross-learner memory. Positive
cases test the preservation of justified strategy, format, language,
accessibility, and teacher-confirmed support, as well as the correct updating or
retirement of outdated state.

## Construction

The initial mathematics material was developed from MathDial. The research team
adapted and extended the material to construct memory-specific tests in
mathematics, science, computing, and other instructional contexts. Stress cases
increase conflict between stored memory and current evidence, extend the memory
history, or increase the potential instructional effect.

## Privacy

The public candidate contains no identifiable learner information. Sensitive
and identity-related content is synthetic and exists only to test whether a
system misuses such information.

## Evaluation

Each benchmark item is run under one or more memory-management designs while
the learning task, current evidence, instructional context, model backend, and
checkpoint schedule are held constant.

The primary risk criterion is an educationally unjustified memory-guided
adjustment: stored learner information changes the proposed instruction, while
the learner's current evidence and instructional context do not support that
change. Valid personalization is assessed separately.

Selected plans undergo blind review by three experienced teachers using a
shared rubric.

## Intended Uses

- Evaluate memory-related instructional risks in LLM tutoring systems.
- Compare learner-state memory-management methods.
- Examine long-horizon memory maintenance and reuse.
- Test whether risk controls preserve valid personalization.

## Out-of-Scope Uses

- Estimating classroom incident rates.
- Assessing real learners.
- Making demographic or psychological claims.
- Treating the benchmark as a general measure of tutoring quality.
- Treating internal artifact fields as an educational ontology.

## Known Limitations

- The scenarios are controlled benchmark constructions rather than live
  classroom interactions.
- The reported experiments use a single LLM backend.
- The current public candidate omits generated plan text pending a final
  redistribution review.
- Item-level expert labels remain pending anonymization and release consent.

## License and Attribution

Benchmark data, evaluation materials, aggregate results, and this data card are
licensed under CC BY-SA 4.0. The initial mathematics material was developed
from MathDial and subsequently adapted and extended for learner-state memory
testing. Users must retain the MathDial attribution in
`THIRD_PARTY_NOTICES.md`, identify modifications where applicable, and
distribute adaptations under compatible ShareAlike terms.
