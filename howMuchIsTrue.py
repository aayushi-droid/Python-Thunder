'''

Problem statement: Create a function which returns the number of True values in a list.
Problem Link: https://edabit.com/challenge/wFpi2zFGxWxfj5mZS

'''

def howMuchIsTrue(arr):
  count = len([ x for x in arr if x ])
  return count
