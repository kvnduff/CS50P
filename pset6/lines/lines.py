"""
Measure lines of code
"""

import sys


def main():

    # Command line argument number check
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # File extension check
    file_split = sys.argv[1].split(".")
    if file_split[-1] != "py":
        sys.exit("Not a python file")

    # Open document
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Initialize variables
    count_line = 0
    count_comment = 0
    count_blank = 0

    # Iterate over lines
    for i, line in enumerate(file):

        # Count number of lines
        count_line = i + 1

        # Count number of comment rows
        if line.lstrip().startswith("#"):
            count_comment += 1

        # Count number of blank rows
        if line.lstrip().rstrip() == "":
            count_blank += 1

    # Print number of non-blank, non-comment rows in file
    print(count_line - count_comment - count_blank)


if __name__ == "__main__":
    main()
