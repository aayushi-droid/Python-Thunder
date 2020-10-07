'''
    Probem Task: Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher (check Resources tab for more info) shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c. Create a function that takes a string s (text to be encrypted) and an integer k (the rotation factor). It should return an encrypted string.
    Problem Link: https://edabit.com/challenge/C45TKLcGxh8dnbgqM
'''

def caesarsCipher(s,k):
    enc_list=[]
    for char in s:
        if char.isalpha() and ord(char) >=97:
            enc_list.append(chr(((ord(char)-97+k)%26)+97))
        elif char.isalpha() and ord(char) <=90:
            enc_list.append(chr(((ord(char)-65+k)%26)+65))
        else:
            enc_list.append(char)
    return ''.join(enc_list)
