# original
import sys

def main():
    while True:
        gas = input("Fraction: ")

        p = convert(gas)
        print(gauge(p))
        break


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            f = int(x) / int(y) * 100

        except (ValueError, ZeroDivisionError):
            raise

        else:
            return int(f)


def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()