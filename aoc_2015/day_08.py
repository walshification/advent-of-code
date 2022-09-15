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
from dataclasses import dataclass


@dataclass
class SpaceCounter:
    """"""

    def __init__(self, string: str) -> None:
        self.string = string

    @property
    def code_size(self) -> int:
        """Return the size of the code characters of a string."""
        return sum([self._count_for_code(c) for c in self.string]) + 2

    @property
    def in_memory_size(self) -> int:
        """Return the size of the in-memory characters of a string."""
        return sum([self._count_for_memory(c) for c in self.string])

    def _count_for_code(self, char: str) -> int:
        """Return the size value for the character.

        Escaped characters are actually 2 characters.
        """
        if char in ['"', "\\"]:
            return 2
        return 1

    def _count_for_memory(self, char: str) -> int:
        """Return the size value for the character."""
        return 1
