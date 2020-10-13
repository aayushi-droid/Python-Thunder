'''
Problem Statement - Check if a given integer num is a Curzon number.
                    If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num,
                    then num is a Curzon number. Given a non-negative integer num, implement a function
                    that returns True if num is a Curzon number, or False otherwise.

Problem Link - https://edabit.com/challenge/HYjQKDXFfeppcWmLX

Example - 2 ** 5 + 1 = 33
          2 * 5 + 1 = 11
        33 is a multiple of 11
'''

def is_curzon(num):
	c1 = 2**num + 1
	c2 = 2*num + 1
	if c1%c2 == 0:
		return(True)
	else:
		return(False)

is_curzon(5)
is_curzon(10)
is_curzon(14)