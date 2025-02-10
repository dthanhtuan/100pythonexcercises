a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
i = 1
max = a if a > b else b
while i <= max:
    if a % i == 0 and b % i == 0:
        print(i)
    i += 1
