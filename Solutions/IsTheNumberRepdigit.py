"""
A repdigit is a positive number composed out of the same digit.

Create a function that takes an integer and returns whether it's a repdigit or not.

Examples
is_repdigit(66) ➞ True

is_repdigit(0) ➞ True

is_repdigit(-11) ➞ False
"""


def is_repdigit(num):
    if num >= 0:
        return True
    else:
        return False


print(is_repdigit(-10))
