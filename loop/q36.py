a = int(input("Enter a number: "))
n = 0
total = 0
while total < a:
    n += 1
    total += 1 / n
print("The smallest n such that 1 + 1/2 + 1/3 + ... + 1/n > ", a, " is ", n)