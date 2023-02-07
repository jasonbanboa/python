vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# hello world
# hello hello

def main():
    tweet = input("Input: ")
    print(shorten(tweet))
    # prints something


def shorten(word):
    s = ""
    for i in word:
        if i not in vowel:
            s += i

    return s


if __name__ == "__main__":
    main()