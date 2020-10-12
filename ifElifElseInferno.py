'''
Problem Statement : Write a function that returns the boolean True if the given number is zero, the string "positive" if the number is greater than zero or the string "negative" if it's smaller than zero.
Problem Link : https://edabit.com/challenge/2TdPmSpLpa8NWh6m9
'''
def equilibrium(x):
	return not x or ('negative', 'positive')[x > 0]
