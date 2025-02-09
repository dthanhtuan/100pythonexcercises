ary = input("Enter the numbers, separated by commas: ")
ary = [float(x) for x in ary.split(",")]
print("input: ", ary)
ary.sort()
print("Sorted: ", ary)