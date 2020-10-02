"""
    Probem Task  : 
    In the Code tab is a function which is meant to return how many uppercase letters there are in a list of various words. 
    Fix the list comprehension so that the code functions normally!

    Examples:
    count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6
    count_uppercase(["little", "lower", "down"]) ➞ 0
    count_uppercase(["EDAbit", "Educate", "Coding"]) ➞ 5

    Problem Link : https://edabit.com/challenge/Hs7YDjZALCEPRPD6Z
"""

def buggyUppercaseCounting(n):
    # n is the list containing strings
    count = 0

    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j].isupper():
                count += 1
    
    return count


# Test Cases
print(buggyUppercaseCounting(["SOLO", "hello", "Tea", "wHat"])) # => 6
print(buggyUppercaseCounting(["little", "lower", "down"])) # => 0
print(buggyUppercaseCounting(["EDAbit", "Educate", "Coding"])) # => 5

