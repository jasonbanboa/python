def convert():
    a = input()
    change = a.replace(":)", "🙂").replace(":(", "🙁")

    if ":)" in a:
        print(change)

    elif ":(" in a:
        print(change)



convert()