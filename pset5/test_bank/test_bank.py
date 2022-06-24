"""
Test value function from bank.py
"""

from bank import value


# Correct payout outputted
def test_amount():
    assert value("hello") == 0       # hello, 0
    assert value("hi") == 20         # starts with h, 20
    assert value("other") == 100     # starts with other, 100

# Case insensitivity
def test_case():
    assert value("HELLO") == 0       # HELLO, 0
    assert value("HI") == 20         # starts with H, 20
    assert value("OTHER") == 100     # starts with OTHER, 100
