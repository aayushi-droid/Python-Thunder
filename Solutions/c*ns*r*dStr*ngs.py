'''
    Problem Task: Given a censored string and a string of the censored vowels, return the original uncensored string.
    Problem Link: https://edabit.com/challenge/ehyZvt6AJF4rKFfXT
'''

def uncensor(txt, vowels):
	return txt.replace("*", "{}").format(*vowels)
  #First we replace "*"s with "{}"s.
  #Then we apply string formatting.
