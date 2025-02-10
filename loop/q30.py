a = int(input("Enter a number: "))
i = 1
count = 0
while i <= a:
    if a % i == 0:
        count += 1
        print(i)
    i += 1
print("Total factors:", count)