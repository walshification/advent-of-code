from aoc_2015.day_03 import Santa


def test_santa_tracks_his_deliveries():
    santa = Santa()
    assert santa.deliver(">") == 2


def test_revisiting_does_not_increase_locations_visited():
    santa = Santa()
    assert santa.deliver("^v^v^v^v^v") == 2


def test_santa_can_go_in_all_cardinal_directions():
    santa = Santa()
    assert santa.deliver("^>v<") == 4
