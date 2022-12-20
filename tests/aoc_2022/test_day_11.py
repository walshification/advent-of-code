import pytest

from aoc_2022.day_11 import MonkeyTest


@pytest.mark.parametrize(
    ("condition", "true", "false", "result"), ((3, 1, 2, 1), (2, 1, 2, 2))
)
def test_understands_conditions(condition, true, false, result):
    assert MonkeyTest(condition, true, false).test(9) == result
