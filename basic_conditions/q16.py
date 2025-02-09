a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))


def is_triangle(a1, b1, c1):
    if all(value > 0 for value in [a1, b1, c1]):
        if a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1:
            print("The numbers can be sides of a triangle")
            return True
        else:
            print("The numbers cannot be sides of a triangle")
            return False
    else:
        print("All numbers are not positive")
        return False


def isoceles(a1, b1, c1):
    if a1 == b1 or b1 == c1 or a1 == c1:
        return True
    return False


def equilateral(a1, b1, c1):
    if a1 == b1 == c1:
        return True
    return False


def right_angled(a1, b1, c1):
    if a1 * a1 == b1 * b1 + c1 * c1 or b1 * b1 == a1 * a1 + c1 * c1 or c1 * c1 == a1 * a1 + b1 * b1:
        return True
    return False


if is_triangle(a, b, c):
    if equilateral(a, b, c):
        print("The triangle is equilateral")
    elif isoceles(a, b, c):
        print("The triangle is isosceles")
    elif right_angled(a, b, c):
        print("The triangle is right-angled")
        if isoceles(a, b, c):
            print("The triangle is also isosceles")
    else:
        print("The triangle is scalene")
