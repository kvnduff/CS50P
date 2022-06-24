"""
Number guessing game
"""

import random


def main():
    get_level()


def get_level():
    """
    Request level and guess from user and provide feedback on guess accuracy
    """
    while True:
        try:

            # Prompt user for level
            level = int(input("Level: "))
            if level > 0:
                while True:
                    try:

                        # Generate a random number between 1 and level
                        number = random.randint(1, level)

                        # Prompt user for guess
                        guess = int(input("Guess: "))

                        # Provide feeback on guess accuracy
                        if guess > 0:
                            if guess < number:
                                print("Too small!")
                                pass
                            elif guess > number:
                                print("Too large!")
                                pass
                            else:
                                print("Just right!")
                                exit()

                    # If guess not int then pass
                    except ValueError:
                        pass

        # If level not int then pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()
