'''
    Problem statement: Create a function that receives a non-negative integer and returns the factorial of that number.
    Problem Link: https://edabit.com/challenge/PNbsQzmDR3CJ9JHkB

'''
def factorial(n):        #function that returns the factorial of the number
    	if n==0:
		return (1)
	else:
		f=1
		for i in range(1,n+1):
			f=f*i
		return (f)

n=int(input())      #takes input from user
if n<0:
    print("Factorial of negative numbers don't exist")
else:
    result=factorial(n)  #function call to return the factorial of the number
    print(result)        # print the factorial of the number
	