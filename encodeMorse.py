  
'''
    Probem Task : This program takes a string and return a non-encoded, encrypted string in morse code
    Problem Link : https://edabit.com/challenge/5bYXQfpyoithnQisa
'''


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

#Take input to be encoded
rawString = input("Enter String to be encoded: \t")

rawString = rawString.upper() #Convert the strign to uppercase
encodedString = ""  #stores the encoded string

for index in range(len(rawString)):
    character = rawString[index]
    encodedString += char_to_dots[character] + " "


encodedString = encodedString[:-1]
print(encodedString)