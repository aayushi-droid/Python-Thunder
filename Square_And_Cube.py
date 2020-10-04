"""
Problem Statement: Create a function that
takes a list of two numbers and checks
if the square root of the first number is equal to
the cube root of the second number.
Problem Link: https://edabit.com/challenge/NMHFTCMqW6j8sXkNd
"""


def check_square_and_cube(lst):
    """Check sqaure root and cube root"""
    return lst[1] == lst[0]* (lst[0])**(0.5)

print(check_square_and_cube([4, 8]))
