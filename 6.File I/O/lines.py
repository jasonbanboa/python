import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few comand-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many comand-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
            tally = 0
            for line in lines:
                if checker(line) == False:
                    tally += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    else:
        print(tally)


def checker(l):
    if l.isspace():
        return True
    if l.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()