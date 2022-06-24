"""
Format pizza menus from CSV to ASCII format
"""

import tabulate
import sys
import csv


def main():

    # Command line argument number check
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # File type check
    file_split = sys.argv[1].split(".")
    if file_split[1] != "csv":
        sys.exit("Not a csv file")

    # Open document
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Initialize table list
    table = []

    # Create CSV reader
    reader = csv.reader(file)

    # Create a list of all rows in the reader
    for row in reader:
        table.append(row)

    # Print formatted menu
    print(tabulate.tabulate(table, headers='firstrow', tablefmt="grid"))


if __name__ == "__main__":
    main()
