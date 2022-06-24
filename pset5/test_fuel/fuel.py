"""
Convert fuel gauge input from fraction to percentage
"""

import sys


def main():
    while True:
        try:
            text = input("Fraction: ")
            percent = convert(text)
            if percent < 0 or percent > 100:
                raise ValueError
            result = gauge(percent)
            print(result)
            sys.exit()
        except (ValueError, IndexError, ZeroDivisionError):
            pass


def convert(fraction):
    num = fraction.split("/")
    numerator = int(num[0])
    denominator = int(num[1])
    if type(numerator) is not int:
        raise ValueError
    if type(denominator) is not int:
        raise ValueError
    percent = int(numerator / denominator * 100)
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif percentage > 100:
        pass
    else:
        return str(f"{int(percentage)}%")


if __name__ == "__main__":
    main()
