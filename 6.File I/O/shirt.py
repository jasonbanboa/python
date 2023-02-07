from PIL import Image, ImageOps
import sys
import os


if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if len(sys.argv) == 3:
    try:
        root1 = os.path.splitext(sys.argv[1])
        root2 = os.path.splitext(sys.argv[2])

        image = Image.open(sys.argv[1])
        shirt = Image.open('shirt.png')

        if root1[1] == root2[1]:
            result = ImageOps.fit(image, shirt.size)
            result.paste(shirt, shirt)
            result.save(sys.argv[2])

        else:
            sys.exit("Input and output have different extensions")

    except FileNotFoundError:
        sys.exit("Invalid input")





