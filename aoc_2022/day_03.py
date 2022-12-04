"""
--- Day 3: Rucksack Reorganization ---

One Elf has the important job of loading all of the rucksacks with
supplies for the jungle journey. Unfortunately, that Elf didn't quite
follow the packing instructions, and so a few items now need to be
rearranged.

Each rucksack has two large compartments. All items of a given type are
meant to go into exactly one of the two compartments. The Elf that did
the packing failed to follow this rule for exactly one item type per
rucksack.

The Elves have made a list of all of the items currently in each
rucksack (your puzzle input), but they need your help finding the
errors. Every item type is identified by a single lowercase or
uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a
single line. A given rucksack always has the same number of items in
each of its two compartments, so the first half of the characters
represent items in the first compartment, while the second half of the
characters represent items in the second compartment.

To help prioritize item rearrangement, every item type can be converted
to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

Find the item type that appears in both compartments of each rucksack.
What is the sum of the priorities of those item types?

--- Part Two ---

As you finish identifying the misplaced items, the Elves come to you
with another issue.

For safety, the Elves are divided into groups of three. Every Elf
carries a badge that identifies their group. For efficiency, within
each group of three Elves, the badge is the only item type carried by
all three Elves. That is, if a group's badge is item type B, then all
three Elves will have item type B somewhere in their rucksack, and at
most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated
authenticity sticker on the badges. All of the badges need to be pulled
out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each
group's badges. The only way to tell which item type is the right one
is by finding the one item type that is common between all three Elves
in each group.

Every set of three lines in your list corresponds to a single group,
but each group can have a different badge item type.

Find the item type that corresponds to the badges of each three-Elf
group. What is the sum of the priorities of those item types?
"""
import string
from typing import List

PRIORITIES = {char: i for i, char in enumerate(string.ascii_letters, start=1)}


def find_common(content: str) -> int:
    half = int(len(content) / 2)
    common = set(content[:half]) & set(content[half:])
    return PRIORITIES[common.pop()]


def sort(contents: List[str]) -> int:
    return sum(find_common(content) for content in contents)


def find_common_by_group(contents: List[str]) -> int:
    # Slice the newline character off the item lists.
    common = set(contents[0][:-1]) & set(contents[1][:-1]) & set(contents[2][:-1])
    return PRIORITIES[common.pop()]


def sort_by_group(contents: List[str]) -> int:
    return sum(
        find_common_by_group(contents[i : i + 3]) for i in range(0, len(contents), 3)
    )


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_03.txt") as data:
        rucksacks = [rucksack for rucksack in data]

    print(f"Part One: {sort(rucksacks)}")
    print(f"Part 2: {sort_by_group(rucksacks)}")
