"""
--- Day 13: Distress Signal ---

You climb the hill and again try contacting the Elves. However, you
instead receive a signal you weren't expecting: a distress signal.

Your handheld device must still not be working properly; the packets
from the distress signal got decoded out of order. You'll need to
re-order the list of received packets (your puzzle input) to decode the
message.

Your list consists of pairs of packets; pairs are separated by a blank
line. You need to identify how many pairs of packets are in the right
order.

Packet data consists of lists and integers. Each list starts with [,
ends with ], and contains zero or more comma-separated values (either
integers or other lists). Each packet is always a list and appears on
its own line.

When comparing two values, the first value is called left and the second
value is called right. Then:

    If both values are integers, the lower integer should come first. If
        the left integer is lower than the right integer, the inputs are
        in the right order. If the left integer is higher than the right
        integer, the inputs are not in the right order. Otherwise, the
        inputs are the same integer; continue checking the next part of
        the input.
    If both values are lists, compare the first value of each list, then
        the second value, and so on. If the left list runs out of items
        first, the inputs are in the right order. If the right list runs
        out of items first, the inputs are not in the right order. If
        the lists are the same length and no comparison makes a decision
        about the order, continue checking the next part of the input.
    If exactly one value is an integer, convert the integer to a list
        which contains that integer as its only value, then retry the
        comparison. For example, if comparing [0,0,0] and 2, convert the
        right value to [2] (a list containing 2); the result is then
        found by instead comparing [0,0,0] and [2].

What are the indices of the pairs that are already in the right order?
(The first pair has index 1, the second pair has index 2, and so on.)

Determine which pairs of packets are already in the right order. What is
the sum of the indices of those pairs?

--- Part Two ---

Now, you just need to put all of the packets in the right order.
Disregard the blank lines in your list of received packets.

The distress signal protocol also requires that you include two
additional divider packets:

[[2]]
[[6]]

Using the same rules as before, organize all packets - the ones in your
list of received packets as well as the two divider packets - into the
correct order.

For the example above, the result of putting the packets in the correct
order is:

[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]

Afterward, locate the divider packets. To find the decoder key for this
distress signal, you need to determine the indices of the two divider
packets and multiply them together. (The first packet is at index 1, the
second packet is at index 2, and so on.) In this example, the divider
packets are 10th and 14th, and so the decoder key is 140.

Organize all of the packets into the correct order. What is the decoder
key for the distress signal?
"""
import json
from itertools import zip_longest
from typing import Optional


def validate(left, right) -> Optional[bool]:
    """Return whether two lists are in the right order."""
    for left_item, right_item in zip_longest(left, right):
        if left_item is None:
            return True

        if right_item is None:
            return False

        if type(left_item) == int and type(right_item) == int:
            if right_item < left_item:
                return False

            if left_item < right_item:
                return True

        if type(left_item) == list and type(right_item) != list:
            return validate(left_item, [right_item])

        if type(right_item) == list and type(left_item) != list:
            return validate([left_item], right_item)

        if type(left_item) == list and type(right_item) == list:
            result = validate(left_item, right_item)
            if result is not None:
                return result
    return None


def compare(pairs) -> int:
    """Return the sum of the indices of pairs in the right order."""
    return sum(
        pair_index for pair_index, pair in enumerate(pairs, start=1) if validate(*pair)
    )


def sort(pairs):
    """For each packet in the signal, sort the packets per the rules."""
    sorted_signal = [[[2]], [[6]]]
    for pair in pairs:
        for packet in pair:
            for index in range(len(sorted_signal)):
                print(index)
                print(sorted_signal)
                sorted_packet = sorted_signal.pop(index)
                if validate(packet, sorted_packet):
                    sorted_signal.insert(index, packet)
                    sorted_signal.insert(index + 1, sorted_packet)
                    break
                else:
                    sorted_signal.insert(index, sorted_packet)

    for item in sorted_signal:
        print(item)
    return [
        index + 1
        for index in range(len(sorted_signal))
        if sorted_signal[index] == [[2]]
    ][0] * [
        index + 1
        for index in range(len(sorted_signal))
        if sorted_signal[index] == [[6]]
    ][
        0
    ]


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_13.txt") as data:
        pairs = [[]]  # type: ignore
        for line in data:
            try:
                packet = json.loads(line)
                pairs[-1].append(packet)
            except json.JSONDecodeError:
                pairs.append([])

    print(f"Part One: {compare(pairs)}")
    print(f"Part Two: {sort(pairs)}")
