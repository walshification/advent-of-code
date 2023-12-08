import pytest

from aoc_2023.day_01 import digits, enhanced_digits, main


@pytest.mark.parametrize(
    ("calibration", "expected"),
    (("1asdf2", 12), ("asdf23", 23), ("34asdf", 34), ("a4s5d", 45), ("a1s2d3f4g", 14)),
)
def test_digits(calibration, expected):
    assert digits(calibration) == expected


def test_main():
    calibrations = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    assert main(calibrations) == 142


def test_enhanced_digits():
    assert enhanced_digits("two1nine") == 29


def test_enhanced_main():
    calibrations = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert main(calibrations, digit_func=enhanced_digits) == 281
