print("Using for loop:")
for i in range(0, 100, 2):
    if i % 3 == 0:
        print(i)

print("Using while loop:")
i = 0
while i < 100:
    if i % 3 == 0:
        print(i)
    i += 2