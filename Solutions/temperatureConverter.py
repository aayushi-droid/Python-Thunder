"""
    Problem statement: Create a function that converts Celcius to Fahrenheit and vice versa.
    Problem Link: https://edabit.com/challenge/pSrCZFim6Y8HcS9Yc
"""

CELCIUS = 'C'
FAHRENHEIT = 'F'
SEP = '*'
ERROR_MSG = 'Error'


def convert(deg):
    '''
    Convert degrees in Celcius to Farenheit and vice versa.
    '''

    try:
        value, unit = deg.split(SEP)
        value = int(value)
    except ValueError:
        return ERROR_MSG
    result = None
    if unit == CELCIUS:
        result = str(int(round(value * 1.8 + 32, 0))) + SEP + FAHRENHEIT
    elif unit == FAHRENHEIT:
        result = str(int(round((value - 32) / 1.8, 0))) + SEP + CELCIUS
    else:
        result = ERROR_MSG
    return result


if __name__ == '__main__':
    INPUTS = ['35*C', '100*F', '0*C', '33', '97K', 'C*C']
    for input_value in INPUTS:
        print(convert(input_value))
