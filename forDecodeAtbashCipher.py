'''
    Problem Task : The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
    Problem Link : https://edabit.com/challenge/MGALfBAXhXqqdFyqo
'''

def decrypt(message):
	reverse_order = ["Z","Y","X","W","V","","U","T","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A"]
	alpha_order = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","","V","W","X","Y","Z"]
	decoded_msg = ""

	for letter in message:
		if letter == " ":
			decoded_msg += " "
		else:
			for i in range(0,26):
				if letter == alpha_order[i]:
					decoded_msg += reverse_order[i]
	print(decoded_msg)

message = raw_input("enter message to decode in atbash cipher: ")
decrypt(message.upper())
