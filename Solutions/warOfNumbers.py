'''
There's a great war between the even and odd numbers. 
Many numbers already lost their life in this war and it's your task to end this. 
You have to determine which group is larger: the even, or the odd. The larger group wins.

Create a function that takes an array of integers, sums the even and odd numbers seperately, 
then returns the larger of the sums minus the smaller.

Examples
warOfNumbers([2, 8, 7, 5]) ➞ 2
// 2 + 8 = 10
// 7 + 5 = 12
// 12 is larger than 10
// So we return 12 - 10 = 2

warOfNumbers([12, 90, 75]) ➞ 27

warOfNumbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168

Problem Link :- https://edabit.com/challenge/Aofd78q72sAtgCyEY

'''

def war_of_numbers(arr):
	even_sum = 0
	odd_sum  = 0
	for element in arr:

		if element % 2 == 0:
			even_sum += element

		else:
			odd_sum += element

	return abs(even_sum-odd_sum)


if __name__ == '__main__':
	print(war_of_numbers([12, 90, 75]))  # Should output :- 27

	print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))  # Should output :- 168