"""
--- Day 10: Cathode-Ray Tube ---

You avoid the ropes, plunge into the river, and swim to shore.

The Elves yell something about meeting back up with them upriver, but
the river is too loud to tell exactly what they're saying. They finish
crossing the bridge and disappear from view.

Situations like this must be why the Elves prioritized getting the
communication system on your handheld device working. You pull it out of
your pack, but the amount of water slowly draining from a big crack in
its screen tells you it probably won't be of much immediate use.

Unless, that is, you can design a replacement for the device's video
system! It seems to be some kind of cathode-ray tube screen and simple
CPU that are both driven by a precise clock circuit. The clock circuit
ticks at a constant rate; each tick is called a cycle.

Start by figuring out the signal being sent by the CPU. The CPU has a
single register, X, which starts with the value 1. It supports only two
instructions:

    addx V takes two cycles to complete. After two cycles, the X
        register is increased by the value V. (V can be negative.)
    noop takes one cycle to complete. It has no other effect.

The CPU uses these instructions in a program (your puzzle input) to,
somehow, tell the screen what to draw.

Consider the following small program:

noop
addx 3
addx -5

Execution of this program proceeds as follows:

    At the start of the first cycle, the noop instruction begins
        execution. During the first cycle, X is 1. After the first
        cycle, the noop instruction finishes execution, doing nothing.
    At the start of the second cycle, the addx 3 instruction begins
        execution. During the second cycle, X is still 1.
    During the third cycle, X is still 1. After the third cycle, the
        addx 3 instruction finishes execution, setting X to 4.
    At the start of the fourth cycle, the addx -5 instruction begins
        execution. During the fourth cycle, X is still 4.
    During the fifth cycle, X is still 4. After the fifth cycle, the
        addx -5 instruction finishes execution, setting X to -1.

Maybe you can learn something by looking at the value of the X register
throughout execution. For now, consider the signal strength (the cycle
number multiplied by the value of the X register) during the 20th cycle
and every 40 cycles after that (that is, during the 20th, 60th, 100th,
140th, 180th, and 220th cycles).

Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and
220th cycles. What is the sum of these six signal strengths?

--- Part Two ---

It seems like the X register controls the horizontal position of a
sprite. Specifically, the sprite is 3 pixels wide, and the X register
sets the horizontal position of the middle of that sprite. (In this
system, there is no such thing as "vertical position": if the sprite's
horizontal position puts its pixels where the CRT is currently drawing,
then those pixels will be drawn.)

You count the pixels on the CRT: 40 wide and 6 high. This CRT screen
draws the top row of pixels left-to-right, then the row below that, and
so on. The left-most pixel in each row is in position 0, and the
right-most pixel in each row is in position 39.

Like the CPU, the CRT is tied closely to the clock circuit: the CRT
draws a single pixel during each cycle. Representing each pixel of the
screen as a #, here are the cycles during which the first and last pixel
in each row are drawn:

Cycle   1 -> ######################################## <- Cycle  40
Cycle  41 -> ######################################## <- Cycle  80
Cycle  81 -> ######################################## <- Cycle 120
Cycle 121 -> ######################################## <- Cycle 160
Cycle 161 -> ######################################## <- Cycle 200
Cycle 201 -> ######################################## <- Cycle 240

So, by carefully timing the CPU instructions and the CRT drawing
operations, you should be able to determine whether the sprite is
visible the instant each pixel is drawn. If the sprite is positioned
such that one of its three pixels is the pixel currently being drawn,
the screen produces a lit pixel (#); otherwise, the screen leaves the
pixel dark (.).

Render the image given by your program. What eight capital letters appear on your CRT?
"""
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Tuple


def noop(strength: str = "0") -> List[int]:
    return [int(strength)]


def addx(strength: str) -> List[int]:
    return [0, int(strength)]


CPU_COMMANDS: Dict[str, Callable] = {
    "noop": noop,
    "addx": addx,
}


@dataclass
class CRT:
    """The CRT of my busted Elven communication device."""

    pixels: List[str] = field(default_factory=list)
    row_length: int = 40
    row_count: int = 6

    def __post_init__(self) -> None:
        self.pixels = ["." for _ in range(self.row_length * self.row_count)]

    def __str__(self) -> str:
        return "\n".join(
            "".join(str(pixel) for pixel in self.pixels[i : i + self.row_length])
            for i in range(0, len(self.pixels), self.row_length)
        )

    def render(self, beam_index: int, cpu_register: int) -> None:
        """Render on the CRT the signal in the CPU register at the pixel
        for the cycle.
        """
        if beam_index % 40 in (cpu_register - 1, cpu_register, cpu_register + 1):
            self.pixels[beam_index] = "#"


@dataclass
class CPU:
    """The CPU of my busted Elven communication device."""

    register: int = 1
    cycles: List = field(default_factory=list)
    key_strengths: List = field(default_factory=list)
    key_cycles: List = field(default_factory=list)
    crt: CRT = field(default_factory=CRT)

    def __post_init__(self) -> None:
        self.key_cycles.extend([220, 180, 140, 100, 60, 20])

    def run(self, instructions: Tuple[str, ...]) -> int:
        """Return signal strength of the 20th, 60th, 100th, 140th,
        180th, and 220th cycles.
        """
        for instruction in instructions:
            self.execute(instruction)

        return sum(self.key_strengths)

    def execute(self, instruction: str):
        command, *args = instruction.split()
        signals = CPU_COMMANDS[command](*args)

        for signal in signals:
            self.cycle(signal)

    def cycle(self, signal: int) -> None:
        self.cycles.append(signal)

        if len(self.cycles) in self.key_cycles:
            key = self.key_cycles.pop()
            self.key_strengths.append(self.register * key)

        self.crt.render(len(self.cycles) - 1, self.register)
        self.register += signal


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_10.txt") as data:
        instructions = tuple(line[:-1] for line in data)

    cpu = CPU()
    print(f"Part One: {cpu.run(instructions)}")
    print(f"Part Two:\n{cpu.crt}")
