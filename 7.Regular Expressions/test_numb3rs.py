from numb3rs import validate


def test_if_digit():
    assert validate("cat") == False

def test_four_numbers():
    assert validate("111.111.111") == False


def test_max_number():
    assert validate("277.0.0.0") == False

def test_correct_format():
    assert validate("255/255/255/255") == False
    assert validate("255.255.255.255") == True

def test_number_range():
    assert validate("0.0.0.0") == True
    assert validate("256.0.0.0") == False
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("cat") == False
