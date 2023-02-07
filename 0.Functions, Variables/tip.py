def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# .strip removes every character inside the arguement
def dollars_to_float(d):
    return float(d.strip("$"))


# the function [:-1] removes the last character of the string
# .strip could also be used e.g p.strip("%")
def percent_to_float(p):
    return float(p.strip("%")) / 100


main()