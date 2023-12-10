"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the
gondola lift will take you up to the water source, but this is as far as
he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a
problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't
working right now; it'll still be a while before I can fix it." You
offer to help.

The engineer explains that an engine part seems to be missing from the
engine, but nobody can figure out which one. If you can add up all the
part numbers in the engine schematic, it should be easy to work out
which part is missing.

The engine schematic (your puzzle input) consists of a visual
representation of the engine. There are lots of numbers and symbols you
don't really understand, but apparently any number adjacent to a symbol,
even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

What is the sum of all of the part numbers in the engine schematic?
"""
import re
from collections import namedtuple
from typing import Dict, List, Sequence, Set

Point = namedtuple("Point", ("x", "y"))


def collect_symbols(schematic: Sequence[str]) -> Dict[Point, List[str]]:
    return {
        Point(x, y): []
        for x in range(len(schematic))
        for y in range(len(schematic))
        if schematic[x][y] not in "0123456789."
    }


def collect_parts(
    symbols: Dict[Point, List[str]], schematic: Sequence[str]
) -> Dict[Point, List[str]]:
    for x, row in enumerate(schematic):
        for number in re.finditer(r"\d+", row):
            edges = collect_edges(number, x)
            for point in edges & symbols.keys():
                symbols[point].append(number.group())

    return symbols


def collect_edges(number: re.Match, found: int) -> Set[Point]:
    return {
        Point(x, y)
        for x in (found - 1, found, found + 1)
        for y in range(number.start() - 1, number.end() + 1)
    }


def sum_parts(parts_map: Dict[Point, List[str]]) -> int:
    return sum(int(part) for parts in parts_map.values() for part in parts)


if __name__ == "__main__":
    with open("aoc_2023/inputs/day_03.txt") as data:
        schematic = tuple(line for line in data)

    print(f"Part 1: {sum_parts(collect_parts(collect_symbols(schematic), schematic))}")
