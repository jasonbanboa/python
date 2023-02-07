import random
import sys


while True:
    try:
        level = int(input("Level: "))
        ans = random.randint(1, level)

    except ValueError:
        pass

    else:
        while True:
            try:
                guess = int(input("Guess: "))

            except ValueError:
                pass

            else:
                if ans == guess:
                    sys.exit("Just right!")

                elif ans > guess:
                    print("Too small!")

                elif ans < guess:
                    print("Too large!")




