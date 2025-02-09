# number of days from the beginning of the year to the date entered by the user

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

m31_days = [1, 3, 5, 7, 8, 10, 12]
m30_days = [4, 6, 9, 11]


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if month in m31_days:
    days_of_input_month = 31
elif month in m30_days:
    days_of_input_month = 30
elif month == 2:
    days_of_input_month = 29 if is_leap_year(year) else 28
else:
    print("Invalid month")
    exit()

number_of_days = 0
for m in range(1, month):
    if m in m31_days:
        number_of_days += 31
    elif m in m30_days:
        number_of_days += 30
    elif m == 2:
        number_of_days += 29 if is_leap_year(year) else 28

number_of_days += day

print("Number of days from the beginning of the year to the date entered by the user:",
      number_of_days)
