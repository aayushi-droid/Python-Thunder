'''
    Probem Task : Create methods for the Calculator class that can do the following:
                  - Add two numbers.
                  - Subtract two numbers.
                  - Multiply two numbers.
                  - Divide two numbers.
    Problem Link : https://edabit.com/challenge/ta8GBizBNbRGo5iC6
'''

class Calculator:

    def __init__(self):
        pass

    def add(self, num1, num2):

        return num1 + num2

    def subtract(self, num1, num2):

        return num1 - num2

    def multiply(self, num1, num2):
        
        return num1 * num2

    def divide(self, num1, num2):
        
        return num1 // num2
    def square (self ,num):
        return num**2
    def power(self,num1 ,num2 ):
        num1**num2 
    




calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
