"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of
houses.

He begins by delivering a present to the house at his starting
location, and then an elf at the North Pole calls him via radio and
tells him where to move next. Moves are always exactly one house to the
north (^), south (v), east (>), or west (<). After each move,
he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much
eggnog, and so his directions are a little off, and Santa ends up
visiting some houses more than once. How many houses receive at least
one present?

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version
of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two
presents to the same starting house), then take turns moving based on
instructions from the elf, who is eggnoggedly reading from the same
script as the previous year.

This year, how many houses receive at least one present?
"""
from typing import Tuple


def move_north(x: int, y: int) -> Tuple[int, int]:
    """Change position by moving up the y-axis."""
    return x, y + 1


def move_south(x: int, y: int) -> Tuple[int, int]:
    """Change position by moving down the y-axis."""
    return x, y - 1


def move_east(x: int, y: int) -> Tuple[int, int]:
    """Change position by moving up the x-axis."""
    return x + 1, y


def move_west(x: int, y: int) -> Tuple[int, int]:
    """Change position by moving down the x-axis."""
    return x - 1, y


DIRECTION_TO_MOVEMENT_MAP = {
    "^": move_north,
    "v": move_south,
    ">": move_east,
    "<": move_west,
}


class Santa:
    """Representation of the Big Man to track his deliveries.

    Attributes:
      tracker (set): set of all the locations visited.
    """

    def __init__(self) -> None:
        """Start Santa with a delivery at the default location."""
        self._position = (0, 0)
        self.tracker = set()
        self.tracker.add(self._position)

    def deliver(self, directions: str) -> int:
        """Track Santa as he follows directions for deliveries.

        Args:
          directions (str): string of directions for Santa to follow.

        Returns:
          (int): number of locations visited.
        """
        for direction in directions:
            self._position = DIRECTION_TO_MOVEMENT_MAP[direction](*self._position)
            self.tracker.add(self._position)

        return len(self.tracker)


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_03_part_1.txt") as data:
        # Remove the trailing newline.
        directions = data.read()[:-1]

    santa = Santa()
    print(f"Part 1: {santa.deliver(directions)}")

    new_santa = Santa()
    robo_santa = Santa()
    human_directions = directions[::2]
    robo_directions = directions[1::2]
    new_santa.deliver(human_directions)
    robo_santa.deliver(robo_directions)
    print(f"Part 2: {len(new_santa.tracker | robo_santa.tracker)}")
