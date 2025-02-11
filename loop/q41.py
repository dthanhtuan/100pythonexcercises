# check if the number is 2^k or not
n = int(input("Enter a number: "))
k = 0
while 2 ** k < n:
    k += 1
    if 2 ** k == n:
        print("Yes")
        break
