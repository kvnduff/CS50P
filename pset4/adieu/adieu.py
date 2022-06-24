"""
Insert "," and "and" according to list of names
"""

import inflect
p = inflect.engine()


def main():
    get_name()


def get_name():
    """
    Request name(s) and convert to list with "," and "and"
    """

    # Request name(s) until EOFError
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            print(f"Adieu, adieu, to {p.join((name_list))}")
            break


if __name__ == "__main__":
    main()
