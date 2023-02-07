def main():
    greet = input("Greeting: ").strip().lower()
    print(f"${value(greet)}")


def value(greeting):
    greeting = greeting.lower()
    greeting_list = list(greeting)
    greeting0 = greeting_list[0]

    if "hello" in greeting:
        a = 0
        return a

    elif greeting0 == "h":
        a = 20
        return a

    else:
        a = 100
        return a


if __name__ == "__main__":
    main()