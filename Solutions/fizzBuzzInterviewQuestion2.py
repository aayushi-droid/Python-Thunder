"""
Problem statement: Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
Problem Link: https://edabit.com/challenge/WXqH9qvvGkmx4dMvp
"""
def fizzBuzz(n):
    if n % 3 == 0:
        return "FizzBuzz" if n % 5 == 0 else "Fizz"
    return "Buzz" if n % 5 == 0 else n

print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))
print(fizzBuzz(7))