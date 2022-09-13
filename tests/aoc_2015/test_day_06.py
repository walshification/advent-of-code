from textwrap import dedent

from aoc_2015.day_06 import Grid, Light


def test_light_becomes_active_if_turned_on():
    light = Light()
    light.turn_on()
    assert light.active
    assert str(light) == "*"


def test_light_becomes_inactive_if_turned_off():
    light = Light()
    light.turn_on()
    light.turn_off()
    assert not light.active
    assert str(light) == " "


def test_light_toggle_flips_activity():
    light = Light()
    assert not light.active
    light.toggle()
    assert light.active
    light.toggle()
    assert not light.active


def test_grid_tracks_decorations_and_returns_active_light_count():
    grid = Grid(10)
    active_lights = grid.decorate(["turn on 0,0 through 0,9"])
    assert active_lights == 10
    assert str(grid) == (
        " * * * * * * * * * *\n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
    )


def test_grid_tracks_decorations_the_other_way():
    grid = Grid(10)
    active_lights = grid.decorate(["turn on 0,9 through 0,0"])
    assert active_lights == 10
    assert str(grid) == (
        " * * * * * * * * * *\n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
        "                    \n"
    )
