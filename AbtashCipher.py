#use _author_ = 'Kuruvilla Jacob'
'''
    Probem Task:  The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
    Create a function that takes a string and applies the Atbash cipher to it.
    Problem Link: https://edabit.com/challenge/MGALfBAXhXqqdFyqo
'''
def atbash(string):
    s2=''
    for char in string:
        if char.islower()==True:
            s2+=chr(122-(ord(char)-97))
        elif char.isupper()==True:
            s2+=chr(90-(ord(char)-65))
        else:
            s2+=char
    string=s2
    return string

