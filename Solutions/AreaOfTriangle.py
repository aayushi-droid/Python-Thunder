'''
    Problem Task : Write a function that takes the base and height of a triangle and returns its area.
    Problem Link : https://edabit.com/challenge/3CaszbdZYGN4otQD8
'''
def tri_area(base, height):
	return (base*height)/2
  
assert tri_area(3, 2) == 3.0
assert tri_area(2, 4) == 4.0
assert tri_area(7, 4) == 14.0
assert tri_area(10, 10) == 50.0
