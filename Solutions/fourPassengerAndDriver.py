'''
    Probem Task : Four Passengers and a Driver
    Problem Link : https://edabit.com/challenge/T7DpLzEkAkcxKijzR
'''
import math
def cars_needed(passenger):
    cars = math.ceil(passenger / 5)
    return cars

print(cars_needed(5))
print(cars_needed(11))
print(cars_needed(0))