"""
--- Day 9: Rope Bridge ---

This rope bridge creaks as you walk along it. You aren't sure how old it
is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a
gorge which was carved out by the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide
to distract yourself by modeling rope physics; maybe you can even figure
out where not to step.

Consider a rope with a knot at each end; these knots mark the head and
the tail of the rope. If the head moves far enough away from the tail,
the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able
to model the positions of the knots on a two-dimensional grid. Then, by
following a hypothetical series of motions (your puzzle input) for the
head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short;
in fact, the head (H) and tail (T) must always be touching (diagonally
adjacent and even overlapping both count as touching):

....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...

If the head is ever two steps directly up, down, left, or right from the
tail, the tail must also move one step in that direction so it remains
close enough:

.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -> ... -> .T.
...    .H.    .H.
...    ...    ...

Otherwise, if the head and tail aren't touching and aren't in the same
row or column, the tail always moves one step diagonally to keep up:

.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -> ...H. -> ..TH.
.T...    .T...    .....
.....    .....    .....

You just need to work out where the tail goes as the head follows a
series of motions. Assume the head and the tail both start at the same
position, overlapping.

Simulate your complete hypothetical series of motions. How many
positions does the tail of the rope visit at least once?
"""
from dataclasses import dataclass, field
from typing import Iterator, List, Tuple


@dataclass
class History:
    """Tracking for a series of events."""

    _events: List[Tuple[int, int]] = field(default_factory=list)

    def __iter__(self) -> Iterator[Tuple[int, int]]:
        return iter(self._events)

    def __str__(self) -> int:
        right = max(event[1] for event in self._events)
        left = min(event[1] for event in self._events)
        top = min(event[0] for event in self._events)
        bottom = max(event[0] for event in self._events)
        return "\n".join(
            "".join(
                "#" if (y, x) in self._events else "." for x in range(left, right + 1)
            )
            for y in range(top, bottom + 1)
        )

    def track(self, event: Tuple[int, int]) -> None:
        """Add an event to history."""
        self._events.append(event)


@dataclass
class Rope:

    DIRECTION_TO_MOTION_MAP = {
        "R": (0, 1),
        "U": (-1, 0),
        "L": (0, -1),
        "D": (1, 0),
    }

    head: Tuple[int, int] = (0, 0)
    tail: Tuple[int, int] = (0, 0)
    history: History = History()

    @property
    def is_too_far(self) -> bool:
        return (
            abs(self.head[0] - self.tail[0]) > 1 or abs(self.head[1] - self.tail[1]) > 1
        )

    def move(self, motions: Tuple[str, ...]) -> int:
        """Follow a string of commands to a destination.

        Args:
            motions: the direction and distance to follow.

        Returns:
            The new position of the head.
        """
        self.history.track(self.tail)
        for motion in motions:
            self._execute(motion)

        return len(set(self.history))

    def _execute(self, motion: str) -> None:
        """Follow a motion with head and tail and record the event."""
        direction, distance = motion.split()
        delta_y, delta_x = self.DIRECTION_TO_MOTION_MAP[direction]
        for _ in range(int(distance)):
            current_y, current_x = self.head
            self.head = current_y + delta_y, current_x + delta_x
            if self.is_too_far:
                self.tail = self.follow_the_head()
                self.history.track(self.tail)

    def follow_the_head(self) -> Tuple[int, int]:
        new_y = self.tail[0]
        new_x = self.tail[1]
        if self.head[0] - self.tail[0] != 0:
            new_y += int(
                (self.head[0] - self.tail[0]) / abs(self.head[0] - self.tail[0])
            )
        if self.head[1] - self.tail[1] != 0:
            new_x += int(
                (self.head[1] - self.tail[1]) / abs(self.head[1] - self.tail[1])
            )
        return new_y, new_x


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_09.txt") as data:
        motions = tuple(line[:-1] for line in data)

    rope = Rope()
    positions = rope.move(motions)
    print(f"Part One: {positions}")
