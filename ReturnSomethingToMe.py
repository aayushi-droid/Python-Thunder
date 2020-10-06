'''
Problem Link: https://edabit.com/challenge/XXJbGFEkrMWCp8yFn

Write a function that returns the string "something" joined with a space " " and the given argument a.

Example:
give_me_something("is better than nothing") ➞ "something is better than nothing"

give_me_something("Bob Jane") ➞ "something Bob Jane"

give_me_something("something") ➞ "something something"
'''

def give_me_something(a):       #Function to return the string 'something' joined with a space and given argument a
    print(f'something {a}')
    return f'something {a}'

if __name__=="__main__":
    give_me_something('**Text Goes Here**') #Replace **Text goes here** with desired text
