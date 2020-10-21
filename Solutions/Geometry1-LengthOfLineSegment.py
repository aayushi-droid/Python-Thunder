'''
Problem statement: Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.
Problem Link: https://edabit.com/challenge/3Ekam9jvbNKHDtx4K
'''

import math
def line_length(dot1, dot2):
	x1, y1 = dot1
	x2, y2 = dot2
	dis = math.pow(x1-x2, 2) + math.pow(y1-y2, 2) 
	return round(math.sqrt(dis), 2)
