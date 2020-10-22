'''
Problem statement: Create a function that returns the thickness (in meters) of a piece of paper
                   after folding it n number of times. 
The paper starts off with a thickness of 0.5mm.

Problem Link: https://edabit.com/challenge/4t6YAJS8dtT7RQjta
'''

def num_layers(n):
    p = str((2**(n-1))/1000)
    return p + "m"
