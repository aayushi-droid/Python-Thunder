
"""python3"""
#Problem Statement : Create a function that gets every pair of numbers from an array that sums up to eight and returns it as an array of pairs (pair sorted ascendingly) collated into an object. See the following examples for more details.
#Problem Link : https://edabit.com/challenge/ZkWSacTDQ65A3gh6j

def esu(lst):
	ans = []
	for i,n in enumerate(lst[::-1]):
		if 8-n in lst[::-1][i+1:]:
			ans.append(sorted([n,8-n]))
	return {"pairs": ans[::-1]}

#esu([1, 2, 3, 4, 5]) ➞ {"pairs": [[3, 5]]}
#esu([10, 9, 7, 2, 8]) ➞ {"pairs": []}
#esu([1, 6, 5, 4, 8, 2, 3, 7]) ➞ {"pairs": [[2, 6], [3, 5], [1, 7]]}
# [6, 2] first to complete the cycle (to sum up to 8)
# [5, 3] follows
# [1, 7] lastly
# [2, 6], [3, 5], [1, 7] sorted according to cycle completeness, then pair-wise

a = [1, 6, 5, 4, 8, 2, 3, 7]
b = esu(a)
print(b)

#to take custom input from user
#a = input()
#b = esu(a)
#print(a)
