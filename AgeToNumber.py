
'''
    Probem Task : This program will convert age to days
    Problem Link : https://edabit.com/challenge/xbZR26rHMNo32yz35
'''

def AgeToNumber(n):
    return n*365

if __name__ =="__main__":
    age = int(input())
    while age < 0:
        print("You entered Invalid age!, Please enter again!")
        age = int(input())

    print(AgeToNumber(age))
