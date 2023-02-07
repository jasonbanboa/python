from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    date = convert(get_date(input("Date of Birth: ")))
    final_date = p.number_to_words(date).capitalize()
    l = final_date.split(" ")

    for word in l:
        if word == "and":
            l.remove(word)

    print(" ".join(l), "minutes")


def get_date(user_input):
    try:
        year, month, day = user_input.split("-")
        given_date = date(int(year), int(month), int(day))

    except ValueError:
        sys.exit("Invalid date")

    else:
        return given_date


def convert(given_date):
    birth_year = given_date
    today = date.today()
    delta_difference = today - birth_year
    days, times = str(delta_difference).split("days")

    minutes = (int(days) * 24) * 60
    return minutes


if __name__ == "__main__":
    main()