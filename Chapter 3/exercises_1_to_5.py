# Exercise 1 - Leap year function
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is not a leap year")

is_leap_year(2024)