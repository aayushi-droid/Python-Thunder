'''
    Probem Task  : Create a function that takes a number as an argument and
                   returns "Fizz", "Buzz" or "FizzBuzz".
    Problem Link : https://edabit.com/challenge/WXqH9qvvGkmx4dMvp
'''


def fizz_buzz(num: int):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))
