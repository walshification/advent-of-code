import pytest

from aoc_2023.day_04 import Scratchcard, sum_tickets, tabulate_tickets


@pytest.mark.parametrize(
    ("row", "card_id", "winning_numbers", "player_numbers", "winners", "score"),
    (
        (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            1,
            {41, 48, 83, 86, 17},
            {83, 86, 6, 31, 17, 9, 48, 53},
            {48, 83, 86, 17},
            8,
        ),
        (
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            5,
            {87, 83, 26, 28, 32},
            {88, 30, 70, 12, 93, 22, 82, 36},
            set(),
            0,
        ),
    ),
)
def test_scratchcard(row, card_id, winning_numbers, player_numbers, winners, score):
    sc = Scratchcard.from_ticket(row)
    assert sc.id == card_id
    assert sc.winning_numbers == winning_numbers
    assert sc.player_numbers == player_numbers
    assert sc.winners == winners
    assert sc.score == score


def test_sum_tickets():
    scratchcards = (
        Scratchcard.from_ticket(ticket)
        for ticket in (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        )
    )
    assert sum_tickets(scratchcards) == 13


@pytest.mark.parametrize(
    ("tickets", "total"),
    (
        # (("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",), 5),
        # (
        # (
        #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        # ),
        # 8,
        # ),
        (
            (
                "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
                "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
                "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
                "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
                "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
                "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
            ),
            30,
        ),
    ),
)
def test_tabulate_tickets(tickets, total):
    scratchcards = tuple(Scratchcard.from_ticket(ticket) for ticket in tickets)
    assert tabulate_tickets(scratchcards, scratchcards) == total
