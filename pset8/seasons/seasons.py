"""
Calculate time from birth date to 2000 with time expressed in words.
"""

from datetime import datetime, time
import sys
import inflect
p = inflect.engine()


def main():
    try:
        print(minbirth(input("Date of birth: ")))
    except (NameError, ValueError):
        sys.exit(1)


def minbirth(dob):
    """
    Get minutes from 2000.
    """
    year, month, day = dob.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    dob_object = datetime(year, month, day)
    twomil = datetime(2000, 1, 1)
    midnight = datetime.combine(twomil, time())
    delta = midnight - dob_object
    minutes = int(delta.total_seconds() / 60)
    words = p.number_to_words(minutes, andword="")
    words_min = f"{words} minutes"
    words_cap = f"{words_min[0].upper()}{words_min[1:]}"
    return words_cap


if __name__ == "__main__":
    main()
