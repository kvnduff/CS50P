"""
Bank payout based on greeting
"""


def main():
    payout = input("Greeting: ")
    print(f"${value(payout)}")


def value(greeting):

    # Clean greeting (lower case and trim whitespace)
    clean = greeting.lower().strip()

    # Payout based on greeting
    if clean.startswith("hello"):
        return 0
    elif clean.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
