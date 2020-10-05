"""
    Probem Task  : Create a function that takes a string and returns a string with its letters in alphabetical order.
    Problem Link : https://edabit.com/challenge/4Agr8CTY7x2rAhh5n
"""

def alphaSoup(string):
    return ''.join(sorted(string))
    
print(alphaSoup('hello'))