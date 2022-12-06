from textwrap import dedent

from aoc_2022.day_05 import CrateMover9000, CrateMover9001, Inventory, Stack, Supply


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
    crane = CrateMover9000(inventory)

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
    crane = CrateMover9000(inventory)

    crane.move_supplies(2, 1, 2)

    assert len(inventory.stacks[1]) == 0
    assert len(inventory.stacks[2]) == 3


def test_crane_accepts_string_commands():
    stacks = [Stack([Supply("S"), Supply("Z")]), Stack([Supply("N")])]
    inventory = Inventory(
        {column: stack for column, stack in enumerate(stacks, start=1)}
    )
    crane = CrateMover9000(inventory)

    top_supplies = crane.rearrange(["move 2 from 1 to 2"])

    assert top_supplies == "S"


def test_cratemover9001_moves_supplies_as_a_unit():
    stacks = [Stack([Supply("S"), Supply("Z")]), Stack([Supply("N")])]
    inventory = Inventory(
        {column: stack for column, stack in enumerate(stacks, start=1)}
    )
    crane = CrateMover9001(inventory)

    top_supplies = crane.rearrange(["move 2 from 1 to 2"])

    assert top_supplies == "Z"


def test_the_sample():
    stacks = {
        1: Stack([Supply("Z"), Supply("N")]),
        2: Stack([Supply("M"), Supply("C"), Supply("D")]),
        3: Stack([Supply("P")]),
    }
    crane = CrateMover9001(Inventory(stacks))

    top_supplies = crane.rearrange(
        [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ]
    )

    assert top_supplies == "MCD"
