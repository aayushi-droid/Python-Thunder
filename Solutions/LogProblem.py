'''
Problem statement: A logarithm is kind of like reverse exponents. There is a base and a number in a logarithm. The point of a logarithm is to find out what power you have to raise the base to get the number next to the base.
Problem Link: https://edabit.com/challenge/o7LPd9dAE5x9k7zFj
'''


def logarithm(base, num):
	if isinstance(base,str) or isinstance(num,str):
		return 'Invalid'
	if base <= 1:
		return 'Invalid'
	if num < 1:
		return 'Invalid'
	if num == 1 :
		return 0

	pow = 0
	while num > 1:
		pow += 1
		num /= base
	return pow
