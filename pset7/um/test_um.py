"""
Test count function from um.py
"""

import pytest
from um import count


# um as substring
def test_sub():
    assert count("yummy") != 1      # surround by letters
    assert count("ummy") != 1       # followed by letter
    assert count("yum") != 1        # preceded by letter


# um as not substring, spaces
def test_space():
    assert count(" um ") == 1       # surround by spaces
    assert count("um ") == 1        # followed by space
    assert count(" um") == 1        # preceded by space


# um a not substring, followed by punctuation
def test_punc():
    assert count(" um,") == 1       # preceded by space, followed by ,
    assert count(" um.") == 1       # preceded by space, followed by .
    assert count(" um?") == 1       # preceded by space, followed by ?


# um case sensitivity
def test_case():
    assert count("UM") == 1         # uppercase
    assert count("UM") != 0         # uppercase
