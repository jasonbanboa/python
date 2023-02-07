from random import randint


def main():
    final_score = generate_level(get_level())
    print(f"Score: {final_score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                return level
        except ValueError:
            pass


def generate_level(level):
    i = 0
    score = 0
    while i < 10:
        if level == 1:
            x = randint(0, 9)
            y = randint(0, 9)
            answer = x + y
            if play_rounds(x, y, answer) == True:
                score += 1
            i += 1
        if level == 2:
            x = randint(10, 99)
            y = randint(10, 99)
            answer = x + y
            if play_rounds(x, y, answer) == True:
                score += 1
            i += 1

        if level == 3:
            x = randint(100, 999)
            y = randint(100, 999)
            answer = x + y
            if play_rounds(x, y, answer) == True:
                score += 1
            i += 1

    return score


def play_rounds(first_n, second_n, ans):
    rounds = 0
    while rounds < 3:
        try:
            question = int(input(f"{first_n} + {second_n} = "))
            if question == ans:
                return True
            elif question != ans:
                raise ValueError

        except ValueError:
            print("EEE")
            rounds += 1
            if rounds == 3:
                print(f"{first_n} + {second_n} = {ans}")


if __name__ == "__main__":
    main()