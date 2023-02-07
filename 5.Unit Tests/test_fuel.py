from Exceptions.fuel import convert, gauge
import pytest


def test_convert_int():
    assert convert("1/2") == 50
    assert convert("99/100") == 99


def test_convert_str():
    assert convert("1/2") != "50"
    assert convert("99/100") != "99"


def test_gauge_int():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"


def test_e_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_e_value():
    with pytest.raises(ValueError):
        convert("Cat/dog")