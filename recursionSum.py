'''
    Probem Task : Write a function that finds the sum of the first n natural numbers. Make your function recursive.
    Problem Link : https://edabit.com/challenge/si2H6WC5YX99cn6LQ
'''
# Create the function 
def sum_numbers(x):
    if x != 0:
        x += sum_numbers(x-1)
    else:
        return 0
    return x

