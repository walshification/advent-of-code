from textwrap import dedent

import pytest

from aoc_2022.day_12 import Cell, Dijkstra, Terrain


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

    assert terrain[0, 0].north == None
    assert terrain[0, 0].east == terrain[0, 1]
    assert terrain[0, 0].south == terrain[1, 0]
    assert terrain[0, 0].west == None

    assert terrain[1, 2].north == terrain[0, 2]
    assert terrain[1, 2].east == None
    assert terrain[1, 2].south == None
    assert terrain[1, 2].west == terrain[1, 1]

    assert terrain.start.links == (terrain[0, 1],)

    assert terrain[1, 0].links == (terrain[0, 0], terrain[1, 1])


def test_dijkstra_can_walk_the_terrain():
    terrain = Terrain.from_input(
        (
            ("S", "a", "b", "q", "p", "o", "n", "m"),
            ("a", "b", "c", "r", "y", "x", "x", "l"),
            ("a", "c", "c", "s", "z", "E", "x", "k"),
            ("a", "c", "c", "t", "u", "v", "w", "j"),
            ("a", "b", "d", "e", "f", "g", "h", "i"),
        )
    )
    dijkstra = Dijkstra()
    assert dijkstra.walk(terrain) == 31
