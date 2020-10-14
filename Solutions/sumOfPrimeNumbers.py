"""
Problem statement : Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.
Problem link : https://edabit.com/challenge/GAbxxcsKoLGKtwjRB
Example:
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
sum_primes([]) ➞ None

"""
import math


def is_prime(num):
    # If given number is greater than 1
    if num > 1:
        target = int(math.sqrt(num))
        # Iterate from 2 to sqrt(n)
        for i in range(2, target+1):
            # If num is divisible by any number between
            # 2 and sqrt(n), it is not prime
            if (num % i) == 0:
                return False
        else:
            return True

    else:
        return False


def sum_primes(numbers):
    prime_nos = [num for num in numbers if is_prime(num)]
    return sum(prime_nos) if prime_nos else None


# Test Cases
print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_primes([2, 3, 4, 11, 20, 50, 71]))
print(sum_primes([]))