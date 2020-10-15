"""
    Problem statement:
        Create a function that will build a staircase using the underscore _ and hash #
        symbols. A positive value denotes the staircase's upward direction and
        downwards for a negative value.
    Problem Link: https://edabit.com/challenge/YqLBEZJR9ySndYQpH
"""

def staircase(num_stairs):
    '''Builds a staircase using underscore ad hash symbols'''

    assert isinstance(num_stairs, int), 'num_stairs should be an integer'
    result = None
    if num_stairs > 0:
        reverse = False
    else:
        reverse = True
        num_stairs = -num_stairs
    stairs = [('_' * (num_stairs-i) + '#' * i) for i in range(1, num_stairs+1)]
    if reverse:
        result = '\n'.join(reversed(stairs))
    else:
        result = '\n'.join(stairs)
    return result


if __name__ == "__main__":
    print(staircase(5))
    print()
    print(staircase(-5))
