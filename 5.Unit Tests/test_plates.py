from Loops.plates import is_valid


def test_length():
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False


def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_lower():
    assert is_valid("HELLO") == True
    assert is_valid("hello") == True


def test_digets():
    assert is_valid("123456") == False

def test_beginning():
    assert is_valid("JC16") == True
    assert is_valid("12JC") == False


def test_special():
    assert is_valid("QWERTY") == True
    assert is_valid("CS!@#$") == False


def test_placement():
    assert is_valid("HE0000") == False
    assert is_valid("CS05") == False
    assert is_valid("CS12CS") == False
