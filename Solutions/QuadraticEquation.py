'''
Problem statement: Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c. The function will take three arguments:
- a as the coefficient of x^2
- b as the coefficient of x
- c as the constant term
Problem Link: https://edabit.com/challenge/MDWFcHCTiJfHmwTFx
'''

def quadratic_equation(a, b, c):
	numerator = -b + (((b**2)-(4*a*c))**(1/2))
	denominator = 2*a
	return numerator/denominator
