n = int(input("Enter a number: "))
if int(n) <= 0:
    print("Enter a positive number")
else:
    even_count = 0
    odd_count = 0
    for num in str(n):
        if int(num) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)