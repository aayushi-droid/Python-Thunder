'''
Description:
Count the amount of ones in the binary representation of an integer.
So for example, since 12 is '1100' in binary, the return value should be 2.

Link: https://edabit.com/challenge/GbyPdqNnp75Wci7Cn
'''

#declare the function
def count_ones(num):    
    bin_num = bin(num)   #inbuilt function to find binary number of a decimal number

    count = 0   #initialise the count variable with 0

    ones = [count+1 for i in bin_num[2:] if int(i)==1]   #appends 1 as the number of 1 in the binary form

    print(len(ones))   #prints the length of the ones list

count_ones(int(input()))   #takes input and call the function