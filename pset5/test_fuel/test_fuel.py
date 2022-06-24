"""
Test convert and guage functions from fuel.py
"""

from fuel import convert, gauge
import pytest


# Convert


# Incorrect integers (out of range) accepted
def test_incorrect_integer():
    assert convert("150/100") == 150    # greater than 100
    assert convert("-10/100") == -10    # less than 0


# Value error raised
def test_value_error():
    with pytest.raises(ValueError):
        convert("hello/there")


# Zero division error raised
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")


# Gauge

# Return "E" if percentage < 1
def test_empty():
    assert gauge(2) == "2%"             # greater than 1 returns percentage
    assert gauge(1) == "E"              # less than or equal to 1 returns "E"
    assert gauge(0) == "E"              # zero returns "E"


# Return "F" if percentage > 99
def test_full():
    assert gauge(98) == "98%"           # less than 99 returns percentage
    assert gauge(99) == "F"             # greater than or equal to 99 returns "F"
    assert gauge(100) == "F"            # 100 returns "F"
