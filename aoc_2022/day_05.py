"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been
unloaded from the ships. Supplies are stored in stacks of marked crates,
but because the needed supplies are buried under many other crates, the
crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between
stacks. To ensure none of the crates get crushed or fall over, the crane
operator will rearrange them in a series of carefully-planned steps.
After the crates are rearranged, the desired crates will be at the top
of each stack.

The Elves don't want to interrupt the crane operator during this
delicate procedure, but they forgot to ask her which crate will end up
where, and they want to be ready to unload them as soon as possible so
they can embark.

They do, however, have a drawing of the starting stacks of crates and
the rearrangement procedure (your puzzle input).

After the rearrangement procedure completes, what crate ends up on top
of each stack?
"""
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Supply:

    name: str

    def __str__(self) -> str:
        return f"[{self.name}]"


@dataclass
class Stack:

    supplies: List[Supply]

    def __getitem__(self, index: int) -> Optional[Supply]:
        try:
            return self.supplies[index]
        except IndexError:
            return None

    def __len__(self) -> int:
        return len(self.supplies)

    def append(self, supply: Supply) -> None:
        """Add the supply to the top of the stack."""
        self.supplies.append(supply)

    def pop(self) -> Supply:
        """Return the top supply in the stack."""
        return self.supplies.pop()


STARTING_STACKS = {
    1: Stack(
        [
            Supply("S"),
            Supply("Z"),
            Supply("P"),
            Supply("D"),
            Supply("L"),
            Supply("B"),
            Supply("F"),
            Supply("C"),
        ]
    ),
    2: Stack(
        [
            Supply("N"),
            Supply("V"),
            Supply("G"),
            Supply("P"),
            Supply("H"),
            Supply("W"),
            Supply("B"),
        ]
    ),
    3: Stack([Supply("F"), Supply("W"), Supply("B"), Supply("J"), Supply("G")]),
    4: Stack(
        [
            Supply("G"),
            Supply("J"),
            Supply("N"),
            Supply("F"),
            Supply("L"),
            Supply("W"),
            Supply("C"),
            Supply("S"),
        ]
    ),
    5: Stack(
        [
            Supply("W"),
            Supply("J"),
            Supply("L"),
            Supply("T"),
            Supply("P"),
            Supply("M"),
            Supply("S"),
            Supply("H"),
        ]
    ),
    6: Stack(
        [Supply("B"), Supply("C"), Supply("W"), Supply("G"), Supply("F"), Supply("S")]
    ),
    7: Stack(
        [
            Supply("H"),
            Supply("T"),
            Supply("P"),
            Supply("M"),
            Supply("Q"),
            Supply("B"),
            Supply("W"),
        ]
    ),
    8: Stack([Supply("F"), Supply("S"), Supply("W"), Supply("T")]),
    9: Stack([Supply("N"), Supply("C"), Supply("R")]),
}


class Inventory:
    """Stacks of supplies needed by the Elves."""

    def __init__(self, stacks: Dict[int, Stack] = STARTING_STACKS):
        self.stacks = stacks

    def __str__(self) -> str:
        """Display inventory in stacked columns."""
        tallest_stack = max(len(stack) for stack in self.stacks.values())
        lines = []
        for i in range(tallest_stack, -1, -1):
            row = ""
            for supplies in self.stacks.values():
                if supply := supplies[i]:
                    row += str(supply)
                else:
                    row += "   "
                row += " "
            lines.append(row)

        row = ""
        for column in self.stacks.keys():
            row += f" {column}  "
        lines.append(row.rstrip())

        return "\n".join(line.rstrip() for line in lines)


@dataclass
class Crane:
    """Use to rearrange inventory supplies."""

    inventory: Inventory

    def rearrange(self, commands: List[str]) -> str:
        """Rearrange per commands and return top supplies."""
        for command in commands:
            _, count, _, source, _, destination = command.split()
            self.move_supplies(int(count), int(source), int(destination))

        return "".join(
            str(supply)[1]  # just get the letter
            for stack in self.inventory.stacks.values()
            if (supply := stack[-1])
        )

    def move_supplies(self, supply_count: int, source: int, destination: int) -> None:
        """Move supplies from source column to destination."""
        for _ in range(supply_count):
            self.move_supply(source, destination)

    def move_supply(self, source: int, destination: int) -> None:
        """Move the top supply from source column to destination."""
        self.inventory.stacks[destination].append(self.inventory.stacks[source].pop())


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_05.txt") as data:
        commands = [command[:-1] for command in data][10:]

    crane = Crane(Inventory())
    top_supplies = crane.rearrange(commands)

    print(crane.inventory)
    print(f"Part One: {top_supplies}")
