"""
Test functions in numb3rs.py
"""

from numb3rs import validate
import pytest


# Incorrect number of numbers (3 expected)
def test_number_numbers():
    assert validate("50.50.50.50.50") is False      # too many numbers
    assert validate("50.50.50") is False            # too few numbers


# Out of range number (0 - 255 expected)
def test_range():
    assert validate("50.50.50.256") is False        # above upper bound
    assert validate("50.50.50.-10") is False        # below lower bound


# Invalid characters (digits expected)
def test_character():
    assert validate("50.50.50.abc") is False        # letters
    assert validate("50.50.50.#~[") is False        # symbols
