"""
Remove vowels from text
"""


def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):

    # Initialize list representing vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # Iterate over char in input, concatenating vowels to output
    output = ""
    for char in word:
        if char not in vowels:
            output += char
    return(output)


if __name__ == "__main__":
    main()
