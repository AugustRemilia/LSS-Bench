"""Canonical component catalog for the public LSS-Bench candidate."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Component:
    key: str
    test_format: str
    test_type: str
    unit_file: str
    expected_units: int
    expected_plans: int
    turn_file: str | None = None
    expected_turn_rows: int | None = None
    checkpoint_file: str | None = None
    expected_checkpoint_rows: int | None = None
    checkpoint_turns: tuple[int, ...] = ()


COMPONENTS = (
    Component(
        key="single_turn_coverage",
        test_format="single_turn",
        test_type="coverage",
        unit_file="data/single_turn/coverage/items.csv",
        expected_units=180,
        expected_plans=900,
    ),
    Component(
        key="single_turn_stress",
        test_format="single_turn",
        test_type="stress",
        unit_file="data/single_turn/stress/items.csv",
        expected_units=60,
        expected_plans=300,
    ),
    Component(
        key="multi_turn_coverage_16",
        test_format="multi_turn",
        test_type="coverage",
        unit_file="data/multi_turn/coverage_16turn/families.jsonl",
        expected_units=30,
        expected_plans=600,
        turn_file="data/multi_turn/coverage_16turn/turns.jsonl",
        expected_turn_rows=480,
        checkpoint_file="data/multi_turn/coverage_16turn/checkpoints.csv",
        expected_checkpoint_rows=600,
        checkpoint_turns=(4, 8, 12, 16),
    ),
    Component(
        key="multi_turn_stress_16",
        test_format="multi_turn",
        test_type="stress",
        unit_file="data/multi_turn/stress_16turn/families.jsonl",
        expected_units=12,
        expected_plans=240,
        turn_file="data/multi_turn/stress_16turn/turns.jsonl",
        expected_turn_rows=192,
        checkpoint_file="data/multi_turn/stress_16turn/checkpoints.csv",
        expected_checkpoint_rows=240,
        checkpoint_turns=(4, 8, 12, 16),
    ),
    Component(
        key="multi_turn_core_stress_24",
        test_format="multi_turn",
        test_type="core_stress",
        unit_file="data/multi_turn/core_stress_24turn/families.jsonl",
        expected_units=5,
        expected_plans=150,
        turn_file="data/multi_turn/core_stress_24turn/turns.csv",
        expected_turn_rows=120,
        checkpoint_file="data/multi_turn/core_stress_24turn/checkpoints.csv",
        expected_checkpoint_rows=150,
        checkpoint_turns=(4, 8, 12, 16, 20, 24),
    ),
)
