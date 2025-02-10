a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
i = 1
max = a if a > b else b
max_factor = 0
while i <= max:
    if a % i == 0 and b % i == 0:
        print(i)
        if i > max_factor:
            max_factor = i
    i += 1
print("Max common factor:", max_factor)