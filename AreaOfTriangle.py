'''
    Probem Task : Write a function that takes the base and height of a triangle and returns its area.
    Problem Link : https://edabit.com/challenge/3CaszbdZYGN4otQD8
'''

# The main function
def tri_area(base, height):
	return (base*height)/2
  
base,height=[int(i) for i in input("Enter base and height: ").split()]
print(tri_area(base,height))







