'''
Problem Statement: Create a function that receives a non-negative
integer and returns the factorial of that number.

Problem Link: https://edabit.com/challenge/PNbsQzmDR3CJ9JHkB
'''

def fact(n):
	if n == 0:
		return 1
	else:
		output = 1
		for i in range(1, n+1):
			output *= i
		return output
