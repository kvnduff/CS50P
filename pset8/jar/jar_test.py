"""
Tests for jar_test.py
"""

import pytest
from jar import Jar


# Test init
def test_init():
    jar = Jar()
    assert jar.capacity == 12                       # initial capacity
    assert jar.size == 0                            # initial size


# Test str
def test_str():
    jar = Jar()
    assert str(jar) == ""                           # initial str
    jar.deposit(1)
    assert str(jar) == "🍪"                         # str after deposit 1
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"   # str after deposit 12


# Test deposit
def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3                            # deposit < capacity
    with pytest.raises(ValueError):
        jar.deposit(10)                             # deposit > capacity


# # Test withdraw
def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4                            # withdraw < size
    with pytest.raises(ValueError):
        jar.withdraw(10)                            # withdraw > size
