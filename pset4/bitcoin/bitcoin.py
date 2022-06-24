"""
Bitcoin purchaser
"""

import requests
import sys


def main():
    try:

        # Command line argument check
        if len(sys.argv) != 2:
            print("Usage: python bitcoin.py number_bitcoins")

        # Assign number of units to variable
        units = float(sys.argv[1])

        # Condesk Bitcoin Price Index API request
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Store and parse API request
        bc_json = (r.json())
        rate = (bc_json["bpi"]["USD"]["rate_float"])

        # Print USD currency amount for bitcoin units requested
        print(f"${rate * units:,.04f}")

    # Handle exceptions
    except (ValueError, TypeError):
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("CoinDesk Bitcoin Price Index exception")


if __name__ == "__main__":
    main()
