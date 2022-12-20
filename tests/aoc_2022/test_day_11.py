import pytest

from aoc_2022.day_11 import Item, Monkey, MonkeyTest


@pytest.mark.parametrize(
    ("condition", "true", "false", "result"), ((3, 1, 2, 1), (2, 1, 2, 2))
)
def test_understands_conditions(condition, true, false, result):
    assert MonkeyTest(condition, true, false)(9) == result


@pytest.mark.parametrize(
    ("operator", "result"),
    (("plus", (2, Item(8))), ("multiply", (2, Item(15)))),
)
def test_monkeys_hold_operations(operator, result):
    operation = {"operator": operator, "operand": 3}
    monkey = Monkey.build(0, [], operation, MonkeyTest(10, 1, 2))
    assert monkey.inspect(Item(5)) == result
