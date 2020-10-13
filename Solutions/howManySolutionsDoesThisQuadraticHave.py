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

if __name__ == "__main__":
    assert solutions(1, 0, -1) == 2
    assert solutions(1, 0, -1) == 2
    assert solutions(1, 0, 0) == 1
    assert solutions(1, 0, 1) == 0
    assert solutions(200, 420, 800) == 0
    assert solutions(200, 420, -800) == 2
    assert solutions(1000, 1000, 0) == 2
    assert solutions(10000, 400, 4) == 1