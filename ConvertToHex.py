'''  
  Problem statement: Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.
  Problem Link: https://edabit.com/challenge/g6yjSfTpDkX2STnSX
'''

def convert_to_hex(txt):
    solution=""
    for chr in txt:
        solution = solution + format(ord(chr), "x") + " "
    return solution[:-1]
