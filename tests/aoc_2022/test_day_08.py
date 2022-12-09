from aoc_2022.day_08 import Grid


def test_can_make_a_grid():
    rows = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]
    grid = Grid.from_rows(rows)

    assert grid.grid[0][0] == 3
    assert grid.grid[1][3] == 1
    assert grid.grid[len(rows) - 1][len(rows) - 1] == 0
