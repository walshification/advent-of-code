from textwrap import dedent

from aoc_2022.day_05 import Crane, Inventory, Stack, Supply


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


def test_crane_can_move_supply_from_column_to_column():
    stacks = [Stack([Supply("S"), Supply("Z")]), Stack([Supply("N")])]
    inventory = Inventory(
        {column: stack for column, stack in enumerate(stacks, start=1)}
    )
    crane = Crane(inventory)

    crane.move_supply(1, 2)

    assert str(inventory) == dedent(
        """
            [Z]
        [S] [N]
         1   2"""
    )


def test_crane_can_move_supplies_from_column_to_column():
    stacks = [Stack([Supply("S"), Supply("Z")]), Stack([Supply("N")])]
    inventory = Inventory(
        {column: stack for column, stack in enumerate(stacks, start=1)}
    )
    crane = Crane(inventory)

    crane.move_supplies(2, 1, 2)

    assert len(inventory.stacks[1]) == 0
    assert len(inventory.stacks[2]) == 3