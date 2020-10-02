'''
    Probem Task : Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.
    Problem Link : https://edabit.com/challenge/5eHy5yapqz8kP94ih
'''

def returnTheAbsoluteSum(nums):
	sum = 0
	for ele in nums: sum = sum + abs(ele)
	return sum
