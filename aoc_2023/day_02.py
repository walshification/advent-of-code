"""
--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory
just barely reaches the surface of a large island floating in the sky.
You gently land in a fluffy pile of leaves. It's quite cold, but you
don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for
the lack of snow. He'll be happy to explain the situation, but it's a
bit of a walk, so you have some time. They don't get many visitors up
here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are
either red, green, or blue. Each time you play this game, he will hide
a secret number of cubes of each color in the bag, and your goal is to
figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will
reach into the bag, grab a handful of random cubes, show them to you,
and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your
puzzle input). Each game is listed with its ID number (like the 11 in
Game 11: ...) followed by a semicolon-separated list of subsets of cubes
that were revealed from the bag (like 3 red, 5 green, 4 blue).

Determine which games would have been possible if the bag had been
loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What
is the sum of the IDs of those games?

--- Part Two ---

The Elf says they've stopped producing snow because they aren't getting
any water! He isn't sure why the water stopped; however, he can show you
how to get to the water source to check it out for yourself. It's just
up ahead!

As you continue your walk, the Elf poses a second question: in each game
you played, what is the fewest number of cubes of each color that could
have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
    Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
    Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
    Game 4 required at least 14 red, 3 green, and 15 blue cubes.
    Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

"""
from dataclasses import dataclass
from typing import Sequence, Tuple

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14


@dataclass
class Pull:

    red: int
    green: int
    blue: int

    @classmethod
    def from_record(cls, record: str) -> "Pull":
        red_count = 0
        green_count = 0
        blue_count = 0

        cubes = record.split(", ")
        for cube in cubes:
            if "red" in cube:
                red_count += int(cube.replace(" red", ""))
            if "green" in cube:
                green_count += int(cube.replace(" green", ""))
            if "blue" in cube:
                blue_count += int(cube.replace(" blue", ""))

        return cls(red_count, green_count, blue_count)


@dataclass(frozen=True)
class CubeGame:

    id: int
    highest_red: int
    highest_green: int
    highest_blue: int
    pulls: Sequence[Pull]

    @classmethod
    def from_record(cls, record: str) -> "CubeGame":
        title, pulls_record = record.split(": ")
        _id = int(title.split(" ")[1])

        pulls = [Pull.from_record(rec) for rec in pulls_record.split("; ")]
        highest_red, highest_green, highest_blue = cls._calc_highest(pulls)

        return cls(_id, highest_red, highest_green, highest_blue, pulls)

    @classmethod
    def _calc_highest(cls, pulls: Sequence[Pull]) -> Tuple[int, int, int]:
        highest_red = 0
        highest_green = 0
        highest_blue = 0
        for pull in pulls:
            if pull.red > highest_red:
                highest_red = pull.red
            if pull.green > highest_green:
                highest_green = pull.green
            if pull.blue > highest_blue:
                highest_blue = pull.blue

        return highest_red, highest_green, highest_blue

    @property
    def is_possible(
        self,
        red_limit: int = RED_LIMIT,
        green_limit: int = GREEN_LIMIT,
        blue_limit: int = BLUE_LIMIT,
    ) -> bool:
        return (
            self.highest_red <= red_limit
            and self.highest_green <= green_limit
            and self.highest_blue <= blue_limit
        )


def sum_possibilities(games: Sequence[CubeGame]) -> int:
    """Return sum of IDs of possible games."""
    return sum(game.id for game in games if game.is_possible)


def sum_power_possibilities(games: Sequence[CubeGame]) -> int:
    """Return sum of red * green * blue for each game."""
    return sum(
        game.highest_red * game.highest_green * game.highest_blue for game in games
    )


if __name__ == "__main__":
    with open("aoc_2023/inputs/day_02.txt") as data:
        records = [line for line in data]

    games = [CubeGame.from_record(record) for record in records]

    sum_of_possibilities = sum_possibilities(games)
    print(f"Part 1: {sum_of_possibilities}")

    sum_of_the_power_of_possibilities = sum_power_possibilities(games)
    print(f"Part 2: {sum_of_the_power_of_possibilities}")
