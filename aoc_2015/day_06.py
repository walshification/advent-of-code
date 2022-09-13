"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house
decorating contest year after year, you've decided to deploy one
million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has
mailed you instructions on how to display the ideal lighting
configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the
lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The
instructions include whether to turn on, turn off, or toggle various
inclusive ranges given as coordinate pairs. Each coordinate pair
represents opposite corners of a rectangle, inclusive; a coordinate
pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your
lights by doing the instructions Santa sent you in order.

After following the instructions, how many lights are lit?
"""
import os
from dataclasses import dataclass
from typing import List


@dataclass
class Light:
    """Representation for a light that can be turned on or off.

    Attributes:
      active (int): whether the light is on or off.
    """

    active: int = 0

    def __repr__(self) -> str:
        return "*" if self.active else " "

    def toggle(self) -> int:
        """Flip the light switch and return its state."""
        if self.active:
            self.turn_off()
        else:
            self.turn_on()
        return self.active

    def turn_on(self) -> int:
        """Set active state to True. Return True."""
        self.active = min(self.active + 1, 1)
        return self.active

    def turn_off(self) -> int:
        """Set active state to False. Return False."""
        self.active = min(self.active - 1, 0)
        return self.active


class Grid:
    """Your basic Cartesian grid."""

    def __init__(self, length: int = 1000) -> None:
        """Build grid of lights to the length."""
        self._coordinates = [[Light() for _ in range(length)] for _ in range(length)]

    def __repr__(self) -> str:
        """Format the grid so it makes visual sense when printed."""
        return " " + " ".join(
            " ".join(str(node) for node in column) + "\n"
            for column in self._coordinates
        )

    @property
    def active_light_count(self) -> int:
        """Return count of currently active lights."""
        return sum(light.active for column in self._coordinates for light in column)

    def decorate(self, instructions: List[str]) -> int:
        """Active lights in the grid according to instructions.

        Args:
          instructions (List[str]): instructions to follow.
          display (bool, default: False): whether or not to print the
            grid to the console.

        Returns:
          (int): count of currently active lights.
        """
        for instruction in instructions:
            *operator, left_corner, _, right_corner = instruction.split()

            x1, y1 = (int(coordinate) for coordinate in left_corner.split(","))
            x2, y2 = (int(coordinate) for coordinate in right_corner.split(","))
            if abs(x1 + y1) > abs(x2 + y2):
                x1, y1, x2, y2 = x2, y2, x1, y1

            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    getattr(self._coordinates[i][j], "_".join(operator))()

        return self.active_light_count


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_06.txt") as data:
        instructions = [instruction for instruction in data]

    grid = Grid()
    grid.decorate(instructions)
    print(f"Part 1: {grid.active_light_count}")
