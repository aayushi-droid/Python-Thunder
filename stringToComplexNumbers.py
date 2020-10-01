'''
    Probem Task : This program takes a string "a + bi" and returns a tuple (a, b).
    Problem Link : https://edabit.com/challenge/oFNJeSzzcTgMwLFy5
'''

def complex_to_tuple(param):
    param = param.replace(" ", "")
    pls = 0
    mins = 0
    for i in param:
        if i == "+":
            pls += 1
        elif i == "-":
            mins += 1
    arr = []
    flag = True
    if pls == 1 :
        arr = param.split("+")
    else:
        arr = param.split("-")
        flag = False
    if flag:
        return(
            int(arr[0]),
             int(arr[1].replace("i",""))
             )
    else:
        if len(arr) == 3:
            return(
                -int(arr[1]), -int(arr[2].replace("i",""))
                )
        else:
            return(
                int(arr[0]),
                 -int(arr[1].replace("i",""))
                 )
