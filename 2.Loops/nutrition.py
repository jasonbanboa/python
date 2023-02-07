fruits = {

"apple" : "130",
"avocado" : "50",
"kiwifruit" : "90",
"pear" : "100",
"sweet cherries" : "100",
"banana" : "110"

}

def main():
    i = input("Item: ").lower()
    cal(i)


def cal(f):
    if f in fruits:
        print("Calories:", fruits[f])

main()