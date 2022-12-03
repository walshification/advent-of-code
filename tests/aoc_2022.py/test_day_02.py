import pytest

from aoc_2022.day_02 import Paper, Player, Rock, Scissors


@pytest.mark.parametrize(
    ["Winner", "Loser"],
    ((Rock, Scissors), (Paper, Rock), (Scissors, Paper)),
)
def test_grater_than_works(Winner, Loser):
    winner = Winner()
    loser = Loser()
    assert winner > loser


@pytest.mark.parametrize(
    ["Winner", "Loser"],
    ((Rock, Scissors), (Paper, Rock), (Scissors, Paper)),
)
def test_less_than_works(Winner, Loser):
    winner = Winner()
    loser = Loser()
    assert loser < winner


@pytest.mark.parametrize("Throw", (Rock, Paper, Scissors))
def test_equality_works(Throw):
    one = Throw()
    two = Throw()
    assert one == two


def test_players_can_win():
    player_one = Player()
    player_two = Player()
    assert player_one.throw("A") > player_two.throw("C")


def test_players_can_lose():
    player_one = Player()
    player_two = Player()
    assert player_one.throw("A") < player_two.throw("B")


def test_players_can_tie():
    player_one = Player()
    player_two = Player()
    assert player_one.throw("A") == player_two.throw("A")