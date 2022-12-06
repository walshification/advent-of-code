import pytest

from aoc_2022.day_06 import Receiver


@pytest.mark.parametrize(
    ("signal", "marker"),
    (("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7), ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5)),
)
def test_receiver_finds_marker(signal, marker):
    assert Receiver(signal).find_marker() == marker
