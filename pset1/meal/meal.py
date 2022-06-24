"""
Indicate meal time
"""


def main():

    # Prompt user for time
    answer = input("What time is it? ")

    # Convert anwer to formatted time
    time = convert(answer)

    # Print meal according to time
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        return


# Convert time to required format
def convert(time):
    components = time.split(":")
    hour = components[0]
    minute = str((float(components[1]) / 60)).lstrip('0')
    return float(hour + minute)


if __name__ == "__main__":
    main()
