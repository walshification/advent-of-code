from collections import deque

import pytest

from aoc_2022.day_11 import Monkey, MonkeyBusinessCalculator, MonkeyTest


@pytest.mark.parametrize(
    ("condition", "true", "false", "result"), ((3, 1, 2, 1), (2, 1, 2, 2))
)
def test_understands_conditions(condition, true, false, result):
    assert MonkeyTest(condition, true, false)(9) == result


@pytest.mark.parametrize(
    ("operator", "result"),
    (("plus", (2, 2)), ("multiply", (2, 5))),
)
def test_monkeys_hold_operations(operator, result):
    operation = {"operator": operator, "operand": 3}
    monkey = Monkey.build(0, [], operation, MonkeyTest(10, 1, 2))
    assert monkey.inspect(5) == result


def test_calculator_can_execute_rount():
    monkeys = [
        {
            "starting": [79, 98],
            "operation": {"operator": "multiply", "operand": 19},
            "test": {"condition": 23, "true": 2, "false": 3},
        },
        {
            "starting": [54, 65, 75, 74],
            "operation": {"operator": "plus", "operand": 6},
            "test": {"condition": 19, "true": 2, "false": 0},
        },
        {
            "starting": [79, 60, 97],
            "operation": {"operator": "multiply", "operand": -1},
            "test": {"condition": 13, "true": 1, "false": 3},
        },
        {
            "starting": [74],
            "operation": {"operator": "plus", "operand": 3},
            "test": {"condition": 17, "true": 0, "false": 1},
        },
    ]
    calc = MonkeyBusinessCalculator.build(monkeys)
    calc.execute_round()
    assert calc.monkeys[0].items == deque([20, 23, 27, 26])
    assert calc.monkeys[1].items == deque([2080, 25, 167, 207, 401, 1046])
    assert calc.monkeys[2].items == deque()
    assert calc.monkeys[3].items == deque()


def test_calculator_calculates_most_active_monkeys():
    monkeys = [
        {
            "starting": [79, 98],
            "operation": {"operator": "multiply", "operand": 19},
            "test": {"condition": 23, "true": 2, "false": 3},
        },
        {
            "starting": [54, 65, 75, 74],
            "operation": {"operator": "plus", "operand": 6},
            "test": {"condition": 19, "true": 2, "false": 0},
        },
        {
            "starting": [79, 60, 97],
            "operation": {"operator": "multiply", "operand": -1},
            "test": {"condition": 13, "true": 1, "false": 3},
        },
        {
            "starting": [74],
            "operation": {"operator": "plus", "operand": 3},
            "test": {"condition": 17, "true": 0, "false": 1},
        },
    ]
    calc = MonkeyBusinessCalculator.build(monkeys)
    assert calc.calculate() == 10605
