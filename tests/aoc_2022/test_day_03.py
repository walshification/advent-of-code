from aoc_2022.day_03 import sort, sort_by_group


def test_sort_finds_common_character_in_rucksack_compartments():
    assert sort(["vJrwpWtwJgWrhcsFMMfFFhFp\n"]) == 16


def test_sort_by_group_finds_common_character_in_group_rucksacks():
    assert (
        sort_by_group(
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp\n",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
                "PmmdzqPrVvPwwTWBwg\n",
            ]
        )
        == 18
    )
