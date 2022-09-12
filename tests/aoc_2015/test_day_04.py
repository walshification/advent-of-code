import hashlib
from unittest.mock import create_autospec

from aoc_2015.day_04 import main


def test_main_finds_number_that_matches_key():
    hash_object = create_autospec(hashlib._hashlib.HASH)
    hash_object.hexdigest.return_value == "000123"
    hash_func = create_autospec(hashlib.md5, return_value=hash_object)
    number = main("000", secret_key="blah", hash_func=hash_func)
    assert number == 0


def test_main_keeps_going_until_a_match():
    hash_object = create_autospec(hashlib._hashlib.HASH)
    hash_object.hexdigest.side_effect = ["blorp123", "000123"]
    hash_func = create_autospec(hashlib.md5, return_value=hash_object)
    number = main("000", secret_key="blah", hash_func=hash_func)
    assert number == 1
    assert hash_func.call_count == 2
