"""
Day 1: Not Quite Lisp

Part 1:

Santa is trying to deliver presents in a large apartment building, but
he can't find the right floor - the directions he got are a little
confusing. He starts on the ground floor (floor 0) and then follows the
instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a
closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he
will never find the top or bottom floors.

Part 2:

Now, given the same instructions, find the position of the first
character that causes him to enter the basement (floor -1). The first
character in the instructions has position 1, the second character has
position 2, and so on.

What is the position of the character that causes Santa to first enter
the basement?
"""
from dataclasses import dataclass, field
from typing import Iterator, List, Optional


def ascend(floor: int) -> int:
    """Go up one floor."""
    return floor + 1


def descend(floor: int) -> int:
    """Go down one floor."""
    return floor - 1


CHAR_TO_COMMAND_MAP = {
    "(": ascend,
    ")": descend,
}


@dataclass
class ElevatorEvent:

    command: str
    floor: int

    def __iter__(self):
        """Allow unpacking."""
        return iter((self.command, self.floor))


@dataclass
class ElevatorHistory:
    """Tracking for an elevator's command history."""

    _events: List[ElevatorEvent] = field(default_factory=list)

    def __iter__(self) -> Iterator[ElevatorEvent]:
        return iter(self._events)

    def __len__(self) -> int:
        return len(self._events)

    def track(self, command: str, floor: int) -> None:
        """Create an event for the command used and resulting floor.

        Args:
          command (str): the command last used.
          floor (int): the floor the elevator was on after executing
            the command.
        """
        self._events.append(ElevatorEvent(command=command, floor=floor))


class Elevator:
    """An elevator for navigating a large apartment building.

    Attributes:
      floor (int): the current floor the elevator's on.
      history (ElevatorHistory): record of the elevator's movements.
    """

    def __init__(
        self, floor: int = 0, history: Optional[ElevatorHistory] = None
    ) -> None:
        """Initialize an elevator at the given floor."""
        self.floor = floor
        self.history = history or ElevatorHistory()

    def execute(self, commands: str) -> int:
        """Follow a string of commands to a destination.

        Args:
          commands (str): the command characters to follow.

        Returns:
          (int): the final destination floor.
        """
        for command in commands:
            self._execute(command)

        return self.floor

    def _execute(self, command: str) -> None:
        """Change floors per command and track the movement."""
        self.floor = CHAR_TO_COMMAND_MAP[command](self.floor)
        self.history.track(command, self.floor)


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_01_part_1.txt") as data:
        # Remove the trailing newline.
        commands = data.read()[:-1]

    elevator = Elevator()
    print(f"Part 1: {elevator.execute(commands)}")
    for position, event in enumerate(elevator.history, start=1):
        if event.floor == -1:
            print(position)
            break
