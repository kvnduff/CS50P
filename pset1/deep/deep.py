"""
Answer the Great Questions of Life, the Universe, and Everything
"""

# Prompt user for answer
answer = input("What is the Answer to the Great Questions of Life, the "
               "Universe, and Everything? ")

# Clean answer (lower case and trim whitespace)
try:
    clean = int(answer)
except ValueError:
    clean = answer.lower().strip()

# Print Yes/No depending on answer
if clean == 42 or clean == "forty-two" or clean == "forty two":
    print("Yes")
else:
    print("No")
