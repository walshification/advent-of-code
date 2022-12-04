import pytest

from aoc_2022.day_04 import Assignment, assess, check_for_containment


@pytest.mark.parametrize(
    ("assignment", "expansion"), (("1-4", {1, 2, 3, 4}), ("3-3", {3}))
)
def test_assignments_expand(assignment, expansion):
    assignment = Assignment(assignment)
    assert assignment.sections == expansion


@pytest.mark.parametrize(
    ("pairs", "containment_count"),
    ((["1-2,3-4", "3-4,2-6"], 1), (["1-2,1-4", "3-4,2-6"], 2), (["1-2,3-4"], 0)),
)
def test_check_for_containment_counts_assignments_that_contain_their_pair(
    pairs, containment_count
):
    assessment_count, _ = assess(pairs)
    assert assessment_count == containment_count


@pytest.mark.parametrize(
    ("pairs", "overlapping_count"),
    ((["1-2,3-4", "3-4,2-6"], 1), (["1-2,2-4", "3-4,2-6"], 2), (["1-2,3-4"], 0)),
)
def test_check_for_overlapping_counts_assignments_that_overlap_at_all(
    pairs, overlapping_count
):
    _, assessment_count = assess(pairs)
    assert assessment_count == overlapping_count
