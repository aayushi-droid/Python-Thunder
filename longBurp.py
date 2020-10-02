"""
    Problem Task: Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.
    Problem Link: https://edabit.com/challenge/irb783PpFTDqnumhN
"""

import sys

def long_burp(num):
    try:
        num = int(num)
        if num >= 1:
            r = "r" * num
            return r
        else:
            print("The number must be equal to or greater than 1")
            sys.exit()
    except ValueError:
        print("Input must be an integer")
        sys.exit()

num = input("Provide a number: ")
r = long_burp(num)
print("Bu" + r + "p")
