'''
    Probem Task : Write a function that returns the least common multiple (LCM) of two integers.
                  Examples:
                      lcm(9, 18) ➞ 18
                      lcm(8, 5) ➞ 40
                      lcm(17, 11) ➞ 187
                  Notes
                      Both values will be positive.
                      The LCM is the smallest integer that is divisible by both numbers such that the remainder is zero.
    Problem Link : https://edabit.com/challenge/rSa8y4gxJtBqbMrPW
'''



def lcm(n1, n2):
	i = max(n1, n2)
	while i%n1 or i%n2:
		i += 1	
	return i
