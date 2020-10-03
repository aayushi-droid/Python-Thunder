'''
    Probem Task : implement a new function that convert interger to string and vise verse.
    Problem Link : https://edabit.com/challenge/pfn6QRn6eiTHEPpSs
'''


def int_to_str(n: int):
    # initialize some helper variable and dict to get our integer
    helper_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    str = ""

    if n == 0:
        return helper_dict[0]

    # to take care of integer less than 0
    sign = 1 if n > 0 else -1
    n = sign * n

    # here i getting how far i can go with inputted interger
    divOn = 1
    while n // divOn > 10:
        divOn *= 10

    # using divOn and minusOff to get every digit alone to get it from the helper dict
    # like 616 6
    #          1
    #          6
    # and append it to my string to combine it
    while n > 0:
        str += helper_dict[n // divOn]
        minusOff = n // divOn * divOn
        divOn //= 10
        n -= minusOff

    if sign == -1:
        str = "-" + str

    return str


def str_to_int(s: str):
    # initialize some helper variable and dict to get our integer
    helper_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    multiply = 1
    integer = 0

    for i in range( len( s ) - 1, -1, -1 ):
        integer += helper_dict[s[i]] * multiply
        multiply *= 10

    return integer
