'''
    Probem Task : The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
    Problem Link : https://edabit.com/challenge/MGALfBAXhXqqdFyqo
'''

from string import ascii_letters as alpha

def atbash(txt):
	return txt.translate(str.maketrans(alpha, alpha[::-1].swapcase()))