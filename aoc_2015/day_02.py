"""
Day 2: I Was Told There Would Be No Math

--- Part 1 ---

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

--- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width,
so they only have to worry about the length they need to order, which
they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around
its sides, or the smallest perimeter of any one face. Each present also
requires a bow made out of ribbon as well; the feet of ribbon required
for the perfect bow is equal to the cubic feet of volume of the
present. Don't ask how they tie the bow, though; they'll never tell.

How many total feet of ribbon should they order?
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
        length_wise_perimeter = 2 * self.length + 2 * self.width
        width_wise_perimeter = 2 * self.width + 2 * self.height
        height_wise_perimeter = 2 * self.height + 2 * self.length
        perimeters = {
            length_wise_perimeter,
            width_wise_perimeter,
            height_wise_perimeter,
        }
        self.shortest_perimeter = min(perimeters)

    def __iter__(self) -> Iterator:
        """Provide unpackable dimensions."""
        return iter((self.length, self.width, self.height))


@dataclass
class Calculator:
    """Calculator to measure total square feet of wrapping paper for
    a list of presents.
    """

    presents: List[Present]

    def calculate_wrapping_paper(self) -> int:
        """Return total needed square feet of wrapping paper for the
        presents.
        """
        return sum(self._calculate_square_feet(present) for present in self.presents)

    def calculate_ribbon(self) -> int:
        """Return total needed length of ribbon for the presents."""
        return sum(self._calculate_ribbon_length(present) for present in self.presents)

    def _calculate_square_feet(self, present: Present) -> int:
        """Return total needed square feet of wrapping paper for a
        present.
        """
        return present.total_area + min(
            present.length_wise_area, present.width_wise_area, present.height_wise_area
        )

    def _calculate_ribbon_length(self, present: Present) -> int:
        """Return length of ribbon needed for a single present."""
        return present.shortest_perimeter + (
            present.length * present.width * present.height
        )


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_02_part_1.txt") as data:
        presents = [
            Present(*[int(dimension) for dimension in dimensions.split("x")])
            for dimensions in data
        ]

    calculator = Calculator(presents)
    print(calculator.calculate_wrapping_paper())
    print(calculator.calculate_ribbon())
