"""
Problem statement: In a video game, a meteor will fall toward the main
                   character's home planet. Given the meteor's trajectory
                   as a string in the form y = mx + b and the character's
                   position as a tuple of (x, y), return True if the meteor
                   will hit the character and False if it will not.
Problem Link: https://edabit.com/challenge/9YfCbQpRPqRLzPCcg

"""


def will_hit(equation, position):
    ''' Checks if a point lies in the trajectory of a meteor'''

    import re

    line_pattern = r'y\s*=\s*(-*\d+)x\s*(\+|\-)\s*(\d+)'
    # Check if the equation matches the line equation format
    # While doing so, capture the values of m, sign of b and b
    matches = re.match(line_pattern, equation)
    if matches:
        slope, b_sign, b_value = matches.groups()
        slope = int(slope)
        b_value = int(b_value)
        if b_sign == '-':
            b_value = -b_value
        return int(position[1]) == (slope * int(position[0]) + b_value)


if __name__ == '__main__':
    equation = input('Enter meteor\'s equation (y = mx + b format): ')
    print('Enter co-ordinates of video game character:')
    x_coord = int(input('X = '))
    y_coord = int(input('Y = '))
    is_hitting = will_hit(equation, (x_coord, y_coord))
    print('Meteor will', 'hit' if is_hitting else 'not hit', 'the main character')
