# Problem statement: Given the month and year as numbers, return whether that month contains a Friday 13th.
# Problem Link: https://edabit.com/challenge/Xkc2iAjwCap2z9N5D

import datetime


def has_friday_13(month, year):
    day = datetime.datetime(year, month, 13).weekday()
    if day == 4:
        return True
    return False


print(has_friday_13(3, 2020))
