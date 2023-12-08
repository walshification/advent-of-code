"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected
to take a look. The Elves have even given you a map; on it, they've used
stars to mark the top fifty locations that are likely to be having
problems.

You've been doing this long enough to know that to restore snow
operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day in the Advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful
enough") and where they're even sending you ("the sky") and why your map
looks mostly blank ("you sure ask a lot of questions") and hang on did
you just say the sky ("of course, where do you think snow comes from")
when you realize that the Elves are already loading you into a trebuchet
("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their
calibration document (your puzzle input) has been amended by a very
young Elf who was apparently just excited to show off her art skills.
Consequently, the Elves are having trouble reading the values on the
document.

The newly-improved calibration document consists of lines of text; each
line originally contained a specific calibration value that the Elves
now need to recover. On each line, the calibration value can be found by
combining the first digit and the last digit (in that order) to form a
single two-digit number.
"""
from typing import Callable, Sequence


def digits(calibration: str) -> int:
    """Return first and last numbers in a calibration as a 2-digit int."""
    numbers = [c for c in calibration if c.isdigit()]
    return int(numbers[0] + numbers[-1])


def enhanced_digits(calibration: str) -> int:
    """Return first and last numbers in a calibration as a 2-digit int,
    including numbers spelled out in letters.
    """
    calibration = (
        calibration.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    numbers = [c for c in calibration if c.isdigit()]
    return int(numbers[0] + numbers[-1])


def main(calibrations: Sequence[str], digit_func: Callable[[str], int] = digits) -> int:
    return sum(digit_func(calibration) for calibration in calibrations)


if __name__ == "__main__":
    with open("aoc_2023/inputs/day_01.txt") as data:
        calibrations = [line for line in data]

    print(f"Part 1: {main(calibrations)}")
    print(f"Part 2: {main(calibrations, digit_func=enhanced_digits)}")
