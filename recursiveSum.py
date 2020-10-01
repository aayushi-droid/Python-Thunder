'''


    Problem statement: Write a function that finds the sum of the first n natural numbers. Make your function recursive.

    Problem Link: https://edabit.com/challenge/si2H6WC5YX99cn6LQ


    Write a function that finds the sum of the first n natural numbers. Make your function recursive.
    
    
    Examples
    sum_numbers(5) ➞ 15
    # 1 + 2 + 3 + 4 + 5 = 15

    sum_numbers(1) ➞ 1

    sum_numbers(12) ➞ 78
'''

def recursiveSum(n : int) -> int:
    if n == 0:
        return 0

    else:
        return n + recursiveSum(n-1)


if __name__ == '__main__':
    print(recursiveSum(1))
    print(recursiveSum(3))
    print(recursiveSum(5))
