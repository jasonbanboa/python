import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    l = []
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for i in range(1, 5):
            l.append(int(matches.group(i)))

        for j in l:
            if j <= 255:
                continue
            else:
                return False

        return True

    elif re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip) == None:
        return False



if __name__ == "__main__":
    main()

