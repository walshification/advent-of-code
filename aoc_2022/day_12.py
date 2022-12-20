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
from dataclasses import dataclass
from typing import Tuple

CHAR_TO_HEIGHT_MAP = {c: n for n, c in enumerate("abcdefghijklmnopqrstuvwxyz")}


@dataclass
class Cell:
    """A unit of terrain on the map."""

    y: int
    x: int
    height: str

    def __xor__(self, other: "Cell") -> bool:
        """Return if one can move from cell to other."""
        return CHAR_TO_HEIGHT_MAP[self.height] >= CHAR_TO_HEIGHT_MAP[other.height] - 1
