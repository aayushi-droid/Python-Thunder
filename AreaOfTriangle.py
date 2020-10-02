'''
    Probem Task : Write a function that takes the base and height of a triangle and returns its area.
    Problem Link : https://edabit.com/challenge/3CaszbdZYGN4otQD8
'''
def tri_area(b, h):
	return (b*h)/2
  
b,h=[int(i) for i in input().split()]
print(tri_area(b,h))
