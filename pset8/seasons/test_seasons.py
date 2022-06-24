"""
Test seasons.py
"""

from seasons import minbirth
import pytest
import sys
import inflect
p = inflect.engine()


# Attribute error raised
def test_error_value():
    with pytest.raises(AttributeError):
        minbirth(1.57373)

# Name error raised
def test_error_name():
    with pytest.raises(NameError):
        minbirth(hello)
