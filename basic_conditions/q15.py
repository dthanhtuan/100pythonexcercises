a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))

if all(value > 0 for value in [a, b, c]):
    if a + b > c and a + c > b and b + c > a:
        print("The numbers can be sides of a triangle")
    else:
        print("The numbers cannot be sides of a triangle")
else:
    print("All numbers are not positive")