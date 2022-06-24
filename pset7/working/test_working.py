"""
Test convert function from working.py
"""

from working import convert
import pytest


# Incorrect pattern raises ValueError
def test_pattern():
    with pytest.raises(ValueError):
        convert("hello")                        # incorrect pattern


# Out of range values raises ValueError
def test_range_long():
    with pytest.raises(ValueError):
        convert("15:88 AM to 28:99 PM")         # out of range values, long

def test_range_short():
    with pytest.raises(ValueError):
        convert("15 AM to 28 PM")               # out of range values, long


# Incorrect "AM/PM" raises ValueError
def test_ampm():
    with pytest.raises(ValueError):
        convert("10:00 GM to 2:00 RM")          # incorrect AM/PM symbols


# Incorrect ":" raises ValueError
def test_colon():
    with pytest.raises(ValueError):
        convert("10;00 AM to 2;00 PM")          # incorrect AM/PM symbols


# Incorrect "to" raises ValueError
def test_to():
    with pytest.raises(ValueError):
        convert("10:00 AM through 2:00 PM")     # incorrect AM/PM symbols


# Incorrect hour/minute values
def test_hour():
    assert convert("10:00 AM to 2:00 PM") != "11:00 to 15:00"   # hours

def test_minute():
    assert convert("10:01 AM to 2:01 PM") != "10:02 to 14:02"   # minutes
