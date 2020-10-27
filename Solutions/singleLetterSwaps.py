'''
Problem Task: Given an array of strings and an original string, 
write a function to output an array of boolean values - True if the word can be formed from the original word by swapping two letters only once and False otherwise.

Problem Link: https://edabit.com/challenge/di7ZjxgvLgz72PvCS
'''

def validate_swaps(lst, txt):
	ret_list = []
	lst_len = len(lst)
	txt_len = len(txt)
	if (lst_len == 0) or (txt_len == 0):
		return []
	for x in range(lst_len):
		test = 0
		txt_lst = list(txt)
		checked = list(lst[x])
		if len(checked) != txt_len:
			ret_list.append(False)
			continue
		if set(checked) != set(txt):
			ret_list.append(False)
			continue
		for y in range(txt_len):
			if checked.pop() != txt_lst.pop():
				test += 1
			if test == 3:
				ret_list.append(False)
				break
		else:
			ret_list.append(True)
	return ret_list
