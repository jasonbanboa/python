from working.working import convert
import pytest


def test_convert_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("9:00 PM - 5 AM")
        convert("9 PM - 5:00 AM")


def test_convert_wrong_hour():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")
        convert("13 PM to 17 PM")


def test_correct():
    convert("9 AM to 5 PM") == "09:00 to 17:00"
    convert("10 PM to 8 AM") == "22:00 to 08:00"
    convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    convert("6 PM to 6 AM") == "18:00 to 18:00"
    convert("6:01 PM to 6 AM") == "18:01 to 06:00"
    convert("6 PM to 6:02 AM") == "18:00 to 06:02"
    convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_i_give_up():
    with pytest.raises(ValueError):
        print(convert("13 PM to 5:00 AM"))

def test_i_dk():
    with pytest.raises(ValueError):
        print(convert("12:61 PM to 5 AM"))