x, y, z = input("Expression: ").split()

float_x = float(x)
float_z = float(z)

if y == "+":
    print(float_x + float_z)

elif y == "-":
    print(float_x - float_z)

elif y == "*":
    print(float_x * float_z)

elif y == "/":
    print(float_x / float_z)
