'''
    Problem Task: Write a function that inverts the keys and values of a dictionary.
    Problem Link: https://edabit.com/challenge/Axim3Ld5zu9RFLZKr
'''

def invert(dct):
    inverse={}
    for x, y in dct.items():
          inverse[y] = x
    return inverse
