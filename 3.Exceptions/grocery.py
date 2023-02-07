def lister():
    grocery = {}

    while True:
        try:
            item = input().strip().upper()
            if item not in grocery:
                grocery[item] = 1

            elif item in grocery:
                grocery[item] = grocery[item] + 1

        except EOFError:
            for stuff in sorted(grocery.keys()):
                print(f"{grocery[stuff]} {stuff}")
            break




lister()
