"""
    
    Problem Statement : 
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

        What is the 10 001st prime number?
        
"""

from math import sqrt
from itertools import count, islice


def prime_number_range(nth):
    count = 1
    num = 2
    while True:
        if num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1))):
            count = count + 1
            yield num
        else:
            num = num + 1

        if count == nth:
            break
    return


ans = [i for i in prime_number_range(10001)][-1]
print(ans)
