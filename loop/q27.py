#    *
#   * *
#  *   *
# *******
h = int(input("Enter the height of the triangle: "))
print("---Using while loop---")
middle_space = 1
i = 1
space_char = "-"
while i <= h:
    left_space = h - i
    if i == 1:
        print(space_char * left_space + "*")
    elif i == h:
        print("*" * (2 * h - 1))
    else:
        print(space_char * left_space + "*" + space_char * middle_space + "*")
        middle_space = middle_space + 2
    i = i + 1


# *******
#  *   *
#   * *
#    *
space_char = "-"
middle_space = 2 * h - 5

for i in range(h, 0, -1):
    left_space = h - i
    if i == 1:
        print(space_char * left_space + "*")
    elif i == h:
        print("*" * (2 * h - 1))
    else:
        print(space_char * left_space + "*" + space_char * middle_space + "*")
        middle_space -= 2



#    *
#   * *
#  *   *
# *******
print("---Using for loop---")
middle_space = 1
for i in range(1, h + 1):
    left_space = h - i
    if i == 1:
        print(space_char * left_space + "*")
    elif i == h:
        print("*" * (2 * h - 1))
    else:
        print(space_char * left_space + "*" + space_char * middle_space + "*")
        middle_space = middle_space + 2


# *******
#  *   *
#   * *
#    *
middle_space = 2 * h - 5
for i in range(h, 0, -1):
    left_space = h - i
    if i == 1:
        print(space_char * left_space + "*")
    elif i == h:
        print("*" * (2 * h - 1))
    else:
        print(space_char * left_space + "*" + space_char * middle_space + "*")
        middle_space -= 2

