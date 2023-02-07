def main():
    global lama
    time = input("what time is it? ")
    lama = time.split(":")
    convert(time)
    if convert(time) in range(420, 481):
        print("breakfast time")

    elif convert(time) in range(720, 781):
        print("lunch time")

    elif convert(time) in range(1080, 1141):
        print("dinner time")


def convert(_):
    return float(lama[0]) * 60 + float(lama[1])


if __name__ == "__main__":
    main()