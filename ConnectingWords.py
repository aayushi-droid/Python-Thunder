"""python3"""
#Problem Statement : Write a function that connects each previous word to the next word by the shared letters. 
                     Return the resulting string (removing duplicate characters in the overlap) and the minimum number of shared letters across all pairs of strings.
#Problem Link : https://edabit.com/challenge/qNQkYzY8GpiFMmndh

import re
def join(lst):
	ol = [len(i) for i in re.findall(r'(\w+) (?=\1)', ' '.join(lst))]
	a = re.sub(r'(\w+) (?=\1)', '', ' '.join(lst)).replace(' ', '')
	return [a, min(ol) if ol else 0]

#join(["to", "ops", "psy", "syllable"]) ➞ ["topsyllable", 1]
# "to" and "ops" share "o" (1)
# "ops" and "psy" share "ps" (2)
# "psy" and "syllable" share "sy" (2)
# the minimum overlap is 1

a = join(["to", "ops", "psy", "syllable"])
print(a)

#for taking input from user
#n=input()
#a=join(n)
