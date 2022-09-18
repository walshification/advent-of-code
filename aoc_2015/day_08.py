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

--- Part Two ---

Now, let's go the other way. In addition to finding the number of
characters of code, you should now encode each code representation as a
new string and find the number of characters of the new encoded
representation, including the surrounding double quotes.

Your task is to find the total number of characters to represent the
newly encoded strings minus the number of characters of code in each
original string literal. For example, for the strings above, the total
encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the
original code representation (23, just like in the first part of this
puzzle) is 42 - 23 = 19.
"""
import ast
import re
from dataclasses import dataclass
from typing import List


slash = re.compile(r"\\\\(?:(?!\\)|(?!\")|(?<!\\))")
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
                cls.get_quote_count(string[1:-1]),
                cls.get_special_count(string),
                cls.get_normal_count(string),
                2,  # enclosing quotation marks
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
        """Return the length of string after removing escaped quotes,
        slashes, and special characters.
        """
        return len(quote.sub("", slash.sub("", special.sub("", string)))) - 2


class MemorySizer:
    @classmethod
    def calculate_memory_size(cls, string: str) -> int:
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
        """Return the number of quotation characters rendered."""
        return len(quote.findall(string))

    @classmethod
    def get_slash_count(cls, string: str) -> int:
        """Return the number of slash characters rendered."""
        return len(slash.findall(string))

    @classmethod
    def get_special_count(cls, string: str) -> int:
        """Return the number of special characters rendered."""
        return len(special.findall(string))

    @classmethod
    def get_normal_count(cls, string: str) -> int:
        """Return the number of normal characters."""
        slash_count = cls.get_slash_count(string)
        quote_count = cls.get_quote_count(string)
        special_count = cls.get_special_count(string)
        return (
            len(string)
            - (slash_count * 2)
            - (quote_count * 2)
            - (special_count * 4)
            - 2
        )


@dataclass
class SpaceCounter:
    """Counter for in-memory and code size of strings."""

    def __init__(self, strings: List[str] = None) -> None:
        self.strings = strings or []
        self.code_sizer = CodeSizer
        self.memory_sizer = MemorySizer

    def count(self) -> int:
        """I found this on the internet."""
        return sum(
            [
                len(string) - len(ast.literal_eval(string))
                # len(string)  # 6489
                for string in self.strings
            ]
        )

    def escaped_count(self) -> int:
        """I found this on the internet."""
        return sum([2 + sum(map(string.count, ['"', "\\"])) for string in self.strings])

    def get_code_size(self, string: str) -> int:
        """Return the size of the code characters of a string."""
        return self.code_sizer.calculate_code_size(string)

    def get_in_memory_size(self, string: str) -> int:
        """Return the size of the in-memory characters of a string."""
        return self.memory_sizer.calculate_memory_size(string)


if __name__ == "__main__":
    with open("aoc_2015/inputs/day_08.txt") as data:
        strings = [string[:-1] for string in data]

    counter = SpaceCounter(strings)
    print(f"Part 1: {counter.count()}")
    print(f"Part 2: {counter.escaped_count()}")
