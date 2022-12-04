import pytest

from aoc_2022.day_04 import Assignment


@pytest.mark.parametrize(("assignment", "expansion"), (("1-4", "1234"), ("3-3", "3")))
def test_assignments_expand(assignment, expansion):
    assignment = Assignment(assignment)
    assert assignment.sections == expansion
