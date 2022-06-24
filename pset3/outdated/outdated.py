"""
Convert middle-endian dates to ISO 8601 dates
"""


def main():
    get_date("Date: ")


# List of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# Get date, allowing specified formats, convert to specified format
def get_date(prompt):
    while True:
        try:
            me_date = input(prompt)

            # If inputted date in format with "/"
            if "/" in me_date:
                m, d, y = me_date.split("/")
                month = int(m)
                day = int(d)
                year = int(y)

            # If inputted date in format with ","
            elif "," in me_date:
                m, d, y = me_date.split()
                month = int(months.index(m) + 1)
                day = int(d.rstrip(","))
                year = int(y)

            # Otherwise reprompt
            else:
                continue

            # Check for permitted day, month, year, reprompt if necessary
            if (
               day < 1 or day > 31 or
               month < 1 or month > 12 or
               year < 0 or year > 9999
               ):
                continue

            # Add leading zeros if month or day a single character
            month = str(month)
            day = str(day)
            if len(month) == 1:
                month = "0" + month
            if len(day) == 1:
                day = "0" + day

            # Print date and break
            print(f"{year}-{month}-{day}", end="")
            break

        # Handle value errors
        except ValueError:
            pass


if __name__ == "__main__":
    main()
