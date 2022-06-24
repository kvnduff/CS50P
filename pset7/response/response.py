"""
Validate an email address using validators
"""

import validators


def main():
    print(validate(input("email: ")))


def validate(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
