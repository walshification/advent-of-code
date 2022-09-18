from aoc_2015.day_08 import SpaceCounter, CodeSizer, MemorySizer


def test_code_sizer_measures_slash():
    assert CodeSizer.get_slash_count('"\\\\"') == 2


def test_code_sizer_measures_quotes():
    assert CodeSizer.get_quote_count('"\\""') == 2


def test_code_sizer_measures_special_characters():
    assert CodeSizer.get_special_count('"\\x27"') == 4


def test_code_sizer_measures_normal_characters():
    assert CodeSizer.get_normal_count('"\\\\k\\"l\\x27"') == 2


def test_code_sizer_measures_slash_quote_and_character_count():
    assert CodeSizer.calculate_code_size('"\\"\\\\l\\x27"') == 10


def test_memory_sizer_measures_slash():
    assert MemorySizer.get_slash_count('"\\\\"') == 1


def test_memory_sizer_measures_quotes():
    assert MemorySizer.get_quote_count('"\\""') == 1


def test_memory_sizer_measures_special_characters():
    assert MemorySizer.get_special_count('"\\x27"') == 1


def test_memory_sizer_measures_normal_characters():
    assert MemorySizer.get_normal_count('"\\\\k\\"l\\x27"') == 2


def test_memory_sizer_measures_slash_quote_and_character_count():
    assert MemorySizer.calculate_memory_size('"\\"\\\\l\\x27"') == 4


# def test_counter_adds_2_to_code_count_for_surrounding_quotes():
#     counter = SpaceCounter()
#     assert counter.get_code_size('""') == 2


# def test_counter_counts_in_memory_size():
#     counter = SpaceCounter()
#     assert counter.get_in_memory_size('""') == 0


# def test_counter_counts_normal_characters():
#     counter = SpaceCounter()
#     assert counter.get_code_size('"abc"') == 5
#     assert counter.get_in_memory_size('"abc"') == 3


# def test_counter_counts_normal_characters():
#     counter = SpaceCounter()
#     assert counter.get_code_size('"\\\\"') == 3
#     assert counter.get_in_memory_size('"\\\\"') == 1


# def test_counter_accounts_for_escaped_characters():
#     counter = SpaceCounter()
#     assert counter.get_code_size('"aaa\\"aaa"') == 10  # fmt: skip
#     assert counter.get_in_memory_size('"aaa\\"aaa"') == 7  # fmt: skip


# def test_counter_accounts_for_weird_characters():
#     counter = SpaceCounter()
#     assert counter.get_code_size('"\\x27"') == 6
#     assert counter.get_in_memory_size('"\\x27"') == 1


# def test_counter_accounts_for_weird_characters():
#     counter = SpaceCounter(['"\\x27"'])
#     assert counter.count() == 5


# '"\\""',
# '"santipvuiq"',
# '"\\"ihjqlhtwbuy\\"hdkiv\\"mtiqacnf\\\\"',
# '"oliaggtqyyx"',
# '"fwwnpmbb"',
# '"yrtdrieazfxyyneo"',
# '"nywbv\\\\"',
# '"twc\\\\ehfqxhgomgrgwpxyzmnkioj"',
# '"qludrkkvljljd\\\\xvdeum\\x4e"'
