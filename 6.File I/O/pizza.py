import sys
import csv
from tabulate import tabulate


menu = []

try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    with open(sys.argv[1]) as file:
        reader = csv.reader(file,)
        for line in reader:
            menu.append(line)


except(FileNotFoundError):
    sys.exit("File does not exist")


else:
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))

