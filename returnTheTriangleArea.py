'''
    Problem Task : This program will get the area of the triangle
    Problem Link : https://edabit.com/challenge/3CaszbdZYGN4otQD8
'''


def tri_area(base, height):
    return (base * height) / 2


def main():
    a, b = input().split()
    a, b = int(a), int(b)
    res = tri_area(a, b)
    print(res)


main()
