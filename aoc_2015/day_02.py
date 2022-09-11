"""
Day 2: I Was Told There Would Be No Math

Part 1:

The elves are running low on wrapping paper, and so they need to submit
an order for more. They have a list of the dimensions (length l,
width w, and height h) of each present, and only want to order exactly
as much as they need.

Fortunately, every present is a box (a perfect right rectangular
prism), which makes calculating the required wrapping paper for each
gift a little easier: find the surface area of the box, which is
2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for
each present: the area of the smallest side.

All numbers in the elves' list are in feet. How many total square feet
of wrapping paper should they order?
"""
from dataclasses import dataclass
from typing import Iterator, List


@dataclass
class Present:
    """Representation of a perfect right rectangular prism."""

    length: int
    width: int
    height: int

    def __post_init__(self) -> None:
        """Calculate remaining box dimensions."""
        self.length_wise_area = self.length * self.width
        self.width_wise_area = self.width * self.height
        self.height_wise_area = self.height * self.length
        self.total_area = (
            2 * self.length_wise_area
            + 2 * self.width_wise_area
            + 2 * self.height_wise_area
        )

    def __iter__(self) -> Iterator:
        """Provide unpackable dimensions."""
        return iter((self.length, self.width, self.height))


class Calculator:
    """Calculator to measure total square feet of wrapping paper for
    a list of presents.
    """

    @classmethod
    def wrapping_paper(cls, presents: List[Present]) -> int:
        """Return total needed square feet of wrapping paper for the
        presents.
        """
        return sum(cls._calculate_square_feet(present) for present in presents)

    @classmethod
    def _calculate_square_feet(cls, present: Present) -> int:
        """Return total needed square feet of wrapping paper for a
        present.
        """
        return present.total_area + min(
            present.length_wise_area, present.width_wise_area, present.height_wise_area
        )


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_02_part_1.txt") as data:
        presents = [
            Present(*[int(dimension) for dimension in dimensions.split("x")])
            for dimensions in data
        ]

    print(Calculator.wrapping_paper(presents))
