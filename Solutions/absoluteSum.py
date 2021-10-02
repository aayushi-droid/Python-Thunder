'''
    Problem Task : Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.
    Problem Link : https://edabit.com/challenge/5eHy5yapqz8kP94ih
'''


def get_abs_sum(lst):
    """ Get absolute sum of list """
    sum = 0
    for x in lst:
        if x < 0:
            sum += (x * -1)
        else:
            sum += x
    return sum

assert get_abs_sum([1, 2, 3, 4, 5]) == 15
assert get_abs_sum([-1, -2, -3, -4, -5]) == 15
assert get_abs_sum([1, -2, 3, -4, 5]) == 15
assert get_abs_sum([-1, 2, -3, 4, -5]) == 15
assert get_abs_sum([]) == 0
assert get_abs_sum([-1]) == 1

""" def get_abs_sum(lst):
    return sum(abs(i) for i in lst)
 """