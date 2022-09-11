from aoc_2015.day_01 import Elevator


def test_elevator_goes_up():
    elevator = Elevator()
    assert elevator.floor == 0
    elevator.execute("(")
    assert elevator.floor == 1


def test_elevator_goes_down():
    elevator = Elevator()
    assert elevator.floor == 0
    elevator.execute(")")
    assert elevator.floor == -1


def test_elevator_follows_many_commands():
    elevator = Elevator()
    elevator.execute("(()(()(")
    assert elevator.floor == 3


def test_elevator_keeps_log_of_movements():
    elevator = Elevator()
    elevator.execute("(()")
    assert len(elevator.history) == 3
    assert tuple((command, floor) for command, floor in elevator.history) == (
        ("(", 1),
        ("(", 2),
        (")", 1),
    )
