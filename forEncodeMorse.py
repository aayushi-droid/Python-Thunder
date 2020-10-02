'''
    Probem Task : Create a function that takes a string as an argument and return a non-encoded, encrypted string.
    Problem Link : https://edabit.com/challenge/5bYXQfpyoithnQisa
'''

mcode = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += mcode[letter] + ' '
        else: 
            cipher += ' '  
    return cipher


def decrypt(message):
 
    message += ' '  
    decipher = '' 
    citext = '' 
    for letter in message: 
        if (letter != ' '):
            i = 0 
            citext += letter 
        else: 
            i += 1
            if i == 2 : 
                decipher += ' '
            else:
                decipher += list(mcode.keys())[list(mcode.values()).index(citext)] 
                citext = '' 
  
    return decipher
def process():
    n = int(input("enter 1 for encryption 0 for decryption "))
    if n == 1:
        enc_message = raw_input("Enter a message to encrypt ")
        result = encrypt(enc_message.upper()) 
        print (result) 
 
    else:
        dec_message = raw_input("Enter encrypted message to decrypt ") 
        result = decrypt(dec_message) 
        print (result) 
  
process()