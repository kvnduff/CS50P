"""
Remove vowels from text
"""

# Initialize list representing vowels
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Prompt user for input
input = input("Input: ")

# Iterate over char in input, concatenating non-vowel letters to output
output = ""
for char in input:
    if char not in vowels:
        output += char
print(output)
