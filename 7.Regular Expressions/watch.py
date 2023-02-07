import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search('src="https{0,1}://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"', s):
        # return_match = f"https://youtu.be/{match.group(2)}"
        return f"https://youtu.be/{match.group(2)}"

    else:
        return None


if __name__ == "__main__":
    main()