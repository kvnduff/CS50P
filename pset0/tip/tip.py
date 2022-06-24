""" Tip calculator """

def main():
    """ Print tip amount """
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    """ Convert dollars to float """
    return float(d.replace("$", ""))

def percent_to_float(p):
    """ Convert percent to float """
    return float(p.replace("%", "")) / 100

main()
