'''
    Probem Task  : Write a function to read the billable days of an employee
                   and return the bonus he/she has obtained in that quarter.
    Problem Link : https://edabit.com/challenge/ksiA6Q34iXgTcMeZF
'''


def bonus(days: int):
    total_bonus = 0
    if days > 48:
        total_bonus += 600 * (days - 48)
        days = 48
    if days >= 41:
        total_bonus += 550 * (days - 40)
        days = 40
    if days >= 33:
        total_bonus += 325 * (days - 32)

    return total_bonus


print(bonus(15))
print(bonus(37))
print(bonus(50))
