'''
problem task: Create a function that takes two parameters and, 
if both parameters are strings, add them as if they were integers 
or if the two parameters are integers, concatenate them.
problem link: https://edabit.com/challenge/6dnhESWBcTMMF3gsa
'''

def stupid_addition(a,b):
    if type(a) == str and type(b) == str:
        c = int(a) + int(b)
        return c
    elif type(a) == int and type(b) == int:
        c = str(a) + str(b)
        return c
    else:
        return None