"""
Backtracking is a form of recursion. But it involves choosing only option out of any possiblities.
        ########################   Arrangement Of Letter Problem          ##########################
######                               Python                                                        ###### 
"""


def arrangement(num, s):

    if num == 1:
        return s
    else:
        return [y + x for y in arrangement(1, s) for x in arrangement(num - 1, s)]


letter = ["1", "2", "3"]
print(arrangement(2, letter))
