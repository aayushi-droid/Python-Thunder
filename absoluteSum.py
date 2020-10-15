'''
    Problem Task : Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.
    Problem Link : https://edabit.com/challenge/5eHy5yapqz8kP94ih
'''


def get_abs_sum(lst):
    sum = 0
    for x in lst:
        if x < 0:
            sum += (x * -1)
        else:
            sum += x
    return sum
