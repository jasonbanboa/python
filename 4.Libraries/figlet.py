from sys import argv, exit
from pyfiglet import Figlet
from random import choice

figlet = Figlet()


if len(argv) == 1:
    random_font = True

elif len(argv) == 3 and argv[1] == "-f" or argv[1] == "--font":
    random_font = False

else:
    print("Invalid usage")
    exit(1)


figlet.getFonts()


if random_font == False:
    try:
        figlet.setFont(font=argv[2])
    except:
        print("Invalid usage")
        exit(1)

elif random_font == True:
    font = choice(figlet.getFonts())


user_input = input("Input: ")

print(f"Output: ")
print(figlet.renderText(user_input))
