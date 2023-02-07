import sys
import csv


students = []


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments ")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                l, f = row["name"].split(" ")
                students.append({"first": f, "last": l.replace(",", ""), "house": row["house"]})


        with open(sys.argv[2], "w") as file:
            fieldnames = ['first', 'last', "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for data in students:
                writer.writerow(data)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")