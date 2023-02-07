valid = [
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

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def date():
    while True:
        try:
            ask = input("Date: ").strip().replace(",", "").title()
            m, d, y = ask.split(" ")
            if m in valid and int(d) <= 31:
                print(f"{y}-{int(months[m]):02}-{int(d):02}")
                break

        except ValueError:
            for i in ask:
                if i == "/":
                    m, d, y = ask.split("/")
                    if m in valid:
                        date()
                    if int(m) <= 12 and int(d) <= 31:
                        print(f"{y}-{int(m):02}-{int(d):02}")
                        return False



date()