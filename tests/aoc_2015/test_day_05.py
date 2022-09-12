from aoc_2015.day_05 import (
    main,
    validate_double_letters,
    validate_pair_of_pairs,
    validate_skipped_repeating_letters,
    validate_special_letters,
    validate_vowels,
)


def test_validate_vowels_returns_true_when_three_or_more():
    assert validate_vowels("akekik")


def test_validate_vowels_returns_false_when_less_than_three():
    assert not validate_vowels("akekk")


def test_validate_vowels_can_be_same():
    assert validate_vowels("akakak")


def test_validate_double_letters_finds_double_letters():
    assert validate_double_letters("asddf")


def test_validate_double_letters_returns_false_if_no_double_letters():
    assert not validate_double_letters("asdfd")


def test_validate_special_letters_returns_false_for_special_letters():
    assert not validate_special_letters("ascdfd")


def test_validate_special_letters_returns_true_if_no_special_letters():
    assert validate_special_letters("asdfdb")


def test_validate_pair_of_pairs_finds_double_pairs_in_string():
    assert validate_pair_of_pairs("abab")
    assert validate_pair_of_pairs("abasdfab")


def test_validate_pair_of_pairs_returns_false_if_none():
    assert not validate_pair_of_pairs("acab")
    assert not validate_pair_of_pairs("abasdfcb")


def test_validate_skipped_repeating_letters_finds_them():
    assert validate_skipped_repeating_letters("xyx")
    assert validate_skipped_repeating_letters("asdfdlkj")


def test_validate_skipped_repeating_letters_returns_false_if_none():
    assert not validate_skipped_repeating_letters("xayx")


def test_main_runs_validators_on_strings_and_returns_number_that_pass():
    good_count = main(["akeddik"])
    assert good_count == 1

    good_count = main(["akeddik", "ascollub"])
    assert good_count == 2


def test_main_skips_strings_that_fail_validation():
    good_count = main(["akeddk", "ascolub", "ascolluab"])
    assert good_count == 0
