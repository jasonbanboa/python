num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

special = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=',
           '{', '[', '}', '}', '|', ':', ';', '"', '<', ',', '>', '.', '?', '/']


def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isdigit():
        return False

    if 2 > len(s) or len(s) > 6:
        return False

    if len(s) > 2 and s[2] == "0":
        return False

    for i in s:
        if i in special:
            return False

    for i in s:
        if i in num and s[-1].isalpha():
            return False

    if s[-1].isdigit() and s[-2].isalpha():
        return False

    else:
        return True


if __name__ == "__main__":
    main()