# Problem-Task : Calculates the sum of n natural numbers recursively.
# Problem Link : https://edabit.com/challenge/si2H6WC5YX99cn6LQ

def sum_numbers(n):
    if(n == 0):
        return 0
    else:
        return n + sum_numbers(n-1)

print(sum_numbers(5))
print(sum_numbers(1))
print(sum_numbers(12))