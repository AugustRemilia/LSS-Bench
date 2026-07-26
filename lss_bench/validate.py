"""Validate the public LSS-Bench component structure."""

from __future__ import annotations

import csv
import json
import sysconfig
from collections import Counter
from pathlib import Path

from lss_bench.catalog import COMPONENTS, Component


EXPECTED_DESIGNS = {"B0", "B1", "B2", "B3", "CLEAR"}
EXPECTED_CATEGORY_ROWS = 20


def _default_root() -> Path:
    source_root = Path(__file__).resolve().parents[1]
    if (source_root / "data").is_dir():
        return source_root

    installed_root = Path(sysconfig.get_path("data")) / "share" / "lss-bench"
    if (installed_root / "data").is_dir():
        return installed_root

    return Path.cwd()


REPO_ROOT = _default_root()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _read_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{path}:{line_number}: {exc}") from exc
    return rows


def _read_rows(path: Path) -> list[dict]:
    return _read_csv(path) if path.suffix == ".csv" else _read_jsonl(path)


def _require_fields(
    rows: list[dict],
    fields: set[str],
    label: str,
    errors: list[str],
) -> None:
    if not rows:
        return
    missing = fields - set(rows[0])
    if missing:
        errors.append(f"{label}: missing fields {sorted(missing)}")


def _validate_single_turn(
    component: Component,
    rows: list[dict],
    errors: list[str],
) -> None:
    _require_fields(
        rows,
        {
            "probe_id",
            "scenario_category",
            "category_type",
            "subject_domain",
            "problem_text",
            "student_answer",
            "current_evidence_summary",
            "teacher_goal",
            "risk_profile_artifact",
            "expected_safe_plan",
            "expected_risky_plan",
        },
        component.key,
        errors,
    )
    ids = [row.get("probe_id", "") for row in rows]
    if len(set(ids)) != len(ids):
        errors.append(f"{component.key}: probe_id values are not unique")


def _validate_multi_turn(
    component: Component,
    root: Path,
    family_rows: list[dict],
    errors: list[str],
) -> None:
    assert component.turn_file
    assert component.checkpoint_file
    turn_path = root / component.turn_file
    checkpoint_path = root / component.checkpoint_file
    for path in (turn_path, checkpoint_path):
        if not path.is_file():
            errors.append(f"{component.key}: missing {path.relative_to(root)}")
            return

    turn_rows = _read_rows(turn_path)
    checkpoint_rows = _read_rows(checkpoint_path)
    if len(turn_rows) != component.expected_turn_rows:
        errors.append(
            f"{component.key}: expected {component.expected_turn_rows} turn rows, "
            f"found {len(turn_rows)}"
        )
    if len(checkpoint_rows) != component.expected_checkpoint_rows:
        errors.append(
            f"{component.key}: expected {component.expected_checkpoint_rows} checkpoint rows, "
            f"found {len(checkpoint_rows)}"
        )

    _require_fields(
        family_rows,
        {"family_id", "category", "subject_domain", "grade_band"},
        f"{component.key} families",
        errors,
    )
    _require_fields(
        turn_rows,
        {
            "session_family_id",
            "scenario_category",
            "turn_index",
            "problem_or_event_text",
        },
        f"{component.key} turns",
        errors,
    )
    _require_fields(
        checkpoint_rows,
        {"session_family_id", "checkpoint_turn", "condition_id"},
        f"{component.key} checkpoints",
        errors,
    )

    family_ids = {row["family_id"] for row in family_rows}
    turns_by_family = Counter(row["session_family_id"] for row in turn_rows)
    checkpoint_families = {row["session_family_id"] for row in checkpoint_rows}
    if set(turns_by_family) != family_ids:
        errors.append(f"{component.key}: family and turn manifests do not align")
    if checkpoint_families != family_ids:
        errors.append(f"{component.key}: family and checkpoint manifests do not align")

    expected_turn_count = component.expected_turn_rows // component.expected_units
    if set(turns_by_family.values()) != {expected_turn_count}:
        errors.append(f"{component.key}: each family must contain {expected_turn_count} turns")

    designs = {row["condition_id"] for row in checkpoint_rows}
    if designs != EXPECTED_DESIGNS:
        errors.append(
            f"{component.key}: expected designs {sorted(EXPECTED_DESIGNS)}, "
            f"found {sorted(designs)}"
        )
    checkpoint_turns = {int(row["checkpoint_turn"]) for row in checkpoint_rows}
    if checkpoint_turns != set(component.checkpoint_turns):
        errors.append(
            f"{component.key}: expected checkpoint turns {component.checkpoint_turns}, "
            f"found {sorted(checkpoint_turns)}"
        )


def validate_release(root: Path = REPO_ROOT) -> list[str]:
    errors: list[str] = []
    for component in COMPONENTS:
        unit_path = root / component.unit_file
        if not unit_path.is_file():
            errors.append(f"{component.key}: missing {component.unit_file}")
            continue
        rows = _read_rows(unit_path)
        if len(rows) != component.expected_units:
            errors.append(
                f"{component.key}: expected {component.expected_units} units, found {len(rows)}"
            )
        if component.test_format == "single_turn":
            _validate_single_turn(component, rows, errors)
        else:
            _validate_multi_turn(component, root, rows, errors)

    mapping_path = root / "data/category_mapping.csv"
    if not mapping_path.is_file():
        errors.append("missing data/category_mapping.csv")
    else:
        mapping = _read_csv(mapping_path)
        if len(mapping) != EXPECTED_CATEGORY_ROWS:
            errors.append(
                f"category mapping: expected {EXPECTED_CATEGORY_ROWS} rows, found {len(mapping)}"
            )
        public_ids = [row["paper_category_id"] for row in mapping]
        if len(public_ids) != len(set(public_ids)):
            errors.append("category mapping: paper_category_id values are not unique")

    expected_plan_total = sum(component.expected_plans for component in COMPONENTS)
    if expected_plan_total != 2190:
        errors.append(f"catalog: expected 2,190 plans, found {expected_plan_total}")
    return errors


def main() -> int:
    errors = validate_release()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("LSS-Bench validation passed: 5 components, 2,190 expected teaching plans.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
