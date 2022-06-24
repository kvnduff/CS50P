"""
Professor calculator
"""

import random


def main():

    # Declare variables to count correct and incorrect answers
    corrects = 0
    incorrects = 0

    # Get level from user
    level = get_level()

    # Present user 10 addition problems
    while True:

        # Declare variable to count number of attempts
        attempts = 0

        # Generate questions and sum
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        question = f"{x} + {y} = "

        # Present question until correct or until three incorrect attempts
        while True:
            try:

                # Prompt user for answer
                answer = int(input(question))

                # If answer equals sum then increment corrects and continue
                if answer == sum:
                    corrects += 1

                    # If corrects + incorrects is ten then print score and quit
                    if corrects + incorrects == 10:
                        print(f"Score: {corrects}")
                        quit()
                    else:
                        break
                
                # If incorrect answer then print EEE, increment attempts
                else:
                    attempts += 1
                    print("EEE")

                    # It three incorrect attempts then print answer and break
                    if attempts == 3:
                        incorrects +=1
                        print(question, sum)
                        break
                    else:
                        continue

            # Value errors are considered incorrect attempts
            except ValueError:
                attempts += 1
                print("EEE")
                if attempts == 3:
                    incorrects += 1
                    print(question, sum)
                    break
                else:
                    continue


def get_level():
    """
    Prompt user for level
    """
    while True:
        try:
            # Prompt user for level
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                pass

        # If level not int then pass
        except ValueError:
            pass


def generate_integer(level):
    """
    Randomly generate a positive integer with level number of digits
    """
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    else:
        integer = random.randint(100, 999)
    return integer


if __name__ == "__main__":
    main()
