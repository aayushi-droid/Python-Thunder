"""python3"""
# Problem Statement : Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Problem Link : https://edabit.com/challenge/npLurjMJofmFRCJwx
from collections import deque


def plc(nu, n, table):
    list = []
    qu = deque()
    qu.append("")
    while len(qu) != 0:
        s = qu.pop()
        if len(s) == n:
            list.append(s)
        else:
            for letter in table[nu[len(s)]]:
                qu.append(s + letter)
    return list


def lc(nu, n):
    table = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    list = plc(nu, n, table)

    s = ""
    for word in list:
        s += word + " "
    print(s)
    return


nu = [2, 3, 4]
n = len(nu)
lc(nu, n)
