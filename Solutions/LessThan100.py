"""
    Probem Task : Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.
    Problem Link : https://edabit.com/challenge/pZ3HxBfvejsvkEDo4
    
    Examples
      less_than_100(22, 15) ➞ True
      # 22 + 15 = 37
      less_than_100(83, 34) ➞ False
      # 83 + 34 = 117
      less_than_100(3, 77) ➞ true
"""


def less_than_100(num1, num2):
    return num1 + num2 < 100


print(less_than_100(22, 15))
print(less_than_100(83, 34))
