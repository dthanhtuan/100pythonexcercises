# ax2 + bx + c = 0
a = float(input("Enter the number 1: "))
b = float(input("Enter the number 2: "))
c = float(input("Enter the number 3: "))
if a == 0:
    if b != 0:
        print("No solution")
    else:
        print("Infinite solutions")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("No solution")
    elif delta == 0:
        print("X = ", -b / (2 * a))
    else:
        print("X1 = ", (-b + delta ** 0.5) / (2 * a))
        print("X2 = ", (-b - delta ** 0.5) / (2 * a))
