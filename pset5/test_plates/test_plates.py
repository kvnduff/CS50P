"""
Test is_valid function from plates.py
"""

from plates import is_valid


# Starts with two letters
def test_start():
    assert is_valid("hh1234") is True
    assert is_valid("123456") is False

# Max of 6 characters, min of 2 characters
def test_length():
    assert is_valid("hh1234") is True
    assert is_valid("hh123456") is False
    assert is_valid("h") is False

# Numbers only at end
def test_numend():
    assert is_valid("hhhh12") is True
    assert is_valid("hh12ab") is False

# First number is not 0
def test_zerofirst():
    assert is_valid("hhhh12") is True
    assert is_valid("hhhh02") is False

# Only alphanumeric characters
def test_alpha():
    assert is_valid("abcdef") is True
    assert is_valid("abc123") is True
    assert is_valid("ab adc") is False
    assert is_valid("ab.,dc") is False
