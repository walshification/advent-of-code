"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise
logic gates! Unfortunately, little Bobby is a little under the
recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a
16-bit signal (a number from 0 to 65535). A signal is provided to each
wire by a gate, another wire, or some specific value. Each wire can
only get a signal from one source, but can provide its signal to
multiple destinations. A gate provides no signal until all of its
inputs have a signal.

The included instructions booklet describes how to connect the parts
together: x AND y -> z means to connect wires x and y to an AND gate,
and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is
      provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by
      2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire
      e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).
If, for some reason, you'd like to emulate the circuit instead, almost
all programming languages (for example, C, JavaScript, or Python)
provide operators for these gates.

In little Bobby's kit's instructions booklet (provided as your puzzle
input), what signal is ultimately provided to wire a?

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal,
and reset the other wires (including wire a). What new signal is
ultimately provided to wire a?
"""
from typing import Dict, List


def AND(left: int, right: int) -> int:
    return left & right


def OR(left: int, right: int) -> int:
    return left | right


def LSHIFT(left: int, right: int) -> int:
    return left << right


def RSHIFT(left: int, right: int) -> int:
    return left >> right


def NOT(left: int, right: int) -> int:
    return ~left & right


BITSHIFT_OPERATIONS = {
    "AND": AND,
    "OR": OR,
    "LSHIFT": LSHIFT,
    "RSHIFT": RSHIFT,
    "NOT": NOT,
}


class Circuit:
    """An object that applies values and bitwise operations to a set of
    logic gates via instructions.
    """

    def __init__(self, wire_map: Dict[str, str]) -> None:
        self._wire_map = wire_map

    @classmethod
    def build(cls, instructions: List[str]) -> "Circuit":
        """Build board out of instructions."""
        wire_map = {}
        for instruction in instructions:
            signal, target = instruction.split(" -> ")
            wire_map[target] = signal

        return cls(wire_map)

    def trace(self, wire_name: str) -> int:
        """Trace a wire back through gates to its source and resolve
        its signal.
        """
        return self.resolve(self._wire_map[wire_name], wire_name)

    def resolve(self, recipe: str, target: str) -> int:
        """Return the signal value of a given operation recipe.

        Args:
          recipe (str): a forumla for a signal value. One of:
            * a wire name (e.g. "x")
            * a signal (e.g. "123")
            * a bitwise operation involving wires (e.g. "x & y")
            * a bitwise operation involving signals (e.g. "1 | x")
          target (str): the wire name for the resulting signal.

        Returns:
          (int): the signal value after all recipes are resolved.
        """
        # If recipe is a signal (e.g. "123"), cache and return its value.
        if recipe.isdigit():
            self._wire_map[target] = recipe
            return int(recipe)

        # If recipe is a wire name (e.g. "x"), trace that to its signal value.
        if recipe in self._wire_map:
            return self.trace(recipe)

        return self._bitshift(recipe, target)

    def _bitshift(self, recipe: str, target: str) -> int:
        """Return the result of a bitwise operation."""
        if "NOT" in recipe:
            operator, left = recipe.split()
            right = "0xFFFF"
        else:
            left, operator, right = recipe.split()

        left_signal = self.trace(left) if not left.isnumeric() else int(left)

        if right == "0xFFFF":
            right_signal = 0xFFFF
        elif right.isnumeric():
            right_signal = int(right)
        else:
            right_signal = self.trace(right)

        result = BITSHIFT_OPERATIONS[operator](left_signal, right_signal)
        # cache result
        self._wire_map[target] = str(result)
        return result


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_07.txt") as data:
        instructions = [instruction[:-1] for instruction in data]

    circuit = Circuit.build(instructions)
    signal_a = circuit.trace("a")
    print(f"Part 1: {signal_a}")

    circuit = Circuit.build(instructions)
    circuit._wire_map["b"] = str(signal_a)
    print(f"Part 2: {circuit.trace('a')}")
