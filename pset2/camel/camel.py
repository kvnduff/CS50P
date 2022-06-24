"""
Convert camel case to snake case
"""

# Prompt user for camelCase
camelCase = input("camelCase: ")

# Split word into list with delimiter (underscore) before upper case
delimit = []
for char in camelCase:
    # Don't insert underscore if first char is upper case
    if char.isupper() and camelCase.index(char) != 0:
        delimit.append("_" + char)
    else:
        delimit.append(char)

# Convert to snake_case by joining list elements and converting to lower case
print(''.join(delimit).lower())
