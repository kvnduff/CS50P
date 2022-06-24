"""
Coke machine coin calculator
"""

# Initialize variables
due = 50
coin = ""

# Loop while due is greater than 0
while due > 0:
    # Prompt user for coin
    coin = int(input("Insert a coin: "))
    # If coin invalid then print amount due
    if coin != 5 and coin != 10 and coin != 25:
        print(f"Amount due: {due}")
    # If coin valid and due greater than zero then adjust due and print
    elif due - coin > 0:
        due = due - coin
        print(f"Amount due: {due}")
    # If coin valid and due less than or equal to zero then print change
    else:
        due = due - coin
        print(f"Change owed: {due * -1}")
