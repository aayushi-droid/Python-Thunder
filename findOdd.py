'''
    Probem Task : Create a function that takes an array and finds the integer which appears an odd number of times.
    Problem Link : https://edabit.com/challenge/wgnmQTbfssuhvZHqe
'''


def findOdd(arr):
    # Initialize result
    res = 0

    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element
    return res
