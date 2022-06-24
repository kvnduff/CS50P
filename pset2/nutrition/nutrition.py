"""
Fruit calorie calculator
"""

# Prompt user for fruit
fruit = input("Fruit: ")

# Create a dictionary to store the FDA fruit colorie data
fruits = {"apple": "130",
          "avocado": "50",
          "banana": "110",
          "cantaloupe": "50",
          "grapefruit": "60",
          "grapes": "90",
          "honeydew melon": "50",
          "kiwifruit": "90",
          "lemon": "15",
          "lime": "20",
          "nectarine": "60",
          "orange": "80",
          "peach": "60",
          "pear": "100",
          "pineapple": "50",
          "plums": "70",
          "strawberries": "50",
          "sweet cherries": "100",
          "tangerine": "50",
          "watermelon": "80"}

# Output calories according to fruit
if fruit.lower() in fruits:
    print(f"Calories: {fruits[fruit.lower()]}")
else:
    print("")
