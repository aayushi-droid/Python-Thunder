'''
Problem statement: Write a function that returns the boolean True if the given number is zero, the string "positive" if the number is greater than zero or the string "negative" if it's smaller than zero.

Problem Link: https://edabit.com/challenge/2TdPmSpLpa8NWh6m9
'''


def if_elif_else(n : int):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return True

if __name__ == '__main__':

    print(if_elif_else(-1))
    print(if_elif_else(1))
    print(if_elif_else(0))
