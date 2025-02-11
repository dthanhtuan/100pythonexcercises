n = int(input("Enter a number: "))
n_str = str(n)
total = 0
for num in n_str:
    total += int(num)
print("Sum of digits:", total)
