import re

import pytest

from aoc_2023.day_03 import (
    Point,
    collect_edges,
    collect_parts,
    collect_symbols,
    sum_gear_ratios,
    sum_parts,
)

SCHEMATIC = (
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
)


def test_collect_symbols():
    expected_symbols = {
        Point(1, 3),
        Point(3, 6),
        Point(4, 3),
        Point(5, 5),
        Point(8, 3),
        Point(8, 5),
    }
    assert collect_symbols(SCHEMATIC).keys() == expected_symbols


@pytest.mark.parametrize(
    ("row", "edges", "found"),
    (
        (
            "4..",
            {
                Point(-1, 1),
                Point(-1, 0),
                Point(-1, -1),
                Point(0, -1),
                Point(0, 0),
                Point(0, 1),
                Point(1, -1),
                Point(1, 0),
                Point(1, 1),
            },
            0,
        ),
        (
            "..114..",
            {
                Point(1, 1),
                Point(0, 1),
                Point(-1, 1),
                Point(-1, 2),
                Point(0, 2),
                Point(1, 2),
                Point(-1, 3),
                Point(0, 3),
                Point(1, 3),
                Point(-1, 4),
                Point(0, 4),
                Point(1, 4),
                Point(-1, 5),
                Point(1, 5),
                Point(0, 5),
            },
            0,
        ),
        (
            ".....+.58.",
            {
                Point(4, 6),
                Point(3, 6),
                Point(2, 6),
                Point(4, 7),
                Point(3, 7),
                Point(2, 7),
                Point(4, 8),
                Point(3, 8),
                Point(2, 8),
                Point(4, 9),
                Point(3, 9),
                Point(2, 9),
            },
            3,
        ),
    ),
)
def test_collect_edges(row, edges, found):
    match = re.search(r"\d+", row)
    assert collect_edges(match, found) == edges


def test_collect_parts():
    assert {
        value
        for values in collect_parts(collect_symbols(SCHEMATIC), SCHEMATIC).values()
        for value in values
    } == {467, 35, 633, 617, 592, 755, 664, 598}


def test_sum_parts():
    assert sum_parts(collect_parts(collect_symbols(SCHEMATIC), SCHEMATIC)) == 4361


def test_sum_gears():
    assert (
        sum_gear_ratios(collect_parts(collect_symbols(SCHEMATIC), SCHEMATIC)) == 467835
    )
