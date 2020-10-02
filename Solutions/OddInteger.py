'''
    Probem Task: Create a function that takes a list and finds the integer which appears an odd number of times.
    Problem Link: https://edabit.com/challenge/9TcXrWEGH3DaCgPBs
'''

def oddInteger(intList):
    xoredValue = intList[0]
    for ele in intList[1:]:
        xoredValue = (xoredValue ^ ele)
    return xoredValue
