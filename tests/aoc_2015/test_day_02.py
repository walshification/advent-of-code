from aoc_2015.day_02 import Calculator, Present


def test_present_knows_dimensions():
    dimensions = (2, 3, 4)
    present = Present(*dimensions)
    length, width, height = present
    assert dimensions == (length, width, height)
    assert present.total_area == 52


def test_calculator_calculates_needed_wrapping_paper_for_presents():
    present = Present(2, 3, 4)
    tall_present = Present(1, 1, 10)
    assert Calculator.wrapping_paper([present]) == 58
    assert Calculator.wrapping_paper([tall_present]) == 43
    assert Calculator.wrapping_paper([present, tall_present]) == 101
