'''
Problem Task : Write a method that returns array of all the numbers from 1 to an integer argument.
                But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”.
                For numbers which are multiples of both three and five use “FizzBuzz”.

Problem Link : https://edabit.com/challenge/cKQA9N9Yg7ExeWusQ

Examples : 
fizzBuzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]

fizzBuzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

'''
for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)
	