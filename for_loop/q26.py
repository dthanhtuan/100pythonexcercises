a = int(input("Enter a number: "))

print("Using for loop:")
for i in range(1, 11):
    print(a, "x", i, "=", a * i)

print("Using while loop:")
i = 1
while i < 11:
    print(a, "x", i, "=", a * i)
    i += 1
