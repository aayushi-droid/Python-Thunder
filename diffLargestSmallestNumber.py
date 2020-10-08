'''
    Probem Task : This program will return the difference between the biggest and smallest numbers
    Problem Link : https://edabit.com/challenge/SFzHtm63XT6EYNHWY
'''


def diffFunc(list):
    sortList = sorted(list)
    return sortList[-1] - sortList[0]

print(diffFunc([10, 4, 1, 4, -10, -50, 32, 21]))
print(diffFunc([44, 32, 86, 19]))