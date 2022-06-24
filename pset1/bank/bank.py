"""
Bank payout based on greeting
"""

# Prompt user for greeting
greeting = input("Greeting: ")

# Clean greeting (lower case and trim whitespace)
clean = greeting.lower().strip()

# Payout based on greeting
if clean.startswith("hello"):
    print("$0")
elif clean.startswith("h"):
    print("$20")
else:
    print("$100")
