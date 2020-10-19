
'''
Problem statement: This is a list of single characters with an unwanted character at the end:
["H", "e", "l", "l", "o", "!", "\0"]
You could also just type "Hello!" when initializing a variable, creating the string "Hello!"
Create a function that will return a string by combining the given character list, not including the unwanted final character.

Problem Link: https://edabit.com/challenge/F4iemEeFfsaFoMpAF
'''
def cpp_txt(lst):
	ans=""
	for i in range(0,len(lst)-1):
		print(lst[i],end="")
		ans+=lst[i]
	return ans
