"""
    Problem Task : This program will find longest substring with alternating odd/even or even/odd digits
    Problem Link : https://edabit.com/challenge/RB6iWFrCd6rXWH3vi
"""


def LongestAlternativeSubstring(digits):
    sol = digits[0]
    for i in range(1, len(digits)):
        if int(digits[i - 1]) % 2 != int(digits[i]) % 2:
            sol += digits[i]
        else:
            sol += " " + digits[i]
    ret = max(sol.split(" "), key=len)
    return ret if len(ret) >= 2 else False


digits = input("Enter string ")
print("Result : ", LongestAlternativeSubstring(digits))
