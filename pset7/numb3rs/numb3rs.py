"""
Validate IPv4 addresses
"""

import sys
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    number = "([0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])"
    if re.fullmatch(number+re.escape(".")+number+re.escape(".")+number+re.escape(".")+number, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
