from solution import convert


def test_single_numeral():
    assert convert("I") == 1


def test_addition():
    assert convert("VI") == 6


def test_subtraction():
    assert convert("IV") == 4


def test_mixed_numeral():
    assert convert("XIX") == 19


def test_invalid_order():
    assert convert("VX") == "Invalid Roman numeral"


def test_invalid_numeral():
    assert convert("XXC") == "Invalid Roman numeral"


def test_invalid_character():
    assert convert("A") == "Invalid Roman numeral"