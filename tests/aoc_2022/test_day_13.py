import pytest

from aoc_2022.day_13 import compare, validate


def test_compare_returns_sum_of_valid_indexes():
    assert compare(
        [
            [[3], [5]],
            [[5], [3]],
            [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]],
            [[1, 1, 5, 1, 1], [1, 1, 3, 1, 1]],
        ]
    ) == 4


@pytest.mark.parametrize(
    ("left", "right", "result"), (([3], [5], True), ([5], [3], False))
)
def test_validate_compares_numbers(left, right, result):
    assert validate(left, right) == result


@pytest.mark.parametrize(
    ("left", "right", "result"),
    (
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], True),
        ([1, 1, 5, 1, 1], [1, 1, 3, 1, 1], False)
    ),
)
def test_validate_continues_comparing_if_equal(left, right, result):
    assert validate(left, right) == result


@pytest.mark.parametrize(("left", "right"), (([1], [[2]]), ([[1]], [2])))
def test_validate_fixes_mixed_types(left, right):
    assert validate(left, right) == True
