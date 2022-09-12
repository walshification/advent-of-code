"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are
naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov,
      or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like
      xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are
      part of one of the other requirements.

How many strings are nice?

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model
of determining whether a string is naughty or nice. None of the old
rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice
      in the string without overlapping, like xyxy (xy) or aabcdefgaa
      (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one
      letter between them, like xyx, abcdefeghi (efe), or even aaa.

How many strings are nice under these new rules?
"""
import re
from typing import Callable, Sequence


def validate_vowels(string: str) -> bool:
    """Return whether string contains at least three vowels."""
    vowels = re.sub("(?i)([^aeiou])", "", string)
    return len(vowels) > 2


def validate_double_letters(string: str) -> bool:
    """Return whether string contains a double letter."""
    for i, c in enumerate(string[:-1]):
        if c == string[i + 1]:
            return True
    return False


def validate_special_letters(string: str) -> bool:
    """Return whether string contains special letter pairs."""
    for pair in ["ab", "cd", "pq", "xy"]:
        if pair in string:
            return False
    return True


VALIDATORS = [
    validate_vowels,
    validate_double_letters,
    validate_special_letters,
]


def main(
    strings: Sequence[str],
    validators: Sequence[Callable[[str], bool]] = VALIDATORS,
) -> int:
    """Return number of strings that pass validation."""
    good_count = []
    for string in strings:
        if all(validate(string) for validate in validators):
            good_count.append(1)
    return sum(good_count)


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_05.txt") as data:
        strings = [string for string in data]

    print(f"Part 1: {main(strings)}")
