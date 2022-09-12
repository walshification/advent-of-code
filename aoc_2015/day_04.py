"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to
use as gifts for all the economically forward-thinking little girls and
boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start
with at least five zeroes. The input to the MD5 hash is some secret key
(your puzzle input, given below) followed by a number in decimal. To
mine AdventCoins, you must find Santa the lowest positive number (no
leading zeroes: 1, 2, 3, ...) that produces such a hash.

--- Part Two ---

Now find one that starts with six zeroes.
"""
from hashlib import md5


SECRET_KEY = "iwrupvqb"


def infinite_sequence(start=0):
    """Yield an infinite number of numbers."""
    n = start
    while True:
        yield n
        n += 1


def main(
    adventcoin_key: str,
    sequence_start: int = 0,
    secret_key: str = SECRET_KEY,
    hash_func=md5,
) -> int:
    """Return the lowest number that combines with the secret_key to
    produce an MD5 hash that begins with the adventcoin_key.
    """
    number_generator = infinite_sequence(sequence_start)
    number = None
    while number is None:
        n = next(number_generator)
        if (
            hash_func(f"{secret_key}{n}".encode())
            .hexdigest()
            .startswith(adventcoin_key)
        ):
            number = n

    return number


if __name__ == "__main__":
    five_zeros = main("00000")
    print(f"Part 1: {five_zeros}")
    print(f"Part 2: {main('000000', sequence_start=five_zeros + 1)}")
