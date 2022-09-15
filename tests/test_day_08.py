from aoc_2015.day_08 import SpaceCounter


def test_counter_adds_2_to_code_count_for_surrounding_quotes():
    counter = SpaceCounter("")
    assert counter.code_size == 2


def test_counter_counts_in_memory_size():
    counter = SpaceCounter("")
    assert counter.in_memory_size == 0


def test_counter_counts_normal_characters():
    counter = SpaceCounter("abc")
    assert counter.code_size == 5
    assert counter.in_memory_size == 3


def test_counter_accounts_for_escaped_characters():
    counter = SpaceCounter("aaa\"aaa")  # fmt: skip
    assert counter.code_size == 10
    assert counter.in_memory_size == 7
