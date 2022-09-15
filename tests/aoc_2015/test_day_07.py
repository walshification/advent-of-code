from aoc_2015.day_07 import Circuit


def test_circuit_can_assign_signals_to_wires():
    circuit = Circuit.build(["123 -> x"])
    assert circuit.trace("x") == 123


def test_circuit_can_assign_left_shifts_to_wires():
    circuit = Circuit.build(["x LSHIFT 2 -> a", "123 -> x"])
    assert circuit.trace("a") == 492


def test_circuit_can_assign_right_shifts_to_wires():
    circuit = Circuit.build(["x RSHIFT 2 -> a", "123 -> x"])
    assert circuit.trace("a") == 30


def test_circuit_can_assign_unions_to_wires():
    circuit = Circuit.build(["x AND y -> a", "123 -> x", "456 -> y"])
    assert circuit.trace("a") == 72


def test_circuit_can_assign_disjuncts_to_wires():
    circuit = Circuit.build(["x OR y -> a", "123 -> x", "456 -> y"])
    assert circuit.trace("a") == 507


def test_circuit_can_assign_negations_to_wires():
    circuit = Circuit.build(["NOT x -> a", "123 -> x"])
    assert circuit.trace("a") == 65412


def test_circuit_can_assign_wires_to_wires():
    circuit = Circuit.build(["x -> a", "123 -> x"])
    assert circuit.trace("a") == 123
