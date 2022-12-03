"""
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets
to be closest to the snack storage, a giant Rock Paper Scissors
tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains
many rounds; in each round, the players each simultaneously choose one
of Rock, Paper, or Scissors using a hand shape. Then, a winner for that
round is selected: Rock defeats Scissors, Scissors defeats Paper, and
Paper defeats Rock. If both players choose the same shape, the round
instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted
strategy guide (your puzzle input) that they say will be sure to help
you win. "The first column is what your opponent is going to play: A
for Rock, B for Paper, and C for Scissors. The second column--"
Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in
response: X for Rock, Y for Paper, and Z for Scissors. Winning every
time would be suspicious, so the responses must have been carefully
chosen.

The winner of the whole tournament is the player with the highest
score. Your total score is the sum of your scores for each round. The
score for a single round is the score for the shape you selected (1 for
Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome
of the round (0 if you lost, 3 if the round was a draw, and 6 if you
won).

Since you can't be sure if the Elf is trying to help you or trick you,
you should calculate the score you would get if you were to follow the
strategy guide.

What would your total score be if everything goes exactly according to
your strategy guide?
"""
from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class Throw:
    """Base class for a Rock Paper Scissors move."""

    CONFIG_MAP = {
        "scissors": 1,
        "paper": -1,
        "rock": 0,
    }

    value: int = 0

    def __gt__(self, other: "Throw") -> bool:
        """Rock beats Scissors; loses to Paper."""
        return self.CONFIG_MAP[type(other).__name__.lower()] == 1

    def __lt__(self, other: "Throw") -> bool:
        """Rock beats Scissors; loses to Paper."""
        return self.CONFIG_MAP[type(other).__name__.lower()] == -1

    def __eq__(self, other: object) -> bool:
        """Rock beats Scissors; loses to Paper."""
        return self.CONFIG_MAP[type(other).__name__.lower()] == 0

    def __add__(self, other: int) -> int:
        return self.value + other


@dataclass
class Rock(Throw):
    """Claustrophobic crusher of scissors."""

    value: int = 1


@dataclass
class Paper(Throw):
    """Haemophiliac cuddler of rocks."""

    CONFIG_MAP = {
        "scissors": -1,
        "paper": 0,
        "rock": 1,
    }

    value: int = 2


@dataclass
class Scissors(Throw):
    """Delicate slicer of paper."""

    CONFIG_MAP = {
        "scissors": 0,
        "paper": 1,
        "rock": -1,
    }

    value: int = 3


DECODER_MAP = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors(),
    "X": Rock(),
    "Y": Paper(),
    "Z": Scissors(),
}


@dataclass
class Player:
    """A player of Rock Paper Scissors."""

    decoder_map: Dict[str, Throw] = field(default_factory=lambda: DECODER_MAP)
    scores: List[int] = field(default_factory=list)

    def throw(self, encoded_move: str) -> Throw:
        """Return the value for a coded move."""
        return self.decoder_map[encoded_move]


@dataclass
class RockPaperScissors:
    """A game of Rock Paper Scissors."""

    player_one: Player
    player_two: Player
    encoded_rounds: List[str]

    def run(self) -> int:
        """Play a game and return player_two's score."""
        for round in self.encoded_rounds:
            throw_one, throw_two = self.decode_round(*(round.split()))
            self.score_round(throw_one, throw_two)

        return sum(self.player_two.scores)

    def decode_round(self, encoded_one, encoded_two) -> Tuple[Throw, Throw]:
        return self.player_one.throw(encoded_one), self.player_two.throw(encoded_two)

    def score_round(self, throw_one, throw_two) -> None:
        if throw_one > throw_two:
            self.player_one.scores.append(throw_one + 6)
            self.player_two.scores.append(throw_two.value)
        elif throw_one < throw_two:
            self.player_two.scores.append(throw_two + 6)
            self.player_one.scores.append(throw_one.value)
        else:
            self.player_one.scores.append(throw_one + 3)
            self.player_two.scores.append(throw_two + 3)


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_02.txt") as data:
        rounds = [round for round in data]

    score = RockPaperScissors(Player(), Player(), rounds).run()

    print(f"Part 1: {score}")
    # print(f"Part 2: {}")
