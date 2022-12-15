from aoc_2022.day_09 import Rope


def test_tail_follows_the_head():
    rope = Rope()
    motions = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]
    positions = rope.move(motions)
    print(rope.history)
    assert positions == 13
