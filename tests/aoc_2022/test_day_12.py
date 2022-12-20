import pytest

from aoc_2022.day_12 import Cell


@pytest.mark.parametrize(
    ("start", "end", "can_move"),
    (("a", "a", True), ("a", "b", True), ("a", "c", False), ("z", "a", True)),
)
def test_cells_can_compare_heights(start, end, can_move):
    start = Cell(0, 0, start)
    end = Cell(0, 1, end)
    assert start ^ end == can_move
