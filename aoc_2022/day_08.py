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
from dataclasses import dataclass, field
from typing import Dict, Set, Tuple


@dataclass(frozen=True)
class Grid:
    """Your basic Cartesian grid."""

    height: int
    width: int
    _values: Tuple[Tuple[int, ...], ...]

    @classmethod
    def from_rows(cls, rows: Tuple[str]) -> "Grid":
        height = len(rows)
        width = len(rows[0]) if height else 0
        return cls(height, width, tuple(tuple(int(i) for i in row) for row in rows))

    def __getitem__(self, coordinates: Tuple[int, int]) -> int:
        y, x = coordinates
        return self._values[y][x]

    def __len__(self) -> int:
        return len(self._values)


@dataclass
class Surveyor:
    """Person checking sight lines for visible trees."""

    sight_lines: Dict[str, int] = field(default_factory=dict)

    def count_visible(self, grid: Grid) -> int:
        visible_trees = self.survey_perimeter(grid)
        visible_trees.update(self.survey_inner_trees(grid))
        return len(visible_trees)

    def survey_perimeter(self, grid: Grid) -> Set[Tuple[int, int]]:
        visible_trees = set()
        side_length = len(grid)
        # Perimeter is visible.
        for i in range(side_length):
            visible_trees.add((0, i))  # top
            visible_trees.add((i, 0))  # left
            visible_trees.add((side_length - 1, i))  # bottom
            visible_trees.add((i, side_length - 1))  # right

        self.sight_lines = {
            "left": grid[1, 0],
            "right": grid[1, -1],
            "top": grid[0, 1],
            "bottom": grid[-1, 1],
        }
        return visible_trees

    def survey_inner_trees(self, grid: Grid) -> Set[Tuple[int, int]]:
        visible_trees: Set[Tuple[int, int]] = set()
        inner_height, inner_length = grid.height - 1, grid.width - 1
        return visible_trees | set(
            visible_tree
            for y in range(1, inner_height + 1)
            for x in range(1, inner_length + 1)
            for visible_tree in self.check_sight_lines(grid, y, x)
        )

    def check_sight_lines(self, grid: Grid, y: int, x: int) -> Set[Tuple[int, int]]:
        self.adjust_vertical_sight_lines(grid[0, x], grid[-1, x])
        tree = grid[y, x]
        return set(
            self.check_sight_line(tree, direction, y, x)
            for direction in self.sight_lines.keys()
        )

    def adjust_vertical_sight_lines(
        self, top_tallest: int, bottom_tallest: int
    ) -> None:
        self.sight_lines["top"] = top_tallest
        self.sight_lines["bottom"] = bottom_tallest

    def check_sight_line(
        self, tree: int, direction: str, y: int, x: int
    ) -> Tuple[int, int]:
        if tree > self.sight_lines[direction]:
            self.sight_lines[direction] = tree
            return (y, x)
        # Otherwise, return a tree that won't count.
        return (0, 0)
