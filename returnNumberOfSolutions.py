'''
    Probem Task : This program will return number of solutions to quadratic equation.
    Problem Link :  https://edabit.com/challenge/o2AKq4xy3nfZabKXL
'''

def solutions(a,b,c):
    if ((b**2 - 4*a*c) > 0):
        return 2
    elif ((b**2 - 4*a*c)==0):
        return 1
    else:
        return 0

if __name__ == "__main__":
    a = int(input("Enter a\n"))
    b = int(input("Enter b\n"))
    c = int(input("Enter c\n"))
    print(f'{a}x\N{SUPERSCRIPT TWO} + {b}x + {c} = 0 has {solutions(a,b,c)} solutions')

