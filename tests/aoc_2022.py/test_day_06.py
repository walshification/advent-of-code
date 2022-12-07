import pytest

from aoc_2022.day_06 import Receiver


@pytest.mark.parametrize(
    ("signal", "marker"),
    (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("aaaaaaaa", None),
    ),
)
def test_receiver_finds_marker(signal, marker):
    assert Receiver(signal).find_marker() == marker


@pytest.mark.parametrize(
    ("signal", "marker"),
    (("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19), ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23)),
)
def test_receiver_finds_start_marker(signal, marker):
    assert Receiver(signal).find_marker(14) == marker
