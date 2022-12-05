"""
--- Day 4: Camp Cleanup ---

Space needs to be cleared before the last supplies can be unloaded from
the ships, and so several Elves have been assigned the job of cleaning
up sections of the camp. Every section has a unique ID number, and each
Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with
each other, they've noticed that many of the assignments overlap. To
try to quickly find overlaps and reduce duplicated effort, the Elves
pair up and make a big list of the section assignments for each pair
(your puzzle input).

In how many assignment pairs does one range fully contain the other?

--- Part Two ---

It seems like there is still quite a bit of duplicate work planned.
Instead, the Elves would like to know the number of pairs that overlap
at all.

In how many assignment pairs do the ranges overlap?
"""
from typing import List, Tuple


class Assignment:
    """A cleaning assignment."""

    def __init__(self, sections: str):
        """Expand assignments (e.g. "1-4" becomes {1, 2, 3, 4})."""
        start, end = sections.split("-")
        self.sections = set(i for i in range(int(start), int(end) + 1))

    def __and__(self, other: "Assignment") -> set:
        """Return the union of sections with another."""
        return self.sections & other.sections

    def __sub__(self, other: "Assignment") -> set:
        """Return the difference in sections from another."""
        return self.sections - other.sections


def assess(section_pairs: List[str]) -> Tuple[int, int]:
    """Check section pairs for overlapping assignments.

    Returns:
        (
            count of assignments fully containing the other,
            count of assignments overlapping at all,
        )
    """
    containment_tracker = []
    overlapping_tracker = []
    for pair in section_pairs:
        raw_first, raw_second = pair.split(",")
        first, second = Assignment(raw_first), Assignment(raw_second)
        if not first - second or not second - first:
            containment_tracker.append(1)
            overlapping_tracker.append(1)
        elif first & second:
            overlapping_tracker.append(1)

    return sum(containment_tracker), sum(overlapping_tracker)


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_04.txt") as data:
        assignment_pairs = [pair for pair in data]

    containment, overlapping = assess(assignment_pairs)
    print(f"Part One: {containment}")
    print(f"Part Two: {overlapping}")
