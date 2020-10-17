'''
Problem Task: Write a function that inverts the keys and values of a dictionary.
Problem Link: https://edabit.com/challenge/Axim3Ld5zu9RFLZKr
'''

## Use Bitwise Operator (% modulo operator disallowed.)
import re
def is_odd(n):
	if (n & 1)==True:
		return "Yes"
	else:
		return "No"
	

## Use Regular Expression (% modulo operator disallowed.)
def is_even(n):
    pattern="^-?\d*[02468]$"
    result = re.match(pattern, n)
    if result:
        return "Yes"
    else:
        return "No"	
	
	
