import inflect

p = inflect.engine()


name_l = []

while True:
    try:
        name = input("Name: ").title().strip()
        name_l.append(name)


    except EOFError:
        print("Adieu, adieu, to",p.join(name_l))
        break