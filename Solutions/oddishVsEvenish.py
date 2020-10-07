import sys
from functools import reduce

"""
    Probem Task: Create a function that determines whether a number is Oddish or Evenish. 
    A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the 
    sum of all of its digits is even. If a number is Oddish, return "Oddish". 
    Otherwise, return "Evenish".

    Problem Link: https://edabit.com/challenge/r6TSNwkLZ2DgsoKiH
"""

def main(number):
    result_map = ["Evenish", "Oddish"]
    total = reduce(lambda x, y: x + int(y), str(number), 0)
    return result_map[total%2]


if __name__ == "__main__":
    print(main(int(sys.argv[1])))
