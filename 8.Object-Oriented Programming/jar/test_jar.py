from jar import Jar


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(2)
    assert jar2.capacity == 2


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert str(jar.cookies) == "2"

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert str(jar.cookies) == "1"