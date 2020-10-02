"""
    Probem Task : This program will check if the number is Oddish or Evenish
    Problem Link : https://edabit.com/challenge/r6TSNwkLZ2DgsoKiH
"""

#!/usr/bin/env python

def sumofdigits(n):
    s = 0
    for digit in str(n):
        s += int(digit)
    return s
    
def oddishOrEvenish(n):
    if sumofdigits(n) % 2 == 0:
        print("Evenish")
    else:
        print("Oddish")
        
oddishOrEvenish(1234)
