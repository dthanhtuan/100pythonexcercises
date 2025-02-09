a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))


def is_triangle(a, b, c):
    if all(value > 0 for value in [a, b, c]):
        if a + b > c and a + c > b and b + c > a:
            print("The numbers can be sides of a triangle")
            return True
        else:
            print("The numbers cannot be sides of a triangle")
            return False
    else:
        print("All numbers are not positive")
        return False


if is_triangle(a, b, c):
    if a == b == c:
        print("The triangle is equilateral")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")
