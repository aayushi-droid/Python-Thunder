'''
Problem statement: Create a function that takes a number as its only argument and 
returns true if it's less than or equal to zero, otherwise return false.

Problem Link: https://edabit.com/challenge/Rx2pkSA9dCmtwS8xt

'''
def check (number):
    if number <=0:
        return True
    else:
        return False
num=int(input("Enter the number"))
print(check(num))