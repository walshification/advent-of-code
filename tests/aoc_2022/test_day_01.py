from aoc_2022.day_01 import Elf, ElfStats


def test_stats_track_elves():
    elf = Elf()
    top_elves = {elf.total_calories: elf}
    stats = ElfStats([elf])
    assert stats.top_elf == elf
    assert stats.top_3_elves == top_elves


def test_stats_replace_top_elf():
    low_elf = Elf([0])
    top_elf = Elf([1])

    # Initialize with the low Elf.
    stats = ElfStats([low_elf])
    stats.check_for_top_elf(top_elf)

    assert stats.top_elf == top_elf


def test_stats_keep_top_elf():
    low_elf = Elf([0])
    top_elf = Elf([1])

    # Initialize with the top Elf.
    stats = ElfStats([top_elf])
    stats.check_for_top_elf(low_elf)

    assert stats.top_elf == top_elf


def test_stats_replaces_top_3():
    low_elf = Elf([0])
    top_elf = Elf([3])

    stats = ElfStats([Elf([2]), Elf([1]), low_elf])
    stats.check_for_top_elf(top_elf)

    top_3 = stats.top_3_elves.values()
    assert top_elf in top_3
    assert low_elf not in top_3


def test_stats_keep_top_3():
    third_elf = Elf([1])
    low_elf = Elf([0])
    top_elf = Elf([3])

    stats = ElfStats([top_elf, Elf([2]), third_elf])
    stats.check_for_top_elf(low_elf)

    top_3 = stats.top_3_elves.values()
    assert third_elf in top_3
    assert low_elf not in top_3


def test_stats_keeps_top_elf_for_second_place():
    new_third = Elf([1])
    low_elf = Elf([0])
    top_elf = Elf([3])

    stats = ElfStats([top_elf, Elf([2]), low_elf])
    stats.check_for_top_elf(new_third)

    top_3 = stats.top_3_elves.values()
    assert new_third in top_3
    assert low_elf not in top_3
    assert stats.top_elf == top_elf


def test_stats_sorts_from_a_calories_list():
    stats = ElfStats.from_calories_list(["3", "3", "\n", "2", "\n", "\n"])
    assert stats.top_elf.total_calories == 6
    assert stats.top_3_calories == 8
