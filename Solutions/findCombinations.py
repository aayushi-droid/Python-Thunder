"""
Problem statement: Create a function that takes a variable number of arguments, each argument representing the number of items
 in a group, and returns the number of permutations (combinations) of items that you could get by taking one item from each group.
Problem Link: https://edabit.com/challenge/G9QRtAGXb9Cu368Pw

"""


def combinations(*items):
    res = 1
    for item in items:
        if item != 0:
            res *= item
    return res


print(combinations(2, 3))
print(combinations(3, 7, 4))
print(combinations(2, 3, 4, 5))
