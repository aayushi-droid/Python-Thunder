'''
    Probem Task : Write a function that takes a string "a + bi" and returns a tuple (a, b).
    Problem Link : https://edabit.com/challenge/oFNJeSzzcTgMwLFy5
'''


def complex_to_tuple(p):
	return (int(p[:-3]), int(p[-3:-1]))