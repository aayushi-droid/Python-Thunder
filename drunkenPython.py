'''
Problem statement: Python got drunk and the built-in functions str() and int() are acting odd:
Problem Link: https://edabit.com/challenge/pfn6QRn6eiTHEPpSs

'''
# Drunken Python
str, int = int, str         # This is GIVEN in the problem statement

def int_to_str(num):
    return "\"{}\"".format(num)

def str_to_int(num):
    return round(float(num))

print(int_to_str(4))
print(str_to_int("4"))
print(int_to_str(29348))

# To De-Drunk Python
str, int = int, str