"""
Convert 12h time to 24h time
"""

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    first = ""
    second = ""

    # Search for long format pattern
    long = re.match(r"((?:[1][0-2])|(?:[0-9])):([0-5][0-9]) (AM|PM) to ((?:[1][0-2])|(?:[0-9])):([0-5][0-9]) (AM|PM)", s)

    # If long format used
    if long is not None:

        # Generate first and second time from capture groups
        if long[3] == "AM":
            first = f"{long[1]}:{long[2]}"
        if long[3] == "PM":
            first = f"{int(long[1]) + 12}:{long[2]}"
        if long[6] == "AM":
            second = f"{long[4]}:{long[5]}"
        if long[6] == "PM":
            second = f"{int(long[4]) + 12}:{long[5]}"

        # If AM hour less than 10 then add leading zero
        if len(long[1]) == 1 and long[3] == "AM":
            first = f"0{first}"
        if len(long[4]) == 1 and long[6] == "AM":
            second = f"0{second}"

        # If AM hour is 12 then change to zero
        if long[1] == "12" and long[3] == "AM":
            first = f"00:{long[2]}"
        if long[4] == "12" and long[6] == "AM":
            second = f"00:{long[5]}"

        # If PM hour is 12 then change to twelve
        if long[1] == "12" and long[3] == "PM":
            first = f"12:{long[2]}"
        if long[4] == "12" and long[6] == "PM":
            second = f"12:{long[5]}"

        # Return 24 hour time
        return f"{first} to {second}"

    # Search for long format pattern
    short = re.match(r"((?:[1][0-2])|(?:[0-9])) (AM|PM) to ((?:[1][0-2])|(?:[0-9])) (AM|PM)", s)

    # If short format used
    if short is not None:

        # Generate first and second time from capture groups
        if short[2] == "AM":
            first = f"{short[1]}"
        if short[2] == "PM":
            first = f"{int(short[1]) + 12}"
        if short[4] == "AM":
            second = f"{short[3]}"
        if short[4] == "PM":
            second = f"{int(short[3]) + 12}"

        # If AM hour less than 10 then add leading zero
        if len(short[1]) == 1 and short[2] == "AM":
            first = f"0{first}"
        if len(short[3]) == 1 and short[4] == "AM":
            second = f"0{second}"

        # If AM hour is 12 then change to zero
        if short[1] == "12" and short[2] == "AM":
            first = "00"
        if short[3] == "12" and short[4] == "AM":
            second = "00"

        # If PM hour is 12 then change to twelve
        if short[1] == "12" and short[2] == "PM":
            first = "12"
        if short[3] == "12" and short[4] == "PM":
            second = "12"

        # Return 24 hour time
        return f"{first}:00 to {second}:00"

    # If improper format then raise error
    if long is None and short is None:
        raise ValueError


if __name__ == "__main__":
    main()
