# calculate the number of days of a month

month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
m31_days = [1, 3, 5, 7, 8, 10, 12]
m30_days = [4, 6, 9, 11]


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if month in m31_days:
    print("31 days")
elif month in m30_days:
    print("30 days")
else:
    if is_leap_year(year):
        print("29 days")
    else:
        print("28 days")
