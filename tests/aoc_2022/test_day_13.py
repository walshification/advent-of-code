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


@pytest.mark.parametrize(
    ("left", "right", "result"), (([], [1], True), ([1], [], False))
)
def test_validate_items_run_out(left, right, result):
    assert validate(left, right) == result


def test_part_one():
    pairs = [
        [
            [1,1,3,1,1],
            [1,1,5,1,1],
        ],  # 1
        [
            [[1],[2,3,4]],
            [[1],4],
        ],  # 2
        [
            [9],
            [[8,7,6]],
        ],
        [
            [[4,4],4,4],
            [[4,4],4,4,4],
        ],  # 4
        [
            [7,7,7,7],
            [7,7,7],
        ],
        [
            [],
            [3],
        ],  # 6
        [
            [[[]]],
            [[]],
        ],
        [
            [1,[2,[3,[4,[5,6,7]]]],8,9],
            [1,[2,[3,[4,[5,6,0]]]],8,9],
        ],
    ]
    assert compare(pairs) == 13  # 1 + 2 + 4 + 6
