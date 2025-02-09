import math

a = int(input("Enter a number: "))
x = math.sqrt(a)
print("x = ", x)
if x == round(x):
    print("True")
else:
    print("False")