from lss_bench.catalog import COMPONENTS
from lss_bench.validate import validate_release


def test_release_structure_is_valid():
    assert validate_release() == []


def test_formal_plan_total_matches_paper():
    assert sum(component.expected_plans for component in COMPONENTS) == 2190
