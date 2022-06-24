"""
Convert fuel gauge input from fraction to percentage
"""


def main():
    print(get_fraction("Fraction: "))


# Get a fraction from user and output percent, handling errors
def get_fraction(prompt):
    while True:
        try:
            fraction = input(prompt).split("/")
            numerator = int(fraction[0])
            denominator = int(fraction[1])
            percent = numerator / denominator * 100
            if percent < 1:
                return "E"
            elif 100 >= percent > 99:
                return "F"
            elif percent > 100:
                pass
            else:
                return str(f"{int(percent)}%")
        except (ValueError, IndexError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
