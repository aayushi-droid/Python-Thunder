'''
Probem Task : This program returns the difference in areas of two squares.
Problem Link: https://edabit.com/challenge/NNhkGocuPMcryW7GP
'''


def square_areas_difference(r):
		print("The difference in area of incircle square and circumcumcircle square is : " + str(((2*r)**2)-(r**2)*2))

radius = int(input("Enter the radius of the circle: "))
square_areas_difference(radius)
