"""
--- Day 1: Calorie Counting ---

Santa's reindeer typically eat regular reindeer food, but they need a
lot of magical energy to deliver presents on Christmas. For that, their
favorite snack is a special type of star fruit that only grows deep in
the jungle. The Elves have brought you on their annual expedition to
the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a
minimum of fifty stars by December 25th. Although the Elves assure you
that the grove has plenty of fruit, you decide to grab any fruit you
see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on
each day in the Advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles
or access from the air; the Elves' expedition traditionally goes on
foot. As your boats approach land, the Elves begin taking inventory of
their supplies. One important consideration is food - in particular,
the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by
the various meals, snacks, rations, etc. that they've brought with
them, one item per line. Each Elf separates their own inventory from
the previous Elf's inventory (if any) by a blank line.

In case the Elves get hungry and need extra snacks, they need to know
which Elf to ask: they'd like to know how many Calories are being
carried by the Elf carrying the most Calories. In the example above,
this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is
that Elf carrying?

--- Part Two ---

By the time you calculate the answer to the Elves' question, they've
already realized that the Elf carrying the most Calories of food might
eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to
know the total Calories carried by the top three Elves carrying the
most Calories. That way, even if one of those Elves runs out of snacks,
they still have two backups.

In the example above, the top three Elves are the fourth Elf (with
24000 Calories), then the third Elf (with 11000 Calories), then the
fifth Elf (with 10000 Calories). The sum of the Calories carried by
these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories
are those Elves carrying in total?

"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elf:
    """An Elf capable of carrying meals."""

    meals: List[int] = field(default_factory=list)

    @property
    def total_calories(self) -> int:
        """A computed count of calories in all this Elf's meals."""
        if self.meals:
            return sum(meal for meal in self.meals)
        return 0


class ElfStats:
    """Collection of relevant Elf stats."""

    def __init__(self, elves: List[Elf]):
        top_3 = sorted(elves, reverse=True, key=lambda e: e.total_calories)[:3]
        self.top_elf = top_3[0]
        self.top_3_elves = {elf.total_calories: elf for elf in top_3}
        self.top_3_calories = self.calculate_top_3_calories()

    @classmethod
    def from_calories_list(cls, calories_list: List[str]) -> "ElfStats":
        """Calculate elf stats from a list of their calories."""
        elf = Elf()
        stats = cls([elf])

        for calories in calories_list:
            # "\n" separates Elves from each other.
            if calories == "\n":
                stats.check_for_top_elf(elf)
                # On to the next Elf.
                elf = Elf()
                continue

            elf.meals.append(int(calories))

        return stats

    def calculate_top_3_calories(self) -> int:
        return sum(calories for calories in self.top_3_elves.keys())

    def check_for_top_elf(self, elf: Elf) -> None:
        """Compare Elf to current top Elves and change if necessary."""
        if self.is_top_3(elf):
            self.add_to_top_3(elf)
            if elf.total_calories > self.top_elf.total_calories:
                self.top_elf = elf

    def is_top_3(self, elf: Elf) -> bool:
        min_calories = min(self.top_3_elves.keys())
        return elf.total_calories > min_calories

    def add_to_top_3(self, elf: Elf) -> None:
        if len(self.top_3_elves) == 3:
            min_elf = min(self.top_3_elves.keys())
            del self.top_3_elves[min_elf]
        self.top_3_elves[elf.total_calories] = elf
        self.top_3_calories = self.calculate_top_3_calories()


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_01.txt") as data:
        calories_list = [line for line in data]

    stats = ElfStats.from_calories_list(calories_list)

    print(f"Part 1: {stats.top_elf.total_calories}")
    print(f"Part 2: {stats.top_3_calories}")
