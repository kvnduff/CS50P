"""
Read input file, split name field, output new file
"""

import sys
import csv


def main():

    # Command line argument number check
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")

    # Initialize output list
    output = []

    # Open document for reading
    try:
        with open(sys.argv[1]) as file:

            # Create dict reader object
            reader = csv.DictReader(file)

            # Iterate over rows
            for row in reader:
                house = row["house"]
                last, first = row["name"].split(", ")
                output.append({'first': first, 'last': last, 'house': house})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Open document for writing
    with open(sys.argv[2], "w") as file:

        # Create dict writer object
        writer = \
            csv.DictWriter(file, fieldnames=['first', 'last', 'house'])

        # Write first, last, house
        writer.writeheader()
        writer.writerows(output)


if __name__ == "__main__":
    main()
