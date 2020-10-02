'''
    Problem statement: Create a function that takes a string and returns it as an integer.
    Problem Link: https://edabit.com/challenge/GPmoRCZKkyNtoJMcN

    Examples:
        string_int("6") ➞ 6

        string_int("1000") ➞ 1000

        string_int("12") ➞ 12
'''

def StringAsInteger(a):
    return int(a)

a = input("Enter Number String that you want to typecast ")
print(StringAsInteger(a))

