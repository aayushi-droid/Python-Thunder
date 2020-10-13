'''
Problem Task: Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.

Problem Link: https://edabit.com/challenge/76ibd8jZxvhAwDskb
'''

def tallest_skyscraper(lst):
    tallest_col = ""
    for x in range(len(lst)):
        if lst[x].count(1) == 0:
            continue
        elif lst[x].count(1) != 0:
            return len(lst) - x
        else:
            return 0
