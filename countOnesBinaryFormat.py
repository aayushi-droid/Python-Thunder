'''
    Probem Task : Count the amount of ones in the binary representation of an integer. So for example, since 12 is '1100' in binary, the return value should be 2.
    Problem Link : https://edabit.com/challenge/GbyPdqNnp75Wci7Cn
'''

def count_ones(n): 
	count = 0
	while (n): 
		count += n & 1
		n >>= 1
	return count 
  
  
i = 0000
print(count_ones(i)) 