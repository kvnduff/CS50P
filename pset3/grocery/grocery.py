"""
Grocery list reminder
"""


def main():
    get_item()


# Store a list of grocery items and frequencies in dict and print
def get_item():
    items = {}
    while True:
        try:
            item = input("\n").strip().upper()
            if item not in items:
                items[item] = 1
            else:
                number = int(items[item])
                number += 1
                items[item] = number
        except EOFError:
            print()
            items_sorted = dict(sorted(items.items()))
            for key, value in items_sorted.items():
                print(value, key)
            break


if __name__ == "__main__":
    main()
