'''
    Probem Task : A number is said to be Harshad if it's exactly divisible by 
    the sum of its digits. Create a function that determines whether a number 
    is a Harshad or not.
    Problem Link : https://edabit.com/challenge/Rrauvu8afRbjqPM8L
'''

sum=0
def harshad(n):
    global sum
    if n==0:
    	return 'Not Harshad'
    if(n>0):
        rem=n%10
        sum=sum+rem
        harshad(n//10)
    if(n % sum ==0):
        return "Harshad"
    else:
        return "Not Harshad"
    
n=int(input("Enter a number:"))
print(harshad(n))  
