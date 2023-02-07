a = input("camelCase: ")
b = "snake_case: "

print(b, end="")


for i in a:

    if i.islower():
        print(i, end="")

    elif i.isupper():
        print("_" + i.lower(), end="")



