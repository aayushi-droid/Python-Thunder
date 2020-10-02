'''
    Probem Task: Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher (check Resources tab for more info) shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c. Create a function that takes a string s (text to be encrypted) and an integer k (the rotation factor). It should return an encrypted string.
    Problem Link: https://edabit.com/challenge/C45TKLcGxh8dnbgqM
'''
def caesar_cipher(s, k):
    s2=''
    for char in s:
        if char>='a' and char<='z':
            asciival=ord(char)+k
            if asciival>122:
                asciival=96+(asciival-122)
            s2+=chr(asciival)
        elif char>='A' and char<='Z':
            asciival=ord(char)+k
            if asciival>90:
                asciival=64+(asciival-90)
            s2+=chr(asciival)
        else:
            s2+=char
    s=s2
    return s

            