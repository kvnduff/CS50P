"""
Vanity plate validity checker
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Determine if plate is valid
def is_valid(s):
    if start(s) and length(s) and end(s) and fnum(s) and alnum(s):
        return True
    else:
        return False


# Starts with two letters
def start(j):
    start = j[0:2]
    for char in start:
        if char.isalpha() is False:
            return False
    return True


# Max of 6 characters and min of 2 characters
def length(k):
    length = 0
    for char in k:
        if char.isalnum() is True:
            length += 1
    if length < 2 or length > 6:
        return False
    else:
        return True


# Numbers only at end
def end(l):
    # Count number of numbers
    num = 0
    for char in l:
        if char.isnumeric() is True:
            num += 1
    # Ensure numbers at end
    end = l[-num:]
    if num != 0:
        for char in end:
            if char.isnumeric() is False:
                return False
    return True


# First number not a "0"
def fnum(m):
    # Count number of numbers
    num = 0
    for char in m:
        if char.isnumeric() is True:
            num += 1
    # Ensure first number is not 0
    if m[-num] == "0":
        return False
    else:
        return True


# Only alphanumeric characters
def alnum(n):
    for char in n:
        if not char.isalnum():
            return False
    return True


main()
