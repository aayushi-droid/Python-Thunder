"""
Imagine you took all the numbers between 0 and n and concatenated them together into a long string. 
How many digits are there between 0 and n? Write a function that can calculate this.
There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits between 0 and 100.

Examples :
digits(1) ➞ 0

digits(10) ➞ 9

"""


def digits(num):
    count = 0
    for i in range(1, num, 10):
        count += num - i + 1
    return count


print(digits(13))
