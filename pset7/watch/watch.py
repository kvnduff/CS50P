"""
Convert YouTube embedded links to shareable links
"""

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    parts = re.search(r'(^<iframe)(.*http[s]?://(www.)?youtube.com/embed/)([^"]*)(.*)', s)
    if parts is None:
        return parts
    else:
        return f"https://youtu.be/{parts[4]}"


if __name__ == "__main__":
    main()
