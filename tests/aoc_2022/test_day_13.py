import pytest

from aoc_2022.day_13 import compare, validate


@pytest.mark.parametrize(
    ("left", "right", "result"), (([3], [5], True), ([5], [3], False)),
)
def test_validate_compares_numbers(left, right, result):
    assert validate(left, right) == result
