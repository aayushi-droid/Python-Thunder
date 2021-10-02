#use _author_ = 'Kuruvilla Jacob'
'''
Problem statement:Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.
Problem Link:https://edabit.com/challenge/GAbxxcsKoLGKtwjRB

'''
def sum_primes(list1):
    sum1=0
    for num in list1:
        if num==2:
            sum1+=2
        elif num>1:
            for k in range(2,num-1):
                if num%k==0:
                    break
            else:
                sum1+=num
    if sum1==0:
        return None
    else:
        return sum1

            
