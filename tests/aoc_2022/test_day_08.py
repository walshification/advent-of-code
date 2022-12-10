import pytest

from aoc_2022.day_08 import Grid


def test_can_make_a_grid():
    rows = (
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    )
    grid = Grid.from_rows(rows)

    assert grid.grid[0][0] == 3
    assert grid.grid[1][3] == 1
    assert grid.grid[len(rows) - 1][len(rows) - 1] == 0


def test_grid_can_count_the_perimeter():
    rows = (
        "313",
        "202",
        "653",
    )
    grid = Grid.from_rows(rows)

    assert grid.count_visible() == 8


@pytest.mark.parametrize(
    "rows",
    (
        ("999", "019", "999"),
        ("999", "910", "999"),
        ("909", "919", "999"),
        ("999", "919", "909"),
    ),
)
def test_grid_checks_visibility(rows):
    grid = Grid.from_rows(rows)
    assert grid.count_visible() == 9


def test_grid_checks_skips_tree_if_not_visible():
    rows = (
        "9999",
        "0109",
        "9009",
        "9999",
    )
    grid = Grid.from_rows(rows)

    assert grid.count_visible() == 13


def test_grid_checks_skips_tree_already_counted():
    rows = (
        "9099",
        "0100",
        "9009",
        "9099",
    )
    grid = Grid.from_rows(rows)

    assert grid.count_visible() == 13


def test_grid_checks_sees_taller_trees_behind_tall_trees():
    rows = (
        "9999",
        "0129",
        "9009",
        "9999",
    )
    grid = Grid.from_rows(rows)

    assert grid.count_visible() == 14


def test_grid_resets_sight_lines_for_top_and_bottom_on_further_rows():
    rows = (
        "9909",
        "9019",
        "9009",
        "9999",
    )
    grid = Grid.from_rows(rows)

    assert grid.count_visible() == 13


def test_count_visible():
    rows = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]
    grid = Grid.from_rows(rows)
    assert grid.count_visible() == 21
