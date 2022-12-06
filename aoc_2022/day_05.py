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

--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you
notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you
quickly wipe it away. The crane isn't a CrateMover 9000 - it's a
CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air
conditioning, leather seats, an extra cup holder, and the ability to
pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means
that those three moved crates stay in the same order, resulting in this
new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain
their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now
it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally
different order: MCD.

Before the rearrangement process finishes, update your simulation so
that the Elves know where they should stand to be ready to unload the
final supplies. After the rearrangement procedure completes, what crate
ends up on top of each stack?
"""
import copy
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

    def __init__(self, stacks: Optional[Dict[int, Stack]] = None):
        self.stacks = stacks or copy.deepcopy(STARTING_STACKS)

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
class CrateMover9000:
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


@dataclass
class CrateMover9001(CrateMover9000):
    """The latest model."""

    def move_supplies(self, supply_count: int, source: int, destination: int) -> None:
        """Move supplies from source column to destination, preserving
        order.
        """
        crates_to_move = [
            self.inventory.stacks[source].pop() for _ in range(supply_count)
        ]
        self.inventory.stacks[destination].supplies.extend(crates_to_move[::-1])


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_05.txt") as data:
        commands = [command[:-1] for command in data][10:]

    crane = CrateMover9000(Inventory())
    crane_9001 = CrateMover9001(Inventory())

    top_supplies = crane.rearrange(commands)
    revised_top_supplies = crane_9001.rearrange(commands)

    print(crane.inventory)
    print(f"Part One: {top_supplies}")
    print(f"Part Two: {revised_top_supplies}")
