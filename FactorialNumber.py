"""
Problem Statement: Create a function that receives a non-negative integer 
and returns the factorial of that number.
Problem Link: https://edabit.com/challenge/PNbsQzmDR3CJ9JHkB
"""


def fact(n):
	if n < 0:
			return "Negative Number"
	elif n == 0:
			return 1
	else:
			if n == 1:
				return 1
	
			return n * fact(n - 1)
fact(1)
