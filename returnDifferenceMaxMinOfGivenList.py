'''
Problem Task:
        Create a function that takes a list and returns the difference between the biggest and smallest numbers.

        Examples-
        difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
        # Smallest number is -50, biggest is 32.

        difference_max_min([44, 32, 86, 19]) ➞ 67
        # Smallest number is 19, biggest is 86.

Problem link:
https://edabit.com/challenge/XsJLwhAddzbxdQqr4

'''

def difference_max_min(l):
    return max(l)- min(l)

t=int(input('Enter no of test case: '))
while(t>0):
    l=list(map(int,input('Enter list :').split()))
    print(difference_max_min(l))
    t-=1
