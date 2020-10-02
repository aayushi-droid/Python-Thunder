'''
    Probem Task : This program tells whether a numbers is oddish or evenish
    Problem Link : https://edabit.com/challenge/r6TSNwkLZ2DgsoKiH
'''

def oddishOrEvenish(n):
    s=0
    while n!=0:
        s=s+(n%10)
        n=n//10
    if s%2==0:
        print("Evenish")
    else:
        print("Oddish")

if __name__ == "__main__":
    num=int(input("Enter the number\n"));
    oddishOrEvenish(num)
