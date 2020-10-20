'''
    Probem Task : Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of compounding periods per year n. The function returns the value at the end of term rounded to the nearest cent.
    Problem Link : https://edabit.com/challenge/HjpihSKFBfRCCg86J
'''

def compound_interest(p,t,r,n):
    
    cp = p*((1 + (r/n))**(n*t))
    return float('%.2f'%cp)
