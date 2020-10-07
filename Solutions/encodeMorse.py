"""

Problem statement: Create a function that takes a string as an argument and
                   return a non-encoded, encrypted string.
Problem Link: https://edabit.com/challenge/5bYXQfpyoithnQisa

"""


def encode_morse(message):
    ''' Take a string as an argument and return a non-encoded, encrypted string
    '''
    if message is None:
        return ''
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    result = []
    message = message.upper()
    for character in message:
        result.append(char_to_dots.get(character, ' '))
    return ' '.join(result)


if __name__ == '__main__':
    print('Enter a string to encode using Morse Code:')
    msg = input('>')
    print('Encoded message in Morse Code:')
    print(encode_morse(msg))
