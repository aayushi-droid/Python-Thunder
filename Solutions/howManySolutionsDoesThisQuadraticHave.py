"""
Problem statement: How Many Solutions Does This Quadratic Have?
Problem Link: https://edabit.com/challenge/o2AKq4xy3nfZabKXL

"""
def solutions(a, b, c):
    delta = b**2-4*a*c
    
    if(delta == 0):
        return 1    
    if(delta > -1):
        return 2    
    if(delta < 0):
        return 0