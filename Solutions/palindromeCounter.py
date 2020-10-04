'''
problem statement: Create a function that returns the number of palindrome numbers in a specified range (inclusive).
Problem Link: https://edabit.com/challenge/BRoBDeEc2be7wm8BD
Examples: 
     
     countPalindromes(1, 10) ➞ 9

     countPalindromes(555, 556) ➞ 1

     countPalindromes(878, 898) ➞ 3

'''

def num_palindromes(start, end):
    count = 0
    for i in range(start, end + 1):
        if str(i) == str(i)[::-1]:
            count += 1
    return count
