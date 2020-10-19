"""
    Probem Task  : Create methods for the Calculator class that can do the following:

				    Add two numbers.
				    Subtract two numbers.
				    Multiply two numbers.
				    Divide two numbers.

Problem Link: https://edabit.com/challenge/ta8GBizBNbRGo5iC6
"""


class Calculator:

	def add(self, a, b):
		print (a + b)

	def subract(self, a, b):
		print (a - b)

	def multiply(self, a, b):
		print (a * b)

	def divide(self, a, b):
		print (a // b)

cal = Calculator()
cal.add(5, 7)
cal.subract(7, 2)
cal.multiply(9, 5)
cal.divide(30, 4)