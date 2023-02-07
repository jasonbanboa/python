import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"((^\d\d?):?(\d?\d?)) ([AP]M) to ((\d\d?):?(\d?\d?)) ([AP]M)$", s, re.IGNORECASE):
        time = list(match.groups())

        if int(time[1]) > 12 or int(time[5]) > 12:
            raise ValueError
        for i in range(len(time)):
            if ":" in time[i]:
                f, s = time[i].split(":")
                if int(s) >= 60:
                    raise ValueError
        _from_ = time[1:4]
        _to_ = time[5:]
        from_ = match_input(_from_)
        to = match_input(_to_)
        return f"{from_} to {to}"

    else:
        raise ValueError


def match_input(time_l):
    hour = time_l[0]
    min = time_l[1]
    apm = time_l[2]
    if hour == "12" and apm == "AM":
        hour = 0
    if hour == "12" and apm == "PM":
        hour = 12
    elif hour != "12" and apm == "PM":
        hour = int(hour) + 12
    if min == "":
        min = "00"
    return f"{int(hour):02}:{min}"


if __name__ == "__main__":
    main()
