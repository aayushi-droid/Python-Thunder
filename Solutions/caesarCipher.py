'''
Caesar's Cipher (https://edabit.com/challenge/C45TKLcGxh8dnbgqM)
Create a function that takes a string s (text to be encrypted) 
and an integer k (the rotation factor). It should return an encrypted string.

Examples
caesar_cipher("middle-Outz", 2) ➞ "okffng-Qwvb"

# m -> o
# i -> k
# d -> f
# d -> f
# l -> n
# e -> g
# -    -
# O -> Q
# u -> w
# t -> v
# z -> b

caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5)
➞ "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

caesar_cipher("A friend in need is a friend indeed", 20)
➞ "U zlcyhx ch hyyx cm u zlcyhx chxyyx"
'''

def caesar_cipher(s, k):
  #convert the given string to char array to do modificatino
	char_list=list(s)

	for i in range(len(char_list)):
			base_factor=0 
      #this is the base value for e.g - for capital case start value is 65 and
      # for small case start value is 97
       
			if ord(char_list[i])>=65 and ord(char_list[i])<=90:
					base_factor=65
			elif ord(char_list[i])>=97 and ord(char_list[i])<=122:
					base_factor=97
			else:
					continue #id the current character is not a small or capital case letter, then no need to transform
			
      #shifting the curr character by k , and by modulo 26 , ensuring 
      # that the transformed value is again in the cyclic range of 1->26->1
      char_list[i]=chr((ord(char_list[i]) - base_factor + k) % 26 + base_factor)

  #join the char list to return the final transformed string    
	return "".join(char_list)
	