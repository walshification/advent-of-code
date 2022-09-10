"""
Day 1: Not Quite Lisp

Santa is trying to deliver presents in a large apartment building, but
he can't find the right floor - the directions he got are a little
confusing. He starts on the ground floor (floor 0) and then follows the
instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a
closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he
will never find the top or bottom floors.
"""


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


class Elevator:
    """An elevator for navigating a large apartment building.

    Attributes:
      floor (int): the current floor the elevator's on.
    """

    def __init__(self, floor: int = 0) -> None:
        """Initialize an elevator at the given floor."""
        self.floor = floor

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({self.floor})>"

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
        """Change floors per a single command."""
        self.floor = CHAR_TO_COMMAND_MAP[command](self.floor)


if __name__ == "__main__":
    with open("2015/inputs/day_01_part_1.txt") as data:
        # Remove the trailing newline.
        commands = data.read()[:-1]

    print(f"Part 1: {Elevator().execute(commands)}")
