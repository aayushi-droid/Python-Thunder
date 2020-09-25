# Problem-Task : Calculates the number of different squares in an n * n square grid.
# Problem Link : https://edabit.com/challenge/ncqFJAp4bBiGwfBcg

def number_squares(n):
    return (n*(n+1)*(2*n+1))/6


print(number_squares(2))
