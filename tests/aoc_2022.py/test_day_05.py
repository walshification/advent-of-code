from textwrap import dedent

from aoc_2022.day_05 import Inventory, Stack, Supply


def test_inventory_renders_nicely():
    stacks = [Stack([Supply("S"), Supply("Z")]), Stack([Supply("N")])]
    inventory = Inventory(
        {column: stack for column, stack in enumerate(stacks, start=1)}
    )
    assert str(inventory) == dedent(
        """
        [Z]
        [S] [N]
         1   2"""
    )
