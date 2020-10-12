"""
    Problem Task : Given a string of characters containing only the three characters : ( ) :
    Create a function which returns a number based on the number of sad and smiley faces there are.

    The happy faces :) and (: are worth 1.
    The sad faces :( and ): are worth -1.
    Problem Link: https://edabit.com/challenge/8qD23E6XRMaWhyJ5z
"""


def smiley_faces(smile_string):
    len_string = len(smile_string)
    score = 0
    for i in range(1, len_string):
        smile = smile_string[i - 1] + smile_string[i]
        print(smile)
        if smile in [":)", "(:"]:
            score += 1
        elif smile in (":(", "):"):
            score -= 1

    return score
