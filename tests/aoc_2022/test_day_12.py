from textwrap import dedent

import pytest

from aoc_2022.day_12 import Cell, Terrain


@pytest.mark.parametrize(
    ("start", "end", "can_move"),
    (("a", "a", True), ("a", "b", True), ("a", "c", False), ("z", "a", True)),
)
def test_cells_can_compare_heights(start, end, can_move):
    start = Cell(0, 0, start)
    end = Cell(0, 1, end)
    assert start ^ end == can_move


def test_terrain_can_be_made():
    terrain = Terrain.from_input((("S", "a", "b"), ("c", "d", "E")))

    assert terrain.start == terrain[0, 0]
    assert terrain.end == terrain[1, 2]

    assert terrain[0, 0].height == "S"
    assert terrain[0, 1].height == "a"
    assert terrain[0, 2].height == "b"
    assert terrain[1, 0].height == "c"
    assert terrain[1, 1].height == "d"
    assert terrain[1, 2].height == "E"

    assert terrain[3, 0] is None
    assert terrain[0, 3] is None

    assert str(terrain) == dedent("S a b\n" "c d E")
