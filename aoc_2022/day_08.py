"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted
carefully in a grid. The Elves explain that a previous expedition
planted these trees as a reforestation effort. Now, they're curious if
this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree
house hidden. To do this, you need to count the number of trees that are
visible from outside the grid when looking directly along a row or
column.

The Elves have already launched a quadcopter to generate a map with the
height of each tree (your puzzle input).

Each tree is represented as a single digit whose value is its height,
where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of
the grid are shorter than it. Only consider trees in the same row or
column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they
are already on the edge, there are no trees to block the view.

Consider your map; how many trees are visible from outside the grid?
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Grid:
    """Your basic Cartesian grid."""

    grid: List[List[int]]

    @classmethod
    def from_rows(cls, rows: List[str]) -> "Grid":
        return cls([[int(i) for i in row] for row in rows])