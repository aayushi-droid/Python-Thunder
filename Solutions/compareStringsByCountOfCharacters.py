'''
    Probem Task : This program will Compare Two Strings by Count of Characters
    Problem Link : https://edabit.com/challenge/C3N2JEfFQoh4cqQ98

    Create a function that takes two strings as arguments and return either True or False
    depending on whether the total number of characters in the
    first string is equal to the total number of characters in the second string.
'''

def compareStringsByCountOfCharacters(string1,string2):
    len1=len(string1)
    len2=len(string2)

    if len1==len2:
        return True
    else:
        return False


string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
print(compareStringsByCountOfCharacters(string1,string2))


        
