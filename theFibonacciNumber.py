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
		return num
	else:
		return fibonacci(num - 1) + fibonacci(num - 2)
    
print(fibonacci(5))


Fibonacci numbers using Dynamic Programming (Memoization) :

def fibonacci(num,qb):
	if num <2:
		return num
	if qb[num]!=0:
		return qb[num]
	
	fibm1=fibonacci(num-1,qb)
	fibm2=fibonacci(num-2,qb)
	fib=fibm1+fibm2
	qb[num]=fib
	
	return fib
	
print(fibonacci(5,[]))
	
	
