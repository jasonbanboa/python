from bank import value


from bank import value


def test_default():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("bro") == 100


def test_caps():
    assert value("HELLO") == 0
    assert value("BRO") == 100
    assert value("HEY") == 20


