"""
--- Day 6: Tuning Trouble ---

The preparations are finally complete; you and the Elves leave camp on
foot and begin to make your way toward the star fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a
handheld device. He says that it has many fancy features, but the most
important one to set up right now is the communication system.

However, because he's heard you have significant experience dealing with
signal-based systems, he convinced the other Elves that it would be okay
to give you their one malfunctioning device - surely you'll have no
problem fixing it.

As if inspired by comedic timing, the device emits a few colorful
sparks.

To be able to communicate with the Elves, the device needs to lock on to
their signal. The signal is a series of seemingly-random characters that
the device receives one at a time.

To fix the communication system, you need to add a subroutine to the
device that detects a start-of-packet marker in the datastream. In the
protocol being used by the Elves, the start of a packet is indicated by
a sequence of four characters that are all different.

The device will send your subroutine a datastream buffer (your puzzle
input); your subroutine needs to identify the first position where the
four most recently received characters were all different. Specifically,
it needs to report the number of characters from the beginning of the
buffer to the end of the first such four-character marker.

How many characters need to be processed before the first
start-of-packet marker is detected?

--- Part Two ---

Your device's communication system is correctly detecting packets, but
still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except
it consists of 14 distinct characters rather than 4.

How many characters need to be processed before the first
start-of-message marker is detected?
"""
from collections import deque
from dataclasses import dataclass
from typing import Deque, Optional


@dataclass
class Receiver:
    """Malfunctioning Elven communication device."""

    signal: str

    def find_marker(self, marker_length: int = 4) -> Optional[int]:
        """Return the first position after the first four unique
        characters in the signal.
        """
        buffer: Deque[str] = deque()
        for i, char in enumerate(self.signal):
            buffer.append(char)
            if len(buffer) == marker_length:
                if self.is_unique(buffer):
                    return i + 1

                buffer.popleft()
        return None

    def is_unique(self, buffer) -> bool:
        """Return whether or not buffer characters are unique."""
        return len(set(buffer)) == len(buffer)


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_06.txt") as data:
        signal = data.readline()

    receiver = Receiver(signal)

    print(f"Part One: {receiver.find_marker()}")
    print(f"Part Two: {receiver.find_marker(14)}")
