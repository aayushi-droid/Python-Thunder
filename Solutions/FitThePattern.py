
"""python3"""
#Problem Statement : Create a function that checks if the sub-lists in a list adhere to the specified pattern.
#Problem Link : https://edabit.com/challenge/z9tnydD5Fix3g3mas

def chec(x):
  return [j for i in x for j in range(len(x)) if i == x[j]]
  
def checp(lst, pattern):
  return chec(lst) == chec(pattern)

check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True

#checp([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") ➞ True
#checp([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") ➞ True
#checp([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") ➞ True
#checp([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") ➞ True

a = [[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]]
b = "DCBA"
c = checp(a,b)
print(c)

#to take input from the user
#a = []
#for i in range(0,4):
#  a[i] = list(input())
#b = input()
#c=checp(a,b)
#print(c)
