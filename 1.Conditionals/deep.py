ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

answers = ["42", "forty two", "forty-two",]

if ans in answers:
    print("Yes")

else:
    print("No")