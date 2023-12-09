import pytest

from aoc_2023.day_02 import CubeGame, Pull, sum_possibilities, sum_power_possibilities


@pytest.mark.parametrize(
    ("record", "red_count", "green_count", "blue_count"),
    (
        ("3 blue, 4 red", 4, 0, 3),
        ("1 red, 2 green, 6 blue", 1, 2, 6),
        ("2 green", 0, 2, 0),
    ),
)
def test_pull_tracks_cube_counts(
    record: str, red_count: int, green_count: int, blue_count: int
):
    pull = Pull.from_record(record)
    assert pull.red == red_count
    assert pull.green == green_count
    assert pull.blue == blue_count


@pytest.mark.parametrize(
    ("record", "game_id", "highest_red", "highest_green", "highest_blue"),
    (
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1, 4, 2, 6),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            2,
            1,
            3,
            4,
        ),
    ),
)
def test_game_records_highest_cube_counts(
    record: str, game_id: int, highest_red: int, highest_green: int, highest_blue: int
):
    game = CubeGame.from_record(record)
    assert game.id == game_id
    assert game.highest_red == highest_red
    assert game.highest_green == highest_green
    assert game.highest_blue == highest_blue


@pytest.mark.parametrize(
    ("record", "expected_possibility"),
    (
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            False,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            False,
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True),
    ),
)
def test_is_possible(record: str, expected_possibility: bool):
    assert CubeGame.from_record(record).is_possible == expected_possibility


def test_sum_possibilities():
    records = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    assert sum_possibilities([CubeGame.from_record(record) for record in records]) == 8


def test_sum_power_possibilities():
    records = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    assert (
        sum_power_possibilities([CubeGame.from_record(record) for record in records])
        == 2286
    )
