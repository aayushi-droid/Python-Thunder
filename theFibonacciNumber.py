'''
    Probem Task : Create a function that, given a number, returns the corresponding Fibonacci number.
    Problem Link : https://edabit.com/challenge/8Ko5tPg8Ch5SRCAhA

Examples:   
    fibonacci(3) ➞ 3

    fibonacci(7) ➞ 21

    fibonacci(12) ➞ 233
'''

def fibonacci(num):
	if num < 2:
		return 1
	else:
		return fibonacci(num - 1) + fibonacci(num - 2)
    
print(fibonacci(6))
