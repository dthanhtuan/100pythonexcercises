a = int(input("Enter a number: "))
i = 2
not_a_prime = False
while i <= a:
    if i != a and a % i == 0:
        not_a_prime = True
    i += 1

if not_a_prime:
    print("Not a prime number")
else:
    print("Prime number")