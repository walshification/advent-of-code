from aoc_2022.day_10 import Cpu


def test_performs_noop():
    cpu = Cpu()
    cpu.cycle(("noop",))
    assert cpu.register == 1
    assert cpu.cycles == [0]
