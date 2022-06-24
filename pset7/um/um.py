"""
Count number of "um"
"""

import re


def main():
    print(count(input("Text: ")))


def count(s):
    lower = s.lower()
    matches = re.findall(r"(?=(^um$))|(?=(^um[ .,?]))|(?=([ .,?]um[ .,?]))|(?=([ .,?]um$))", lower)
    return len(matches)


if __name__ == "__main__":
    main()
