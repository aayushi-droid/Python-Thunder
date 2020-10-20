"""
    Probem Task  : "A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not."
    Problem Link : https://edabit.com/challenge/eADRy5SA5QbasA3Qt
"""

def is_harshad(inp):
    sum_of_digits = sum([int(digit) for digit in str(inp)])
    if inp % sum_of_digits == 0:
        return True
    else:
        return False

if __name__=='__main__': 
    if is_harshad(481) == True:
        print("Case 1 passed")
    if is_harshad(89) == False:
        print("Case 2 passed")
    if is_harshad(516) == True:
        print("Case 3 passed")
    if is_harshad(200) == True:
        print("Case 4 passed")