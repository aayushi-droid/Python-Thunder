'''
    Probem Task : This program takes a positive integer and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
    Problem Link : https://edabit.com/challenge/G9QRtAGXb9Cu368Pw
'''

def pentagonal(n):
	return int(1+n*(n-1)*5/2)
