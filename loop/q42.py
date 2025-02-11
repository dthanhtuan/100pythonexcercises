# fibonacci series
a = int(input("Enter a number: "))
n1 = 1
n2 = 1
next_number = n1 + n2
while next_number <= a:
    print(next_number)
    n1 = n2
    n2 = next_number
    next_number = n1 + n2
print(n2)
