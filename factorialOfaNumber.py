import functools
factorial = lambda n: functools.reduce(lambda x, y: x * y, range(1, n+1))
num=int(input('Enter any Integer: '))
print(factorial(num))