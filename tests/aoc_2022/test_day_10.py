from aoc_2022.day_10 import Cpu


def test_performs_noop():
    cpu = Cpu()
    cpu.execute(("noop",))
    assert cpu.register == 1
    assert cpu.cycles == [0]


def test_performs_addx():
    cpu = Cpu()
    cpu.execute(("addx 3",))
    assert cpu.register == 4
    assert cpu.cycles == [0, 3]
