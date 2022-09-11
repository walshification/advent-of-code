from aoc_2015.day_02 import Calculator, Present


def test_present_knows_dimensions():
    dimensions = (2, 3, 4)
    present = Present(*dimensions)
    length, width, height = present
    assert dimensions == (length, width, height)
    assert present.total_area == 52
    assert present.shortest_perimeter == 10


def test_calculator_calculates_needed_wrapping_paper_for_presents():
    present = Present(2, 3, 4)
    tall_present = Present(1, 1, 10)
    assert Calculator([present]).calculate_wrapping_paper() == 58
    assert Calculator([tall_present]).calculate_wrapping_paper() == 43
    assert Calculator([present, tall_present]).calculate_wrapping_paper() == 101
