"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river
you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle
input). The heightmap shows the local area from above broken into a
grid; the elevation of each square of the grid is given by a single
lowercase letter, where a is the lowest elevation, b is the next-lowest,
and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S)
and the location that should get the best signal (E). Your current
position (S) has elevation a, and the location that should get the best
signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few
steps as possible. During each step, you can move exactly one square up,
down, left, or right. To avoid needing to get out your climbing gear,
the elevation of the destination square can be at most one higher than
the elevation of your current square; that is, if your current elevation
is m, you could step to elevation n, but not to elevation o. (This also
means that the elevation of the destination square can be much lower
than the elevation of your current square.)

What is the fewest steps required to move from your current position to
the location that should get the best signal?
"""
from dataclasses import dataclass, field
from typing import Dict, Iterator, List, Optional, Tuple

CHAR_TO_HEIGHT_MAP = {
    c: n
    for n, c in list(enumerate("abcdefghijklmnopqrstuvwxyz")) + [(0, "S"), (25, "E")]
}


class Cell:
    """A unit of terrain on the map."""

    def __init__(
        self,
        y: int,
        x: int,
        height: str,
        north: Optional["Cell"] = None,
        east: Optional["Cell"] = None,
        south: Optional["Cell"] = None,
        west: Optional["Cell"] = None,
    ) -> None:
        self.y = y
        self.x = x
        self.height = height
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def __iter__(self) -> Iterator[int]:
        """Return a tuple of the cell's row and column positions."""
        return (i for i in (self.y, self.x))

    def __str__(self) -> str:
        return self.height

    def __xor__(self, other: "Cell") -> bool:
        """Return if one can move from cell to other."""
        return CHAR_TO_HEIGHT_MAP[self.height] >= CHAR_TO_HEIGHT_MAP[other.height] - 1

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self.y, self.x

    @property
    def links(self) -> Tuple["Cell", ...]:
        return tuple(cell for cell in self.neighbors if self ^ cell)

    @property
    def neighbors(self) -> Tuple["Cell", ...]:
        return tuple(
            cell
            for cell in (self.north, self.east, self.south, self.west)
            if cell is not None
        )


@dataclass
class Terrain:
    """Heightmap to my destination."""

    grid: List[List[Cell]]
    start: Cell
    end: Cell

    def __post_init__(self) -> None:
        for cell in self:
            self.link(cell)

    @classmethod
    def from_input(cls, heightmap: Tuple[Tuple[str, ...], ...]) -> "Terrain":
        """Draw the terrain from the heightmap input."""
        grid: List[List[Cell]] = []
        for y, row in enumerate(heightmap):
            grid.append([])
            for x, height in enumerate(row):
                cell = Cell(y, x, height)
                if height == "S":
                    start = cell
                if height == "E":
                    end = cell
                grid[y].append(cell)

        return cls(grid, start, end)

    def __getitem__(self, position: Tuple[int, int]) -> Optional[Cell]:
        """Return a cell for the given position if it exists."""
        y, x = position
        if y < 0 or y >= len(self.grid):
            return None

        if x < 0 or x >= len(self.grid[0]):
            return None

        return self.grid[y][x]

    def __iter__(self) -> Iterator:
        """Return each cell of the grid."""
        return iter(cell for row in self.grid for cell in row)

    def __str__(self) -> str:
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)

    def link(self, cell: Cell) -> None:
        """Configure directions."""
        row, column = cell

        cell.north = self[row - 1, column]
        cell.south = self[row + 1, column]
        cell.east = self[row, column + 1]
        cell.west = self[row, column - 1]


@dataclass
class Dijkstra:
    """Walk a terrain to find the shortest route to the end."""

    paths: Dict[Tuple[int, int], int] = field(default_factory=dict)

    def walk(self, terrain: Terrain) -> int:
        """Return fewest steps to move from start to end of terrain."""
        self.paths[terrain.start.coordinates] = 0

        frontier = [terrain.start]
        while frontier:
            new_frontier = []

            for cell in frontier:
                for link in cell.links:
                    if link.coordinates in self.paths:
                        continue

                    self.paths[link.coordinates] = self.paths[cell.coordinates] + 1
                    new_frontier.append(link)

            frontier = new_frontier

        return self.paths[terrain.end.coordinates]
