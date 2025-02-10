n = int(input("Enter the number: "))

print("Using for loop")
x = 0
for i in range(1, n + 1):
    x = x + i
print(x)

print("Using while loop")
x = 0
i = 1
while i <= n:
    x = x + i
    i = i + 1
print(x)

print("Using formula")
print(n * (n + 1) // 2)

