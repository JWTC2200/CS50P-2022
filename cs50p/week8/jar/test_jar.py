from jar import Jar
import pytest


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    jar.deposit(3)
    assert jar.stored == 8
    with pytest.raises(ValueError):
        jar.deposit(100)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.stored == 5
    jar.withdraw(2)
    assert jar.stored == 3
    with pytest.raises(ValueError):
        jar.withdraw(100)
