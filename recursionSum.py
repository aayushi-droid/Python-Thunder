'''
    Probem Task : Write a function that finds the sum of the first n natural numbers. Make your function recursive.
    Problem Link : https://edabit.com/challenge/si2H6WC5YX99cn6LQ
'''

def sum_of_numbers(x):
    if x != 0:
        x += sum_of_numbers(x-1)
    else:
        return 0
    return x

