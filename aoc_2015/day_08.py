"""
--- Day 8: Matchsticks ---

Space on the sleigh is limited this year, and so Santa will be bringing
his list as a digital copy. He needs to know how much space it will
take up when stored.

It is common in many programming languages to provide a way to escape
special characters in strings. For example, C, JavaScript, Perl,
Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number
of characters in the code representation of the string literal and the
number of characters in the in-memory string itself.

Santa's list is a file that contains many double-quoted string
literals, one on each line. The only escape sequences used are \\
(which represents a single backslash), \" (which represents a lone
double-quote character), and \\x plus two hexadecimal characters (which
represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of
characters of code for string literals minus the number of characters
in memory for the values of the strings in total for the entire file?
"""
import re
from dataclasses import dataclass
from typing import List


slash = re.compile(r"\\{2}")
quote = re.compile(r"\\\"")
special = re.compile(r"\\x[\d\w]{2}")
normal = re.compile(r"[^\\{2}|\\\"|\\x[\d\w]{2}]?")


class CodeSizer:

    @classmethod
    def calculate_code_size(cls, string: str) -> int:
        """"""
        return sum(
            [
                cls.get_slash_count(string),
                cls.get_quote_count(string),
                cls.get_special_count(string),
                cls.get_normal_count(string),
            ]
        )

    @classmethod
    def get_quote_count(cls, string: str) -> int:
        """Return the number of escaped quotation characters found."""
        return len(quote.findall(string)) * 2

    @classmethod
    def get_slash_count(cls, string: str) -> int:
        """Return the number of escaped slash characters found."""
        return len(slash.findall(string)) * 2

    @classmethod
    def get_special_count(cls, string: str) -> int:
        """Return the number of escaped special characters found."""
        return len(special.findall(string)) * 4

    @classmethod
    def get_normal_count(cls, string: str) -> int:
        """Return the number of normal characters found plus 2 for the
        enclosing quotation marks.
        """
        return len(normal.findall(string)) + 2


        return sum(
            [
                normal_character_length,
                slash_length
                # len(quote.findall(string)),
                # len(special_character.findall(string)),
                # len(string) - (3 * slash_length),
            ]
        )


@dataclass
class SpaceCounter:
    """Counter for in-memory and code size of strings."""

    def __init__(self, strings: str = None) -> None:
        self.strings = strings or []
        self.code_sizer = size_for_code

    def count(self) -> int:
        """"""
        return sum(
            [
                self.get_code_size(string) - self.get_in_memory_size(string)
                for string in self.strings
            ]
        )

    def get_code_size(self, string: str) -> int:
        """Return the size of the code characters of a string."""
        return self.code_sizer(string)
        # return sum(
        #     [
        #         len(slash.findall(string)),
        #         len(quote.findall(string)),
        #         len(string)
        #     ]
        # )

    def get_in_memory_size(self, string: str) -> int:
        """Return the size of the in-memory characters of a string."""
        return sum(
            [
                len(string),
                # Correct the count for memory.
                -len(special_character.findall(string)) * 3,
                -2,  # Account for quotation marks
            ]
        )


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_08.txt") as data:
        strings = [string[:-1] for string in data]

    counter = SpaceCounter(strings)
    print(f"Part 1: {counter.count()}")
