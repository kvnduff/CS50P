"""
Convert text to emojis
"""

import emoji


def main():

    # Request user input
    text = input("Input: ")

    # Output text replacing emoji text and aliases as emojis
    print(f"Output: {emoji.emojize(text, language='alias')}")


if __name__ == "__main__":
    main()
