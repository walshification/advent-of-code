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
from typing import Optional, Set, Tuple


class Point:
    def __init__(self, y: int, x: int) -> None:
        self.y = y
        self.x = x


class Tree(Point):
    def __init__(self, height: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.height = height

    def __gt__(self, other: "Tree") -> bool:
        return self.height > other.height

    @property
    def position(self) -> Tuple[int, int]:
        return self.y, self.x


@dataclass(frozen=True)
class Grid:
    """Your basic Cartesian grid."""

    height: int
    width: int
    _grid: Tuple[Tuple[Tree, ...], ...]

    @classmethod
    def from_rows(cls, rows: Tuple[str, ...]) -> "Grid":
        height = len(rows)
        width = len(rows[0]) if height else 0
        return cls(
            height,
            width,
            tuple(
                tuple(
                    Tree(y=y, x=x, height=int(height)) for x, height in enumerate(row)
                )
                for y, row in enumerate(rows)
            ),
        )

    def __getitem__(self, coordinates: Tuple[int, int]) -> Tree:
        y, x = coordinates
        return self._grid[y][x]


@dataclass
class Surveyor:
    """Person checking sight lines for visible trees."""

    grid: Grid

    def count_visible(self) -> int:
        return len(self.survey_perimeter() | self.survey_inner_trees())

    def survey_perimeter(self) -> Set[Tuple[int, int]]:
        visible_trees = set()
        # Perimeter is visible.
        for i in range(self.grid.width):
            visible_trees.add((0, i))  # top
            visible_trees.add((i, 0))  # left
            visible_trees.add((self.grid.width - 1, i))  # bottom
            visible_trees.add((i, self.grid.width - 1))  # right

        return visible_trees

    def survey_inner_trees(self) -> Set[Tuple[int, int]]:
        inner_height, inner_length = self.grid.height - 1, self.grid.width - 1
        return set(
            visible_tree.position
            for y in range(1, inner_height)
            for x in range(1, inner_length)
            if (visible_tree := self.check_sight_lines(y, x))
        )

    def check_sight_lines(self, y: int, x: int) -> Optional[Tree]:
        tree = self.grid[y, x]
        return (
            self.check_sight_line(tree, set(self.grid[y, i] for i in range(0, x)))
            or self.check_sight_line(
                tree, set(self.grid[y, i] for i in range(x + 1, self.grid.width))
            )
            or self.check_sight_line(tree, set(self.grid[i, x] for i in range(0, y)))
            or self.check_sight_line(
                tree, set(self.grid[i, x] for i in range(y + 1, self.grid.height))
            )
            or None
        )

    def check_sight_line(self, tree: Tree, trees: Set[Tree]) -> Optional[Tree]:
        if all(tree > left_tree for left_tree in trees):
            return tree
        return None


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_08.txt") as data:
        rows = tuple(line[:-1] for line in data)

        grid = Grid.from_rows(rows)
        surveyor = Surveyor(grid)

        print(f"Part One: {surveyor.count_visible()}")
        # print(f"Part Two: {}")
