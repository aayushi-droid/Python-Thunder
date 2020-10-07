"""
    Probem Task  : Create a function that takes an integer n and returns
                   the identity matrix of n x n dimensions. For this cha-
                   llenge, if the integer is negative, return the mirror
                   image of the identity matrix of n x n dimensions. It 
                   does not matter if the mirror image is left-right or
                   top-bottom.
    Problem Link : https://edabit.com/challenge/QN4RMpAnktNvMCWwg
"""


def id_mtrx(n):
    '''
    Return an identity matrix of dimensions n X n if
    n is positive else return mirror image of identity
    matrix with dimensions n X n.
    '''
    # Return Error in case the dim passed is a string
    if type(n) != int:
        return 'Error'

    # Construct the identity matrix
    mtrx = [[0 if i != j else 1 for j in range(abs(n))] for i in range(abs(n))]
    # If negative n, get the mirror image of the matrix
    if n < 0:
        mtrx = mtrx[::-1]
    return mtrx


if __name__ == '__main__':
    dim = int(input("Enter dimension of the identity matrix: "))
    mtrx = id_mtrx(dim)
    print(mtrx)
