"""
Test twttr.py shorten function
"""


from twttr import shorten


# No vowels: all input shoud be returned as output
def test_novowels():
    assert shorten("hllwrld") == "hllwrld"

# Vowels: lower and upper case vowels should be excluded from output
def test_case():
    assert shorten("hEllOwOrld") == "hllwrld"       # upper case vowels
    assert shorten("helloworld") == "hllwrld"       # lower case vowels

# Numbers: numbers should be retained in ouput
def test_numbers():
    assert shorten("helloworld123") == "hllwrld123"

# Symbols: symbols should be retained in ouput
def test_symbols():
    assert shorten("helloworld!#%+_") == "hllwrld!#%+_"
